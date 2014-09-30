#!/usr/bin/env python

from fabric.api import run, env
import os

# internal IP
#env.hosts = ['172.16.100.169']

# external IP
#env.hosts = ['61.43.139.143']

def host_type():
    run('uname -s')

