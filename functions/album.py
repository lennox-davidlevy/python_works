def make_album(artist_name, album_title, num_songs=None):
    if num_songs:
        return {"artist": artist_name, "album": album_title, "num_songs": num_songs}
    else:
        return {"artist": artist_name, "album": album_title}


album_list = []

active_flag = True
while active_flag:
    artist = input("input artist: ")
    album = input("input album: ")
    num_songs = input("input number of tracks: ")
    album_list.append(make_album(artist, album, num_songs and num_songs))
    repeat = input("continue (yes/no)? ")
    if repeat == "no" or repeat == "n":
        active_flag = False


print("\n--- LIST OF ALBUMS ---")
print("Artist -------- Album -------- No. of Songs\n")
for album in album_list:
    artist = album["artist"].title()
    title = album["album"].title()
    if album["num_songs"]:
        num_songs = album["num_songs"]
        print(f"{artist} -- {title} -- {num_songs}")
    else:
        print(f"{artist} -- {title}")
