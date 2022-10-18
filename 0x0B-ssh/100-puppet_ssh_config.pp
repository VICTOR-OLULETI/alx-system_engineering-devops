file_line { 'configure file':
  ensure => present,
  path   => '~/.ssh/authorized_keys'
  line   => '    PasswordAuthentication no'
  match  => '#   PasswordAuthentication yes'
}
file_line { 'private key':
  ensure => present,
  path   => '~/.ssh/authorized_keys'
  line   => '    IdentityFile ~/.ssh/school'
  before => 'Port 22'
}
