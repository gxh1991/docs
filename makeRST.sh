#!/bin/bash
cwd=$(pwd)
cd ./manuals/howto-openstack
mvn clean compile
cp -r $cwd/manuals/howto-openstack/target/generated-docs $cwd/docs2
mv $cwd/docs2/generated-docs $cwd/docs2/howto-openstack
mvn clean
cd $cwd/docs2/howto-openstack
pandoc -f docbook -t rst -s openstack.xml -o index.rst
sphinx-build -b html $cwd/docs2 $cwd/docs2/html



