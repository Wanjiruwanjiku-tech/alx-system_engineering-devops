# This Manifest Executes a command

exec { 'killmenow_process':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', 'usr/sbin']
}
