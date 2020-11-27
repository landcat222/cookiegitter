#!/usr/bin/env python3.7
from cookiecutter.main import cookiecutter
from sys import argv
from subprocess import call
call(["cookie.sh",cookiecutter(argv[1])])
