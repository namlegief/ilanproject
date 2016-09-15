from os import system
import common_functions


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



