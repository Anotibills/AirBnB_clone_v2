#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['3.90.70.201', '100.26.239.192']

def do_deploy(archive_path):
    '''This distributes an archive to the web servers'''
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('mkdir -p {0}{1}/'.format(path, no_ext))
        run('tar -xzf /tmp/{0} -C {1}{2}/'.format(file_name, path, no_ext))
        run('rm /tmp/{0}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {0}{1}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {0}{1}/ /data/web_static/current'.format(path, no_ext))

        return True
    except Exception as e:
        return False

