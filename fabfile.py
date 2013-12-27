from fabric.api import local


def push():
    push_to_github()
    push_to_heroku()


def push_to_github():
    local('git push origin master')


def push_to_heroku():
    local('git push heroku master')
