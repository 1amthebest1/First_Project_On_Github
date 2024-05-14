start up the apache server using
sudo systemctl restart apache2     # For Ubuntu, Debian, and other systemd-based distributions

start up python server using
sudo python3 -m http.server


start up netcat listener using 

nc -l -p [port]
nc -l -p [port] -s [ip]


