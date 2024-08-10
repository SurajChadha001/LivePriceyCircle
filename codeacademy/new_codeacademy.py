song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
   'Wait For Limit': ['rap', 'upbeat', 'romance'],
   'Stomping Cue': ['country', 'fiddle', 'party'],
   'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
   'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
   'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
   'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
   'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
           'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Write your code below!
tags_recent_song1 = set(song_data['Retro Words'])
tags_recent_song2 = set(song_data['Lowkey Space'])

tags_int = tags_recent_song1.intersection(tags_recent_song2)

recommended_songs = {}
for song, tags in song_data.items():
if song not in ['Retro Words','Lowkey Space'] and tags_int.intersection(set(tags)):
recommended_songs[song] = tags
print(recommended_songs)