#!/usr/bin/env python
# coding: utf-8

#Imports pandas package
import pandas as pd

#Reads library data like Title, Author, Genre, Read Status, Location on bookshelf, Description and Setting
books = pd.read_csv('Library.csv' ,sep = ',')

#Returns first 5 rows of librabry
books.head()

#Turns primary key into index for easier searching
books.set_index("Title")



#PART 1: Organization of Library

#What are the most common genres found in this library?
books["Genre"].value_counts()

#How many copies of each book can be found in this library? 
books['Title'].value_counts()

#Searches library based on specific book title, then returns the location on bookshelf, along with other relevant info on the book.
user_search=str(input("Hi Makhimba! Please tell me what book you are looking for! "))
book_info=books[books['Title']== user_search]
print(book_info)


#PART 2: Generates book for user to read

#Step 1: Shows user available genres, descriptions and settings.
#Step 2: Asks user to input genres, description and setting based on what they are in the mood for.

print("Here are all the available genres",books["Genre"].unique())
genre_user_search=str(input("What genre do you want to read?"))
print("Here are all the available descriptions",books["Description"].unique())
descr_user_search=str(input("What sort of story are you in the mood for?"))
print("Here are all the available Settings",books["Setting"].unique())
setting_user_search=str(input("Where would you like this book to take you?"))
print("Type one of the below",books["Read"].unique())
read_user_search=str(input("Do you want to read something new?"))

#Step 3: Combines user input of genre, description, setting and if the user wants to read a new title or one they've already read to 
# generate all possible titles that user may be good picks for reader at that moment.

you_should_read = books[(books['Genre']==genre_user_search)&
                      (books['Description']==descr_user_search)&
                      (books['Setting']==setting_user_search)&
                      (books['Read']!=read_user_search)]
print("You should read", you_should_read)

#PART 3: Additional Capabilites 

#Capability 1

# The current working version of this program is a bit analoguous and can be improved using a waterfall of elimination.
# Presently, when asking for user input to narrow down the program's search it returns all possible values within the librabry for each category. 
# Ideally, after the user inputs a genre, only descriptions that fall under the selected Genre should show up, then when user inputs a Setting, only Settings that 
#fall under the prior 2 inputs would show up. 
#This additional feature would prevent user from having to go through entire search process if no book is available that matches the prior search term.
#For example, if user selects the 'Fantasy' genre, when asked to select a description, there are only 7 unique options but the program returns all the unique 
#options for the entire library. This creates the possiblity for the user to select a decription that is not related to a fantasy book which breaks the program.

