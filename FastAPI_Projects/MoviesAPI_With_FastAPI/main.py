from fastapi import FastAPI
import mysql.connector
from fastapi.openapi.models import Response
from pydantic import BaseModel
from Movies import Movie
from typing import Optional



mydb = mysql.connector.connect(host="localhost",user="root",password="",database="python")
mycursor = mydb.cursor()

app = FastAPI()


#movies = [{"title":"","Year":0},
       #  {"title":"Batman","Year":2021},
       # {"title":"Lion King","Year":1999},
       # {"title":"Snow White","Year":1998},
       # {"title":"Ice age","Year":2012}]



@app.get("/")
async def root():
    return {"message": "welcome To Precious Edmund Movies API"}

# get all movies
@app.get("/All_movies")
def get_movies():
    sql = "SELECT * FROM movies"
    mycursor.execute(sql)
    movies = mycursor.fetchall()
    return movies

#get movie by title
@app.get("/movie_by_title/{movie_title}")
def get_movie_bt_title(movie_title:str):
    sql = "SELECT * FROM movies WHERE title = %s"
    val = (movie_title,)
    mycursor.execute(sql,val)
    movie = mycursor.fetchall()
    return movie

#get single movie
@app.get("/movie_by_id/{movie_id}")
def get_movie(movie_id:int):
    sql = "SELECT * FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql,val)
    movie = mycursor.fetchall()
    return movie[0]

#creating a new movie
@app.post("/create_movie")
def create_movie(movie:Movie):
    sql = "INSERT INTO movies (title,Year,storyline) VALUES (%s,%s,%s)"
    val = (movie.title, movie.Year, movie.storyline)
    mycursor.execute(sql,val)
    mydb.commit()
    return movie_title

#updating a movie (renaming or fixing the year of an existing movie)
@app.post("/update_movie")
def update_movies(movie:Movie,movie_id:int):
    sql = "UPDATE movies SET title = %s , Year = %s, storyline = %s WHERE id = %s"
    val = (movie.title, movie.Year, movie.storyline, movie.movie_id)
    mycursor.execute(sql,val)
    mydb.commit()
    return movie

   # movie_to_be_updated = movies[movie_id] # get movie to be updated
   # movie_to_be_updated['title'] = movie['title'] # update title
   # movie_to_be_updated['Year'] = movie['Year'] # update year
   # movies[movie_id] = movie_to_be_updated # movie updated successfully
   # return movie_to_be_updated

    #Deleting a movie
@app.delete("/movie/{movie_id}")
def delete_movie(movie_id:int):
    sql = "DELETE FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql,val)
    mydb.commit()
    # movies.pop(movie_id) #pop is used to delete items ina n array
    return {"message":" Movie has been deleted succesfully👍"}
 