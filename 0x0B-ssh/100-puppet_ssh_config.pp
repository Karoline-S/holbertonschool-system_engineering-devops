# apply changes to ssh-config file

exec { 'update_ssh_config':
  command  => 'echo "Host 54.242.211.172
    IdentifyFile ~/.ssh/school
    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  provider => 'shell',
}
