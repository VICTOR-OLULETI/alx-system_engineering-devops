file_line { 'configure file':
  ensure => present,
  path   => '/etc/ssh/ssh_config'
  line   => '    PasswordAuthentication no'
  match  => '#   PasswordAuthentication yes'
}
file_line { 'private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config'
  line   => '    IdentityFile ~/.ssh/school'
  before => 'Port 22'
}
