# This Manifest Executes a command

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  onlyif      => 'pgrep killmenow',
  path        => '/usr/bin:/bin'
  refreshonly => true 
}
