from os import system
from os import mkdir


def list_all_mounts():
    system("mount")


def mount_folder():
    mount_point = '/mnt/' + raw_input("Please give a name for the mountpoint: ")
    mkdir(mount_point)
    print("Mount point created on "+ path)
