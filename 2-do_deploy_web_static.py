#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.api import run, put, env
import os.path

# Define the web server hosts - replace with your actual server IPs
env.hosts = ['100.25.19.204', '54.157.159.85']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    Args:
        archive_path: path to the archive to deploy
    Returns:
        True if all operations have been done correctly, False otherwise
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        # Get the filename and directory name from the archive path
        file_name = os.path.basename(archive_path)
        folder_name = file_name.split(".")[0]
        folder_path = "/data/web_static/releases/{}".format(folder_name)

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Create the directory for the release
        run("mkdir -p {}".format(folder_path))

        # Uncompress the archive
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))

        # Remove the archive
        run("rm /tmp/{}".format(file_name))

        # Move the contents to the correct location
        run("mv {}/web_static/* {}".format(folder_path, folder_path))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(folder_path))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(folder_path))

        print("New version deployed!")
        return True
    except Exception:
        return False 