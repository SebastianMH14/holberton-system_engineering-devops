#chnague config file
include stdlib
file_line { 'use private key':
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentityFile ~/.ssh/holberton',
    replace => true,
}

file_line { 'using password':
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
    replace => true,
}
