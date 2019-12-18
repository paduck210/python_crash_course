def make_album(artist_name, album_name):
    album = {}
    album['artist_name'] = artist_name
    album['album_name'] = album_name
    return(album)

while True:
    print('Input q to escape')
    artist_name = input("artist name: ")
    if artist_name == 'q': break
    album_name = input("album name: ")
    if album_name == 'q': break
    print(make_album(artist_name, album_name))

