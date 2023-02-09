# Install nginx and configure it
exec {'install nginx':
  command  => 'sudo apt-get -y update;
        sudo apt-get -y upgrade; sudo apt install -y nginx;
        echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html;
        sudo sed -i s/"# SSL configuration"/"\tlocation \/redirect_me \{\n\t\treturn 301 \
        https:\/\/www.youtube.com\;\n\t\}\n\t# SSL configuration"/ /etc/nginx/sites-enabled/default;
        sudo service nginx reload',
  provider => 'shell',
}
