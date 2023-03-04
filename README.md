Lukas DeArruda 
COMP 490 Project 1

Need to install requests, pyside6, and create a file called secrets.py that 
contains api_key

This project grabs data from a specified API in json format and saves it to database. 

The database has two tables:
responses, which has columns entryNum, fname, lname, title, orgName, email, orgsite, phoneNum, opportunities, collabTime, permission, claimed, and claimed_email

and

user_records, which has columns claimed_email, fname, lname, title, and dept



Entries are displayed in buttons on the side. Clicking one will show the full information of the entry. After an entry is displayed, a user can click the claim button to begin the claim process. Upon doing so, the user will be propmpted to enter an email. If that email is in the user_records table, the rest of the info auto populates. If not, the user will be prompted to fill in the rest of their info. Once user info is in the database table, the porject can be claimed.

Nothing is missing from this project

Wufoo form: https://lukasdearruda.wufoo.com/forms/zo0ciwg171djx7/

