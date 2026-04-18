import random
import os
import datetime


# =========================================================
# ANSI COLOUR CODES FOR BEAUTIFUL TERMINAL UI
# =========================================================
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BG_BLUE = "\033[44m"
    BG_DARK = "\033[40m"

def clr(text, *codes):
    return "".join(codes) + str(text) + Color.RESET

def banner(text):
    width = 44
    print(clr("╔" + "═" * width + "╗", Color.CYAN, Color.BOLD))
    print(clr("║" + text.center(width) + "║", Color.CYAN, Color.BOLD))
    print(clr("╚" + "═" * width + "╝", Color.CYAN, Color.BOLD))

def section(text):
    print(clr(f"\n  ┌─ {text} ", Color.BLUE, Color.BOLD) +
          clr("─" * max(0, 38 - len(text)) + "┐", Color.BLUE))

def divider():
    print(clr("  " + "─" * 42, Color.BLUE))


# =========================================================
# MEMBER 1 – SONG NODE (DOUBLY LINKED LIST)
# =========================================================
class Song:
    def __init__(self, title, artist, lyrics):
        self.title       = title
        self.artist      = artist
        self.lyrics      = lyrics
        self.is_favourite = False
        self.rating      = 0          # ★ NEW: 1–5 stars (0 = unrated)
        self.play_count  = 0          # ★ NEW: how many times played
        self.next        = None
        self.prev        = None


