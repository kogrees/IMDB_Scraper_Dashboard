import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

movies_data = []

res = requests.get("https://www.yidio.com/redesign/json/browse_results.php?sort=imdb_rating&type=movie&index=0&limit=1000")

soup = bs(res.content,'html.parser')

data = res.json()

movies = data["response"]

for movie in movies:
    
    movie_url = movie["url"]
    movie_request = requests.get(movie_url)
    movie_soup = bs(movie_request.content,'html.parser')
    details = movie_soup.find('div',class_ = 'details').find('ul',class_ = 'attributes')

    title = details.find_all('li')

    items = details.find_all('li')

    certificate = items[0].get_text(strip=True) if len(items) > 0 else ""
    year = items[1].get_text(strip=True) if len(items) > 1 else ""
    duration = items[2].get_text(strip=True) if len(items) > 2 else ""
    imdb_rating = items[3].get_text(strip=True) if len(items) > 3 else ""
    movies_data.append({"Name": movie["name"]
                        ,"Certificate":certificate,
                        "Year of relase":year,
                        "Duration":duration,
                        "IMDB Rating": imdb_rating})


df = pd.DataFrame(movies_data)
df['id'] = range(1,len(df)+1)
df = df[['id','Name','Certificate','Year of relase','Duration','IMDB Rating']]

df.to_csv("movies_data.csv")
print(df.head())