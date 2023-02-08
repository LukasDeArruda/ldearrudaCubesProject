import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def write_response_to_database(response, cursor):
    values = response.get("Entries")  # get the values of initial json dict
    for i in range(len(values)):
        entry_responses = list(values[i].values())  # get the values for the next entry
        try:
            cursor.execute("""INSERT INTO responses (entryNum, prefix, fName, lName, title, orgName, email,
            orgSite, phoneNum, opportunities, collabTime, permission) VALUES (?,?,?,?,?,?,?,?,?,?,?,?) """,
                       (entry_responses[0], entry_responses[1], entry_responses[2], entry_responses[3],
                        entry_responses[4], entry_responses[5], entry_responses[6], entry_responses[7],
                        entry_responses[8], entry_responses[9], entry_responses[10], entry_responses[11]))
        # Insert the values into the database
        except sqlite3.IntegrityError:  # pass if primary key is already used
            pass
