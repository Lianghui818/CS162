class LibraryItem:


    def __init__(self, id_code, title):

        self._id_code = id_code
        self._title = title
        self._location = "ON_SHELF" # set to "ON_SHELF"
        self._checked_out_by = None # will be set to a Patron object
        self._requested_by = None # will be set to a Patron object
        self._date_checked_out = 0 # will be set to an int


    def get_id_code(self):
        return self._id_code


    def get_title(self):
        return self._title


    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_checked_out_by(self):
        return self._checked_out_by


    def set_checked_out_by(self, patron):
        self._checked_out_by = patron


    def get_requested_by(self):
        return self._requested_by

    def set_requested_by(self, patron):
        self._requested_by = patron

    def get_date_checked_out(self):
        return self._date_checked_out

    def set_date_checked_out(self, current_date):
        self._date_checked_out = current_date




class Book(LibraryItem):

    def __init__(self, id_code, title, author):

        self._id_code = id_code
        self._title = title
        self._author = author
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None

    def get_author(self):
        return self._author


    def get_check_out_length(self):
        return 21





class Album(LibraryItem):


    def __init__(self, id_code, title, artist):

        self._id_code = id_code
        self._title = title
        self._artist = artist
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None


    def get_artist(self):
        return self._artist


    def get_check_out_length(self):
        return 14





class Movie(LibraryItem):


    def __init__(self, id_code, title, director):

        self._id_code = id_code
        self._title = title
        self._director = director
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None

    def get_director(self):
        return self._director


    def get_check_out_length(self):
        return 7




class Patron:


    def __init__(self, id_num, name):

        self._id_num = id_num
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0 # amount owed


    def get_name(self):
        return self._name


    def get_id_num(self):
        return self._id_num


    def get_checked_out_items(self):
        return self._checked_out_items


    def add_library_item(self, item):
 
        self._checked_out_items.append(item)


    def remove_library_item(self, item):

        self._checked_out_items.remove(item)


    def amend_fine(self, amount):


        self._fine_amount += amount


    def get_fine_amount(self):
        return self._fine_amount




class Library:

    def __init__(self):

        self._current_date = 0
        self._holdings = [] # list of Item objects
        self._members = [] # list of Patron objects


    def get_current_date(self):
        return self._current_date

    def get_holdings(self):
        return self._holdings


    def get_members(self):
        return self._members


    def check_if_in_members(self, patron):

        if patron in self._members:
            return True
        else:
            return False


    def check_if_in_holdings(self, item):

        if item in self._holdings:
            return True
        else:
            return False

    def get_library_item(self, id):

        for item in self._holdings:
            if item.get_id_code() == id:
                return item
            continue
        return None

    def get_patron(self, id):

        for patron in self._members:
            if patron.get_id_num() == id:
                return patron
            continue
        return None


    def add_library_item(self, item):

        self._holdings.append(item)


    def add_patron(self, patron):

        self._members.append(patron)


    def check_out_library_item(self, id_num, id_code):

    # check if patron in members list:
        for patron in self._members:
            if patron.get_id_num() == id_num:
    # check if item in holdings:
                for item in self._holdings:
                    if item.get_id_code() == id_code:
    # check if item checked_out:
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


    def return_library_item(self, id_code):

# check it item in holdings:
        for item in self._holdings:
            if item.get_id_code() == id_code:
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


    def request_library_item(self, id_num, id_code):

        # check if the patron in memebers:
        for patron in self._members:
            if patron.get_id_num() == id_num:
                for item in self._holdings:
                    if item.get_id_code() == id_code:
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

    # check if patron in member:
        for patron in self._members:
            if patron.get_id_num() == id:
                patron.amend_fine(-amount) # subtract payment from fines owed
                return "payment successful"
        return "patron not found"


    def increment_current_date(self):

        self._current_date +=1
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