"""
Invokes pygin admin when the pygin module is run as a script.

Example: python -m pygin --version
"""
from _management import execute_from_command_line


if __name__ == "__main__":
    execute_from_command_line()
