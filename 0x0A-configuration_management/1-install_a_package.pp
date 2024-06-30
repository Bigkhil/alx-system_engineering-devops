# this puppet manifest should install a package
exec { 'python3-pip':
  ensure => 'installed',
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['python3-pip']
}
