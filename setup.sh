#!/usr/bin/env bash         

# login as root and run this script via bash & curl:

apt-get update
apt-get install -y build-essential bison openssl libreadline5 libreadline5-dev curl \
git-core zlib1g zlib1g-dev libopenssl-ruby libcurl4-openssl-dev libssl-dev \
libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev libmysqlclient-dev \
mysql-client mysql-server

bash -s stable < <(curl -s https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer)

cd && echo "[[ -s "/usr/local/rvm/scripts/rvm" ]] && . "/usr/local/rvm/scripts/rvm"" >> .bashrc

source /usr/local/rvm/scripts/rvm

type rvm | head -n1

rvm install 1.9.3
rvm use 1.9.3 --default      

echo "gem: --no-rdoc --no-ri" >> /etc/gemrc

gem install passenger
passenger-install-nginx-module --auto --auto-download     

rvm wrapper 1.9.3 passenger

cd &&
git clone git://github.com/jnstq/rails-nginx-passenger-ubuntu.git &&
mv rails-nginx-passenger-ubuntu/nginx/nginx /etc/init.d/nginx &&
chown root:root /etc/init.d/nginx

update-rc.d nginx defaults   

echo "Nginx successfully installed!"
echo "add this section (or similar) to your nginx.conf and edit:"
echo
echo "server {"
echo "  listen 80;"
# echo "  server_name screencake.com;"
echo "  root /vagrant/public;"
echo "  passenger_enabled on;"
echo "}"
echo    


sudo apt-get install tasksel
sudo tasksel install lamp-server
