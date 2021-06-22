# pyomegle2021
Python API for Omegle webchat. Compatible with Python3.
# Installation 
$ pip install pyomegle2021
# Usage
Go to pyomegle2021/pyomegle2021/user.py

Then execute user.py

$ python3 pyomegle2021/pyomegle2021/user.py

# Greeting
The script will send a fisrt message with 'Hola', to greeting, you can modife this greeting

To modify greeting go to 

$ cd pyomegle2021/pyomegle2021/pyomegle.py

Then go to line 138 and modify fist message o delete it

# Events
List of events accessible by OmegleHandler. Note that OmegleHandler uses a loop optional parameter, valid for start a new chat when a stranger disconnects.

    waiting() Called when we are waiting for a stranger to connect
    connected() Called when we are connected with a stranger
    typing() Called when the user is typing a message
    stopped_typing() Called when the user stop typing a message
    message(message) Called when a message is received from the connected stranger
    common_likes(likes) Called when you and stranger likes the same thing
    disconnected() Called when a stranger disconnects
    captcha_required() Called when the server asks for captcha
    captcha_rejected() Called when server reject captcha
    server_message(message) Called when the server report a message
    status_info(status) Status info received from server
    ident_digest(digests) Identity digest received from server

Inherit OmegleHandler class for implement your custom events.
