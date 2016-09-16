from os import system
import os.path
import common_functions
import routes


def get_users_list():
    counter = 1
    myFile = open('/etc/passwd', 'r')
    raw_data = myFile.readlines()
    users = {}
    for line in raw_data:
        splited = line.split(':')
        if float(splited[2]) >= 1000:
            users[counter] = splited[0]
            counter += 1
    myFile.close()
    return users


def pick_user():
    display_users_list()
    user_number = int(common_functions.get_user_input("Please choose user: ", "int"))
    users = get_users_list()
    username = users[user_number]
    return username


def get_task_over_user():
    common_functions.display_menu("users_data_menu")
    uc = int(common_functions.get_user_input("Please choose entry: ", "int"))
    return uc


def display_users_list():
    users = get_users_list()
    for key in users.keys():
        print str(key) + ": " + users[key]


def show_user_groups(username):
    print(system("groups %s" % username))
    uc = get_task_over_user()
    routes.user_data_routes(uc, username)


def show_user_id(username):
    print(system("id -u %s" % username))
    uc = get_task_over_user()
    routes.user_data_routes(uc, username)


def show_user_aliases(username):
    #show_aliases = ("cat /home/%s/.bashrc | grep ^alias" %username)
    #print(system(show_aliases))
    myFile = open('/home/' + username + '/.bashrc', 'r')
    raw_data = myFile.readlines()
    for line in raw_data:
        if line.startswith("alias"):
            print line
    uc = get_task_over_user()
    routes.user_data_routes(uc, username)


def create_new_alias(username):
    new_alias = raw_input("Please input alias to be created , for example : alias ls='ls -aF --color=always'")
    homefolder = os.path.expanduser('~%s' % username)
    bashrc = os.path.abspath('%s/.bashrc' % homefolder)
    with open(bashrc, 'r') as f:
        lines = f.readlines()
        if new_alias not in lines:
            out = open(bashrc, 'a')
            out.write(new_alias)
            out.close()
    uc = get_task_over_user()
    routes.user_data_routes(uc, username)


def reset_password(username):
    system("passwd %s" % username)
    uc = get_task_over_user()
    routes.user_data_routes(uc, username)


def is_user_exist(username):
    users = get_users_list()
    if username in users.values():
        return True
    else:
        return False


def create_user(method):
    username = common_functions.get_user_input("Please type username: ")
    if is_user_exist(username):
        print("User " + username + " already exists. Type new name: ")
        create_user(method)
    else:
        if method == "1":
            system("useradd -s /bin/bash -r %s" % username)
        elif method == "2":
            system("useradd -s /bin/false %s" % username)
        elif method == "3":
            system("useradd -s /bin/bash $s" % username)


def display_user_creation_methods():
    common_functions.display_menu("user_creation_methods")


