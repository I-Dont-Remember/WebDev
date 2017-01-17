#! /usr/bin/env python
import fresh_tomatoes
import media
import sys

# Adds Movie objects to a given list
#! no checks for duplicates in this function
# @returns a boolean on whether or not user gave "done" as the input
def add_movie(movies):
  # function to ask for movie information, intentionally ignored sanitizing input as useful links/names as I will be the only one ever using this, but it would normally be a very important piece of the program
  print("When finished, please type \"done\"")
  title = raw_input("title: ")
  plot = raw_input("Plot/Storyline: ")
  image = raw_input("Image URL: ")
  trailer = raw_input("Trailer URL (Youtube): ")
  movies.append(media.Movie(title, plot, image, trailer))
  return raw_input("finished?") == "done"

# adds a generic batch of movies to the list, no checks for duplicates
def add_batch(movies):
  movies.append(media.Movie("The Grey", "Liam Neeson: Wolf Man",
   "http://graphicdesignjunction.com/wp-content/uploads/2011/12/grey-movie-poster.jpg",
   "https://www.youtube.com/watch?v=ujrBaHS8UTg" ))
  movies.append(media.Movie("GhostBusters","Ghosts and people, together",
   "https://s-media-cache-ak0.pinimg.com/736x/ae/b3/de/aeb3de3c96639fd44e3c8e7f50a59725.jpg",
    "https://www.youtube.com/watch?v=w3ugHP-yZXw" ))
  movies.append(media.Movie("Avatar","Blue people and racist humans",
  "http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg",
  "https://www.youtube.com/watch?v=d1_JBMrrYw8"))
  movies.append(media.Movie("Thor","Large attractive man gets girls",
  "http://www.impawards.com/2011/posters/thor_ver3_xlg.jpg",
  "https://www.youtube.com/watch?v=JOddp-nlNvQ"))
  movies.append(media.Movie("The Martian","Awesome movie, better than you",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR15ls0Ca7NvjBWzXAeDFHLO00nDDYEcYLty1Xkf8B9v-2L0jFz",
  "https://www.youtube.com/watch?v=ej3ioOneTy8"))
  movies.append(media.Movie("Star Wars: A New Hope","Lasers, pew pew, and robots",
  "https://s-media-cache-ak0.pinimg.com/736x/86/48/02/864802d9fae547f8b72a1c88af852162.jpg",
  "https://www.youtube.com/watch?v=1g3_CFmnU7k"))

movies = []
choice = input(" Two options,\n1. Add movies yourself\n2. Take existing Batch: ")
if choice == 1:
  done = False
  while not done:
    done = add_movie(movies)
elif choice == 2:
  add_batch(movies)
else:
  # could instead have loop at main menu instead of exit
  print("Incorrect Usage, program will now terminate, thanks to you!")
  sys.exit()

fresh_tomatoes.open_movies_page(movies)
