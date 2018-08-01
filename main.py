#!/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from shelf_g import *


def main():
  x = 0
  BS= ["one", "two", "three"]
  while True:
    #isbn = '0136108040'
    isbn = input("Enter your ISBN: ")
    
    if isbn == 'stop':
      break

    f = urlopen('https://www.ottobib.com/isbn/%s/bibtex' % (isbn))
    html = f.read()
    soup = bs(html, 'html.parser')
    bibtex = soup.find('textarea').text
        
    str5 = parse(bibtex)
    
    #Nonse to try and store multiple enteries
    x +=1
    if x == 1:
      book1 = book(str5[0], str5[1], str5[2], str5[3], str5[4], str5[5])
      BS[0] = book1
      
    elif x == 2:
      book2 = book(str5[0], str5[1], str5[2], str5[3], str5[4], str5[5])
      BS[1] = book2
    
    elif x == 3:
      book3 = book(str5[0], str5[1], str5[2], str5[3], str5[4], str5[5])
      BS[2] = book3
    
  
  for j in range(x):
    print(BS[j])
  

  
    

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
  return str5 

main()


