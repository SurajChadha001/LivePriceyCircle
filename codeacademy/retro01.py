user_tags = set()
for key, val in user_song_history.items():
  user_tags.update(set(val))

friend_tags = set()
for key, val in user_song_history.items():
  friend_tags.update(set(val))
unique_tags = user_tags ^ friend_tags
print(unique_tags)