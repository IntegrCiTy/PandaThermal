# PandaThermal


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Python >= 3.5 (https://www.python.org/downloads/)

```

### Installing

Install git (if not already done) (More info on [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))

If you’re on a Debian-based distribution like Ubuntu, try apt-get:

```
$ sudo apt-get install git-all
```

Install virtualenv (if not already done) (More info on [virtualenv](https://virtualenv.pypa.io/en/stable/installation/))

```
$ pip install virtualenv
```

Create a Python 3.5 virtual env

```
$ virtualenv -p python3 ict
```

Activate the created virtual env (ict)

```
$ source link/to/ict/bin/activate
```

Install dependencies

```
$ pip install -r requirements.txt
```

## Running the tests

Pytest (https://docs.pytest.org/en/latest/) is used in this project.
To run tests just run `pytest` with command line in the dedicated environment in the root forlder of this package.

### Break down into end to end tests


## Built With

* [Pandas](https://pandas.pydata.org/) - data structures and data analysis tools
* [Networkx](https://networkx.github.io/) - manipulation of graph and network

## Authors

* **Pablo Puerto** - *Initial work*

## License

You should have received a copy of the Apache License Version 2.0 along with this program.
If not, see http://www.apache.org/licenses/LICENSE-2.0.

## Acknowledgments

* TO DO ...

