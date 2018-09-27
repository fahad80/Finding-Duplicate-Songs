"""List all the files in a folder"""
import os

num_of_song = 0
song_file = open('listOfSongs.txt', 'w')


for all_song in os.walk('C:\\Users\\Fahad\\Music'):
    # allSong is a list of 3-tuple
    # Actual file names are in the 3rd tuple
    for song in all_song[2]:

        # Just wanted to see what other file format I had
        # split = song.split('.')
        # extension = split[len(split) - 1]

        # if (extension != 'mp3' and extension != 'MP3'):
        #     count2 = count2 + 1
        #     print(song)

        song_file.write(song)
        song_file.write('\r\n')
        num_of_song = num_of_song + 1

print('Total files:' + str(num_of_song))
song_file.close()