# =========================================================
# MEMBER 2 – PLAYLIST CORE
# =========================================================
class Playlist:
    def __init__(self, name):
        self.name          = name
        self.head          = None
        self.repeat        = False
        self._delete_stack = []        # ★ NEW: undo stack for deleted songs

    # ----------------------------------------------------------
    # ADD SONG
    # ----------------------------------------------------------
    def add_song_from_library(self):
        songs = list(SONG_LIBRARY.keys())
        section("Available Songs")
        for i, title in enumerate(songs, start=1):
            artist = SONG_LIBRARY[title][0]
            print(f"    {clr(str(i)+'.', Color.YELLOW)} {clr(title, Color.WHITE)} "
                  f"{clr('by '+artist, Color.CYAN)}")
        divider()
        try:
            choice = int(input(clr("  Enter song number: ", Color.GREEN))) - 1
        except ValueError:
            print(clr("  ✗ Invalid input.", Color.RED))
            return

        if choice < 0 or choice >= len(songs):
            print(clr("  ✗ Invalid choice.", Color.RED))
            return

        title = songs[choice]

        # Check for duplicates
        temp = self.head
        while temp:
            if temp.title == title:
                print(clr(f"  ⚠ '{title}' is already in the playlist.", Color.YELLOW))
                return
            temp = temp.next

        artist, lyrics = SONG_LIBRARY[title]
        new_song = Song(title, artist, lyrics)

        if not self.head:
            self.head = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song
            new_song.prev = temp

        print(clr(f"\n  ✔ '{title}' by {artist} added to '{self.name}'.", Color.GREEN))

    # ----------------------------------------------------------
    # DELETE SONG  (stores deleted node on undo stack)
    # ----------------------------------------------------------
    def delete_song(self, title):
        temp = self.head
        while temp:
            if temp.title == title:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                # Save isolated node for undo
                temp.next = None
                temp.prev = None
                self._delete_stack.append(temp)
                print(clr(f"  🗑  '{title}' deleted. (Undo available)", Color.YELLOW))
                return
            temp = temp.next
        print(clr("  ✗ Song not found.", Color.RED))

    # ----------------------------------------------------------
    # ★ NEW: UNDO LAST DELETE
    # ----------------------------------------------------------
    def undo_delete(self):
        if not self._delete_stack:
            print(clr("  ✗ Nothing to undo.", Color.RED))
            return
        song = self._delete_stack.pop()
        # Append to end of list
        if not self.head:
            self.head = song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = song
            song.prev = temp
        song.next = None
        print(clr(f"  ↩  '{song.title}' restored to playlist.", Color.GREEN))

    # ----------------------------------------------------------
    # SHUFFLE
    # ----------------------------------------------------------
    def shuffle(self):
        songs = []
        temp = self.head
        while temp:
            songs.append(temp)
            temp = temp.next
        if not songs:
            print(clr("  Playlist is empty.", Color.RED))
            return
        random.shuffle(songs)
        for i in range(len(songs)):
            songs[i].prev = songs[i - 1] if i > 0 else None
            songs[i].next = songs[i + 1] if i < len(songs) - 1 else None
        self.head = songs[0]
        print(clr("  🔀 Playlist shuffled!", Color.MAGENTA))

    # ----------------------------------------------------------
    # TOGGLE REPEAT
    # ----------------------------------------------------------
    def toggle_repeat(self):
        self.repeat = not self.repeat
        state = clr("ON 🔁", Color.GREEN) if self.repeat else clr("OFF", Color.RED)
        print(f"  Repeat: {state}")

    # ----------------------------------------------------------
    # LIST SONGS
    # ----------------------------------------------------------
    def list_songs(self):
        if not self.head:
            print(clr("  Playlist is empty.", Color.RED))
            return []
        songs = []
        temp = self.head
        index = 1
        section(f"Songs in '{self.name}'")
        print(f"  {'#':<4} {'Title':<28} {'Artist':<22} {'★':>3}  {'Plays':>5}  {'Fav'}")
        divider()
        while temp:
            stars = ("★" * temp.rating + "☆" * (5 - temp.rating)) if temp.rating else "☆☆☆☆☆"
            fav   = clr("♥️", Color.RED) if temp.is_favourite else " "
            star_clr = clr(stars, Color.YELLOW)
            print(f"  {clr(str(index)+'.',Color.YELLOW):<13} "
                  f"{clr(temp.title,Color.WHITE):<36} "
                  f"{clr(temp.artist,Color.CYAN):<30} "
                  f"{star_clr}  "
                  f"{clr(str(temp.play_count),Color.MAGENTA):>5}   {fav}")
            songs.append(temp)
            temp = temp.next
            index += 1
        divider()
        return songs

    # ----------------------------------------------------------
    # ★ NEW: SEARCH SONGS
    # ----------------------------------------------------------
    def search(self, query):
        query = query.lower()
        results = []
        temp = self.head
        while temp:
            if query in temp.title.lower() or query in temp.artist.lower():
                results.append(temp)
            temp = temp.next
        return results

    # ----------------------------------------------------------
    # ★ NEW: PLAYLIST STATISTICS
    # ----------------------------------------------------------
    def show_stats(self):
        songs = []
        temp = self.head
        while temp:
            songs.append(temp)
            temp = temp.next

        if not songs:
            print(clr("  Playlist is empty.", Color.RED))
            return

        total_plays = sum(s.play_count for s in songs)
        favourites  = sum(1 for s in songs if s.is_favourite)
        rated       = [s for s in songs if s.rating > 0]
        avg_rating  = round(sum(s.rating for s in rated) / len(rated), 1) if rated else 0
        top_played  = max(songs, key=lambda s: s.play_count)
        top_rated   = max(rated, key=lambda s: s.rating) if rated else None

        section(f"Playlist Stats — '{self.name}'")
        print(f"  Total songs    : {clr(len(songs), Color.CYAN, Color.BOLD)}")
        print(f"  Total plays    : {clr(total_plays, Color.MAGENTA, Color.BOLD)}")
        print(f"  Favourites     : {clr(favourites, Color.RED, Color.BOLD)} ♥️")
        print(f"  Avg rating     : {clr(str(avg_rating)+' / 5', Color.YELLOW, Color.BOLD)}")
        print(f"  Most played    : {clr(top_played.title, Color.GREEN)} "
              f"({clr(top_played.play_count, Color.MAGENTA)} plays)")
        if top_rated:
            print(f"  Highest rated  : {clr(top_rated.title, Color.GREEN)} "
                  f"({clr('★'*top_rated.rating, Color.YELLOW)})")
        print(f"  Repeat mode    : {clr('ON', Color.GREEN) if self.repeat else clr('OFF', Color.RED)}")
        divider()

    # ----------------------------------------------------------
    # ★ NEW: EXPORT PLAYLIST TO .TXT FILE
    # ----------------------------------------------------------
    def export_to_file(self):
        if not self.head:
            print(clr("  Playlist is empty. Nothing to export.", Color.RED))
            return
        filename = f"{self.name.replace(' ','_')}_playlist.txt"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{'='*50}\n")
            f.write(f"  Playlist: {self.name}\n")
            f.write(f"  Exported: {timestamp}\n")
            f.write(f"{'='*50}\n\n")
            temp = self.head
            index = 1
            while temp:
                stars = "★" * temp.rating + "☆" * (5 - temp.rating)
                fav   = " [FAVOURITE]" if temp.is_favourite else ""
                f.write(f"{index}. {temp.title} - {temp.artist}{fav}\n")
                f.write(f"   Rating: {stars}  |  Plays: {temp.play_count}\n\n")
                temp = temp.next
        print(clr(f"  ✔ Exported to '{filename}'", Color.GREEN))


