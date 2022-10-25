# Install and configure nginx HTTP response with custom header
exec {'install nginx':
  command  => 'sudo apt-get -y update;
        sudo apt-get -y upgrade; sudo apt install -y nginx;
        echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html;
        sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect\/*$
         https:\/\/www.youtube.com\/watch\?v\=QH2\-TGUlwu4 permanent;/" /etc/nginx/sites-enabled/default;
        sudo touch /usr/share/nginx/html/custom_404.html;
	echo "Ceci n\'est pas une page" | sudo tee /usr/share/nginx/html/custom_404.html;
	sudo sed -i "s/index.nginx-debian.html;/index.nginx-debian.html;
	\n\terror_page 404 \/custom_404.html;
	\n\tlocation \= \/custom_404.htm\{\n\t\troot \/usr\/share\/nginx\/html;\n\t\tinternal;
	\n\t\}/" /etc/nginx/sites-enabled/default;
	sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;
	/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By ${HOSTNAME};/" /etc/nginx/nginx.conf;
	sudo service nginx start',
  provider => 'shell',
}

