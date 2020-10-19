#!/usr/bin/env python
# coding: utf-8

#Imports pandas package
import pandas as pd

#Reads library data like Title, Author, Genre, Read Status, Location on bookshelf, Description and Setting
books = pd.read_csv('Library.csv' ,sep = ',')

#Returns first 5 rows of library
books.head()

#Turns primary key into index for easier searching
books.set_index("Title")

#PART 1: Organization of Library

#What are the most common genres found in this library?
books["Genre"].value_counts()

#How many copies of each book can be found in this library? 
books['Title'].value_counts()

#Searches library based on specific book title, then returns the location on bookshelf, along with other relevant info on the book.
user_search=str(input("Hi! Please tell me what book you are looking for! "))
book_info=books[books['Title']== user_search]
print(book_info)


#PART 2: Generates book for user to read
#Step 1: Shows user available genres, descriptions and settings.
#Step 2: Asks user to input genres, description and setting based on what they are in the mood for.

print("Here are all the available genres",books["Genre"].unique())
genre_user_search=str(input("What genre do you want to read?"))
genre_user_answer=books[books['Genre']==genre_user_search]

print("Here are all the available descriptions",genre_user_answer["Description"].unique())
descr_user_search=str(input("What sort of story are you in the mood for?"))
descr_user_answer=genre_user_answer[genre_user_answer['Description']==descr_user_search]

print("Here are all the available Settings",descr_user_answer["Setting"].unique())
setting_user_search=str(input("Where would you like this book to take you?"))
setting_user_answer=descr_user_answer[descr_user_answer['Setting']==setting_user_search]

print("Type one of the below",setting_user_answer["Read"].unique())
read_user_search=str(input("Do you want to read something new?"))
read_user_answer=setting_user_answer[setting_user_answer['Read']!=read_user_search]

#Step 3: Combines user input of genre, description, setting and if the user wants to read a new title or one they've already read to 
# generate all possible titles that user may be good picks for reader at that moment.

you_should_read = books[(books['Genre']==genre_user_search)&
                      (books['Description']==descr_user_search)&
                      (books['Setting']==setting_user_search)&
                      (books['Read']!=read_user_search)]
print("You should read", you_should_read)
