"""
This file is intended to manage commands received via command line and some operations derived of then
"""


import sys
import os
import errno
import shutil


user_path = os.path.realpath("")
file_path = os.path.realpath(__file__)
pygin_path = os.path.dirname(file_path)
template_path = os.path.join(os.path.join(pygin_path, 'example_games'), 'template_game')
version = str(open(os.path.join(pygin_path, 'VERSION'), 'r').read())


class BColors:
    """
    Class that contains bash string colors
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def substitute_string_in_file(file_path, old_string, new_string):
    """
    Will open the file and substitute all old_string on it with the new_string
    :param file_path: the path to file
    :param old_string: the string that will be substituted
    :param new_string: the string that will be placed on place of old_string
    """
    file_r = open(file_path, 'r')
    code = file_r.read()
    file_r.close()
    file_w = open(file_path, 'w')
    file_w.write(code.replace(old_string, new_string))


def print_version():
    """
    Print the current pygin version
    """
    print("pygin " + version)


def new_project():
    """
    Will try to create a new project in the folder that the user currently is
    """
    try:
        project_name = str(sys.argv[2])
    except:
        project_name = input("What is the project name? ")
    create_new_project(project_name)


def copytree(src, dst, symlinks=False, ignore=None):
    """
    Will copy src directory into dst directory
    :param src: is the directory that contains the files that will be copied into dst directory
    :param dst: is the destiny directory
    """
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def create_new_project(project_name):
    """
    Will try to create a project named project_name in current directory
    :param project_name: the name of the project
    """
    print("Creating project '" + project_name + "'...")
    directory = os.path.join(user_path, project_name)
    try:
        if os.path.isdir(directory):
            print(BColors.FAIL + "Warning: A project folder named '" + project_name +
                  "' already exists in this directory" + BColors.ENDC)
            print("Process aborted")
        else:
            os.makedirs(directory)
            copytree(template_path, directory)
            game_settings_path = os.path.join(os.path.join(directory, 'scripts'), 'game_settings.py')
            substitute_string_in_file(game_settings_path, "default", project_name)
            print("Done")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def help_func():
    """
    Help command
    """
    print_help()


"""
Just Create a new function, and add it name to function dictionary to it became a command
"""
functions = {
    "--version": print_version,
    "-v": print_version,
    "new_project": new_project,
    "help": help_func
}


def print_help():
    """
    Will print information about how to use commands
    """
    print("Type 'python -m pygin help <subcommand>' for help on a specific subcommand\n")
    print("Available subcommands:\n")
    print("[pygin]")
    for key in functions:
        print("    " + key)
    print("")


def execute_from_command_line():
    """
    Will try to execute command passed via cmd arguments
    """
    try:
        arg1 = str(sys.argv[1])
        functions[arg1]()
    except:
        if len(sys.argv) == 1:
            print("\nYou must specify a subcommand")
            print("    Example:")
            print("    'python -m pygin --version'\n")
            print_help()
        else:
            print("Command not valid")
            print("Type 'python -m pygin help' for help\n")
