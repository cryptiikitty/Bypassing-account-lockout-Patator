
# Description

Automation of bruteforce ActiveSync/ldap (can be adapted to any one if desired) using patator without account blocking (many companies have restrictions, the script will help you remain invisible)
! use the official Patator docker image

The scripts have built-in bots for the eXpress messenger (not popular, replace with the one you need)

```bash
start_activesync.py - main script, there is also a version for testing via ldap - start_ldap.py
bot.py - bot for sending results for the current night
end_of_scan.py, bot2.py - sending final results
```
## cron
```bash
40 22 1 * * python3 start_activesync.py -p all_pass.txt 2>&1
...
00 09 17 * * python3 end_of_scan.py 2>&1
```
