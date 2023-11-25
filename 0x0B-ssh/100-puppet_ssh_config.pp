# 100-puppet_ssh_config.pp

file { '~/.ssh/config':
  ensure => file,
  owner  => 'ubuntu',
  content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}
