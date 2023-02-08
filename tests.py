from main import get_from_api
import database_setup


def test_get_data():
    url = 'https://lukasdearruda.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries.json'
    responses = get_from_api(url)
    values = responses.get("Entries")
    assert len(values) == 10


def test_database():
    test_response = {
        'Entries': [{'EntryId': '1', 'Field1': 'Mr.', 'Field2': 'Joe', 'Field3': 'Schmoe', 'Field4': 'Dude',
                     'Field6': 'Company Inc.', 'Field7': 'therealjoeschmoe@company.net', 'Field8': '',
                     'Field9': '1234567890', 'Field10': 'Guest Speaker', 'Field11': 'Spring 2023', 'Field14': 'Yes'
                     }]}

    connection, cursor = database_setup.open_db("testdb.db")
    cursor.execute("""CREATE TABLE IF NOT EXISTS responses(entryNum PRIMARY KEY , prefix, fName, lName, title, orgName,
            email, orgSite, phoneNum, opportunities, collabTime, permission)""")
    database_setup.write_response_to_database(test_response, cursor)
    connection.commit()

    # Fetch the response from the table
    cursor.execute("""SELECT * FROM responses""")

    # Take the entry retrieved from the db and make it into a list
    entry_from_db = cursor.fetchall()
    database_setup.close_db(connection)
    entry_from_db = list(entry_from_db[0])

    # Make a list of the values from the initial response
    initial_entry = test_response.get("Entries")
    entry_values = list(initial_entry[0].values())

    # See if the two lists are equal
    assert entry_from_db == entry_values

