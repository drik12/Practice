import random, datetime, webbrowser, threading, time
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# ─────────────────────────────────────────────
# DATA LAYER  (same doubly-linked list logic)
# ─────────────────────────────────────────────
class Song:
    def __init__(self, title, artist, lyrics):
        self.title        = title
        self.artist       = artist
        self.lyrics       = lyrics
        self.is_favourite = False
        self.rating       = 0
        self.play_count   = 0
        self.next         = None
        self.prev         = None

    def to_dict(self):
        return {
            "title":       self.title,
            "artist":      self.artist,
            "lyrics":      self.lyrics,
            "is_favourite": self.is_favourite,
            "rating":      self.rating,
            "play_count":  self.play_count,
        }


class Playlist:
    def __init__(self, name):
        self.name          = name
        self.head          = None
        self.repeat        = False
        self._delete_stack = []

    def songs_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur)
            cur = cur.next
        return out

    def add(self, title):
        if title not in SONG_LIBRARY:
            return False, "Not in library"
        for s in self.songs_list():
            if s.title == title:
                return False, "Already in playlist"
        artist, lyrics = SONG_LIBRARY[title]
        node = Song(title, artist, lyrics)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next  = node
            node.prev = cur
        return True, "Added"

    def delete(self, title):
        cur = self.head
        while cur:
            if cur.title == title:
                if cur.prev: cur.prev.next = cur.next
                else:        self.head     = cur.next
                if cur.next: cur.next.prev = cur.prev
                cur.next = cur.prev = None
                self._delete_stack.append(cur)
                return True
            cur = cur.next
        return False

    def undo_delete(self):
        if not self._delete_stack:
            return None
        node = self._delete_stack.pop()
        node.next = node.prev = None
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next: cur = cur.next
            cur.next  = node
            node.prev = cur
        return node.title

    def shuffle(self):
        songs = self.songs_list()
        if not songs: return
        random.shuffle(songs)
        for i, s in enumerate(songs):
            s.prev = songs[i-1] if i > 0 else None
            s.next = songs[i+1] if i < len(songs)-1 else None
        self.head = songs[0]

    def search(self, q):
        q = q.lower()
        return [s for s in self.songs_list()
                if q in s.title.lower() or q in s.artist.lower()]

    def stats(self):
        songs = self.songs_list()
        if not songs: return {}
        rated   = [s for s in songs if s.rating > 0]
        avg_r   = round(sum(s.rating for s in rated) / len(rated), 1) if rated else 0
        top_p   = max(songs, key=lambda s: s.play_count)
        top_r   = max(rated, key=lambda s: s.rating) if rated else None
        return {
            "total":       len(songs),
            "total_plays": sum(s.play_count for s in songs),
            "favourites":  sum(1 for s in songs if s.is_favourite),
            "avg_rating":  avg_r,
            "top_played":  top_p.title,
            "top_rated":   top_r.title if top_r else "—",
            "repeat":      self.repeat,
        }


# ─────────────────────────────────────────────
# SONG LIBRARY
# ─────────────────────────────────────────────
SONG_LIBRARY = {
    "Shape of You": ("Ed Sheeran", "The club isn't the best place to find a lover\nSo the bar is where I go\nMe and my friends at the table doing shots\nDrinking fast and then we talk slow\nCome over and start up a conversation with just me\nAnd trust me I'll give it a chance now\nGirl, you know I want your love\nYour love was handmade for somebody like me\nCome on now, follow my lead"),
    "Believer":     ("Imagine Dragons", "First things first\nI'ma say all the words inside my head\nI'm fired up and tired of the way that things have been\nSecond thing second\nDon't you tell me what you think that I could be\nI'm the one at the sail, I'm the master of my sea\nI was broken from a young age\nSinging from heartache from the pain\nPain!"),
    "Perfect":      ("Ed Sheeran", "I found a love for me\nDarling, just dive right in and follow my lead\nWell, I found a girl, beautiful and sweet\n'Cause we were just kids when we fell in love\nI will not give you up this time\nBaby, I'm dancin' in the dark\nWith you between my arms\nDarling, you look perfect tonight"),
    "Closer":       ("The Chainsmokers", "Hey, I was doing just fine before I met you\nI drink too much and that's an issue, but I'm okay\nFour years, no calls\nNow you're lookin' pretty in a hotel bar\nSo baby pull me closer in the backseat of your Rover\nBite that tattoo on your shoulder\nWe ain't ever gettin' older"),
    "Faded":        ("Alan Walker", "You were the shadow to my light\nDid you see us?\nAnother star, you fade away\nAfraid our aim is out of sight\nWanna see us, alive\nWhere are you now?\nWas it all in my fantasy?\nWhere are you now?"),
    "Golden Brown": ("The Stranglers", "Golden brown, texture like sun\nLays me down, with my mind she runs\nThroughout the night\nNo need to fight\nNever a frown with golden brown\nEvery time just like the last\nOn her ship tied to the mast\nNever a frown with golden brown"),
    "Blinding Lights": ("The Weeknd", "I've been tryna call\nI've been on my own for long enough\nMaybe you can show me how to love\nI said ooh, I'm blinded by the lights\nNo, I can't sleep until I feel your touch\nI said ooh, I'm drowning in the night"),
    "Levitating":   ("Dua Lipa", "If you wanna run away with me, I know a galaxy\nAnd I can take you for a ride\nI had a premonition that we fell into a rhythm\nYou can levitate\nCome take my hand\nWe're gonna fly so high"),
    "Stay":         ("The Kid LAROI & Justin Bieber", "I do the same thing I told you that I never would\nI told you I'd change, even when I knew I never could\nI know that I can't find nobody else as good as you\nI need you to stay, need you to stay"),
}

