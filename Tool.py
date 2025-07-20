import os
import sys
import json
import whois
import requests
import time as t
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# Version: 0.4

# Setup Global
global account
global choice

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
    found = []
    def check_site(site):
        try:
            url = site["url_check"].format(account=account2)
            response = requests.get(url, timeout=10)
            if response.status_code == site["e_code"] and site["e_string"] in response.text:
                return f'Name: {site["name"]}, Username: {account2}, URL: {url}, Category: {site["cat"]}'
        except:
            pass
        return None
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_site, site) for site in json_data["sites"]]
        for future in tqdm(as_completed(futures), total=len(futures), desc="Checking sites"):
            result = future.result()
            if result:
                found.append(result)
    clear()
    for site in found:
        print(site)
    t.sleep(1)
    input("Press Enter To Continue")
    clear()

def whois2(website_url):
    domain_info = whois.whois(website_url)
    print(f"Registrar: {domain_info.registrar}, Creation Date: {domain_info.creation_date[0].strftime('%Y-%m-%d %H:%M:%S')}, Expiration Date: {domain_info.expiration_date[0].strftime('%Y-%m-%d %H:%M:%S')}")
    t.sleep(1)
    input("Press Enter To Continue")
    clear()

def main():
    while True:
        while True:
            try:
                print("""0. Quit
1. Username Finder
2. IP Lookup
3. Domain Lookup
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
            print("What is the website url? (Example: https://google.com)")
            url = input('> ')
            whois2(url)
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
        elif choice == 0:
            print('Stoping Program...')
            t.sleep(1)
            clear()
            quit(1)
        choice = ''

if __name__ == "__main__":
    clear()
    main()
