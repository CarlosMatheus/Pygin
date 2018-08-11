# Pygin

Pygin is a simple game engine made using [Pygame](https://www.pygame.org/).  
One of the purposes of this engine is for making to build more complex games using python.  
This engine includes support for collisions, meshes, materials, game objects and scenes.  
The elements used are very similar to the ones used in the engine [Unity](https://unity3d.com/ "Unity Official Website").

## Getting Started

These instructions will get you the Pygin package ready to run on your local machine if you use Linux. 
Instructions for Windows and Mac would be quite similar.

### Prerequisites

You will just have to install Pygin. The instructions below will show you how to do this for Linux (Ubuntu 16.04).

#### Install Python

First, install de most recent Python version and the most recent version of pip.
Therefore install Python3 setup tools and pip:

```
$ sudo apt-get install python3-setuptools
$ sudo easy_install3 pip
```

#### Install Pygin

Now you will just have to install the Pygin packge.
Then install Pygin using pip:

```
$ pip install pygin
```

## About

This project aims to create a game engine to make easier the precess of game development using python.
To understand a little bit more about how the code is structured visit the [wiki](https://github.com/CarlosMatheus/Engine/wiki).

## Example Games

![game](https://media.giphy.com/media/xB2Y7NHFE8C2Ip9EHD/giphy.gif)
![game](https://media.giphy.com/media/cdyniVu3x1ydtoq99k/giphy.gif)

Check out the game [Balance](https://github.com/CarlosMatheus/Balance), a simple and challenging arcade game made using Pygin.

## Authors

* **Carlos Matheus Barros da Silva** - [CarlosMatheus](https://github.com/CarlosMatheus)
* **Aloysio Galvão Lopes** - [aloysiogl](https://github.com/aloysiogl)
* **Igor Albuquerque Silva** - [igoralbuq](https://github.com/igoralbuq)
* **Eric Pereira Queiroz Moreira** - [ericpqmor](https://github.com/ericpqmor)
* **Igor Mourão Ribeiro** - [igor-ribeiiro](https://github.com/igor-ribeiiro)

## Notes about documentation and contributing

If any substantial change is made, please, help out with the documentation using the [wiki](https://github.com/CarlosMatheus/Balance/wiki).

### Upgrading version on Pypi

Make sure you have the latest versions of setuptools and wheel installed:

```
python -m pip install --upgrade setuptools wheel
```

Now run this command from the same directory where setup.py is located:

```
python3 setup.py sdist
```

This command will generate a file in dist directory.

Now you’ll need to install Twine:

```
python -m pip install --upgrade twine
```

Once installed, run Twine to upload all of the archives under dist:

```
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

You will be asked your username and password from your Pypi account, in which you must have access to the project in oder to upload.

After this, the version on Pypi is already updated. 

Now you should delete the dist folder.

## License

This project is licensed under the MIT License - see the [licence](LICENCE.md) file for details.

## Acknowledgments

* **Professor Edgar Toshiro Yano** - [Curriculum](http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4798593T1&idiomaExibicao=2)



