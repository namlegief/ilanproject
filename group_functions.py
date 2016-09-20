from os import system
import common_functions
import user_functions
import routes


def get_groups_list():
    counter = 1
    myFile = open('/etc/group', 'r')
    raw_data = myFile.readlines()
    all_groups = {}
    for line in raw_data:
        splited = line.split(':')
        all_groups[counter] = splited[0]
        counter += 1
    myFile.close()
    return all_groups


def pick_group():
    display_groups_list()
    group_number = int(common_functions.get_user_input("Please choose group: ", "int"))
    groups = get_groups_list()
    groupname = groups[group_number]
    return groupname


def get_task_over_group():
    common_functions.display_menu("groups_data_menu")
    uc = int(common_functions.get_user_input("Please choose entry: ", "int"))
    return uc


def display_groups_list():
    groups = get_groups_list()
    for key in groups.keys():
        print str(key) + ": " + groups[key]


def show_users_in_group(groupname):
    print ("Users in group ")
    uc = get_task_over_group()
    routes.group_data_routes(uc, groupname)


def show_group_id(groupname):
    group_id = "awk -F\: '{print \"Group \" $1 \" with GID=\" $3}' /etc/group | grep %s" % groupname
    print group_id
    system(group_id)
    uc = get_task_over_group()
    routes.group_data_routes(uc, groupname)


def add_user_to_this_group(groupname):
    user_functions.display_users_list()
    user_number = int(common_functions.get_user_input("Please choose user: ", "int"))
    users = user_functions.get_users_list()
    username = users[user_number]
    system("usermod %s -G %s" % (username, groupname))
    uc = get_task_over_group()
    routes.group_data_routes(uc, groupname)


def is_group_exist(groupname):
    all_groups = get_groups_list()
    if groupname in all_groups.values():
        return True
    else:
        return False


def create_group():
    groupname = raw_input("Please enter name for new group :")
    if is_group_exist(groupname):
        print("Group " + groupname + " already exists. Type new groupname: ")
        create_group()
    else:
        command = ('groupadd ' + groupname)
        system(command)
        routes.main_menu_routes()



