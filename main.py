import sys
from requests.auth import HTTPBasicAuth
import requests
import json
from secrets import api_key
import database_setup
import sqlite3


def get_from_api(url):
    entry = requests.get(url, auth=HTTPBasicAuth(api_key, 'pass'))
    if entry.status_code != 200:
        print(f"Failed to get data, response code: {entry.status_code} and error message: {entry.reason}")
        sys.exit(-1)
    json_response = entry.json()
    return json_response
    # write_response_to_file(json_response)


def write_response_to_file(response):
    file = open("responses.txt", "w+")  # May need to mess around with appropriate privileges
    # file.write(str(json.dumps(response, indent=4)))
    # file.write(str(response))
    # comment to test workflow
    file.close()


def write_response_to_database(response, cursor):
    values = response.get("Entries")  # get the values of initial json dict
    for i in range(len(values)):
        entry_responses = list(values[i].values())  # get the values for the next entry
        cursor.execute("""INSERT INTO responses (entryNum, prefix, fName, lName, title, orgName, email,
            orgSite, phoneNum, opportunities, collabTime, permission) VALUES (?,?,?,?,?,?,?,?,?,?,?,?) """,
                       (entry_responses[0], entry_responses[1], entry_responses[2], entry_responses[3],
                        entry_responses[4], entry_responses[5], entry_responses[6], entry_responses[7],
                        entry_responses[8], entry_responses[9], entry_responses[10], entry_responses[11]))


def main():
    url = 'https://lukasdearruda.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries.json'

    connection, cursor = database_setup.open_db("responses.db")
    cursor.execute("""CREATE TABLE IF NOT EXISTS responses(entryNum, prefix, fName, lName, title, orgName, email,
    orgSite, phoneNum, opportunities, collabTime, permission)""")
    response = get_from_api(url)
    write_response_to_database(response, cursor)
    connection.commit()
    database_setup.close_db(connection)


if __name__ == '__main__':
    main()
