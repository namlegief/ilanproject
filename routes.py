import user_functions
import group_functions
import common_functions


def main_menu_routes():
    common_functions.display_menu("main_menu")
    task = int(common_functions.get_user_input("Please choose task: ", "int"))
    if task == 1:
        username = user_functions.pick_user()
        uc = user_functions.get_task_over_user()
        user_data_routes(uc, username)
    elif task == 2:
        groupname = group_functions.pick_group()
        uc = group_functions.get_task_over_group()
        group_data_routes(uc, groupname)
    elif task == 3:
        username = user_functions.pick_user()
        user_data_routes("5", username)
    elif task == 4:
        user_create_menu_routes()
    elif task == 5:
        group_functions.create_group()
    # elif task == 6:
    #     list_mounts()
    # elif task == 7:
    #     mount_folder()
    # elif task == 8:
    #     add_new_command()
    # elif task == 9:
    #     exit_programm()
    else:
        print("Now such option.")


def user_data_routes(uc, username):
    uc = int(uc)
    if uc == 1:
        user_functions.show_user_groups(username)
    elif uc == 2:
        user_functions.show_user_id(username)
    elif uc == 3:
        user_functions.show_user_aliases(username)
    elif uc == 4:
        user_functions.create_new_alias(username)
    elif uc == 5:
        user_functions.reset_password(username)
    elif uc == 6:
        main_menu_routes()


def user_create_menu_routes():
    user_functions.display_user_creation_methods()
    method = common_functions.get_user_input("Choose the method: ")
    user_functions.create_user(method)


def group_data_routes(uc, groupname):
    uc = int(uc)
    if uc == 1:
        group_functions.show_users_in_group(groupname)
    elif uc == 2:
        group_functions.show_group_id(groupname)
    elif uc == 3:
        group_functions.add_user_to_this_group(groupname)
    elif uc == 4:
        main_menu_routes()