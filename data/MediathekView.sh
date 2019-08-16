#!/bin/sh
dir=$(dirname $(readlink -f "$0"))
cd "$dir"

/etc/alternatives/jre_11/bin/java -Xmx1G -jar ./MediathekView.jar "$@"
fi
cd $OLDPWD
