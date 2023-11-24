# Create a file using puppet in /tmp
file {'/tmp/school/0-create_a_file.pp':
ensure  => present,
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
