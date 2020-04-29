# Bot_Insta_DM_Export

Automated program to Convert Instagram Direct Messages export from JSON format to readable text format

HOW TO:

1. How to Download Instagram Messages Data:

Instagram >> Profile >> Settings >> Privacy and Security >> Data Download >> Request Download >> Confirm Email and Password

Data file will be sent to your Email address. It may take up to 48 hours for Instagram to collect this data and send it to you.

2. How to run the program follow below steps:

a. Get the latest version of Python at http://www.python.org/getit/.

b. Ensure that python and pip3 path is added in the environment variables

c. Modify InstaDMsExport.py and change MYUSERNAME to your username. Set PERSONAL_CHAT= None (for all chats).

d. Copy messages.json file from the zip received on Instagram to the InstaDMsExport.py path

e. Run InstaDMsExport.py on CMD using below command

python InstaDMsExport.py
