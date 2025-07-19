import sys
import json
import requests
import time as t
from tqdm import tqdm

# Version: 0.1

# Setup Global
global account

# Setup
found = []
choice = ''
ip = ''

def clear():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def ip_lookuo(ipv4):
    request = requests.get(f"http://ip-api.com/json/{ipv4}")
    if request.status_code == 200:
        json_data = json.loads(request.text)
        if json_data["status"] == "success":
            print(f'IP Address: {ipv4}, Country: {json_data["country"]}, Region: {json_data["regionName"]}, City: {json_data["city"]}, Latitude: {json_data["lat"]}, Longitude: {json_data["lon"]}')
    t.sleep(1)
    input("Press Enter To Continue")
    clear()

def whats_my_name(account2):
    with open('data.json', 'r') as d:
        json_data = json.load(d)

    for site in tqdm(json_data["sites"], desc="Checking sites"):
        try:
            request = requests.get(site["url_check"].format(account=account2), timeout=10)
            if request.status_code == site["e_code"] and site["e_string"] in request.text:
                found.append(f'Name: {site["name"]}, Username: {account2}, URL: {site["url_check"].format(account=account2)}, Category: {site["cat"]}')
            elif request.status_code == site["m_code"]:
                pass
            else:
                pass
        except:
            pass

    for found_site in found:
        print(found_site)
    t.sleep(1)
    input("Press Enter To Continue")
    clear()

def main():
    while True:
        while True:
            try:
                print("""1. Username Finder
2. IP Lookup
3.
4.
5.
5.
7.
8.
9.
10.""")
                choice = int(input('> '))
                clear()
                break
            except ValueError:
                print('Please enter a number')
                t.sleep(2)
                clear()

        if choice == 1:
            print("What is the username?")
            account = input('> ')
            whats_my_name(account)
        elif choice == 2:
            print("What is the IPv4 address?")
            ip = input('> ')
            ip_lookuo(ip)
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            pass
        elif choice == 9:
            pass
        elif choice == 10:
            pass
        choice = ''

if __name__ == "__main__":
    main()
