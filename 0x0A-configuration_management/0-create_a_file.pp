#my first file with puppet

file { '/tmp/holberton':
ensure  => present,
content => 'I love puppet',
owner   => www-data,
group   => www-data,
mode    => '0744',
}
