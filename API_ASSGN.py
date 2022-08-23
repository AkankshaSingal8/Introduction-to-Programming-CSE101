#Akanksha Singal-2021008
#Bhavya Gupta-2021245
import requests,json,pprint

api_key = "a5a07d936cea3585f8b478cb024a05e0"

def movies_based_on_genres(genres):
  api_key = "a5a07d936cea3585f8b478cb024a05e0"
  api_url_movies = 'https://api.themoviedb.org/3/discover/movie?'

  url_movies = api_url_movies+'api_key='+api_key
  url_movies+='&language=en-US&sort_by=popularity.desc&page=1&include_video=false&with_watch_monetization_types=flatrate'+f'&with_genres={genres}'

  response = requests.get(url_movies)

  if response.status_code == 200:
    movies = json.loads(response.text)
    m=movies["results"][:5]
    for i in m:
      print(i["title"])
  else:
    print("Request failed, status code: ", response.status_code)
    

def trending_day():
  api_url_trending_day = 'https://api.themoviedb.org/3/trending/movie/day?'
  api_key = "a5a07d936cea3585f8b478cb024a05e0"
  url_trending_day = api_url_trending_day+'api_key='+api_key+'&page=1'
  response_trending_day = requests.get(url_trending_day)

  if response_trending_day.status_code == 200:
    trending_day = json.loads(response_trending_day.text)
    day=trending_day["results"][:10]
    for i in day:
      print(i["title"])
  
  else:
    print("Request failed, status code: ", response_trending_day.status_code)

def trending_week():
  api_url_trending_week = 'https://api.themoviedb.org/3/trending/movie/week?'
  api_key = "a5a07d936cea3585f8b478cb024a05e0"
  url_trending_week = api_url_trending_week+'api_key='+api_key
  response_trending_week = requests.get(url_trending_week)

  if response_trending_week.status_code == 200:
    trending_week = json.loads(response_trending_week.text)
    week=trending_week["results"][:10]
    for w in week:
      print(w["title"])
  
  else:
    print("Request failed, status code: ", response_trending_week.status_code)
  
def movies_in_theatres():
  api_url_movies_available_in_theatre="https://api.themoviedb.org/3/discover/movie?"
  api_key = "a5a07d936cea3585f8b478cb024a05e0"
  url_movies_available_in_theatre=api_url_movies_available_in_theatre+'api_key='+api_key
  response_movies_available_in_theatre = requests.get(url_movies_available_in_theatre)

  if response_movies_available_in_theatre.status_code == 200:
    movies_available_in_theatre= json.loads(response_movies_available_in_theatre.text)
    theatre=movies_available_in_theatre["results"]
    for i in theatre:
      print(i["title"])
  
  else:
    print("Request failed, status code: ", response_movies_available_in_theatre.status_code)
api_url_rate_a_movie="https://api.themoviedb.org/3/rate/movie?"

 


ch=0
while ch<4:
    print("1. Movies based on genres")
    print("2. Movies in theatres")
    print("3. Trending movies")
    ch=int(input("Enter choice"))
    if ch==1:
        genres=input("Enter 1 genre ")
        movies_based_on_genres(genres)
    elif ch==2:
      print("movies available in theatres")
      movies_in_theatres()
    elif ch==3:
      print("Trending movies")
      print("1. Top rated movies of the day")
      print("2. Top rated movies of the week")
      ch1=int(input("Enter choice"))
      if ch1==1:
        print("Top rated movies of the day")
        trending_day()
      elif ch1==2:
        print("Top rated movies of the week")
        trending_week()
