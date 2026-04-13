import random
import pygame

# Initialize Audio Mixer
pygame.mixer.init()


# ------------------------------------------
# Song Node Class (Doubly Linked List Node)
# ------------------------------------------
class SongNode:
    def __init__(self, title, artist, filepath, lyrics):
        self.title = title
        self.artist = artist
        self.filepath = filepath
        self.lyrics = lyrics

        self.prev = None
        self.next = None


# ------------------------------------------
# Playlist Class (Doubly Linked List)
# ------------------------------------------
class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    # Add Song
    def add_song(self, title, artist, filepath, lyrics):
        new_song = SongNode(title, artist, filepath, lyrics)

        if self.head is None:
            self.head = self.tail = self.current = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song

        print(f"Song Added: {title}")

    # Display Playlist
    def display_playlist(self):
        if self.head is None:
            print("Playlist is empty!")
            return

        print("\n🎵 Playlist Songs:")
        temp = self.head
        count = 1
        while temp:
            print(f"{count}. {temp.title} - {temp.artist}")
            temp = temp.next
            count += 1
        print()

    # Play Current Song
    def play_song(self):
        if self.current is None:
            print("No song selected!")
            return

        print(f"\n▶ Now Playing: {self.current.title} - {self.current.artist}")

        pygame.mixer.music.load(self.current.filepath)
        pygame.mixer.music.play()

    # Stop Song
    def stop_song(self):
        pygame.mixer.music.stop()
        print("⏹ Song Stopped!")

    # Pause Song
    def pause_song(self):
        pygame.mixer.music.pause()
        print("⏸ Song Paused!")

    # Resume Song
    def resume_song(self):
        pygame.mixer.music.unpause()
        print("▶ Song Resumed!")

    # Next Song
    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play_song()
        else:
            print("Already at Last Song!")

    # Previous Song
    def previous_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.play_song()
        else:
            print("Already at First Song!")

    # Shuffle Playlist
    def shuffle_playlist(self):
        if self.head is None:
            print("Playlist is empty!")
            return

        songs = []
        temp = self.head
        while temp:
            songs.append(temp)
            temp = temp.next

        random.shuffle(songs)

        # Rebuild Doubly Linked List
        self.head = songs[0]
        self.head.prev = None

        for i in range(len(songs) - 1):
            songs[i].next = songs[i + 1]
            songs[i + 1].prev = songs[i]

        self.tail = songs[-1]
        self.tail.next = None
        self.current = self.head

        print("Playlist Shuffled Successfully!")
        self.play_song()

    # Show Lyrics
    def show_lyrics(self):
        if self.current is None:
            print("No song is playing!")
            return

        print("\n🎤 Lyrics / Description:")
        print("------------------------------------")
        print(self.current.lyrics)
        print("------------------------------------")


# ------------------------------------------
# Main Music Player Menu
# ------------------------------------------
def menu():
    playlist = Playlist()

    # Classroom-Friendly Instrumental Songs Preloaded
    playlist.add_song(
        "River Flows Piano",
        "Instrumental",
        "songs/river.mp3",
        "Relaxing calm piano music for classroom demo."
    )

    playlist.add_song(
        "Canon in D",
        "Classical Instrumental",
        "songs/canon.mp3",
        "A soft classical instrumental composition."
    )

    playlist.add_song(
        "Magic Theme (Harry Potter Style)",
        "Fantasy Instrumental",
        "songs/hp.mp3",
        "A magical fantasy background theme."
    )

    playlist.add_song(
        "Space Cinematic (Interstellar Style)",
        "Cinematic Instrumental",
        "songs/interstellar.mp3",
        "Epic space ambience cinematic instrumental track."
    )

    while True:
        print("\n========== 🎶 MUSIC PLAYER MENU ==========")
        print("1. Display Playlist")
        print("2. Play Current Song")
        print("3. Next Song")
        print("4. Previous Song")
        print("5. Pause Song")
        print("6. Resume Song")
        print("7. Stop Song")
        print("8. Shuffle Playlist")
        print("9. Show Lyrics")
        print("10. Exit")
        print("=========================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            playlist.display_playlist()

        elif choice == 2:
            playlist.play_song()

        elif choice == 3:
            playlist.next_song()

        elif choice == 4:
            playlist.previous_song()

        elif choice == 5:
            playlist.pause_song()

        elif choice == 6:
            playlist.resume_song()

        elif choice == 7:
            playlist.stop_song()

        elif choice == 8:
            playlist.shuffle_playlist()

        elif choice == 9:
            playlist.show_lyrics()

        elif choice == 10:
            playlist.stop_song()
            print("Exiting Music Player. Goodbye!")
            break

        else:
            print("Invalid Choice! Try again.")


# Run Program
if __name__ == "__main__":
    menu()
