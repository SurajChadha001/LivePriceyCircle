song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Write your code below!
tag_set = set(song_data['Retro Words'])
print(tag_set)

tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)

print(tag_set) 

song_data['Retro Words']=list(tag_set)
print(song_data)