genre_results = ['rock','pop','jazz','rock','classical','pop','hip hop','jazz','electronic']
survey_genres = set(genre_results)
print("Unique Genres:",survey_genres)

survey_abbreviated = {genre[:3] for genre in genre_results}
print("Abbreviated Genres:",survey_abbreviated)