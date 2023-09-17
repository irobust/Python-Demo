current_movies = {'equalizer 3': '11:00am',
                 'john wick 4': '1:00pm',
                 'batman': '3:00pm'}

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie.lower())
if showtime:
    print(movie, 'is playing at', showtime)
else:
    print("Requested movie isn't playing")
