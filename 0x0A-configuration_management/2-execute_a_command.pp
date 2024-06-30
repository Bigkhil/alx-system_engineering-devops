# manifest to kill a process
exec { 'killmenow':
  command => 'pkill killmenow',
}
