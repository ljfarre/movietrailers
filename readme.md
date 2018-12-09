# Udacity FSND Movie Trailer Project
This file is the readme file for the Movie Trailer project.  It is a required file in the
FSND rubric for this project.  I developed the code for this project as part of the
IPND program.  Below I include the evaluation I received from my IPND reviewer as well as
the necessary information needed to execute the movie trailer code correctly.

## Table of Contents
1. IPND Movie Trailer Evaluation
2. Basic Requirements
3. Running the Code
4. Using the Movie Trailer Website

## IPND Movie Trailer Evaluation
Below is a text version of the project review that I received for this project
in the IPND program.

Meets Specifications:
Congratulations!
  Your project exceeds the specifications!
  You did a great job commenting it!
  Keep up the good work!

Functionality:
  Page presents all required content (movie title, poster art, and trailer link)
  Page is dynamically generated from a Python data structure
  Page is free of errors, glitches, and bugs

Code Review:
  Code uses variables to avoid magic numbers
  Each variable name reflects the purpose of the value stored in it
  Once initiated, the purpose of each variable is maintained throughout the program
  No variables override Python built-in values (for example, def)
  Functions are used as tools to automate tasks which are likely to be repeated
  Functions produce the appropriate output (typically with a return statement) from the appropriate input (function parameters)
  No functions are longer than 18 lines of code (does not include blank lines, comments, or function and variable definitions)
  The appropriate data types are used consistently (strings for text, lists for ordered data, nested lists as appropriate)
  Student demonstrates coding techniques like branching and loops appropriately (i.e. to loop through a list, for element in list:; or to test whether something is in a list, if name in list_names:)
  Code defines classes properly and uses instances of those classes in the code
  Each function includes a comment which explains the intended behavior, inputs, and outputs (if applicable)
  You did a great job commenting your project!

## Basic Requirements
In order to build and access the movie trailer website the following files are required:
  1. entertainment-center.py
  2. fresh_tomatoes.py
  3. media.py

  The media.py python code defines the class Movie. This class definition is used as the
  data structure for the movies table and the movie trailer website. The fresh_tomatoes.py file includes
  the css styles and the html page structure for the website.  It also has python code for creating
  the fresh_tomatoes.html file and opening it in the browser.  Finally, the entertainment-center.py file
  imports the fresh_tomatoes.py and media.py modules and includes the movie trailer data that is rendered
  by the movie trailer website.  Here the movies array that is fed into the open_movies_page funtion in
  fresh_tomatoes.py is defined and opened.

In addition to the files above, you will need:
  1. Access to the internet from your development machine in order to access web based content, e.g.,
    Bootstrap css styles, java scripts, movie trailers, movie posters.
  2. Python installed and working.  Here we use Python 2.7.12.
  3. Access to a working command line interface.  Here we are using Git Bash for Windows.

## Building the website
To create and launch the fresh_tomatoes.html web page:
  1. Place entertainment-center.py, fresh_tomatoes.py and media.py in the same folder/directory.
  2. From the command line interface, go to the directory which contains these files.
  3. From the command line execute this command:  python entertainment-center.py

This should create and launch the movie trailer web page.  To verify this, check the directory
from which you executed the above command for the following files:
  1. fresh_tomatoes.html
  2. fresh_tomatoes.pyc
  3. media.pyc

## Using the Movie Trailer Website
If you have done everything correctly, the movie trailer website should launch in the browser and you
should be able to open Lee's six favorite movies without error.  To see a trailer just click on the
poster for the trailer you want to watch.
