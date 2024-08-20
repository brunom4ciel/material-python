#!/bin/sh

pytest --cov=./tests/ --cov-report term-missing

#pytest --cov='./tests/' --junitxml=junit.xml -o junit_family=xunit2

#python3 -m coverage html

# or command python3 -m pytest --cov