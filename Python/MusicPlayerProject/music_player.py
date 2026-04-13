import random

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
    "Believer": ("Imagine Dragons","""First things first
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
    "Golden Brown": (" The Stranglers", """Golden brown, texture like sun
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
Never a frown with golden brown""")
}


# =========================================================
# MEMBER 1 – SONG NODE
# =========================================================
class Song:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics
        self.is_favourite = False
        self.next = None


# =========================================================
# MEMBER 2 – PLAYLIST CORE (LINKED LIST)
# =========================================================
class Playlist:
    def __init__(self, name):
        self.name = name
        self.head = None
        self.repeat = False

    # 🔹 ADD SONG FROM PREDEFINED LIBRARY
    def add_song_from_library(self):
        songs = list(SONG_LIBRARY.keys())

        print("\n🎶 Available Songs to Add:")
        for i, title in enumerate(songs, start=1):
            print(f"{i}. {title}")

        try:
            choice = int(input("Enter song number to add: ")) - 1
        except ValueError:
            print("Invalid input.")
            return

        if choice < 0 or choice >= len(songs):
            print("Invalid choice.")
            return

        title = songs[choice]
        artist, lyrics = SONG_LIBRARY[title]

        new_song = Song(title, artist, lyrics)

        if not self.head:
            self.head = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song

        print(f"'{title}' by {artist} added to playlist.")

    def delete_song(self, title):
        temp = self.head
        prev = None

        while temp:
            if temp.title == title:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print("Song deleted.")
                return
            prev = temp
            temp = temp.next
        print("Song not found.")

    def shuffle(self):
        songs = []
        temp = self.head
        while temp:
            songs.append(temp)
            temp = temp.next

        if not songs:
            print("Playlist empty.")
            return

        random.shuffle(songs)
        for i in range(len(songs) - 1):
            songs[i].next = songs[i + 1]
        songs[-1].next = None
        self.head = songs[0]
        print("Playlist shuffled.")

    def toggle_repeat(self):
        self.repeat = not self.repeat
        print("Repeat:", "ON" if self.repeat else "OFF")

    def list_songs(self):
        if not self.head:
            print("Playlist empty.")
            return []

        songs = []
        temp = self.head
        index = 1

        print("\n🎵 Songs in Playlist:")
        while temp:
            fav = "❤️" if temp.is_favourite else ""
            print(f"{index}. {temp.title} - {temp.artist} {fav}")
            songs.append(temp)
            temp = temp.next
            index += 1

        return songs


# =========================================================
# MEMBER 3 – PLAYBACK LOGIC
# =========================================================
class Playback:
    def play_flow(self, playlist):
        songs = playlist.list_songs()
        if not songs:
            return

        try:
            pos = int(input("\nEnter song number to play: ")) - 1
        except ValueError:
            print("Invalid input.")
            return

        if pos < 0 or pos >= len(songs):
            print("Invalid choice.")
            return

        current = songs[pos]
        is_paused = False   # 🔹 Pause state

        while current:
            if not is_paused:
                print(f"\n▶️ Now Playing: {current.title} - {current.artist}")
                print(f"📜 Lyrics: {current.lyrics}")
            else:
                print(f"\n⏸ Paused: {current.title} - {current.artist}")

            print("""
1. Next Song
2. Add to Favourites
3. Delete This Song
4. Shuffle Playlist
5. Toggle Repeat
6. Pause / Resume
7. Exit Playback
""")

            choice = input("Enter choice: ")

            if choice == "1":
                if is_paused:
                    print("Resume the song first.")
                else:
                    if current.next:
                        current = current.next
                    elif playlist.repeat:
                        current = playlist.head
                    else:
                        print("End of playlist.")
                        break

            elif choice == "2":
                current.is_favourite = True
                print("Added to favourites ❤️")

            elif choice == "3":
                playlist.delete_song(current.title)
                break

            elif choice == "4":
                playlist.shuffle()
                break

            elif choice == "5":
                playlist.toggle_repeat()

            elif choice == "6":
                is_paused = not is_paused
                print("Paused ⏸️" if is_paused else "Resumed ▶️")

            elif choice == "7":
                break

            else:
                print("Invalid choice.")



# =========================================================
# MEMBER 5 – CONTROLLER & MENU
# =========================================================
class MusicPlayer:
    def __init__(self):
        self.playlists = {}
        self.current_playlist = None
        self.playback = Playback()

    def create_playlist(self):
        name = input("Playlist name: ")
        self.playlists[name] = Playlist(name)
        print("Playlist created.")

    def select_playlist(self):
        name = input("Playlist name: ")
        if name in self.playlists:
            self.current_playlist = self.playlists[name]
            print(f"Playlist '{name}' selected.")
        else:
            print("Playlist not found.")

    def show_playlists(self):
        print("\n📂 Playlists:")
        for p in self.playlists:
            print("-", p)


# =========================================================
# MAIN PROGRAM
# =========================================================
player = MusicPlayer()

while True:
    print("""
========= MUSIC PLAYER =========
1. Create Playlist
2. Select Playlist
3. Add Song (from library)
4. Show Songs in Playlist
5. Play Songs
6. Show Playlists
0. Exit
""")

    ch = input("Enter choice: ")

    if ch == "1":
        player.create_playlist()

    elif ch == "2":
        player.select_playlist()

    elif ch == "3":
        if player.current_playlist:
            player.current_playlist.add_song_from_library()
        else:
            print("Select playlist first.")

    elif ch == "4":
        if player.current_playlist:
            player.current_playlist.list_songs()
        else:
            print("Select playlist first.")

    elif ch == "5":
        if player.current_playlist:
            player.playback.play_flow(player.current_playlist)
        else:
            print("Select playlist first.")

    elif ch == "6":
        player.show_playlists()

    elif ch == "0":
        print("Music Player Closed.")
        break

    else:
        print("Invalid choice.")