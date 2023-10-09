#!/usr/bin/python3
"""
Fabric script that delete out-of-date archives using do_clean
"""
import os
from fabric.api import *

env.hosts = ["3.90.70.201", "54.146.67.238"]


def do_clean(number=0):
    '''
    This delete out-of-date archives.
    '''
    number = max(1, int(number))

    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs rm -f".format(number))

    with cd("/data/web_static/releases"):
        run("ls -t | grep 'web_static_' | tail -n +{} | xargs rm -rf".format(number))
