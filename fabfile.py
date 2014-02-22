from fabric.api import local, lcd
import os

# Make sure to set this to where your project is or some commands will fail.
project_dir = os.getenv('PROJECT_DIR')


def push():
    push_to_github()
    push_to_heroku()


def push_to_github():
    local('git push origin master')


def push_to_heroku():
    local('git push heroku master')


def shell():
    with lcd(project_dir):
        local('./manage.py shell --settings=quotes.settings_dev')


def server():
    with lcd(project_dir):
        local('./manage.py runserver --settings=quotes.settings_dev')
