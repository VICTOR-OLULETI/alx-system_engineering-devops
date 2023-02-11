# Installs a Nginx server with custome HTTP header

#exec {'update':
#  provider => 'shell',
#  command  => 'sudo apt-get -y update',
#  before   => Exec['install Nginx'],
#}

#exec {'install Nginx':
#  provider => 'shell',
#  command  => 'sudo apt-get -y install nginx',
#  before   => Exec['add_header'],
#}

#exec { 'add_header':
#  provider    => 'shell',
#  environment => ["HOST=${HOSTNAME}"],
#  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;
#  /include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
#  before      => Exec['restart Nginx'],
#}

#exec { 'restart Nginx':
#  provider => 'shell',
#  command  => 'sudo service nginx restart',
#}

exec {'update':
  command => 'sudo apt-get -y install nginx',
  before  => Exec['install Nginx'],
}

exec {'install Nginx':
  command => 'sudo apt-get -y install nginx',
  before  => Exec['add_header'],
}

exec {'add_header':
  environment => ["HOST=${HOSTNAME}"],
  command     => 'sudo sed -i "s/# SSL configuration/\tadd_header X-Served-By \$hostname;\n\t# SSL configuration/" /etc/nginx/sites-enabled/default',
  before      => Exec['start Nginx'],
}

exec { 'start Nginx':
  command     => 'sudo service nginx start',
}
