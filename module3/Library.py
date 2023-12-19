# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/09/2023
# Description: Write the LibraryItem, Patron and Library classes, and the three classes that inherit from LibraryItem (Book, Album and Movie).

class LibraryItem: 
    """ A LibraryItem object represents a library item that a patron can check out from a library. """

    def __init__(self, library_item_id, title): 
        """ Create six private variables. Initialize library_item_id and title """
        self._library_item_id = library_item_id
        self._title = title
        self._location = 'ON_SHELF'
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_library_item_id(self):
        """ Create a method to get the id code of the LibraryItem """
        return self._library_item_id

    def get_title(self):
        """ Create a method to get the title of the LibraryIteCreate a m """
        return self._title

    def get_location(self):
        """ Create a method to get the current location of the LibraryItem """
        return self._location

    def set_location(self, location):
        """ Create a method to set the location of the LibraryItem """
        self._location = location

    def get_checked_out_by(self):
        """ Create a method to get the Patron who has checked out the LibraryItem """
        return self._checked_out_by

    def set_checked_out_by(self, patron):
        """ Create a method to set the Patron who has checked out the LibraryItem """
        self._checked_out_by = patron

    def get_requested_by(self):
        """ Create a method to get the Patron who has requested the LibraryItem"""
        return self._requested_by

    def set_requested_by(self, patron):
        """ Create a method to set the Patron who has requested the LibraryItem """
        self._requested_by = patron

    def get_date_checked_out(self):
        """ Create a method to get the date on which the LibraryItem was checked out """
        return self._date_checked_out

    def set_date_checked_out(self, current_date):
        """ Create a method to set the current_date on which the LibraryItem was checked out """
        self._date_checked_out = current_date


class Book(LibraryItem):
    """ This class inherit from LibraryItem """

    def __init__(self, library_item_id, title, author):         # super inherit library_item_id and title from LibraryItem
        """ Initialize author """
        super().__init__(library_item_id, title)
        self._author = author
    
    def get_check_out_length(self):
        # Returns the number of days a book can be checked out
        return 21
    
    def get_author(self):
        # Returns the author of the book
        return self._author


class Album(LibraryItem):
    """ This class inherit from LibraryItem """

    def __init__(self, library_item_id, title, artist):
        """ Initialize artist """
        super().__init__(library_item_id, title)           # super inherit library_item_id and title from LibraryItem
        self._artist = artist
    
    def get_check_out_length(self):
        """ Returns the number of days an album can be checked out """
        return 14
    
    def get_artist(self):
        """ Returns the artist of the album """
        return self._artist


class Movie(LibraryItem):
    """ This class inherit from LibraryItem """

    def __init__(self, library_item_id, title, director):
        """ Initialize director """
        super().__init__(library_item_id, title)        # super inherit library_item_id and title from LibraryItem
        self._director = director
    
    def get_check_out_length(self):
        """ Returns the number of days a movie can be checked out """
        return 7
    
    def get_director(self):
        """ Returns the director of the movie """
        return self._director
    


class Patron:
    """ A Patron object represents a patron of a library. """
    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.0

    def get_fine_amount(self):
        """ Create a method to get the fine amount for a patron """
        return self._fine_amount
     
    def get_patron_id(self):
        """ Create a method to get the patron's id number """
        return self._patron_id
            
    def get_name(self):
        """ Create a method to get the name """
        return self._name
    
    def get_checked_out_items(self):
        """ Create a method to get a list of library items checked out by the patron """
        return self._checked_out_items
       
    def add_library_item(self, item): 
        """ Create a method to add a library item to the list of checked out items """
        self._checked_out_items.append(item)
      
    def remove_library_item(self, item):
        """ Creatw a method to remove a library item from the list of checked out item """
        self._checked_out_items.remove(item)
       
    def amend_fine(self, amount):
        """ Create a method to add or subtract from the fine amount for a patron """
        self._fine_amount += amount
      
 

