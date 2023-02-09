# Installs a Nginx server

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/# SSL configuration/\tlocation \/redirect_me \{\n\t\treturn 301 https:\/\/www.youtbue.com;\n\t\}\n\t# SSL configuration/" /etc/nginx/sites-enabled/default ; sudo service nginx start',
}
