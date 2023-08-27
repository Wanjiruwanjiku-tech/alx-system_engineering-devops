# This puppet manifest cofigures an ssh client

file_line { 'Turn off passwd Authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentifyFile ~/.ssh/school',
  match => '^#?IdentifyFile',
}
