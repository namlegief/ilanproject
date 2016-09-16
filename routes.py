import user_functions
import group_functions
import common_functions


def main_menu_routes(uc):
    uc = int(uc)
    if uc == 1:
        username = user_functions.pick_user()
        uc = user_functions.get_task_over_user()
        user_data_routes(uc, username)
    elif uc == 2:
        group_choice_route("list_groups")
    elif uc == 3:
        username = user_functions.pick_user()
        user_data_routes("5", username)
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
        print("6")
    else:
        print("back")
        user_data_routes()


def user_create_menu_routes():
    user_functions.display_user_creation_methods()
    method = common_functions.get_user_input("Choose the method: ")
    user_functions.create_user(method)


def group_choice_route(task):
    group_functions.display_groups_list()
    group_number = common_functions.get_user_input("Please choose group: ", "int")
    groups = group_functions.get_groups_list()
    groupname = groups[group_number]
    if task == "list_groups":
        common_functions.display_menu("groups_data_menu")
        uc = int(common_functions.get_user_input("Please choose entry: ", "int"))
        group_data_routes(uc, groupname)


def group_data_routes(uc, groupname):
    uc = int(uc)
    if uc == 1:
        group_functions.show_users_in_group(groupname)
    elif uc == 2:
        group_functions.show_group_id(groupname)
    elif uc == 3:
        group_functions.add_user_to_this_group(groupname)
    else:
        print("back")
        user_data_routes()