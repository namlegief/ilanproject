#!/usr/bin/env python

import common_functions
import routes


def main():
    user_choice = 0
    while user_choice != 9:
        common_functions.display_menu("main_menu")
        user_choice = raw_input("Please enter your choice 1-9:\n")
        user_choice = int(user_choice)
        if user_choice < 1 or user_choice > 9:
            print "not valid choise"
        else:
            routes.main_menu_routes(user_choice)
            #user_choice = common_functions.get_user_choice()


main()