class Library:
    """A Library object represents a library that contains variaous library items, and is used by various patrons."""

    def __init__(self):
        """ Initializes the holdings and members as empty collections and initializes the current_date to zero """
        self._holdings = []       # a list to hold all the items in the library
        self._members = []        # a list to hold all the patrons in the library
        self._current_date = 0    # the current date in the library, initialized to 0

    def add_library_item(self, item):
        """ takes a LibraryItem object as a parameter and adds it to the holdings """
        self._holdings.append(item)  # add an item to the holdings list

    def add_patron(self, patron):
        """ takes a Patron object as a parameter and adds it to the members """
        self._members.append(patron)  # add a patron to the members list

    def lookup_library_item_from_id(self, library_item_id):
        """returns the LibraryItem object corresponding to the ID parameter, or None if no such LibraryItem is in the holdings"""
        for item in self._holdings:
            if item.library_item_id == library_item_id:
                return item   # return the item object with the given library_item_id
        return None          # return None if the item is not found

    def lookup_patron_from_id(self, patron_id):
        """returns the Patron object corresponding to the ID parameter, or None if no such Patron is a member"""
        for patron in self._members:
            if patron.patron_id == patron_id:
                return patron  # return the patron object with the given patron_id
        return None          # return None if the patron is not found

    def check_out_library_item(self, patron_id, library_item_id):
        """ takes as parameters a patron ID and a library item ID """
        for patron in self._members:            # check if patron in members list:
            if patron.get_patron_id() == patron_id:       # check if item in holdings:
                for item in self._holdings:
                    if item.get_library_item_id() == library_item_id:           # check if item checked_out:
                        if item.get_location() == "CHECKED_OUT": # if item checked out...
                            return "item already checked out"
                        elif item.get_location() == "ON_HOLD_SHELF": #if item NOT checked out, but is on hold:
                            return "item on hold by other patron"
                        else: # if item NOT checked out AND NOT on hold:
                            # update item
                            item.set_checked_out_by(patron)
                            item.set_date_checked_out(self._current_date)
                            item.set_location("CHECKED_OUT")
                            if item.get_requested_by() == patron:
                                item.set_requested_by(None)
                            # update patron
                            patron.add_library_item(item)
                            return "check out successful"
                    continue
                return "item not found" # item not in holdings
            continue
        return "patron not found" # patron not in members


    def return_library_item(self, library_item_id):
        """ takes as its parameter a library item ID """
        for item in self._holdings:
            if item.get_library_item_id() == library_item_id:
            # check if checked_out:
                if item.get_location() == "CHECKED_OUT":
                    # update Patron's checked_out_items list:
                    patron = item.get_checked_out_by()
                    patron.remove_library_item(item)
                    # update item location:
                    if item.get_requested_by() != None: # is on hold
                        item.set_location("ON_HOLD_SHELF")
                    item.set_location("ON_SHELF") # not on hold
                    #update item checked_out_by:
                    item.set_checked_out_by(None)
                    return "return successful"
                # item not checked out:
                return "item already in library"
            # item not in holdings:
            continue
        return "item not found"


    def request_library_item(self, patron_id, library_item_id):
        """takes as parameters a patron ID and a library item ID, in that order"""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                for item in self._holdings:
                    if item.get_library_item_id() == library_item_id:
                        if item.get_requested_by() != None: # if already on hold:
                            return "item already on hold"
                        # update item:
                        item.set_requested_by(patron)
                        if item.get_location() == "ON_SHELF":
                            item.set_location("ON_HOLD_SHELF")
                        return "request successful"
                    continue
                return "item not found"
            continue
        return "patron not found"

    def pay_fine(self, id, amount):
        """takes as parameters a Patron ID and the amount (in dollars) being paid (in that order)"""
        for patron in self._members:
            if patron.get_patron_id() == id:
                patron.amend_fine(-amount) # subtract payment from fines owed
                return "payment successful"
        return "patron not found"


    def increment_current_date(self):
        """takes no parameters"""
        self._current_date += 1
        for patron in self._members:
            for item in patron.get_checked_out_items():
                if (self._current_date - item.get_date_checked_out()) > item.get_check_out_length():
                    patron.amend_fine(0.10)
                continue



def main():
    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")
    print(b1.get_author())
    print(a1.get_artist())
    print(m1.get_director())
    
    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")
    
    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_patron(p1)
    lib.add_patron(p2)
    
    lib.check_out_library_item("bcd", "456")
    for _ in range(7):
        lib.increment_current_date()  # 7 days pass
    lib.check_out_library_item("abc", "567")
    loc = a1.get_location()
    lib.request_library_item("abc", "456")
    for _ in range(57):
        lib.increment_current_date()   # 57 days pass
    p2_fine = p2.get_fine_amount()
    lib.pay_fine("bcd", p2_fine)
    lib.return_library_item("456")

if __name__ == '__main__':
    main()