from requests.auth import HTTPBasicAuth
import requests
import json
from secrets import api_key

url = 'https://lukasdearruda.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries.json'


def get_from_api():
    entry = requests.get(url, auth=HTTPBasicAuth(api_key, 'pass'))
    json_response = entry.json()
    write_response_to_file(json_response)


def write_response_to_file(response):
    file = open("responses.json", "w+")  # May need to mess around with appropriate privileges
    file.write(str(json.dumps(response, indent=4)))
    file.close()


def main():
    get_from_api()


if __name__ == '__main__':
    main()
