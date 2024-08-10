tag_set = set(song_data_users['Retro Words'])

bad_tags = []
for tag in tag_set:
  if tag not in allowed_tags:
    bad_tags.append(tag)
for tag in bad_tags:
  tag_set.remove(tag)
print(tag_set)

song_data_users['Retro Words'] = tag_set
print(song_data_users)