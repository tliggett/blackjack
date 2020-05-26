# blackjack

Analysis of the game of blackjack using the pyjack21 blackjack simulator.
This repository is set up as an environment to host a jupyter server.

## Running a jupyter server with this repository

### Install Required Packages

This environment requires the following software packages:
+ python (python 3)
+ pip
+ pipenv

### Spinning up a server
Running the following commands will spin-up a local jupyter server:

```
pipenv shell
pipenv install
jupyter-notebook
```

### To update pyjack21

pyjack21 is still in its alpha phase, so it is important to have the latest version of the package

```
pipenv update pyjack21
```
