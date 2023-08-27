# This puppet manifest cofigures an ssh client

include stdlib

file_line { 'Turn off passwd Authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '   PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '   IdentifyFile ~/.ssh/school',
}
