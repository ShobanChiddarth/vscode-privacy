# Please run as sudo
import  os
import sys
import json

SETTINGS_DOT_JSON = "/home/shobanchiddarth/.config/Code/User/settings.json"
HOSTS_FILE = "/etc/hosts"

if os.path.exists("./assets/settings_default.json"):
    pass
else:
    with open(SETTINGS_DOT_JSON, 'r', newline='\n') as fh:
        default_settings = fh.read()
    with open("./assets/settings_default.json", "w", newline="\n") as fh:
        fh.write(default_settings)

if os.path.exists("./assets/hosts_default"):
    pass
else:
    with open(HOSTS_FILE, "r", newline='\n') as fh:
        hosts_data = fh.read()
    with open("./assets/hosts_default", "w", newline="\n") as fh:
        fh.write(hosts_data)

def increase_privacy():
    final_host_data = ""
    with open("./assets/hosts_default", 'r', newline="\n") as fh:
        final_host_data += fh.read()
    with open("./assets/hosts_increase_privacy", 'r', newline="\n") as fh:
        final_host_data += fh.read()

    with open(HOSTS_FILE, 'w', newline='\n') as fh:
        fh.write(final_host_data)


    final_json_dict = {}
    with open("./assets/settings_default.json", "r", newline='\n') as fh:
        final_json_dict.update(json.loads(fh.read()))
    with open("./assets/setting_increase_privacy.json", "r", newline='\n') as fh:
        final_json_dict.update(json.loads(fh.read()))
    
    with open(SETTINGS_DOT_JSON, 'w', newline='\n') as fh:
        fh.write(json.dumps(final_json_dict, indent=4))


def decrease_privacy():
    with open("./assets/hosts_default", 'r', newline="\n") as fh:
        final_host_data = fh.read()
    with open(HOSTS_FILE, 'w', newline='\n') as fh:
        fh.write(final_host_data)

    with open("./assets/settings_default.json", "r", newline='\n') as fh:
        final_json_data = fh.read()
    with open(SETTINGS_DOT_JSON, 'w', newline='\n') as fh:
        fh.write(final_json_data, indent=4)

if len(sys.argv)>2:
    raise SyntaxError("Only 1 argument allowed")

if len(sys.argv)==1:
    sys.exit()
elif sys.argv[1]=="--increase-privacy":
    increase_privacy()
elif sys.argv[1]=="--decrease-privacy":
    decrease_privacy()
elif sys.argv[1]=='--wipe':
    os.remove("./assets/hosts_default")
    os.remove("./assets/settings_default.json")
elif sys.argv[1]=="--help":
    print("Refer README.md")
else:
    raise SyntaxError("Unknown Arguement")
