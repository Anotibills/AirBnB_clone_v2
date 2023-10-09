# Configures a web server for deployment of web_static.

$nginx_conf = "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;

    location /404 {
        root /var/www/html;
        internal;
    }
}
"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
}

file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School Puppet\n",
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}

file { ['/var/www', '/var/www/html']:
  ensure => 'directory',
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n",
}

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n",
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf,
}

exec { 'nginx_restart':
  command => '/etc/init.d/nginx restart',
  refreshonly => true,
  path => ['/sbin', '/usr/sbin', '/usr/local/sbin', '/bin', '/usr/bin'],
}
