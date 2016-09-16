#!/usr/bin/env python

import common_functions
import routes


def main():
    common_functions.display_menu("main_menu")
    task = common_functions.get_user_input("Please choose task: ", "int")
    routes.main_menu_routes(task)
main()


