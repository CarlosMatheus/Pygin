import sys
from _version import get_version


def print_version():
    print("pygin " + get_version())


def new_project():
    try:
        project_name = str(sys.argv[2])
        print("Creating project " + project_name)

        print("Done")
    except:
        print("you must specify the project name")


functions = {"--version": print_version, "-v": print_version, "new_project": new_project}


def execute_from_command_line():
    try:
        arg1 = str(sys.argv[1])
        functions[arg1]()
    except:
        if len(sys.argv) == 1:
            print("You must specify a command")
            print("Example:")
            print("python -m pygin --version")
        else:
            print("Command not valid")