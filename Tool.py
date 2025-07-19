import json
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# Setup Global
global account

# Setup
found = []
input = ''

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
def main():
    while True:
        print("""1. Username Finder
        2.
        3.
        4.
        5.
        5.
        7.
        8.
        9.
        10.
        """)
        while True:
            try:
                input = int(input('> '))
                break
            except ValueError:
                print('Please enter a number')

        if input == 1:
            print("What is the username?")
            account = input('> ')
            whats_my_name(account)
        elif input == 2:
            pass
        elif input == 3:
            pass
        elif input == 4:
            pass
        elif input == 5:
            pass
        elif input == 6:
            pass
        elif input == 7:
            pass
        elif input == 8:
            pass
        elif input == 9:
            pass
        elif input == 10:
            pass

if __name__ == "__main__":
    main()
