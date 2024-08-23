#!/bin/sh

#pytest --cov=./tests/ --cov-report term-missing

#pytest --cov='./tests/' --junitxml=junit.xml -o junit_family=xunit2

#python3 -m coverage html

# or command python3 -m pytest --cov

pytest --maxfail=1  --cov-fail-under=100 --disable-warnings --cov=./src --cov-report=html --cov-report=term-missing