import user_function
import group_functions
import common_functions


def main_menu_routes(uc):
    uc = int(uc)
    if uc == 1:
        user_choice_route("list_users")
    elif uc == 2:
        group_functions.display_groups_list()
    elif uc == 3:
        user_choice_route("reset_password")
    elif uc == 4:
        user_create_menu_routes()
    # elif uc == 5:
    #     create_group()
    # elif uc == 6:
    #     list_mounts()
    # elif uc == 7:
    #     mount_folder()
    # elif uc == 8:
    #     add_new_command()
    # elif uc == 9:
    #     exit_programm()
    else:
        print("Now such option.")


def user_choice_route(task):
    user_function.display_users_list()
    user_number = common_functions.get_user_choice("Please choose user:\n")
    if common_functions.validate_choice(user_number, "int"):
        user_number = int(user_number)
        users = user_function.get_users_list()
        username = users[user_number]
    else:
        print("Wrong user number. Choose again: ")
        user_choice_route(task)
    if task == "list_users":
        uc = 0
        while uc != 6:
            common_functions.display_menu("users_data_menu")
            uc = int(common_functions.get_user_choice("Please choose entry: "))
            if uc < 1 or uc > 6:
                print "not valid choise"
            else:
                user_data_routes(uc, username)

    elif task == "reset_password":
        user_function.reset_password(username)


def user_data_routes(uc, username):
    uc = int(uc)
    if uc == 1:
        user_function.show_user_groups(username)
    elif uc == 2:
        user_function.show_user_id(username)
    elif uc == 3:
        user_function.show_user_aliases(username)
    elif uc == 4:
        user_function.create_new_alias(username)
    elif uc == 5:
        print("back")
    elif uc == 6:
        print("6")
    else:
        print("back")
        user_data_routes()


def user_create_menu_routes():
    user_function.display_user_creation_methods()
    method = common_functions.get_user_input("Choose the method:\n")
    user_function.create_user(method)
