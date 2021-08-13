# my first file with puppet

file{ '/tmp/holberton':
ensure  =>'file',
mode    =>'0744',
owner   =>'www-data',
content =>'I love puppet'
}
