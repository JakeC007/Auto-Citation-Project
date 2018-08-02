#Created by Jake Chanenson on 8/1/18 for use in the citation machine program. 
class book(object):
    """class for single citation object"""

    def __init__(self, author, title, publisher, year, address, isbn):
        """constructor for player object, given name, etc"""
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.address = address
        self.isbn = isbn
 


    def __str__(self):
        """pretty-print info about this object"""
        s = "%s. '%s' %s, \n \t %s, %s." % (self.author, self.title, self.publisher,self.address, self.year)
        return s

def main():
  if __name__ == '__main__':
    main() 
