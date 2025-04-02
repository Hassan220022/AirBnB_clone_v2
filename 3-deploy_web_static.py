#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""
from fabric.api import env, local, run, put
from datetime import datetime
import os.path

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_pack():
    """
    Generates a .tgz archive from the contents of web_static folder
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        file_path = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception:
        return None


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


def deploy():
    """
    Creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path) 