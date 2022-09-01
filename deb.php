#!/bin/bash
#
# Toggles xdebug
#

if [ ! -z $(php -m | grep "xdebug") ] ; then
    phpdismod xdebug
    echo "xdebug is now disabled"
else
    phpenmod xdebug
    echo "xdebug is now enabled"
fi

# exit success
exit 0
