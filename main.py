import sys
import json
import database_setup
from PySide6 import QtWidgets
import updateEntriesWindow


def write_response_to_file(response):
    file = open("responses.json", "w+")
    file.write(str(json.dumps(response, indent=4)))
    file.close()


def main():
    connection, cursor = database_setup.open_db("responses.db")
    database_setup.create_table(cursor)
    connection.commit()

    app = QtWidgets.QApplication()
    update_window = updateEntriesWindow.UpdateEntriesWindow(connection, cursor)
    update_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
