from pyomegle import OmegleClient, OmegleHandler
import time
"""
    Omegle inteface for python

    /next
        starts a new conversation
    /exit
        exits chat session
"""

h = OmegleHandler(loop=True)            # session loop
c = OmegleClient(h, wpm=47, lang='en')  # 47 words per minute
c.start()

while 1:
    input_str = input('')           # string input

    if input_str.strip() == '/next':
        c.next()                        # new conversation
    elif input_str.strip() == '/exit':
        c.disconnect()                  # disconnect chat session
        break
    else:
        c.send(input_str)               # send string