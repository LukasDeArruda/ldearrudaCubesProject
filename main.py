import sys
from requests.auth import HTTPBasicAuth
import requests
import json
from secrets import api_key


def get_from_api(url):
    entry = requests.get(url, auth=HTTPBasicAuth(api_key, 'pass'))
    if entry.status_code != 200:
        print(f"Failed to get data, response code: {entry.status_code} and error message: {entry.reason}")
        sys.exit(-1)
    json_response = entry.json()
    return json_response
    # write_response_to_file(json_response)


def write_response_to_file(response):
    file = open("responses.json", "w+")  # May need to mess around with appropriate privileges
    file.write(str(json.dumps(response, indent=4)))
    file.close()


def main():
    url = 'https://lukasdearruda.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries.json'
    response = get_from_api(url)
    write_response_to_file(response)


if __name__ == '__main__':
    main()
