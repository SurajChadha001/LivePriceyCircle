song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Create a set from the song data
tag_set = set(song_data['Retro Words'])

# Add the user tags to the set
tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)

# Update the song_data dictionary with the updated tag set as a list
song_data['Retro Words'] = tag_set

print(song_data)
