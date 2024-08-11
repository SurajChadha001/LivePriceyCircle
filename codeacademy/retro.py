user_tags = set()
for song in user_song_history:
    user_tags.update(friend_song_history[song])

friend_tags = set()
for song in friend_song_history:
    user_tags.update(friend_song_history[song])

unique_tags = user_tags.symmetric_difference(friend_tags)
print(unique_tags)