# =========================================================
# MEMBER 3 – PLAYBACK LOGIC
# =========================================================
class Playback:
    def play_flow(self, playlist):
        songs = playlist.list_songs()
        if not songs:
            return

        try:
            pos = int(input(clr("\n  Enter song number to play: ", Color.GREEN))) - 1
        except ValueError:
            print(clr("  ✗ Invalid input.", Color.RED))
            return

        if pos < 0 or pos >= len(songs):
            print(clr("  ✗ Invalid choice.", Color.RED))
            return

        current   = songs[pos]
        is_paused = False

        while current:
            os.system("cls" if os.name == "nt" else "clear")
            banner("♪  NOW PLAYING  ♪")

            if is_paused:
                status = clr("⏸  PAUSED", Color.YELLOW, Color.BOLD)
            else:
                status = clr("▶️  PLAYING", Color.GREEN, Color.BOLD)

            stars = clr("★" * current.rating + "☆" * (5 - current.rating), Color.YELLOW) \
                    if current.rating else clr("☆☆☆☆☆  (unrated)", Color.YELLOW)
            fav   = clr("  ♥️ FAVOURITE", Color.RED) if current.is_favourite else ""

            print(f"\n  {status}")
            print(f"  {clr(current.title, Color.WHITE, Color.BOLD)}")
            print(f"  {clr('by ' + current.artist, Color.CYAN)}")
            print(f"  Rating : {stars}{fav}")
            print(f"  Plays  : {clr(current.play_count, Color.MAGENTA)}\n")

            # Increment play count only when playing (not paused)
            if not is_paused:
                current.play_count += 1

            # Show lyrics
            section("Lyrics")
            for line in current.lyrics.strip().split("\n"):
                print(f"    {clr(line, Color.WHITE)}")
            divider()

            # Controls menu
            print(f"""
  {clr('Controls', Color.BOLD, Color.BLUE)}
  {clr('1', Color.YELLOW)} Next Song          {clr('2', Color.YELLOW)} Previous Song
  {clr('3', Color.YELLOW)} Add to Favourites  {clr('4', Color.YELLOW)} Remove from Fav
  {clr('5', Color.YELLOW)} Rate This Song     {clr('6', Color.YELLOW)} Delete This Song
  {clr('7', Color.YELLOW)} Undo Delete        {clr('8', Color.YELLOW)} Shuffle Playlist
  {clr('9', Color.YELLOW)} Toggle Repeat      {clr('P', Color.YELLOW)} Pause / Resume
  {clr('0', Color.YELLOW)} Exit Playback
""")

            choice = input(clr("  Enter choice: ", Color.GREEN)).strip().upper()

            if choice == "1":
                if current.next:
                    current = current.next
                    is_paused = False
                elif playlist.repeat:
                    current = playlist.head
                    is_paused = False
                else:
                    print(clr("\n  ⏹  End of playlist.", Color.YELLOW))
                    input(clr("  Press Enter to go back...", Color.CYAN))
                    break

            elif choice == "2":
                if current.prev:
                    current = current.prev
                    is_paused = False
                else:
                    print(clr("  ✗ This is the first song.", Color.RED))
                    input(clr("  Press Enter to continue...", Color.CYAN))

            elif choice == "3":
                current.is_favourite = True
                print(clr("  ♥️  Added to favourites!", Color.RED))
                input(clr("  Press Enter to continue...", Color.CYAN))

            elif choice == "4":
                current.is_favourite = False
                print(clr("  ♡  Removed from favourites.", Color.YELLOW))
                input(clr("  Press Enter to continue...", Color.CYAN))

            elif choice == "5":
                # ★ NEW: Rate the current song
                try:
                    r = int(input(clr("  Enter rating (1-5): ", Color.GREEN)))
                    if 1 <= r <= 5:
                        current.rating = r
                        print(clr(f"  ★  Rated {r}/5!", Color.YELLOW))
                    else:
                        print(clr("  ✗ Enter a number between 1 and 5.", Color.RED))
                except ValueError:
                    print(clr("  ✗ Invalid input.", Color.RED))
                input(clr("  Press Enter to continue...", Color.CYAN))

            elif choice == "6":
                playlist.delete_song(current.title)
                input(clr("  Press Enter to go back...", Color.CYAN))
                break

            elif choice == "7":
                # ★ NEW: Undo delete from within playback
                playlist.undo_delete()
                input(clr("  Press Enter to continue...", Color.CYAN))

            elif choice == "8":
                playlist.shuffle()
                input(clr("  Press Enter to go back...", Color.CYAN))
                break

            elif choice == "9":
                playlist.toggle_repeat()
                input(clr("  Press Enter to continue...", Color.CYAN))

            elif choice == "P":
                is_paused = not is_paused
                print(clr("  ⏸  Paused.", Color.YELLOW) if is_paused
                      else clr("  ▶️  Resumed.", Color.GREEN))
                input(clr("  Press Enter to continue...", Color.CYAN))

            elif choice == "0":
                break
            else:
                print(clr("  ✗ Invalid choice.", Color.RED))
                input(clr("  Press Enter to continue...", Color.CYAN))


