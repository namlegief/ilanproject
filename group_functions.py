from os import system
import common_functions
import user_functions

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


def display_groups_list():
    groups = get_groups_list()
    for key in groups.keys():
        print str(key) + ": " + groups[key]


def show_users_in_group(groupname):
    print ("Users in group ")


def show_group_id(groupname):
    print ("group ID is: ABC")


def add_user_to_this_group(groupname):
    user_functions.display_users_list()
    user_number = int(common_functions.get_user_input("Please choose user: ", "int"))
    users = user_functions.get_users_list()
    username = users[user_number]
    system("usermod %s -G %s" % (username, groupname))