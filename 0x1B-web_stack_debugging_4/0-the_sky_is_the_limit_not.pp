# Fix nginx

service { 'nginx stop':
    ensure => stopped;
}

exec { 'fix--for-nginx':
    command => "sed -i 's/15/2000/g' /etc/default/nginx",
    path    => ['/bin'],
}

service { 'nginx':
    ensure => running,
}