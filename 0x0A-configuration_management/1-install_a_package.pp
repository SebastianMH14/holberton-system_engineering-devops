#install puppet-lint style check

package{'puppet-lint':
ensure   =>'2.1.1',
provider =>'gem',
}
