"""Compare song titles"""

list_of_songs = []


with open('listOfSongs.txt', 'r') as song_file:
    allSong_list = song_file.read().lower().split('\n\n')

for song in allSong_list:
    split_words = song.split('.')
    # There can be more '.' in the song title. We are interested about the last one
    extension = split_words[len(split_words) - 1]
    # now let's separate the extension from the song title
    song_title = song.split('.' + extension)[0]
    list_of_songs.append(song_title)


num_of_duplicate_songs = 0
starting_index = 1
for song in list_of_songs:
    for i in range(starting_index, len(list_of_songs)):
        if song == list_of_songs[i]:
            print(song)
            num_of_duplicate_songs = num_of_duplicate_songs + 1
    # You don't want to start searching from the beginning.
    # Otherwise you will end up comparing with itself
    starting_index = starting_index + 1

print('Total Duplicate = ' + str(num_of_duplicate_songs))
