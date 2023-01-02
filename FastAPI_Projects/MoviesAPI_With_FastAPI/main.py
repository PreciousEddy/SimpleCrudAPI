from fastapi import FastAPI


app = FastAPI()


movies = [{"title":"","Year":0},
         {"title":"Batman","Year":2021},
         {"title":"Joker","Year":2022},
         {"title":"Lion King","Year":1999},
         {"title":"Snow White","Year":1998},
         {"title":"Ice age","Year":2012}]



@app.get("/")
async def root():
    return {"message": "welcome"}

# get all movies
@app.get("/movies")
def get_movies():
    return movies

#get single movie
@app.get("/movie/{movie_id}")
def get_movie(movie_id:int):
    return movies[movie_id]

#Deleting a movie
@app.delete("/movie/{movie_id}")
def delete_movie(movie_id:int):
    movies.pop(movie_id) #pop is used to delete items ina n array
    return {"message":" Movie has been deleted succesfully👍"}


#creating a new movie
@app.post("/create_movie")
def create_movie(movie:dict):
    movies.append(movie)# append functions inserts a data at the end of the array
    return movies[-1]

#updating a movie (renaming or fixing the year of an existing movie)
@app.post("/update_movie")
def update_movies(movie_id:int,movie:dict):
    movie_to_be_updated = movies[movie_id] # get movie to be updated
    movie_to_be_updated['title'] = movie['title'] # update title
    movie_to_be_updated['year'] = movie['year'] # update year
    movies[movie_id] = movie_to_be_updated # movie updated successfully
    return movie_to_be_updated