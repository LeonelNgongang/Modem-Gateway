#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

import os
import re
import time
import threading
import traceback
import sys

from pygsm import GsmModem
from pygsm import errors

import modem
import port


class App(GsmModem):
    pass

if __name__=="__main__":
    
    print( "run control port")
    node = modem.Modem(port="/dev/ttyACM0")
    #node = modem.GsmModem(port="/dev/ttyACM0")
    print( "int done")
    #node.ping()
    print( "run modem port")
    #time.sleep(2)
    #node.send(number="+393294572379",text="Hello")
    #time.sleep(1)
    #node.send_ussd(pdu="*123#")
    #time.sleep(1)
    #node.start()

    
