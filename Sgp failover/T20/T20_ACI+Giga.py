import time
import socket
import http.client
import json
import ssl
import paramiko
import re

UM = "zuyiszh_nm"   #change to your account.
PWD = "Weareosrnoc10"     #change to your password.
t = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
print(t)

ssl._create_default_https_context = ssl._create_unverified_context

try:
    def login(ip, username, pwd):
        conn = http.client.HTTPSConnection(ip)
        payload = "{ \"aaaUser\" : { \"attributes\": {\"name\":\"" + username + "\",\"pwd\":\"" + pwd + "\" } } } "
        headers = {
            'Content-Type': 'application/xml',
        }
        conn.request("POST", "/api/aaaLogin.json", payload, headers)
        res = conn.getresponse()
        data = res.read()
        dd = data.decode("UTF-8")
        aa = json.loads(dd)
        return aa["imdata"][0]["aaaLogin"]["attributes"]["token"]


    subnet = '100.104.2.151CC31'
    ip = subnet[:-4]
    token = login(ip, UM, PWD)
    conn = http.client.HTTPSConnection(ip)
    payload = ''
    headers = {
        'Cookie': "APIC-cookie=" + token
    }
    device_aci = ['101','102','110','111','112','113','114','115','116','117','118','119',
                  '120','121','122','123','124','125','126','127','128','129','130','131','132','133','134','135']
    for ii in device_aci:
        print('-' * 50)
        print(subnet[-4:] + "-node" + ii + "\n")
        conn.request("GET", "/api/node/mo/topology/pod-1/node-" +ii +".json?query-target=subtree&target-subtree-class=eqptPsu",
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        aa = data.decode("utf-8")
        aa_json = json.loads(aa)
        try:
            psu1_device1 = aa_json["imdata"][1]
            psu2_device1 = aa_json["imdata"][0]
            print(
                psu1_device1['eqptPsu']['attributes']['descr'] + '1' + ' ' * 16 + (psu1_device1['eqptPsu']['attributes']['operSt']))
            print(
                psu2_device1['eqptPsu']['attributes']['descr'] + "2" + ' ' * 16 + (psu2_device1['eqptPsu']['attributes']['operSt']))
        except IndexError as e:
            print("Device is not reachable!!!")

    subnet_cc32 = '100.104.0.151CC32'
    ip = subnet_cc32[:-4]
    token = login(ip, UM, PWD)
    conn = http.client.HTTPSConnection(ip)
    payload = ''
    headers = {
        'Cookie': "APIC-cookie=" + token
    }
    device_aci_cc32 = ['101', '102', '110', '111', '112', '113', '114', '115', '116', '117']
    for iii in device_aci_cc32:
        print('-' * 50)
        print(subnet_cc32[-4:] + "-node" + iii + "\n")
        conn.request("GET",
                     "/api/node/mo/topology/pod-1/node-" + iii + ".json?query-target=subtree&target-subtree-class=eqptPsu",
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        aa = data.decode("utf-8")
        aa_json = json.loads(aa)
        try:
            psu1_device1 = aa_json["imdata"][1]
            psu2_device1 = aa_json["imdata"][0]
            print(
                psu1_device1['eqptPsu']['attributes']['descr'] + '1' + ' ' * 16 + (
                psu1_device1['eqptPsu']['attributes']['operSt']))
            print(
                psu2_device1['eqptPsu']['attributes']['descr'] + "2" + ' ' * 16 + (
                psu2_device1['eqptPsu']['attributes']['operSt']))
        except IndexError as e:
            print("Device is not reachable!!!")

except socket.error:
    print("APIC is not reachable!!!")


try:
    def login(ip, username, pwd):
        conn = http.client.HTTPSConnection(ip)
        payload = "{ \"aaaUser\" : { \"attributes\": {\"name\":\"" + username + "\",\"pwd\":\"" + pwd + "\" } } } "
        headers = {
            'Content-Type': 'application/xml',
        }
        conn.request("POST", "/api/aaaLogin.json", payload, headers)
        res = conn.getresponse()
        data = res.read()
        dd = data.decode("UTF-8")
        aa = json.loads(dd)
        return aa["imdata"][0]["aaaLogin"]["attributes"]["token"]


    subnet = ['100.104.2.151CC31', '100.104.0.151CC32']
    for i in subnet:
        ip = i[:-4]
        token = login(ip, UM, PWD)
        conn = http.client.HTTPSConnection(ip)
        payload = ''
        headers = {
            'Cookie': "APIC-cookie=" + token
        }
        conn.request("GET", "/api/node/mo/topology/pod-1/node-1.json?query-target=subtree&target-subtree-class=eqptPsu",
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        aa = data.decode("utf-8")
        aa_json = json.loads(aa) 
        psu1_apic1 = aa_json["imdata"][1]
        psu2_apic1 = aa_json["imdata"][0]
        print('-' * 50)
        print(i[-4:] + "-APIC1" + "\n")
        print(
            psu1_apic1['eqptPsu']['attributes']['descr'] + ' ' * 16 + (psu1_apic1['eqptPsu']['attributes']['operSt']))
        print(
            psu2_apic1['eqptPsu']['attributes']['descr'] + ' ' * 16 + (psu2_apic1['eqptPsu']['attributes']['operSt']))
        conn.request("GET", "/api/node/mo/topology/pod-1/node-3.json?query-target=subtree&target-subtree-class=eqptPsu",
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        aa = data.decode("utf-8")
        aa_json = json.loads(aa)  # 字符串转成字典
        psu1_apic3 = aa_json["imdata"][1]
        psu2_apic3 = aa_json["imdata"][0]
        # print("\n")
        print('-' * 50)
        print(i[-4:] + "-APIC3" + "\n")
        print(
            psu1_apic3['eqptPsu']['attributes']['descr'] + ' ' * 16 + (psu1_apic3['eqptPsu']['attributes']['operSt']))
        print(
            psu2_apic3['eqptPsu']['attributes']['descr'] + ' ' * 16 + (psu2_apic3['eqptPsu']['attributes']['operSt']))

except socket.error:
    print("APIC is not reachable!!!")

devices_ios_gigamon={
"CCSGP-SGP2-GIGAMON-01": "100.104.2.252",
"CCSGP-SGP2-GIGAMON-02": "100.104.2.254",
}
for i in devices_ios_gigamon.items():
    try:
        print('-' * 50)
        print(i[0]+"\n")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(i[1], port=22, username=UM, password=PWD)
        remote = ssh.invoke_shell()
        time.sleep(3)
        remote.send('enable'+'\n')
        remote.send('terminal length 999'+'\n')
        output = remote.send('show env'+'\n')
        time.sleep(2)
        output = remote.recv(65000).decode('ASCII')
        output = re.search(r'Power Module([\w\W]*)Fan tray 1', output).group()
        output = output[:-10]
        print(output)
        ssh.close()
    except socket.error:
        print("Device is not reachable!!!")


x = input("Please input any key to exit it!")