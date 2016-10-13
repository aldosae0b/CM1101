from Map import rooms

import string

def remove_punct(text):

    txt = ""
    for c in text:
        if c.isdigit() or c.isalpha() or c.isspace():
            txt = txt + c
    return txt

def remove_spaces(text):

    text =text.strip()
    return text

def normalise_input(user_input):

    pass

    normalized1 = remove_punct(user_input)
    normalized2 = remove_spaces(normalized1).lower()

    return normalized2

def display_room(room):

    print("")
    print(room["name"].upper())
    print("")
    print(room["description"])
    print("")

def exit_leads_to(exits, direction):


    return rooms[exits[direction]] ["name"]

def print_menu_line(direction, leads_to):



    print("Go " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits):

    print("You can:")

    for x in exits:
        leads_to = exit_leads_to(exits,x)
        print_menu_line(x, leads_to)


    print("Where do you want to go?")

def is_valid_exit(exits, user_input):

    if user_input in exits:
        return True
    else:
        return False

def menu(exits):

    while True:
        # COMPLETE THIS PART:

        # Display menu
        print_menu(exits)
        # Read player's input
        user_input = str(raw_input(">\n"))
        # Normalise the input
        normalise_input(user_input)
        # Check if the input makes sense (is valid exit)
        if is_valid_exit(exits, user_input) == True:
            # If so, return the player's choice
            return user_input
        else:
            pass

        #    exits1= str(input())

 #   q = normalise_input(exits1)

  #  while is_valid_exit(exits,q) == False :

   #     q = normalise_input(exits1)

    #    print_menu(exits)

    #return q

def move(exits, direction):

    return rooms[exits[direction]]

def main():

    current_room = rooms["Reception"]

    while True:

        display_room(current_room)

        exits = current_room["exits"]


        direction = menu(exits)


        current_room = move(exits, direction)

if __name__ == "__main__":
    main()