# =========================================================
# MEMBER 4 – PREDEFINED SONG DATA (LIBRARY)
# =========================================================
SONG_LIBRARY = {
    "Shape of You": ("Ed Sheeran", """The club isn't the best place to find a lover
So the bar is where I go (mm)
Me and my friends at the table doing shots
Drinking fast and then we talk slow (mm)
Come over and start up a conversation with just me
And trust me I'll give it a chance now (mm)
Take my hand, stop, put Van the Man on the jukebox
And then we start to dance, and now I'm singing like
Girl, you know I want your love
Your love was handmade for somebody like me
Come on now, follow my lead
I may be crazy, don't mind me
Say, boy, let's not talk too much
Grab on my waist and put that body on me
Come on now, follow my lead
Come, come on now, follow my lead, mm"""),

    "Believer": ("Imagine Dragons", """First things first
I'ma say all the words inside my head
I'm fired up and tired of the way that things have been, oh-ooh
The way that things have been, oh-ooh
Second thing second
Don't you tell me what you think that I could be
I'm the one at the sail, I'm the master of my sea, oh-ooh
The master of my sea, oh-ooh
I was broken from a young age
Taking my sulking to the masses
Writing my poems for the few
That look at me, took to me, shook to me, feeling me
Singing from heartache from the pain
Taking my message from the veins
Speaking my lesson from the brain
Seeing the beauty through the...
Pain!"""),

    "Perfect": ("Ed Sheeran", """I found a love for me
Darling, just dive right in and follow my lead
Well, I found a girl, beautiful and sweet
Oh, I never knew you were the someone waitin' for me
'Cause we were just kids when we fell in love
Not knowin' what it was
I will not give you up this time
Darling, just kiss me slow
Your heart is all I own
And in your eyes, you're holdin' mine
Baby, I'm dancin' in the dark
With you between my arms
Barefoot on the grass
Listenin' to our favourite song
When you said you looked a mess
I whispered underneath my breath
But you heard it
Darling, you look perfect tonight"""),

    "Closer": ("The Chainsmokers", """Hey, I was doing just fine before I met you
I drink too much and that's an issue, but I'm okay
Hey, you tell your friends it was nice to meet them
But I hope I never see them again
I know it breaks your heart
Moved to the city in a broke-down car, and
Four years, no calls
Now you're lookin' pretty in a hotel bar
And I-I-I can't stop
No, I-I-I can't stop
So, baby, pull me closer in the backseat of your Rover
That I know you can't afford, bite that tattoo on your shoulder
Pull the sheets right off the corner of the mattress that you stole
From your roommate back in Boulder, we ain't ever gettin' older"""),

    "Faded": ("Alan Walker", """You were the shadow to my light
Did you see us?
Another star, you fade away
Afraid our aim is out of sight
Wanna see us, alive
Where are you now?
Where are you now?
Where are you now?
Was it all in my fantasy?
Where are you now?"""),

    "Golden Brown": ("The Stranglers", """Golden brown, texture like sun
Lays me down, with my mind she runs
Throughout the night
No need to fight
Never a frown with golden brown
Every time just like the last
On her ship tied to the mast
To distant lands
Takes both my hands
Never a frown with golden brown
Golden brown, finer temptress
Through the ages she's heading west
From far away
Stays for a day
Never a frown with golden brown"""),
}


