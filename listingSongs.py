import os, sys
numOfSong = 0
count2 = 0
listOfSongsFile = open('listOfSongs.txt','w')


for allSong in os.walk('C:\\Users\\Fahad\\Music'):
    # allSong is a list of 3-tuple
    # Actual file names are in the 3rd tuple
    for song in allSong[2]:

        # Just wanted to see what other file format I had
        #split = song.split('.')
        #extension = split[len(split) - 1]
        
        #if (extension != 'mp3' and extension != 'MP3'):
        #    count2 = count2 + 1
        #    print(song)

        listOfSongsFile.write(song)
        listOfSongsFile.write('\r\n')
        numOfSong = numOfSong + 1

print('Total files:' + str(numOfSong))
#print('Total not mp3:' + str(count2))
listOfSongsFile.close()
