import os
import sys

list_of_songs = []
list_of_songs_file = open('listOfSongs.txt', 'r')

allSong_str = list_of_songs.read().lower()


allSong_list = allSong_str.split('\n\n')

for song in allSong_list:
    split_words = song.split('.')
    # There can be more '.' in the song name. We are interested about the last one
    extension = split_words[len(split_words) - 1]
    # now let's separate the extension from the song name
    song_name = song.split('.' + extension)[0]
    list_of_songs.append(song_name)


numOfDuplicateSong = 0
startingIndex = 1
for songName in listOfSongName:
    for i in range(startingIndex, len(list_of_songs)):
        if songName == list_of_songs[i]:
            print(songName)
            numOfDuplicateSong = numOfDuplicateSong + 1
    # You don't want to start searching from the beginning.
    # Otherwise you will end up comparing with itself
    startingIndex = startingIndex + 1

print('Total Duplicate = ' + str(numOfDuplicateSong))
list_of_songs_file.close()
