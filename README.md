### python-task

## Prerequisites

1) Have [Python](https://www.python.org/downloads/) installed (Used version 3.9.6)

2) Make sure that your device has **virtualization** enabled

## Installation

Clone the repository and run these commands in the python-task folder in terminal

1) Create an virtual environment on your device:

`python -m venv env`

2) Enter the virtual environment:

`env\scripts\activate`

3) (Optional) If a database is missing:

`python manage.py migrate`

4) Load data from the dictionary JSON file:

`python manage.py loaddata dictionary.json`

5) Run the server:

`python manage.py runserver`

## Usage

There are two endpoints for this project:

1) localhost:8000/words/ - it will display all words in the database in JSON format

2) localhost:8000/words_from_digits/?digit=X

Where `X` can be an integer, for example `228`, `2288`, `28`, `9894`. The numbers will be converted to character combinations on a typical phone and corresponding words will be taken from a dictionary database.

cURL command in terminal can be used:

![example](https://i.imgur.com/hTLGUJb.png)