# =========================================================
# MEMBER 5 – CONTROLLER
# =========================================================
class MusicPlayer:
    def __init__(self):
        self.playlists        = {}
        self.current_playlist = None
        self.playback         = Playback()

    def create_playlist(self):
        name = input(clr("  Playlist name: ", Color.GREEN)).strip()
        if not name:
            print(clr("  ✗ Name cannot be empty.", Color.RED))
            return
        if name in self.playlists:
            print(clr(f"  ✗ Playlist '{name}' already exists.", Color.RED))
            return
        self.playlists[name] = Playlist(name)
        print(clr(f"  ✔ Playlist '{name}' created!", Color.GREEN))

    def select_playlist(self):
        if not self.playlists:
            print(clr("  ✗ No playlists exist. Create one first.", Color.RED))
            return
        self.show_playlists()
        name = input(clr("  Enter playlist name: ", Color.GREEN)).strip()
        if name in self.playlists:
            self.current_playlist = self.playlists[name]
            print(clr(f"  ✔ Switched to playlist '{name}'.", Color.GREEN))
        else:
            print(clr("  ✗ Playlist not found.", Color.RED))

    def show_playlists(self):
        section("Your Playlists")
        if not self.playlists:
            print(clr("  No playlists yet.", Color.RED))
        for name, pl in self.playlists.items():
            count = 0
            temp = pl.head
            while temp:
                count += 1
                temp = temp.next
            active = clr(" ◀️ active", Color.GREEN) if pl == self.current_playlist else ""
            print(f"  {clr('♫', Color.CYAN)} {clr(name, Color.WHITE)}  "
                  f"{clr(f'[{count} songs]', Color.YELLOW)}{active}")
        divider()

    # ★ NEW: Search across current playlist
    def search_in_playlist(self):
        if not self.current_playlist:
            print(clr("  ✗ Select a playlist first.", Color.RED))
            return
        query = input(clr("  Search by title or artist: ", Color.GREEN)).strip()
        results = self.current_playlist.search(query)
        if not results:
            print(clr(f"  ✗ No songs matching '{query}'.", Color.RED))
        else:
            section(f"Search results for '{query}'")
            for i, s in enumerate(results, 1):
                stars = clr("★" * s.rating + "☆" * (5 - s.rating), Color.YELLOW) if s.rating else ""
                print(f"  {clr(str(i)+'.', Color.YELLOW)} {clr(s.title, Color.WHITE)} "
                      f"— {clr(s.artist, Color.CYAN)} {stars}")
            divider()

    # ★ NEW: Top-5 most played songs in current playlist
    def top_played(self):
        if not self.current_playlist:
            print(clr("  ✗ Select a playlist first.", Color.RED))
            return
        temp, songs = self.current_playlist.head, []
        while temp:
            songs.append(temp)
            temp = temp.next
        if not songs:
            print(clr("  Playlist is empty.", Color.RED))
            return
        top = sorted(songs, key=lambda s: s.play_count, reverse=True)[:5]
        section("Top 5 Most Played")
        for i, s in enumerate(top, 1):
            print(f"  {clr(str(i)+'.', Color.YELLOW)} {clr(s.title, Color.WHITE):<30} "
                  f"{clr(str(s.play_count)+' plays', Color.MAGENTA)}")
        divider()


