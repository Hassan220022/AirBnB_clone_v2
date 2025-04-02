# Puppet manifest to set up web servers for deployment of web_static

# Update package lists
exec { 'update':
  command => '/usr/bin/apt-get -y update',
}

# Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

# Create required directories
file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data'],
}

file { '/data/web_static/releases':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static'],
}

file { '/data/web_static/shared':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static'],
}

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases'],
}

# Create test HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "<html>\n  <head>\n  </head>\n  <body>\n    ALX\n  </body>\n</html>\n",
  require => File['/data/web_static/releases/test'],
}

# Create symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  force   => true,
  require => File['/data/web_static/releases/test/index.html'],
}

# Configure Nginx
file_line { 'add-location-block':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => "\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n",
  require => Package['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Package['nginx'], File_line['add-location-block']],
} 