# ─────────────────────────────────────────────
# APP STATE
# ─────────────────────────────────────────────
playlists: dict[str, Playlist] = {}
current_playlist_name: str | None = None

def get_pl() -> Playlist | None:
    return playlists.get(current_playlist_name)

# ─────────────────────────────────────────────
# API ROUTES
# ─────────────────────────────────────────────
@app.route("/api/library")
def api_library():
    return jsonify([{"title": t, "artist": a} for t, (a,_) in SONG_LIBRARY.items()])

@app.route("/api/playlists", methods=["GET"])
def api_playlists():
    return jsonify({
        "playlists": [{"name": n, "count": len(p.songs_list())} for n, p in playlists.items()],
        "current":   current_playlist_name,
    })

@app.route("/api/playlists", methods=["POST"])
def api_create_playlist():
    global current_playlist_name
    name = request.json.get("name","").strip()
    if not name:           return jsonify({"ok":False,"msg":"Name required"})
    if name in playlists:  return jsonify({"ok":False,"msg":"Already exists"})
    playlists[name] = Playlist(name)
    current_playlist_name = name
    return jsonify({"ok":True})

@app.route("/api/playlists/select", methods=["POST"])
def api_select():
    global current_playlist_name
    name = request.json.get("name")
    if name not in playlists: return jsonify({"ok":False,"msg":"Not found"})
    current_playlist_name = name
    return jsonify({"ok":True})

@app.route("/api/songs")
def api_songs():
    pl = get_pl()
    if not pl: return jsonify([])
    return jsonify([s.to_dict() for s in pl.songs_list()])

@app.route("/api/songs/add", methods=["POST"])
def api_add():
    pl = get_pl()
    if not pl: return jsonify({"ok":False,"msg":"No playlist"})
    ok, msg = pl.add(request.json.get("title",""))
    return jsonify({"ok":ok,"msg":msg})

@app.route("/api/songs/delete", methods=["POST"])
def api_delete():
    pl = get_pl()
    if not pl: return jsonify({"ok":False})
    ok = pl.delete(request.json.get("title",""))
    return jsonify({"ok":ok})

@app.route("/api/songs/undo", methods=["POST"])
def api_undo():
    pl = get_pl()
    if not pl: return jsonify({"ok":False})
    t = pl.undo_delete()
    return jsonify({"ok": bool(t), "title": t})

@app.route("/api/songs/favourite", methods=["POST"])
def api_fav():
    pl = get_pl()
    if not pl: return jsonify({"ok":False})
    title = request.json.get("title")
    for s in pl.songs_list():
        if s.title == title:
            s.is_favourite = not s.is_favourite
            return jsonify({"ok":True,"state":s.is_favourite})
    return jsonify({"ok":False})

@app.route("/api/songs/rate", methods=["POST"])
def api_rate():
    pl = get_pl()
    if not pl: return jsonify({"ok":False})
    title  = request.json.get("title")
    rating = int(request.json.get("rating",0))
    for s in pl.songs_list():
        if s.title == title:
            s.rating = rating
            return jsonify({"ok":True})
    return jsonify({"ok":False})

@app.route("/api/songs/play", methods=["POST"])
def api_play():
    pl = get_pl()
    if not pl: return jsonify({"ok":False})
    title = request.json.get("title")
    for s in pl.songs_list():
        if s.title == title:
            s.play_count += 1
            return jsonify({"ok":True,"song":s.to_dict()})
    return jsonify({"ok":False})

@app.route("/api/playlist/shuffle", methods=["POST"])
def api_shuffle():
    pl = get_pl()
    if not pl: return jsonify({"ok":False})
    pl.shuffle()
    return jsonify({"ok":True})

@app.route("/api/playlist/repeat", methods=["POST"])
def api_repeat():
    pl = get_pl()
    if not pl: return jsonify({"ok":False})
    pl.repeat = not pl.repeat
    return jsonify({"ok":True,"repeat":pl.repeat})

@app.route("/api/playlist/stats")
def api_stats():
    pl = get_pl()
    if not pl: return jsonify({})
    return jsonify(pl.stats())

@app.route("/api/songs/search")
def api_search():
    pl = get_pl()
    if not pl: return jsonify([])
    q = request.args.get("q","")
    return jsonify([s.to_dict() for s in pl.search(q)])

@app.route("/api/playlist/export")
def api_export():
    pl = get_pl()
    if not pl: return jsonify({"ok":False})
    lines = [f"Playlist: {pl.name}", f"Exported: {datetime.datetime.now():%Y-%m-%d %H:%M}", "="*40]
    for i,s in enumerate(pl.songs_list(),1):
        stars = "★"*s.rating+"☆"*(5-s.rating)
        fav   = " ♥️" if s.is_favourite else ""
        lines.append(f"{i}. {s.title} — {s.artist}{fav}")
        lines.append(f"   {stars}  |  Plays: {s.play_count}")
    return jsonify({"ok":True,"text":"\n".join(lines)})

