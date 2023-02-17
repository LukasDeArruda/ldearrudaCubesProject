import sys
from requests.auth import HTTPBasicAuth
import requests
import json
from secrets import api_key
import database_setup
from PySide6 import QtCore, QtWidgets, QtGui
import UI

def get_from_api(url):
    entry = requests.get(url, auth=HTTPBasicAuth(api_key, 'pass'))
    if entry.status_code != 200:
        print(f"Failed to get data, response code: {entry.status_code} and error message: {entry.reason}")
        sys.exit(-1)
    json_response = entry.json()
    return json_response


def write_response_to_file(response):
    file = open("responses.json", "w+")
    file.write(str(json.dumps(response, indent=4)))
    file.close()


def main():
    url = 'https://lukasdearruda.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries.json'

    connection, cursor = database_setup.open_db("responses.db")
    cursor.execute("""CREATE TABLE IF NOT EXISTS responses(entryNum PRIMARY KEY , prefix, fName, lName, title, orgName,
        email, orgSite, phoneNum, opportunities, collabTime, permission)""")
    response = get_from_api(url)
    database_setup.write_response_to_database(response, cursor)
    connection.commit()
    database_setup.close_db(connection)

    app = QtWidgets.QApplication()
    main_window = UI.Window()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
