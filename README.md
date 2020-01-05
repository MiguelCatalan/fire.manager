# fire.manager

Fire manager is a simple service that aims to handle all the fire-squad members and rotations.

### Get everything ready


#### 1- Install pipenv

This project uses pipenv to handle the dependencies and the environment.

If you do not have it yet, install it running: 

```shell script
$ pip install --user pipenv
```

And add the path to your bash

```shell script
$ python -m site --user-base
```
_A sample output can be: `/Users/mike/.local`_

Add this path to bash
```shell script
$ export PATH="$PATH:Users/jetbrains/.local/bin"
```
Run the following command to make the changes effective:
```shell script
$ source ~/.bashrc
```
Ensure you have enabled bashrc in your bash_profile.


#### 2- Run the environment

Gather all the dependencies for the project:

```shell script
$ pipenv install
```

And activate the environment:

```shell script
$ pipenv shell
```

 You are ready to go!!
 

### Test it locally

With the environment activated (see section above) run:

```shell script
$ chalice local
```

And the server should be listening at `http://127.0.0.1:8000`
