#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""
from fabric.api import env, local, run, cd
import os

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)
    if number == 0 or number == 1:
        number = 1
    else:
        number = int(number)

    # Local cleanup
    local('cd versions && ls -t | tail -n +{} | xargs -I {{}} rm {{}}'.format(
        number + 1))

    # Remote cleanup
    with cd('/data/web_static/releases'):
        run('ls -t | grep -v "current" | tail -n +{} | xargs -I {{}} rm -rf {{}}'.format(
            number + 1)) 