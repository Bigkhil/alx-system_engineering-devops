# this manifest changes the ssh client config. file
$content = 'Host 485479-web-01
    HostName 54.152.135.240
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no'
file { '/etc/ssh/ssh_config':
    ensure  => file
    content => $content
}
