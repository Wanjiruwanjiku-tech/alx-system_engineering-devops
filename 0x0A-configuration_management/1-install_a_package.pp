# Installs a package using puppet

package{ 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
