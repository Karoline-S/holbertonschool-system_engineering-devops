# apply changes to ssh-config file

exec { 'update_ssh_config':
  command => 'echo "Host 54.242.211.172\n\tIdentifyFile ~/.ssh/school\n\tPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}
