import random
import pygame
import time

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

        print("Song Added Successfully!")

    # Add Song Dynamically
    def add_new_song(self):
        title = input("Enter Song Title: ")
        artist = input("Enter Artist/Composer: ")
        filepath = input("Enter File Path (example: songs/song.mp3): ")

        print("Enter Lyrics (use \\n for multiple lines):")
        lyrics = input("Lyrics: ")

        self.add_song(title, artist, filepath, lyrics)

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

    # Select Song by Number
    def select_song_by_number(self, song_number):
        temp = self.head
        count = 1

        while temp:
            if count == song_number:
                self.current = temp
                self.play_song()
                return
            temp = temp.next
            count += 1

        print("Invalid Song Number!")

    # Delete Song by Number
    def delete_song(self, song_number):
        if self.head is None:
            print("Playlist is empty!")
            return

        temp = self.head
        count = 1

        while temp:
            if count == song_number:

                # If deleting head
                if temp == self.head:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None

                # If deleting tail
                elif temp == self.tail:
                    self.tail = temp.prev
                    self.tail.next = None

                # If deleting middle song
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev

                # Reset current song if deleted
                if temp == self.current:
                    self.current = self.head

                print("Song Deleted Successfully!")
                return

            temp = temp.next
            count += 1

        print("Invalid Song Number!")

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
        songs = []
        temp = self.head

        while temp:
            songs.append(temp)
            temp = temp.next

        random.shuffle(songs)

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

    # Real-Time Lyrics Display
    def show_lyrics_realtime(self):
        if self.current is None:
            print("No song is playing!")
            return

        print("\n🎤 Lyrics (Real-Time Display):")
        print("------------------------------------")

        lines = self.current.lyrics.split("\\n")

        for line in lines:
            print(line)
            time.sleep(1.5)

        print("------------------------------------")


# ------------------------------------------
# Main Music Player Menu
# ------------------------------------------
def menu():
    playlist = Playlist()

    # Preloaded Songs
    playlist.add_song(
        "River Flows Piano",
        "Yiruma",
        "songs/river.mp3",
        "Relaxing calm piano music...\nSoft piano tones...\nPeaceful vibes..."
    )

    playlist.add_song(
        "Canon in D",
        "Johann Pachelbel",
        "songs/canon.mp3",
        "Classical melody...\nWedding favorite...\nBaroque masterpiece..."
    )

    while True:
        print("\n========== 🎶 MUSIC PLAYER MENU ==========")
        print("1. Display Playlist")
        print("2. Select Song by Number")
        print("3. Next Song")
        print("4. Previous Song")
        print("5. Pause Song")
        print("6. Resume Song")
        print("7. Stop Song")
        print("8. Shuffle Playlist")
        print("9. Show Lyrics in Real Time")
        print("10. Add New Song")
        print("11. Delete Song")
        print("12. Exit")
        print("=========================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            playlist.display_playlist()

        elif choice == 2:
            playlist.display_playlist()
            num = int(input("Enter song number: "))
            playlist.select_song_by_number(num)

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
            playlist.show_lyrics_realtime()

        elif choice == 10:
            playlist.add_new_song()

        elif choice == 11:
            playlist.display_playlist()
            num = int(input("Enter song number to delete: "))
            playlist.delete_song(num)

        elif choice == 12:
            playlist.stop_song()
            print("Exiting Music Player. Goodbye!")
            break

        else:
            print("Invalid Choice! Try again.")


# Run Program
if __name__ == "__main__":
    menu()