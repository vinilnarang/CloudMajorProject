sudo apt-get install git

sudo apt-get install   ant   gcc   g++   libkrb5-dev   libmysqlclient-dev   libssl-dev   libsasl2-dev   libsasl2-modules-gssapi-mit   libsqlite3-dev   libtidy-0.99-0   libxml2-dev   libxslt-dev   maven2   libldap2-dev   python-dev   python-simplejson   python-setuptools   

git clone http://github.com/cloudera/hue.git

cd hue/

cd /usr/lib/python2.7

sudo cp plat-i386-linux-gnu/_sysconfigdata_nd.py .

sudo make apps

build/env/bin/hue runserver

