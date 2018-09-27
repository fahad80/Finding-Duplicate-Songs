import os
import sys

listOfSongsName = []
listOfSongsFile = open('listOfSongs.txt','r')

allSong_str = listOfSongsName.read().lower()


allSong_list = allSong_str.split('\n\n')

for song in allSong_list:
    split_words = song.split('.')
    # There can be more '.' in the song name. We are interested about the last one
    extension = split_words[len(split_words) - 1]
    # now let's separate the extension from the song name
    song_name = song.split('.' + extension)[0]
    listOfSongsName.append(song_name)


numOfDuplicateSong = 0
startingIndex = 1
for songName in listOfSongName:
    for i in range(startingIndex, len(listOfSongsName)):
        if songName == listOfSongsName[i]:
            print(songName)
            numOfDuplicateSong = numOfDuplicateSong + 1
    # You don't want to start searching from the beginning.
    # Otherwise you will end up comparing with itself
    startingIndex = startingIndex + 1

print('Total Duplicate = ' + str(numOfDuplicateSong) )
listOfSongsFile.close()
