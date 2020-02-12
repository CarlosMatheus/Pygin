# Pygin

Pygin is a simple game engine made using [Pygame](https://www.pygame.org/). 
The main purpose of this engine is to make the development of a more complex game using python easier.
This engine includes support for collisions, meshes, materials, game objects, and scenes.  
The elements used are very similar to the ones used in the engine [Unity](https://unity3d.com/ "Unity Official Website").

## Getting Started

These instructions will get you the Pygin package ready to run on your local machine if you use Linux. 
Instructions for Windows and Mac would be quite similar.

### Prerequisites

Make sure you have python3 and pip3 installed.

### Install Pygin

Now you will just have to install the pygin package.
Then install pygin using pip:

```
$ pip3 install pygin
```

## About

This project aims to create a game engine to make easier the process of game development using python.
To understand a little bit more about how the code is structured visit the [wiki](https://github.com/CarlosMatheus/Engine/wiki).

## Usage

The project doesn't have official documentation yet. 

> But the usage is similar to Unity's scripts on GameObjects making use of start and update functions. There are also GameObjects and they have components, similarly to Unity.

The overall structure of a project that uses pygin can be seen on the game example bellow.

## Example Games

![game](https://media.giphy.com/media/xB2Y7NHFE8C2Ip9EHD/giphy.gif)
![game](https://media.giphy.com/media/cdyniVu3x1ydtoq99k/giphy.gif)

Check out the game [Balance](https://github.com/CarlosMatheus/Balance), a simple and challenging arcade game made using Pygin.

## Notes about documentation and contributing

If any substantial change is made, please, help out with the documentation using the [wiki](https://github.com/CarlosMatheus/Balance/wiki).

### Upgrading version on PyPI

Make sure you have the latest versions of setuptools and wheel installed:

```
python -m pip install --upgrade setuptools wheel
```

Now run this command from the same directory where setup.py is located:

```
python setup.py sdist
```

This command will generate a file in the dist directory.

Now you’ll need to install Twine:

```
python -m pip install --upgrade twine
```

Once installed, run Twine to upload all of the archives under dist:

```
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

You will be asked your username and password from your Pypi account, in which you must have access to the project to upload.

After this, the version on Pypi is already updated. 

Now you should **delete the dist folder**.

