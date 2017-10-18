#!/usr/bin/python3

from map import rooms
import string


def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:

    >>> remove_punct("Hello, World!")
    'Hello World'
    >>> remove_punct("-- ...Hey! -- Yes?!...")
    ' Hey  Yes'
    >>> remove_punct(",go!So.?uTh")
    'goSouTh'
    """

    #alias
    user_input = text

    #initializion
    new_string = ""

    permitted_characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for character in user_input:  # get each character from the user_input string
        for char in permitted_characters:  # get each character from the permitted characters


            if character == char:
                new_string += character
                break  # if the character is found break out of the loop
            elif character != char and char == 'Z':  # elif not needed but ...
                pass

    return new_string.lower()
    
    
def remove_spaces(text):
    """This function is used to remove leading and trailing spaces from a string.
    It takes a string and returns a new string with does not have leading and
    trailing spaces. For example:

    >>> remove_spaces("  Hello!  ")
    'Hello!'
    >>> remove_spaces("  Python  is  easy!   ")
    'Python  is  easy!'
    >>> remove_spaces("Python is easy!")
    'Python is easy!'
    >>> remove_spaces("")
    ''
    >>> remove_spaces("   ")
    ''
    """
    return text.strip()


def normalise_input(user_input):
    """This function removes all punctuation, leading and trailing
    spaces from a string, and converts the string to lower case.
    For example:

    >>> normalise_input("  Go south! ")
    'go south'
    >>> normalise_input("!!! tAkE,. LAmp!?! ")
    'take lamp'
    >>> normalise_input("HELP!!!!!!!")
    'help'
    """

    # clean up user input
    result = remove_punct(user_input)
    result = remove_spaces(result)


    return result


    
def display_room(room):
    """This function takes a room as an input and nicely displays its name
    and description.

    The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. For example:

    >>> display_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print("")
    print(room["name"].upper())
    print("")
    # Display room description
    print(room["description"])
    print("")
    
def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """

    return rooms[exits[direction]]["name"]

def print_menu_line(direction, leads_to):
    """This function prints a line of a menu of exits. It takes two strings: a
    direction (the name of an exit) and the name of the room into which it
    leads (leads_to), and should print a menu line in the following format:

    Go <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_menu_line("east", "you personal tutor's office")
    Go EAST to you personal tutor's office.
    >>> print_menu_line("south", "MJ and Simon's room")
    Go SOUTH to MJ and Simon's room.
    """

    print ("Go %s to %s." % (direction.upper(), leads_to))


def print_menu(exits):
    # This function displays the menu of available exits to the player. The
    # argument exits is a dictionary of exits as exemplified in map.py.
    #
    #
    # **The menu should, for each exit, call the function print_menu_line() to print
    # the information about each exit in the appropriate format.
    #
    # **The room into which an exit leads is obtained using the function exit_leads_to().
    #
    # For example, the menu of exits from Reception may look like this:
    #
    # You can:
    # Go EAST to your personal tutor's office.
    # Go WEST to the parking lot.
    # Go SOUTH to MJ and Simon's room.
    # Where do you want to go?
    #
    print("You can:")
    
    # COMPLETE THIS PART:
    # Iterate over available exits:

    for exit,leads_to_room in exits.items():
        print_menu_line(exit, rooms[leads_to_room]["name"])
    #     and for each exit print the appropriate menu line

    print("Where do you want to go?")


def is_valid_exit(exits, user_input):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "user_input" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """

    #alias
    key = str(user_input)


    if key == "north" or key == "south" or key == "east" or key == "west":
        # the get() method iterates through the dictionary to check for a valid key
        # .get() method of the dict object returns None if a value is return for a given key
        if (exits.get(key)) == None:
            return False
        else:
            return True
    else:
        return False



def menu(exits):

    # This function, given a dictionary of possible exits from a room, prints the
    # menu of exits using print_menu() function.


    # It then prompts the player to type the name of an exit where she wants to go.


    # The players's input is normalised using the normalise_input() function before
    # further checks are done.


    # The function then checks whether this exit is a valid one, using the function
    # is_valid_exit().


    # If the exit is valid then the function returns the name
    # of the chosen exit (room/area name).
    #
    # Otherwise the menu is displayed again and the player
    # prompted, repeatedly, until a correct choice is entered.

    # Display menu

    print_menu(exits)

    # Repeat until the player enter a valid choice
    while True:

        # Read player's input

        user_input = raw_input("Choice>>> : ")

        # Normalise the input

        user_input = normalise_input(user_input)

        # Check if the input makes sense (is valid exit)
            # If so, return the player's choice

        if (is_valid_exit(exits, user_input) == True):
            return user_input
        else:
            print "Din't quite get that"
            pass #loop around until a valid choice is made






def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Convert user input to lower case
    direction.lower()

    # e.g rooms["Reception" <- exits[direction]] returns the name of the room
    current_room = rooms[exits[direction]]

    return current_room

# This is the entry point of our program
def main():
    """The initial point. current_room will be updated dynamically later by asking the user for directions"""
    current_room = rooms["Reception"] #room_reception variable

    # Main game loop
    while True:
        # Display game status (room description etc.)

        #Call the display_room method and pass the current room reference
        display_room(current_room)

        # What are the possible exits from the current room?
        # Points to the dictionary of exits (based on which room you're in)

        exits = current_room["exits"] #exits = room_reception["exits"]->{key:value,...}

        # Show the menu with exits and ask the player
        direction = menu(exits)

        # Move the protagonist, i.e. update the current room
        current_room = move(exits, direction)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