# ─────────────────────────────────────────────
# FRONTEND  (single HTML page)
# ─────────────────────────────────────────────
HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Melodia — Music Player</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;1,300&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0a0a0f;--bg2:#111118;--bg3:#1a1a24;--bg4:#22222e;
  --acc:#c8f064;--acc2:#7c6af7;--acc3:#f06464;
  --txt:#e8e8f0;--txt2:#9090a8;--txt3:#5a5a72;
  --rad:12px;--rad2:20px;
}
body{background:var(--bg);color:var(--txt);font-family:'Syne',sans-serif;min-height:100vh;overflow-x:hidden}

/* ── LAYOUT ── */
.app{display:grid;grid-template-columns:280px 1fr 340px;grid-template-rows:64px 1fr 140px;height:100vh;gap:0}
.topbar{grid-column:1/-1;display:flex;align-items:center;justify-content:space-between;padding:0 28px;background:var(--bg2);border-bottom:1px solid rgba(255,255,255,.06)}
.sidebar{grid-row:2/3;background:var(--bg2);border-right:1px solid rgba(255,255,255,.06);display:flex;flex-direction:column;overflow:hidden}
.main{grid-row:2/3;overflow-y:auto;padding:28px}
.rightpanel{grid-row:2/3;background:var(--bg2);border-left:1px solid rgba(255,255,255,.06);display:flex;flex-direction:column;overflow-y:auto}
.player{grid-column:1/-1;background:var(--bg2);border-top:1px solid rgba(255,255,255,.06);display:flex;align-items:center;gap:24px;padding:0 32px}

/* ── TOPBAR ── */
.logo{font-weight:800;font-size:20px;letter-spacing:-1px;color:var(--acc)}
.logo span{color:var(--txt2)}
.search-wrap{position:relative;flex:1;max-width:380px;margin:0 auto}
.search-wrap input{width:100%;background:var(--bg3);border:1px solid rgba(255,255,255,.08);border-radius:30px;padding:9px 18px 9px 42px;color:var(--txt);font-family:'Syne',sans-serif;font-size:14px;outline:none;transition:border .2s}
.search-wrap input:focus{border-color:var(--acc2)}
.search-icon{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--txt3);font-size:16px}
.header-btns{display:flex;gap:10px}

