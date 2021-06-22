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
