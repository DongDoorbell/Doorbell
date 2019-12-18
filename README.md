# Doorbell
Budget Security doorbell made with a raspberry pi

# Make sure to install motion

wget github.com/Motion-Project/motion/releases/download/release-4.0.1/pi_jessie_motion_4.0.1-1_armhf.deb

sudo apt-get install gdebi-core

sudo gdebi pi_jessie_motion_4.0.1-1_armhf.deb

# install msmtp

make sure to install get msmtp

# where the files go

msmtprc goes in /etc/

motion.conf goes in /home/pi/.motion

epic.txt goes in /home/pi/

python scripts also go in /home/pi/
