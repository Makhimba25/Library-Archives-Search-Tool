#!/usr/bin/env python
# coding: utf-8

# In[170]:



#reads library data like Title, Author, Genre, Read, and Location
import pandas as pd
books = pd.read_csv('Library.csv' ,sep = ',')
books.head()
books.set_index("Title")


# In[22]:


#PART 1
#Problem: organize by library to avoid double purchases, rereading same bo
#user inputs name of book
#output is book information
#user wants to read book they haven't read before of a certain genre
#What book should I read
#Feature 1: Type in title and get information
#Feature 2: Type in genre and if i read it and get info


# In[241]:


#What is my favorite genre?
books["Genre"].value_counts()


# In[115]:


#shows count of each title to see what books I have several copies of
books['Title'].value_counts()


# In[172]:


#General Search by Title
user_search=str(input("Hi Makhimba! Please tell me what book you are looking for! "))

book_info=books[books['Title']== user_search]

print(book_info)


# In[108]:


#PART 2
#What book should I read?
#1 What genre do you feel like reading?
#Here are possible genres
#Input /choose genre
#2 What vibe are you looking for?
##Here are possible vibes
#Input /choose Vibe
#3Where do you want this bok to take you?
#Here are possible settings
#Input/choose setting
#Do you want to read something new?
#Input yes or no
#Output:here is possible books for you


# In[147]:


#What book should I read?
#Possible genres and user input chosen genre?
print("Here are all the available genres",books["Genre"].unique())
genre_user_search=str(input("What genre do you want to read?"))
#Here are possible genres
#Input /choose genre
genre_user_answer=books[books['Genre']==genre_user_search]
print(genre_user_answer)


#return all possible books


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[176]:


print("Here are all the available genres",books["Genre"].unique())
genre_user_search=str(input("What genre do you want to read?"))
genre_user_answer=books[books['Genre']==genre_user_search]

print("Here are all the available descriptions",books["Description"].unique())
descr_user_search=str(input("What sort of story are you in the mood for?"))
descr_user_answer=books[books['Description']==descr_user_search]

print("Here are all the available Settings",books["Setting"].unique())
setting_user_search=str(input("Where would you like this book to take you?"))
setting_user_answer=books[books['Setting']==setting_user_search]

print("Type one of the below",books["Read"].unique())
read_user_search=str(input("Do you want to read something new?"))
read_user_answer=books[books['Read']!=read_user_search]


you_should_read=books[(books['Genre']==genre_user_search)&(books['Description']==descr_user_search)&(books['Setting']==setting_user_search)&(books['Read']!=read_user_search)]
print("You should read", you_should_read)


# In[177]:


#most basic version
print("Here are all the available genres",books["Genre"].unique())
genre_user_search=str(input("What genre do you want to read?"))
print("Here are all the available descriptions",books["Description"].unique())
descr_user_search=str(input("What sort of story are you in the mood for?"))
print("Here are all the available Settings",books["Setting"].unique())
setting_user_search=str(input("Where would you like this book to take you?"))
print("Type one of the below",books["Read"].unique())
read_user_search=str(input("Do you want to read something new?"))
you_should_read=books[(books['Genre']==genre_user_search)&(books['Description']==descr_user_search)&(books['Setting']==setting_user_search)&(books['Read']!=read_user_search)]
print("You should read", you_should_read)


# In[238]:


#psuedo code for additional capabilities
#version with waterfall elimination
print("Here are all the available genres",books["Genre"].unique())
genre_user_search=str(input("What genre do you want to read?"))

#print descriptions for only genre that was input above
print("Here are all the available descriptions",books["Description"].unique())
descr_user_search=str(input("What sort of story are you in the mood for?"))
#print settings for only genre and descriptions that was input above
print("Here are all the available Settings",books["Setting"].unique())
setting_user_search=str(input("Where would you like this book to take you?"))
print("Type one of the below",books["Read"].unique())
read_user_search=str(input("Do you want to read something new?"))
you_should_read=books[(books['Genre']==genre_user_search)&(books['Description']==descr_user_search)&(books['Setting']==setting_user_search)&(books['Read']!=read_user_search)]
print("You should read", you_should_read)


# In[ ]:





# In[ ]:





# In[ ]:




