song_data_users = {
  'Retro Words':{'onion','helloworld','spam','jazz','blues'}
}
tag_set = set(song_data_users['Retro Words'])

tag_set.discard('onion')
tag_set.discard('helloworld')
tag_set.discard('spam')

song_data_users['Retro Words'] = tag_set
print(song_data_users)
try:
  tag_set.remove('onion')
  tag_set.remove('helloworld')
  tag_set.remove('spam')
except KeyError as e:
  print(f"tag not found:{e}")

song_data_users['Retro Words'] = tag_set
print(song_data_users)