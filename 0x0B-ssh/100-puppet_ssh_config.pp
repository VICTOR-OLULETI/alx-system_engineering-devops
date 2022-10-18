# configures the configuration file
file_line { 'must authenticate without password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '#   PasswordAuthentication yes',
}
file_line { 'use the given private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  before => 'Port 22',
}
