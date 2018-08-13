import subprocess
import os
path = os.path.realpath("pygin/VERSION")
root_path = os.path.realpath("")

version_file = open(path, 'w')
version = input("What will be this version? ")
version_file.write("def get_version():\n    return '" + str(version) + "'\n")

bashCommands = ["cd " + root_path + " ; python -m pip install --upgrade setuptools wheel",
                "cd " + root_path + " ; python setup.py sdist",
                "cd " + root_path + " ; python -m pip install --upgrade twine",
                "cd " + root_path + " ; twine upload --repository-url https://upload.pypi.org/legacy/ dist/*"]

for bashCommand in bashCommands:
    print(bashCommand)
    process = subprocess.call(bashCommand.split())
