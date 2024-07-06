# this manifest changes the ssh client config. file
$content = 'IdentityFile ~/.ssh/school
    PasswordAuthentication no'
file { '/etc/ssh/ssh_config':
    ensure  => file
    content => $content
}
