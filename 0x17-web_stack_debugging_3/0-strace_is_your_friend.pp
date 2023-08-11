# debugging a wrong extension for a php file

exec { 'fix-bug':
    command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
    path    => '/usr/local/bin/:/bin/',
}
