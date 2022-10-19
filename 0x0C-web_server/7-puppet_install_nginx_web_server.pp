# Install nginx and configure it
exec {'install nginx':
  command  => 'sudo apt-get -y update;
	sudo apt-get -y upgrade; sudo apt install -y nginx; 
	echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html;
	sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect\/*$
	 https:\/\/www.youtube.com\/watch\?v\=QH2\-TGUlwu4 permanent;/" /etc/nginx/sites-enabled/default;
	sudo service nginx start',
  provider => 'shell',
}
