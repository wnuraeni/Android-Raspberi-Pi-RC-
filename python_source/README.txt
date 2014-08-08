#setting an server motor dan webcam
lokasi bash script : 
1. motor 
/usr/sbin/servo.sh
2. webcam
/usr/sbin/webcam.sh
3. ultrasonic
/usr/sbin/ultrasonic.sh

ultrasonic sensor, coding fix :
/home/pi/ultrasonic_tes.3py

bash script dibuat run on startup ==> pake crontab

lokasi codingan utama server untuk motor : 
1.  pyro(remote object) server dalam python : /home/pi/movement_server.py
2.  client pyro : /home/robotweb/app.py
    setup aplikasi web app.py sebagai enabled site di ==> /etc/apache2/sites-enabled 
