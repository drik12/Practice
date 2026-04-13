import random

class SongNode:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None


    def add_song(self, title, artist, lyrics):
        new_song = SongNode(title, artist, lyrics)

        if self.head is None:
            self.head = self.tail = self.current = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song


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

        self.head = songs[0]
        self.head.prev = None

        for i in range(len(songs) - 1):
            songs[i].next = songs[i + 1]
            songs[i + 1].prev = songs[i]

        self.tail = songs[-1]
        self.tail.next = None

        self.current = self.head

        print("Playlist Shuffled Successfully!")


    def show_lyrics(self):
        if self.current is None:
            print("No song playing!")
            return

        print("\nLyrics:", self.current.title)
        print("--------------------------------")
        print(self.current.lyrics)
        print("--------------------------------\n")