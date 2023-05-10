import argparse
import json
import requests
from rich import print

print('''[red]               
\t  _     _  __/_
\t /_//_//_ / /  
\t/   _/         
\t\t[blue] coded by ryuku 🥷
''')

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", help="The domain to search for on crt.sh", required=True)
parser.add_argument("-o", "--output", help="Write the results to a file", required=False)

args = parser.parse_args()

target = f"https://crt.sh/?q={args.domain}&output=json"
try:
    response = requests.get(target)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
    exit()

data = json.loads(response.content)
subs = set()
for item in data:
    sub = item["common_name"]
    if sub not in subs:
        subs.add(sub)
        print(sub)

if args.output:
    with open(args.output, "w") as f:
        for sub in subs:
            f.write(sub + "\n")
