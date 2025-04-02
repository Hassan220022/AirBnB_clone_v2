#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of the AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime


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