# Installs a Nginx server with custome HTTP header

exec {'update':
  provider => 'shell',
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => 'shell',
  command  => 'sudo apt install -y nginx',
  before   => Exec['add_header'],
}

exec {'add_header':
  provider => 'shell',
  command  => 'sudo sed -i "s/# SSL configuration/\tadd_header X-Served-By \$HOSTNAME;\n\t# SSL configuration/" /etc/nginx/sites-enabled/default',
  before   => Exec['start Nginx'],
}

exec { 'start Nginx':
  provider => 'shell',
  command  => 'sudo service nginx start',
}