# =========================================================
# MAIN PROGRAM
# =========================================================
player = MusicPlayer()

while True:
    os.system("cls" if os.name == "nt" else "clear")
    banner("  ♪  MUSIC PLAYER  ♪  ")

    active = (clr(f" [{player.current_playlist.name}]", Color.GREEN)
              if player.current_playlist else clr(" [no playlist selected]", Color.RED))
    print(f"\n  Active playlist:{active}\n")

    print(f"  {clr('── Playlist ──', Color.BLUE, Color.BOLD)}")
    print(f"  {clr('1', Color.YELLOW)} Create Playlist        {clr('2', Color.YELLOW)} Select Playlist")
    print(f"  {clr('3', Color.YELLOW)} Show All Playlists")
    print(f"\n  {clr('── Songs ──', Color.BLUE, Color.BOLD)}")
    print(f"  {clr('4', Color.YELLOW)} Add Song               {clr('5', Color.YELLOW)} Show Songs")
    print(f"  {clr('6', Color.YELLOW)} Search Songs           {clr('7', Color.YELLOW)} Undo Last Delete")
    print(f"\n  {clr('── Playback ──', Color.BLUE, Color.BOLD)}")
    print(f"  {clr('8', Color.YELLOW)} Play Songs")
    print(f"\n  {clr('── Stats & Export ──', Color.BLUE, Color.BOLD)}")
    print(f"  {clr('9', Color.YELLOW)} Playlist Statistics    {clr('T', Color.YELLOW)} Top 5 Most Played")
    print(f"  {clr('E', Color.YELLOW)} Export Playlist to File")
    print(f"\n  {clr('0', Color.YELLOW)} Exit")
    divider()

    ch = input(clr("  Enter choice: ", Color.GREEN)).strip().upper()

    if ch == "1":
        player.create_playlist()

    elif ch == "2":
        player.select_playlist()

    elif ch == "3":
        player.show_playlists()

    elif ch == "4":
        if player.current_playlist:
            player.current_playlist.add_song_from_library()
        else:
            print(clr("  ✗ Select a playlist first.", Color.RED))

    elif ch == "5":
        if player.current_playlist:
            player.current_playlist.list_songs()
        else:
            print(clr("  ✗ Select a playlist first.", Color.RED))

    elif ch == "6":
        player.search_in_playlist()

    elif ch == "7":
        if player.current_playlist:
            player.current_playlist.undo_delete()
        else:
            print(clr("  ✗ Select a playlist first.", Color.RED))

    elif ch == "8":
        if player.current_playlist:
            player.playback.play_flow(player.current_playlist)
        else:
            print(clr("  ✗ Select a playlist first.", Color.RED))

    elif ch == "9":
        if player.current_playlist:
            player.current_playlist.show_stats()
        else:
            print(clr("  ✗ Select a playlist first.", Color.RED))

    elif ch == "T":
        player.top_played()

    elif ch == "E":
        if player.current_playlist:
            player.current_playlist.export_to_file()
        else:
            print(clr("  ✗ Select a playlist first.", Color.RED))

    elif ch == "0":
        banner("  Goodbye! Keep the music playing ♪  ")
        break

    else:
        print(clr("  ✗ Invalid choice.", Color.RED))

    if ch != "0":
        input(clr("\n  Press Enter to continue...", Color.CYAN))