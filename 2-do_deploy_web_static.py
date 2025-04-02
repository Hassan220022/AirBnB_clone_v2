#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.api import run, put, env
import os.path

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        folder_name = file_name.split(".")[0]
        folder_path = "/data/web_static/releases/{}".format(folder_name)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}/web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print("New version deployed!")
        return True
    except Exception:
        return False 