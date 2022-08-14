# creates a file in /tmp folder with given permissions and content

$str = 'I love Puppet'
$mode = 'a=r,u+wx'

file { '/tmp/school':
  ensure  => file,
  content => $str,
  owner   => www-data,
  group   => www-data,
  mode    => $mode,
  }