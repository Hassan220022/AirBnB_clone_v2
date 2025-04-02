#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Install Nginx if not installed
apt-get -y update
apt-get -y install nginx

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart

exit 0 