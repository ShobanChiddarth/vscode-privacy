# Script to increase and decrease privacy in vscode

## Important Notice (for Windows Users)

- **Privacy Concerns**: It is well known that Microsoft collects your data even if you don't use VSCode.
- **Recommendation**: Like every other Linux user, I am suggesting you to switch to Linux, for enhanced privacy.
- **Alternative Option**: However if it is impossible at the moment, like if you are in a school computer,
   - watch [this video](https://www.youtu.be/SvhRXLmsyJ8),
   - and visit [this link](https://briteccomputers.co.uk/posts/stop-windows-spying-on-you-2/)
   
   to stop the data collection (not a foolproof way but works to some extent).
   I have visited and tested what is said in the links myself and it works fine. I recommend you too try doing it
   and test it with Wireshark if you want to,
- **Note**: You can't stop it 100% because Windows is propertiary spyware and that is why you should switch to Linux.


## Who is this for?
This script is for those
1. [Who care about Microsoft collecting your data through VS Code telemetry without consent](https://www.roboleary.net/tools/2022/04/20/vscode-telemetry.html) | [Archived](https://web.archive.org/web/20240117122417/https://www.roboleary.net/tools/2022/04/20/vscode-telemetry.html)
2. Can't use [VSCodium](https://vscodium.com/) because you have to use propertiary extensions / features like sync and etc
3. And don't want Microsoft to collect your data while you are not using the features


## USAGE [TL;DR]

1. Open up [vscode-privacy.py](./vscode-privacy.py) and edit `SETTINGS_DOT_JSON` and `HOSTS_FILE` to their respective paths in your computer
2. (Optional) To create a copy of hosts file and settings.json file without changing anything, run
   ```sh
   sudo python3 vscode-privacy.py
   ```
3. To increase privacy, run
   ```sh
   sudo python3 vscode-privacy.py --increase-privacy
   ```
4. To decrease privacy, run
   ```sh
   sudo python3 vscode-privacy.py --decrease-privacy
   ```
5. (Optional) To wipe out the copies of hosts file and settings.json file, run
   ```sh
   sudo python3 vscode-privacy.py --wipe
   ```

## USAGE [In detail]

When this script "increases" your privacy, it appends few lines to host file and
edits some settings in vscode's settings.json. They can be found in [`hosts_increase_privacy`](./assets/hosts_increase_privacy)
and [`settings_increase_privacy.json`](./assets/setting_increase_privacy.json)
respectively. Alternatively, when this script "decreases" your privacy, it reverts
back to what they were before you ran this script. 

The few lines appended to hosts file block the vscode domains by redirecting them
to localhost. And the settings edit turns off all telemetry possible. So if you
want to sign in to enable sync, or install any extensions, or use any extensions
that require connecting those services, make sure you aren't already blocing those
domains (settings.json is not a problem initially) run
```sh
sudo python3 vscode-privacy.py --decrease-privacy
```
and do what you want to do.

After your job of connecting VSCode to the internet is done, run
```sh
sudo python3 vscode-privacy.py --increase-privacy
```

This script is for automating the process of editing host file and settings file
for those who constantly need to run services that cost your privacy in vscode.

## Requirements

- Python 3.x (I used 3.11.2 while writing this script)
