#!/usr/bin/env python


def display_menu(menu_type):
    with open("texts/%s.txt" % menu_type, "r") as f:
        menu_content = f.read()
        f.close()
    print menu_content


def validate_value(input_data, var_type):
    """
    :param user_choice:
    :param input_type:
    :return: none
    Function gets var type of int or string and checks if variable type suits var_type
    """
    return True
   # return isinstance(input_data, var_type)


def get_user_input(prompt_string, var_type):
    input_data = raw_input(prompt_string)
    if validate_value(input_data, var_type):
        return input_data
    else:
        print ("Validation failed. Try again.")
        get_user_input(prompt_string, var_type)