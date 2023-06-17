## import statements
from random import randrange
from threading import Thread
from time import sleep, ctime
from requests import get
from os import system as system_caller, remove, system


## all tunnels to be made along with their name in dictionary, port, other details
tunnels_to_be_made = {
'0a':{
"key":"adfly_host_page_list",
"config":"""
version: "2"
region: in
authtoken: 288KImUNY3LWKmEPFNNUmDCk2OV_3LQiUwwthDHkmQ2Eo8NAx
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_host_page_list:
        addr: 127.0.0.1:65500
        inspect: false
        proto: http
        schemes:
            - https
            - http
"""},
'0b':{
"key":"adfly_user_tcp_connection_list",
"config":"""
version: "2"
region: in
authtoken: 28oHShvU9VUXOCY6aQWDpVNi8pG_3nU1hBpDQPMTqPxyrEtaK
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_user_tcp_connection_list:
        addr: 127.0.0.1:65499
        inspect: false
        proto: tcp
"""},
'1a':{
"key":"adfly_host_page_list",
"config":"""
version: "2"
region: in
authtoken: 2DcEw2SNo1b7gtrI8F3Nvqn0BXV_2RovXkJDK8V7mP5zFRkps
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_host_page_list:
        addr: 127.0.0.1:65500
        inspect: false
        proto: http
        schemes:
            - https
            - http
"""},
'1b':{
"key":"adfly_user_tcp_connection_list",
"config":"""
version: "2"
region: in
authtoken: 2DcFDbjSWoONL9wPpqR7TrzRkG0_691tmp39xLpAJn25FiaC5
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_user_tcp_connection_list:
        addr: 127.0.0.1:65499
        inspect: false
        proto: tcp
"""},
'2a':{
"key":"adfly_host_page_list",
"config":"""
version: "2"
region: in
authtoken: 2DcFZvIBBfSxHswi1uEilJiOCgM_W5xTFuKVMuqdB8ToSbJk
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_host_page_list:
        addr: 127.0.0.1:65500
        inspect: false
        proto: http
        schemes:
            - https
            - http
"""},
'2b':{
"key":"adfly_user_tcp_connection_list",
"config":"""
version: "2"
region: in
authtoken: 2DcFLz4kDWgTfkoacSGOSPwzrCL_7iVhooTMGr8QqfiD5A995
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_user_tcp_connection_list:
        addr: 127.0.0.1:65499
        inspect: false
        proto: tcp
"""},
'3a':{
"key":"adfly_host_page_list",
"config":"""
version: "2"
region: in
authtoken: 2DcEjq3TBJGAzc3N3bHtscnIqS1_4CFoSJtWdDGQ2T7wwUL9t
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_host_page_list:
        addr: 127.0.0.1:65500
        inspect: false
        proto: http
        schemes:
            - https
            - http
"""},
'3b':{
"key":"adfly_user_tcp_connection_list",
"config":"""
version: "2"
region: in
authtoken: 2DcF4xgpB8NR8RicbmRk3HsLSgB_J1TffcJApwCcZ5fSoDfp
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_user_tcp_connection_list:
        addr: 127.0.0.1:65499
        inspect: false
        proto: tcp
"""},
'4a':{
"key":"adfly_host_page_list",
"config":"""
version: "2"
region: in
authtoken: 2HRf8FYa3MQVhzdQFZvxHPtDk7F_2JAshTRU7kUuW4Y5FW5Lr
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_host_page_list:
        addr: 127.0.0.1:65500
        inspect: false
        proto: http
        schemes:
            - https
            - http
"""},
'4b':{
"key":"adfly_user_tcp_connection_list",
"config":"""
version: "2"
region: in
authtoken: 2HRf1qBP3y3CaSv1BA2b7wVBIHk_4hLrhTATrSVzJeEkNZizh
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_user_tcp_connection_list:
        addr: 127.0.0.1:65499
        inspect: false
        proto: tcp
"""},
'5a':{
"key":"adfly_host_page_list",
"config":"""
version: "2"
region: in
authtoken: 2HRexNynMGyhwU72nfvRs5OmE8f_6WvwqGRbSEi5FwgRwZG4T
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_host_page_list:
        addr: 127.0.0.1:65500
        inspect: false
        proto: http
        schemes:
            - https
            - http
"""},
'5b':{
"key":"adfly_user_tcp_connection_list",
"config":"""
version: "2"
region: in
authtoken: 2HReqArC0mWtExMr5vdZaKQniW6_5xhYZTPHxHHuSuxYWERdH
web_addr: 127.0.0.1:INSPECT_PORT
inspect_db_size: -1
log_level: crit
tunnels:
    adfly_user_tcp_connection_list:
        addr: 127.0.0.1:65499
        inspect: false
        proto: tcp
"""}
}

final_readme_data = {}

def check_ngrok_yml_location():
    default_locations = [
        r"C:\Users\Administrator\AppData\Local\ngrok\ngrok.yml",
        r"C:\Users\Administrator\.ngrok2\ngrok.yml"
    ]
    for location in default_locations:
        try:
            open(location, 'r').read()
            return location
        except:
            pass


def check_and_lock_yml():
    string = str(randrange(1, 10000))
    for _ in range(5):
        try:
            open(config_location.replace("ngrok.yml", "ngrok.yml.lock"),'r')
            sleep(1)
        except:
            break
    open(config_location.replace("ngrok.yml", "ngrok.yml.lock"), 'w').write(string)
    return string


def free_yml(string):
    try:
        if open(config_location.replace("ngrok.yml", "ngrok.yml.lock"), 'r').read() == string:
            remove(config_location.replace("ngrok.yml", "ngrok.yml.lock"))
    except:
        pass


def create_tunnel(index):
    url = ''
    while True:
        inspect_port = randrange(52000, 55000)
        with open(config_location, 'w') as file:
            file.write(tunnels_to_be_made[index]['config'].replace("INSPECT_PORT", str(inspect_port)))
        Thread(target=system_caller, args=("ngrok start --all",)).start()
        for _ in range(100):
            xml_data = eval(get(f"http://127.0.0.1:{inspect_port}/api/tunnels").text.replace("false", "False").replace("true", "True"))
            tunnels = xml_data["tunnels"]
            if len(tunnels) != 0:
                break
            sleep(0.1)
        else:
            input("\n\nno tunnels\n\n")
            continue
        for tunnel_index in range(len(tunnels)):
            url = tunnels[tunnel_index]['public_url']
        break
    return url


def git_commit():
    with open('README.md', 'w') as file:
        file.write(str(final_readme_data))
    system('git add .')
    system(f'git commit -m "{ctime()}"')
    system('git push')


config_location = check_ngrok_yml_location()
for index in tunnels_to_be_made:
    lock_string = check_and_lock_yml()
    url = create_tunnel(index).replace("tcp://","").replace("http://", "https://")
    key = tunnels_to_be_made[index]['key']
    if key in final_readme_data:
        final_readme_data[key].append(url)
    else:
        final_readme_data[key] = [url]
    free_yml(lock_string)
git_commit()
