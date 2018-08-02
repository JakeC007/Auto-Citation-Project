#!/bin/env python3
#Created by Jake Chanenson 8/1/18. 
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from shelf_g import *

#List of Sample ISBN Numbers
#isbn = '0743297334' TSOR
#isbn = '0788789813' LOTR
#isbn = '0743273567' Gats
#isbn = '0684801221' OMAS
#isbn = '0684803356' For who the bell tolls 
#isbn = '1841499889' The expanse book 1
#isbn = '1503261964' Emma
#isbn = '0060850523' BNW
#isbn = '0399501487' LoF
#isbn = '185326086X' Dracula
#isbn = '0141439475' Frankenstien 


def main():
  print("Welcome to the citation generator. This program prints MLA style citations if you input an ISBN. Type 'bib' if you want a list of all stored entries. Type 'stop' to quit.\n"+"*"*100)

  BS= [] #stands for Book Shelf
  while True:
    isbn = input("\n Enter your ISBN: ")
    if isbn == "bib":
      BS.sort(key=lambda book: (book.author, book.title)) #sorts on author first, title second.
      print("\n Bibliography\n" + "-"*90)
      for i in range(len(BS)):
        print(BS[i])
      print("-"*90)
    elif isbn == "stop":
      break
    else: #scrape the webpage and get the book info 
      f = urlopen('https://www.ottobib.com/isbn/%s/bibtex' % (isbn))
      html = f.read()
      soup = bs(html, 'html.parser')
      bibtex = soup.find('textarea').text
      str5 = parse(bibtex)
      n_book = book(str5[0], str5[1], str5[2], str5[3], str5[4], str5[5])
      print(n_book)
      BS.append(n_book)
      
  
    
#Parses the scaped string into a format to create the class
def parse(string):
  str2 = string.splitlines() #split into a list
  str2 = str2[1:len(str2)-1] #take off the end bits 
  str3 = [] 
  for i in range(6): #split into a longer list 
    str3 += str2[i].split('=')
  str4 = str3[1::2] # Take out the unwated entries
  str5 = str4
  for i in range (6):
    str5[i] = str4[i].strip('{ },') #strip the brackets 
  str5[1] = str5[1].title()
  return str5 

main()


