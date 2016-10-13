#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *

def list_of_items(items):

    i_list = ""
    for item in items:
        i_list = i_list + item["name"] + ", "

    i_list = i_list[:-2]
    return i_list

def print_room_items(room):

    print_items = list_of_items(room["items"])
    if len(print_items) > 1:
        print("There is " + print_items + " here." + "\n")
    else:
        pass

def print_inventory_items(items):
    print_items = list_of_items(inventory)
    print("You have " + print_items + "." + "\n")

def print_room(room):

    print("\n" + room["name"].upper() + "\n")
    print(room["description"] + "\n")
    print_room_items(room)

def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):

    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):

    print("You can:")
    for direction in exits:

        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print("TAKE " + item["id"] + " to take " + item["name"] + ".")
    for item in inv_items:
        print("DROP " + item["id"] + " to drop " + item["name"] + ".")

    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

def execute_go(direction):
    global current_room
    a = is_valid_exit(current_room["exits"], direction)
    x = ""
    if a == True:
        x = current_room["exits"][direction]
        x = rooms[x]
        current_room = x

def execute_take(item_id):

    n = 0
    for i in current_room["items"]:
        if item_id == i["id"]:
            inventory.append(i)
            current_room["items"].remove(i)
            n = 1
        else:
            pass
    if n == 0:
        print("You cannot take that.")
    else:
        pass

def execute_drop(item_id):
    n = 0
    for i in inventory:
        if item_id == i["id"]:
            current_room["items"].append(i)
            inventory.remove(i)
            n = 1
        else:
            pass
    if n == 0:
        print("You cannot drop that.")
    else:
        pass

def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")

def menu(exits, room_items, inv_items):

    print_menu(exits, room_items, inv_items)

    user_input = str(raw_input("> "))

    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def move(exits, direction):

    return rooms[exits[direction]]

def main():
    while True:
        print_room(current_room)
        print_inventory_items(inventory)

        command = menu(current_room["exits"], current_room["items"], inventory)

        execute_command(command)

if __name__ == "__main__":
    main()

