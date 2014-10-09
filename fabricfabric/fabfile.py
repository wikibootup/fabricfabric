#!/usr/bin/env python

from fabric.api import run, sudo, env
import os

# internal IP
env.hosts = [os.environ['BUILDBUILD_IN_IP']]

# external IP
#env.hosts = [os.environ['BUILDBUILD_EX_IP']]
env.user = 'buildbuild'

def host_type():
    run('uname -s')

