import sys
import database_setup
import UI
from PySide6 import QtWidgets
import user_info_window

app = QtWidgets.QApplication()

def test_get_data():
    responses = database_setup.get_from_api()
    values = responses.get("Entries")
    assert len(values) == 11


def test_database():
    test_response = {
        'Entries': [{'EntryId': '1', 'Field1': 'Mr.', 'Field2': 'Joe', 'Field3': 'Schmoe', 'Field4': 'Dude',
                     'Field6': 'Company Inc.', 'Field7': 'therealjoeschmoe@company.net', 'Field8': '',
                     'Field9': '1234567890', 'Field10': 'Guest Speaker', 'Field11': 'Spring 2023', 'Field14': 'Yes',
                     'Field15': 0, 'Field16': ''
                     }]}

    connection, cursor = database_setup.open_db("testdb.db")
    database_setup.create_table(cursor)
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


def test_data_in_db():
    conn, cur = database_setup.open_db("testdb.db")
    cur.execute("""SELECT * FROM responses""")
    data = cur.fetchall()
    assert data != None


def test_gui_population():
    conn, cur = database_setup.open_db("testdb.db")
    database_setup.create_table(cur)

    responses = database_setup.get_from_api()
    database_setup.write_response_to_database(responses, cur)
    test_window = UI.Window(conn, cur)
    test_window.show()

    cur.execute("""SELECT * FROM responses""")
    test_data = cur.fetchall()

    test_window.fname_box.setText(test_data[0][1])
    test_window.lname_box.setText(test_data[0][2])
    test_window.guest_speaker_box.setChecked(True)
    test_window.spr2023_box.setChecked(True)

    assert test_data[0][1] == test_window.fname_box.text()
    assert test_data[0][2] == test_window.lname_box.text()
    assert test_window.guest_speaker_box.isChecked()
    assert test_window.spr2023_box.isChecked()


def test_user_creation():
    conn, cur = database_setup.open_db("testdb.db")
    database_setup.create_table(cur)

    window = user_info_window.UserInfoWindow(conn, cur, 0)
    window.show()

    test_entry = ("user@blank.com", "name1", "name2", "title", "dept")

    window.email_box.setText(test_entry[0])
    window.add_email_to_db()

    window.fname_box.setText(test_entry[1])
    window.lname_box.setText(test_entry[2])
    window.title_box.setText(test_entry[3])
    window.dept_box.setText(test_entry[4])

    window.add_new_user()

    cur.execute("""SELECT * FROM user_records WHERE claimed_email = ?""", ("user@blank.com",))
    test_response = cur.fetchall()

    assert test_response[0] == test_entry


def test_populate_user_data():
    conn, cur = database_setup.open_db("testdb.db")
    database_setup.create_table(cur)

    conn.execute("""INSERT OR REPLACE INTO user_records VALUES(?,?,?,?,?)""", ("test@test.com", "fname", "lname", "title",
                                                                    "department"))

    window = user_info_window.UserInfoWindow(conn, cur, 0)
    window.show()

    window.email_box.setText("test@test.com")
    window.add_email_to_db()

    assert window.fname_box.text() == "fname"
    assert window.lname_box.text() == "lname"
    assert window.title_box.text() == "title"
    assert window.dept_box.text() == "department"


