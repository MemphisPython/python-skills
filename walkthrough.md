# Walkthrough

This document includes some discussion and code samples presented during
the workshop. These all assume you're using Python 3.


## One-liners

Python allows you to run python code by either with `python -m`, which lets
you invoke a module directly, or with `python -c` which lets you specify a
command.  The following are a set of simple, useful tools you can run
from a command line interface.

### Print a Calendar

Print a calendar for the current year:

    python -m calendar

Print a calendar for a specified year:

    python -m calendar 2018

Print a calendar for a specified year and a specified month:

    python -m calendar 2018 12


For more details, see the [calendar docs](https://docs.python.org/3/library/calendar.html).


### Run a webserver

Run a local webserver in the current directory.

    python -m http.server


For more information, see the [http.server docs](https://docs.python.org/3/library/http.server.html#module-http.server).

### Handle .zip files

You can create, extract, or just list the contents of a zipfile with python.
To list the contents of a zip file without extracting, use the `-l` flag:

    python -m zipfile -l SomeFile.zip

To extract files (i.e. unzip a zip file), specify the directory you want to
extract into. This will create a directory if necessary.

    python -m zipfile -e SomeFile.zip contents


To create a zipfile, first specify the name of the zip file, then specify
the list of files you want to include.

    python -m zipfile -c MyFiles.zip document.doc readme.txt index.html

To learn more, see the [zipfile docs](https://docs.python.org/3/using/cmdline.html#options-you-shouldn-t-use)


## Print a random number

Print a random number from 0-10:

    from random import randint
    print(randint(0, 10))


You can also run this on the command line with:

    python -c "from random import randint; print(randint(0, 10))"


## Pick a random item from a list

See `code/random_number.py`.

## Generate a random password

See `code/random_password.py`.

There's also an open-source python module that will generate readable passwords:
[ninethreesix](https://github.com/bradmontgomery/python-ninethreesix). You can
install it with

    pip install python-ninethreesix

## Process a CSV

There's a subset of data from the [College Scorecard Data](https://catalog.data.gov/dataset/college-scorecard)
retreived from data.gov, and there are two tasks we'll peform:

1. List the women-only schools, including in-state and out-of-state tuition.
2. Generate a new CSV that contains all the schools in Alaska.

You can see example implementations of this in `code/process_csv.py`.

## Scrape a web page


