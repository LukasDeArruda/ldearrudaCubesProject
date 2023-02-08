Lukas DeArruda 
COMP 490 Project 1 Sprint 2

Need to install requests, and create a file called secrets.py that 
contains api_key

This project grabs data from a specified API in json format and saves it to database. The database has one table with
12 columns: entryNum, prefix, fName, lName, title, orgName, email, ,orgSite, phoneNum, opportunities, collabTime, permission

Currently, partially missing database test. current test creates a test database and writes a test response to it,
but does not check for if that data is the same as what is initially pushed 