/* ── SIDEBAR ── */
.sidebar-title{padding:20px 20px 12px;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--txt3)}
.pl-list{flex:1;overflow-y:auto;padding:0 12px}
.pl-item{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:var(--rad);cursor:pointer;transition:background .15s;margin-bottom:4px}
.pl-item:hover{background:var(--bg3)}
.pl-item.active{background:linear-gradient(90deg,rgba(200,240,100,.12),transparent);border-left:2px solid var(--acc)}
.pl-icon{width:36px;height:36px;border-radius:8px;background:var(--bg4);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.pl-info{flex:1;min-width:0}
.pl-name{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pl-count{font-size:12px;color:var(--txt3);font-family:'DM Mono',monospace}
.sidebar-bottom{padding:16px}
.btn-create{width:100%;background:var(--acc);color:#111;border:none;border-radius:30px;padding:11px;font-family:'Syne',sans-serif;font-weight:700;font-size:14px;cursor:pointer;transition:opacity .15s}
.btn-create:hover{opacity:.85}

/* ── SONG CARDS ── */
.section-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px}
.section-title{font-size:22px;font-weight:800}
.song-grid{display:flex;flex-direction:column;gap:8px}
.song-card{background:var(--bg2);border:1px solid rgba(255,255,255,.06);border-radius:var(--rad2);padding:14px 18px;display:flex;align-items:center;gap:14px;cursor:pointer;transition:all .18s;position:relative;overflow:hidden}
.song-card::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(200,240,100,.04),transparent);opacity:0;transition:opacity .2s}
.song-card:hover::before{opacity:1}
.song-card:hover{border-color:rgba(200,240,100,.2);transform:translateX(4px)}
.song-card.playing{border-color:var(--acc);background:rgba(200,240,100,.06)}
.song-num{width:28px;text-align:center;font-family:'DM Mono',monospace;font-size:13px;color:var(--txt3);flex-shrink:0}
.song-num.eq{display:flex;align-items:flex-end;gap:2px;height:20px}
.eq-bar{width:3px;background:var(--acc);border-radius:2px;animation:eq .6s ease-in-out infinite alternate}
.eq-bar:nth-child(2){animation-delay:.15s;height:70%}
.eq-bar:nth-child(3){animation-delay:.3s;height:45%}
@keyframes eq{from{transform:scaleY(.3)}to{transform:scaleY(1)}}
.song-thumb{width:44px;height:44px;border-radius:10px;background:var(--bg4);display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0}
.song-meta{flex:1;min-width:0}
.song-title{font-size:15px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.song-artist{font-size:13px;color:var(--txt2);margin-top:2px;font-family:'DM Mono',monospace}
.song-rating{display:flex;gap:2px}
.star{font-size:13px;cursor:pointer;color:var(--txt3);transition:color .1s}
.star.on{color:#f5c518}
.song-plays{font-family:'DM Mono',monospace;font-size:12px;color:var(--txt3);margin-left:8px}
.song-actions{display:flex;gap:6px;opacity:0;transition:opacity .15s}
.song-card:hover .song-actions{opacity:1}
.action-btn{background:var(--bg4);border:none;color:var(--txt2);border-radius:8px;width:30px;height:30px;cursor:pointer;font-size:14px;transition:all .15s;display:flex;align-items:center;justify-content:center}
.action-btn:hover{background:var(--bg3);color:var(--txt)}
.action-btn.fav.active{color:#f06090}
.action-btn.del:hover{background:rgba(240,100,100,.15);color:var(--acc3)}

/* ── RIGHT PANEL ── */
.lyrics-panel{padding:24px}
.lyrics-panel h3{font-size:13px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--txt3);margin-bottom:16px}
.now-playing-art{width:100%;aspect-ratio:1;border-radius:var(--rad2);background:linear-gradient(135deg,var(--bg3),var(--bg4));display:flex;align-items:center;justify-content:center;font-size:64px;margin-bottom:20px;position:relative;overflow:hidden}
.now-playing-art::after{content:'';position:absolute;inset:0;background:radial-gradient(circle at 30% 30%,rgba(200,240,100,.08),transparent 60%)}
.now-title{font-size:20px;font-weight:800;margin-bottom:4px;line-height:1.2}
.now-artist{font-family:'DM Mono',monospace;font-size:13px;color:var(--txt2);margin-bottom:14px}
.lyrics-text{font-family:'DM Mono',monospace;font-size:13px;line-height:1.9;color:var(--txt2);white-space:pre-wrap;max-height:240px;overflow-y:auto}
.lyrics-text::-webkit-scrollbar{width:4px}
.lyrics-text::-webkit-scrollbar-track{background:transparent}
.lyrics-text::-webkit-scrollbar-thumb{background:var(--bg4);border-radius:2px}

/* ── STATS ── */
.stats-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:20px;border-top:1px solid rgba(255,255,255,.06)}
.stat-card{background:var(--bg3);border-radius:var(--rad);padding:12px 14px}
.stat-val{font-size:22px;font-weight:800;color:var(--acc)}
.stat-label{font-size:11px;color:var(--txt3);margin-top:2px;font-family:'DM Mono',monospace}

/* ── PLAYER BAR ── */
.player-left{display:flex;align-items:center;gap:14px;width:240px;flex-shrink:0}
.player-art{width:54px;height:54px;border-radius:10px;background:var(--bg3);display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0}
.player-info{min-width:0}
.player-title{font-size:14px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.player-artist{font-size:12px;color:var(--txt2);font-family:'DM Mono',monospace}
.player-fav{background:none;border:none;font-size:18px;cursor:pointer;color:var(--txt3);transition:color .2s;flex-shrink:0}
.player-fav.on{color:#f06090}
.player-center{flex:1;display:flex;flex-direction:column;align-items:center;gap:8px}
.controls{display:flex;align-items:center;gap:14px}
.ctrl-btn{background:none;border:none;color:var(--txt2);cursor:pointer;font-size:18px;transition:all .15s;width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.ctrl-btn:hover{color:var(--txt);background:var(--bg3)}
.ctrl-btn.active{color:var(--acc)}
.play-btn{background:var(--acc);color:#111;width:46px;height:46px;border-radius:50%;font-size:20px;border:none;cursor:pointer;transition:transform .15s,opacity .15s;display:flex;align-items:center;justify-content:center}
.play-btn:hover{transform:scale(1.08)}
.progress-wrap{width:100%;display:flex;align-items:center;gap:10px}
.prog-time{font-family:'DM Mono',monospace;font-size:11px;color:var(--txt3);width:32px;text-align:center}
.progress{flex:1;height:4px;background:var(--bg4);border-radius:2px;cursor:pointer;position:relative}
.progress-fill{height:100%;border-radius:2px;background:var(--acc);width:0;transition:width .1s linear;position:relative}
.progress-fill::after{content:'';position:absolute;right:-5px;top:-4px;width:12px;height:12px;border-radius:50%;background:var(--acc);opacity:0;transition:opacity .15s}
.progress:hover .progress-fill::after{opacity:1}
.player-right{display:flex;align-items:center;gap:10px;width:180px;flex-shrink:0;justify-content:flex-end}
.vol-icon{font-size:16px;color:var(--txt3)}
.vol-slider{-webkit-appearance:none;width:90px;height:4px;border-radius:2px;background:var(--bg4);outline:none;cursor:pointer}
.vol-slider::-webkit-slider-thumb{-webkit-appearance:none;width:12px;height:12px;border-radius:50%;background:var(--txt);cursor:pointer}

/* ── MODALS ── */
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.7);backdrop-filter:blur(4px);z-index:100;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .2s}
.overlay.show{opacity:1;pointer-events:all}
.modal{background:var(--bg2);border:1px solid rgba(255,255,255,.1);border-radius:var(--rad2);padding:28px;width:420px;max-width:90vw;transform:translateY(20px);transition:transform .2s}
.overlay.show .modal{transform:none}
.modal h2{font-size:20px;font-weight:800;margin-bottom:20px}
.modal input,.modal textarea{width:100%;background:var(--bg3);border:1px solid rgba(255,255,255,.1);border-radius:var(--rad);padding:12px 16px;color:var(--txt);font-family:'Syne',sans-serif;font-size:14px;outline:none;margin-bottom:12px;transition:border .2s}
.modal input:focus,.modal textarea:focus{border-color:var(--acc2)}
.modal-btns{display:flex;gap:10px;justify-content:flex-end;margin-top:6px}

/* ── BUTTONS ── */
.btn{padding:10px 20px;border-radius:30px;border:none;font-family:'Syne',sans-serif;font-weight:700;font-size:14px;cursor:pointer;transition:all .15s}
.btn-primary{background:var(--acc);color:#111}
.btn-primary:hover{opacity:.85}
.btn-ghost{background:var(--bg3);color:var(--txt2);border:1px solid rgba(255,255,255,.08)}
.btn-ghost:hover{color:var(--txt);background:var(--bg4)}
.btn-sm{padding:7px 14px;font-size:13px}
.btn-icon{background:var(--bg3);border:1px solid rgba(255,255,255,.08);color:var(--txt2);border-radius:var(--rad);padding:8px 12px;font-size:13px;cursor:pointer;font-family:'Syne',sans-serif;font-weight:600;transition:all .15s;display:flex;align-items:center;gap:6px}
.btn-icon:hover{color:var(--txt);border-color:rgba(255,255,255,.18)}

/* ── EMPTY STATE ── */
.empty{display:flex;flex-direction:column;align-items:center;justify-content:center;height:60%;gap:12px;color:var(--txt3)}
.empty-icon{font-size:56px;opacity:.3}
.empty-text{font-size:16px;font-weight:600}
.empty-sub{font-size:13px;font-family:'DM Mono',monospace}

/* ── LIBRARY MODAL SONGS ── */
.lib-list{display:grid;grid-template-columns:1fr 1fr;gap:8px;max-height:340px;overflow-y:auto;margin-bottom:14px}
.lib-item{background:var(--bg3);border:1px solid rgba(255,255,255,.07);border-radius:var(--rad);padding:12px;cursor:pointer;transition:all .15s}
.lib-item:hover{border-color:var(--acc);background:rgba(200,240,100,.06)}
.lib-item.added{border-color:var(--acc2);opacity:.5;cursor:default}
.lib-item-title{font-size:13px;font-weight:700}
.lib-item-artist{font-size:11px;color:var(--txt2);margin-top:2px;font-family:'DM Mono',monospace}

/* ── TOAST ── */
.toast{position:fixed;bottom:170px;left:50%;transform:translateX(-50%) translateY(10px);background:var(--bg3);border:1px solid rgba(255,255,255,.1);border-radius:30px;padding:10px 20px;font-size:13px;font-weight:600;opacity:0;transition:all .3s;z-index:200;white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

/* ── SCROLLBAR ── */
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--bg4);border-radius:3px}

/* ── RESPONSIVE ── */
@media(max-width:900px){
  .app{grid-template-columns:220px 1fr;grid-template-rows:64px 1fr 1fr 140px}
  .rightpanel{grid-column:1/-1;grid-row:3/4;border-left:none;border-top:1px solid rgba(255,255,255,.06)}
}
</style>
</head>
<body>
<div class="app">

<!-- TOPBAR -->
<header class="topbar">
  <div class="logo">melodia<span>.</span></div>
  <div class="search-wrap">
    <span class="search-icon">⌕</span>
    <input id="searchInput" type="text" placeholder="Search songs, artists…" oninput="onSearch(this.value)">
  </div>
  <div class="header-btns">
    <button class="btn-icon" onclick="openExport()">⬇ Export</button>
    <button class="btn-icon" onclick="openStats()">◎ Stats</button>
  </div>
</header>

<!-- SIDEBAR -->
<aside class="sidebar">
  <div class="sidebar-title">Playlists</div>
  <div class="pl-list" id="playlists"></div>
  <div class="sidebar-bottom">
    <button class="btn-create" onclick="openCreatePlaylist()">+ New Playlist</button>
  </div>
</aside>

<!-- MAIN CONTENT -->
<main class="main">
  <div id="mainContent">
    <div class="empty">
      <div class="empty-icon">♪</div>
      <div class="empty-text">No playlist selected</div>
      <div class="empty-sub">Create or select a playlist to start</div>
    </div>
  </div>
</main>

<!-- RIGHT PANEL -->
<aside class="rightpanel">
  <div class="lyrics-panel" id="lyricsPanel">
    <div class="now-playing-art" id="nowArt">♪</div>
    <div class="now-title" id="nowTitle">Not playing</div>
    <div class="now-artist" id="nowArtist">Select a song to play</div>
    <h3>Lyrics</h3>
    <div class="lyrics-text" id="lyricsText">—</div>
  </div>
  <div id="statsSection" style="display:none"></div>
</aside>

<!-- PLAYER BAR -->
<footer class="player">
  <div class="player-left">
    <div class="player-art" id="playerArt">♪</div>
    <div class="player-info">
      <div class="player-title" id="playerTitle">Not playing</div>
      <div class="player-artist" id="playerArtist">—</div>
    </div>
    <button class="player-fav" id="playerFav" onclick="toggleFavCurrent()">♡</button>
  </div>
  <div class="player-center">
    <div class="controls">
      <button class="ctrl-btn" id="shuffleBtn" onclick="doShuffle()" title="Shuffle">⇄</button>
      <button class="ctrl-btn" onclick="prevSong()" title="Previous">⏮</button>
      <button class="play-btn" id="playBtn" onclick="togglePlay()">▶️</button>
      <button class="ctrl-btn" onclick="nextSong()" title="Next">⏭</button>
      <button class="ctrl-btn" id="repeatBtn" onclick="doRepeat()" title="Repeat">↻</button>
    </div>
    <div class="progress-wrap">
      <span class="prog-time" id="timeCur">0:00</span>
      <div class="progress" id="progressBar" onclick="seekTo(event)">
        <div class="progress-fill" id="progressFill"></div>
      </div>
      <span class="prog-time" id="timeTot">3:30</span>
    </div>
  </div>
  <div class="player-right">
    <span class="vol-icon">♪</span>
    <input type="range" class="vol-slider" id="volSlider" min="0" max="100" value="80">
  </div>
</footer>

</div>

<!-- MODALS -->
<div class="overlay" id="createModal">
  <div class="modal">
    <h2>New Playlist</h2>
    <input id="plNameInput" type="text" placeholder="Playlist name…" onkeydown="if(event.key==='Enter')createPlaylist()">
    <div class="modal-btns">
      <button class="btn btn-ghost btn-sm" onclick="closeModal('createModal')">Cancel</button>
      <button class="btn btn-primary btn-sm" onclick="createPlaylist()">Create</button>
    </div>
  </div>
</div>

<div class="overlay" id="addSongModal">
  <div class="modal">
    <h2>Add Songs</h2>
    <div class="lib-list" id="libList"></div>
    <div class="modal-btns">
      <button class="btn btn-ghost btn-sm" onclick="closeModal('addSongModal')">Done</button>
    </div>
  </div>
</div>

<div class="overlay" id="statsModal">
  <div class="modal">
    <h2>Playlist Stats</h2>
    <div id="statsContent"></div>
    <div class="modal-btns">
      <button class="btn btn-ghost btn-sm" onclick="closeModal('statsModal')">Close</button>
    </div>
  </div>
</div>

<div class="overlay" id="exportModal">
  <div class="modal">
    <h2>Export Playlist</h2>
    <textarea id="exportText" rows="12" style="resize:none;font-family:'DM Mono',monospace;font-size:12px;line-height:1.6" readonly></textarea>
    <div class="modal-btns">
      <button class="btn btn-ghost btn-sm" onclick="closeModal('exportModal')">Close</button>
      <button class="btn btn-primary btn-sm" onclick="copyExport()">Copy</button>
    </div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
// ─── STATE ───
let queue = [];
let qIdx  = -1;
let isPlaying = false;
let isRepeat  = false;
let isShuffle = false;
let progTimer = null;
let progSec   = 0;
let progTotal = 210;
let currentFav = false;

// ─── UTILS ───
const $ = id => document.getElementById(id);
function toast(msg, dur=2200){
  const el=$('toast'); el.textContent=msg; el.classList.add('show');
  setTimeout(()=>el.classList.remove('show'),dur);
}
async function api(path,data){
  const opts=data?{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}:{};
  const r=await fetch(path,opts); return r.json();
}

// ─── PLAYLISTS ───
async function loadPlaylists(){
  const d=await api('/api/playlists');
  const el=$('playlists'); el.innerHTML='';
  d.playlists.forEach(p=>{
    const div=document.createElement('div');
    div.className='pl-item'+(p.name===d.current?' active':'');
    div.innerHTML=`<div class="pl-icon">♬</div><div class="pl-info"><div class="pl-name">${p.name}</div><div class="pl-count">${p.count} songs</div></div>`;
    div.onclick=()=>selectPlaylist(p.name);
    el.appendChild(div);
  });
}
function openCreatePlaylist(){
  $('plNameInput').value='';
  $('createModal').classList.add('show');
  setTimeout(()=>$('plNameInput').focus(),100);
}
async function createPlaylist(){
  const name=$('plNameInput').value.trim();
  if(!name)return;
  const d=await api('/api/playlists',{name});
  if(d.ok){closeModal('createModal');loadPlaylists();loadSongs();toast('Playlist created ✓');}
  else toast(d.msg);
}
async function selectPlaylist(name){
  await api('/api/playlists/select',{name});
  queue=[];qIdx=-1;isPlaying=false;updatePlayerBar(null);
  loadPlaylists();loadSongs();
}

// ─── SONGS ───
async function loadSongs(filter=''){
  let songs;
  if(filter) songs=(await api(`/api/songs/search?q=${encodeURIComponent(filter)}`));
  else        songs=(await api('/api/songs'));

  const el=$('mainContent');
  if(!Array.isArray(songs)||songs.length===0){
    const d=await api('/api/playlists');
    if(!d.current){
      el.innerHTML=`<div class="empty"><div class="empty-icon">♪</div><div class="empty-text">No playlist selected</div><div class="empty-sub">Create or select a playlist to start</div></div>`;
      return;
    }
    el.innerHTML=`<div class="section-header"><div class="section-title">${d.current}</div><div style="display:flex;gap:8px"><button class="btn-icon" onclick="openAddSong()">+ Add Songs</button><button class="btn-icon" onclick="undoDelete()">↩ Undo</button></div></div><div class="empty" style="height:50%"><div class="empty-icon" style="font-size:40px">♩</div><div class="empty-text">${filter?'No results':'Playlist is empty'}</div><div class="empty-sub">${filter?'Try a different search':'Add songs from the library'}</div></div>`;
    return;
  }

  const d=await api('/api/playlists');
  let html=`<div class="section-header"><div class="section-title">${d.current||'Songs'}</div><div style="display:flex;gap:8px"><button class="btn-icon" onclick="openAddSong()">+ Add Songs</button><button class="btn-icon" onclick="undoDelete()">↩ Undo</button></div></div><div class="song-grid">`;

  songs.forEach((s,i)=>{
    const stars=Array.from({length:5},(_,j)=>`<span class="star${j<s.rating?' on':''}" onclick="rateSong('${escape(s.title)}',${j+1});event.stopPropagation()">★</span>`).join('');
    const isNow=(qIdx>=0&&queue[qIdx]&&queue[qIdx].title===s.title);
    html+=`<div class="song-card${isNow?' playing':''}" onclick="playSong('${escape(s.title)}',${i})">
      <div class="song-num">${isNow?`<div class="eq-bar"></div><div class="eq-bar"></div><div class="eq-bar"></div>`:i+1}</div>
      <div class="song-thumb">${emojiFor(s.artist)}</div>
      <div class="song-meta">
        <div class="song-title">${s.title}</div>
        <div class="song-artist">${s.artist}</div>
      </div>
      <div class="song-rating">${stars}<span class="song-plays">${s.play_count} plays</span></div>
      <div class="song-actions">
        <button class="action-btn fav${s.is_favourite?' active':''}" onclick="toggleFav('${escape(s.title)}');event.stopPropagation()" title="Favourite">♥️</button>
        <button class="action-btn del" onclick="deleteSong('${escape(s.title)}');event.stopPropagation()" title="Delete">🗑</button>
      </div>
    </div>`;
  });
  html+='</div>';
  el.innerHTML=html;
  queue=songs;
}

function emojiFor(artist){
  const map={'Ed Sheeran':'🎸','Imagine Dragons':'🎵','The Chainsmokers':'🎧','Alan Walker':'🎛','The Stranglers':'🎶','The Weeknd':'🌃','Dua Lipa':'💃','The Kid LAROI & Justin Bieber':'🎤'};
  return map[artist]||'🎵';
}

function escape(s){return s.replace(/'/g,"\\'")}

async function openAddSong(){
  const [lib,songs]=await Promise.all([api('/api/library'),api('/api/songs')]);
  const inPl=new Set(songs.map(s=>s.title));
  $('libList').innerHTML=lib.map(s=>`<div class="lib-item${inPl.has(s.title)?' added':''}" onclick="${inPl.has(s.title)?'':`addSong('${escape(s.title)}')`}">
    <div class="lib-item-title">${s.title}</div>
    <div class="lib-item-artist">${s.artist}</div>
    ${inPl.has(s.title)?'<div style="font-size:10px;color:var(--acc2);margin-top:4px">Already added</div>':''}
  </div>`).join('');
  $('addSongModal').classList.add('show');
}
async function addSong(title){
  const d=await api('/api/songs/add',{title});
  if(d.ok){toast(`Added: ${title}`);openAddSong();loadSongs();}
  else toast(d.msg);
}
async function deleteSong(title){
  await api('/api/songs/delete',{title:unescape(title)});
  loadSongs();toast('Deleted — press ↩ Undo to restore');
}
async function undoDelete(){
  const d=await api('/api/songs/undo',{});
  if(d.ok) toast(`↩ Restored: ${d.title}`);
  else toast('Nothing to undo');
  loadSongs();
}
async function toggleFav(title){
  const d=await api('/api/songs/favourite',{title:unescape(title)});
  loadSongs();
  if(qIdx>=0&&queue[qIdx]&&queue[qIdx].title===unescape(title)){
    currentFav=d.state;
    $('playerFav').textContent=currentFav?'♥️':'♡';
    $('playerFav').classList.toggle('on',currentFav);
  }
}
async function toggleFavCurrent(){
  if(qIdx<0||!queue[qIdx])return;
  toggleFav(queue[qIdx].title);
}
async function rateSong(title,rating){
  await api('/api/songs/rate',{title:unescape(title),rating});
  loadSongs();toast(`Rated ${rating} ★`);
}

// ─── PLAYBACK ───
async function playSong(title,idx){
  title=unescape(title);
  const d=await api('/api/songs/play',{title});
  if(!d.ok)return;
  qIdx=queue.findIndex(s=>s.title===title);
  if(qIdx<0)qIdx=idx;
  const s=d.song;
  isPlaying=true;
  currentFav=s.is_favourite;
  updatePlayerBar(s);
  updateNowPlaying(s);
  startProgress();
  loadSongs();
}
function updatePlayerBar(s){
  if(!s){
    $('playerTitle').textContent='Not playing';
    $('playerArtist').textContent='—';
    $('playerArt').textContent='♪';
    $('playerFav').textContent='♡';
    $('playerFav').classList.remove('on');
    $('playBtn').textContent='▶️';
    return;
  }
  $('playerTitle').textContent=s.title;
  $('playerArtist').textContent=s.artist;
  $('playerArt').textContent=emojiFor(s.artist);
  $('playerFav').textContent=s.is_favourite?'♥️':'♡';
  $('playerFav').classList.toggle('on',s.is_favourite);
  $('playBtn').textContent='⏸';
}
function updateNowPlaying(s){
  $('nowArt').textContent=emojiFor(s.artist);
  $('nowTitle').textContent=s.title;
  $('nowArtist').textContent=s.artist;
  $('lyricsText').textContent=s.lyrics;
}
function togglePlay(){
  if(qIdx<0){toast('Select a song first');return;}
  isPlaying=!isPlaying;
  $('playBtn').textContent=isPlaying?'⏸':'▶️';
  if(isPlaying)startProgress(); else clearInterval(progTimer);
}
function nextSong(){
  if(!queue.length)return;
  let next=qIdx+1;
  if(next>=queue.length) next=isRepeat?0:-1;
  if(next<0){toast('End of playlist');isPlaying=false;$('playBtn').textContent='▶️';return;}
  playSong(queue[next].title,next);
}
function prevSong(){
  if(!queue.length)return;
  let prev=qIdx-1;
  if(prev<0)prev=0;
  playSong(queue[prev].title,prev);
}
async function doShuffle(){
  await api('/api/playlist/shuffle',{});
  const songs=await api('/api/songs');
  queue=songs; qIdx=0;
  isShuffle=!isShuffle;
  $('shuffleBtn').classList.toggle('active',isShuffle);
  toast('Shuffled ⇄');
  loadSongs();
}
async function doRepeat(){
  const d=await api('/api/playlist/repeat',{});
  isRepeat=d.repeat;
  $('repeatBtn').classList.toggle('active',isRepeat);
  toast(isRepeat?'Repeat ON ↻':'Repeat OFF');
}

// Progress bar simulation
function startProgress(){
  clearInterval(progTimer);
  progSec=0; progTotal=210;
  progTimer=setInterval(()=>{
    if(!isPlaying)return;
    progSec++;
    if(progSec>=progTotal){clearInterval(progTimer);nextSong();return;}
    $('progressFill').style.width=(progSec/progTotal*100)+'%';
    $('timeCur').textContent=fmt(progSec);
    $('timeTot').textContent=fmt(progTotal);
  },1000);
}
function fmt(s){return `${Math.floor(s/60)}:${String(s%60).padStart(2,'0')}`}
function seekTo(e){
  const r=e.currentTarget.getBoundingClientRect();
  const pct=(e.clientX-r.left)/r.width;
  progSec=Math.floor(pct*progTotal);
  $('progressFill').style.width=(pct*100)+'%';
  $('timeCur').textContent=fmt(progSec);
}

// ─── SEARCH ───
let searchTimer;
function onSearch(val){
  clearTimeout(searchTimer);
  searchTimer=setTimeout(()=>loadSongs(val),250);
}

// ─── STATS ───
async function openStats(){
  const d=await api('/api/playlist/stats');
  if(!d.total){toast('No stats yet');return;}
  $('statsContent').innerHTML=`
    <div class="stats-grid" style="padding:0;margin-bottom:16px">
      <div class="stat-card"><div class="stat-val">${d.total}</div><div class="stat-label">songs</div></div>
      <div class="stat-card"><div class="stat-val">${d.total_plays}</div><div class="stat-label">total plays</div></div>
      <div class="stat-card"><div class="stat-val">${d.favourites}</div><div class="stat-label">favourites</div></div>
      <div class="stat-card"><div class="stat-val">${d.avg_rating}/5</div><div class="stat-label">avg rating</div></div>
    </div>
    <div style="font-size:13px;color:var(--txt2);line-height:2;font-family:'DM Mono',monospace">
      <div>Most played: <span style="color:var(--acc)">${d.top_played}</span></div>
      <div>Highest rated: <span style="color:var(--acc)">${d.top_rated}</span></div>
      <div>Repeat: <span style="color:${d.repeat?'var(--acc)':'var(--acc3)'}">${d.repeat?'ON':'OFF'}</span></div>
    </div>`;
  $('statsModal').classList.add('show');
}

// ─── EXPORT ───
async function openExport(){
  const d=await api('/api/playlist/export');
  if(!d.ok){toast('No playlist to export');return;}
  $('exportText').value=d.text;
  $('exportModal').classList.add('show');
}
function copyExport(){
  navigator.clipboard.writeText($('exportText').value);
  toast('Copied to clipboard ✓');
}

// ─── MODALS ───
function closeModal(id){$(id).classList.remove('show');}
document.querySelectorAll('.overlay').forEach(o=>o.addEventListener('click',e=>{if(e.target===o)o.classList.remove('show')}));

// ─── KEYBOARD ───
document.addEventListener('keydown',e=>{
  if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA')return;
  if(e.code==='Space'){e.preventDefault();togglePlay();}
  if(e.code==='ArrowRight')nextSong();
  if(e.code==='ArrowLeft')prevSong();
});

// ─── INIT ───
loadPlaylists();
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

# ─────────────────────────────────────────────
# LAUNCH
# ─────────────────────────────────────────────
if __name__ == "__main__":
    def open_browser():
        time.sleep(1)
        webbrowser.open("http://127.0.0.1:5000")
    threading.Thread(target=open_browser, daemon=True).start()
    print("\n  🎵  Melodia Music Player")
    print("  ─────────────────────────────")
    print("  Running at: http://127.0.0.1:5000")
    print("  Press  Ctrl+C  to stop\n")
    app.run(debug=False, port=5000)