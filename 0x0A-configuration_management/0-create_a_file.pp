#my first file with puppet

file { '/tmp/holberton':
ensure  => present,
content => 'I love Puppet',
owner   => www-data,
group   => www-data,
mode    => '0744',
}
