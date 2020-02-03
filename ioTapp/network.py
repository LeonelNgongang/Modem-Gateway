import re
import time
import threading
import traceback
import Queue
import sys

from datetime import datetime

from pygsm import GsmModem
from pygsm import errors


import port
import patterns
import pdu as gsmpdu


class Gprs(GsmModem):
    
    
    def __init__(self,*args,**kwargs):
        
        GsmModem.__init__(self,*args,**kwargs)
        print("initializing Gprs session")
    
    # Function for save configurations that be done in current session. 
    def saveConfigurations(self):
        self.command("AT&W")

    # Function for getting IMEI number
    def getIMEI(self):
        return self.command("AT+CGSN")  # Identical command: AT+GSN

    # Function for getting firmware info
    def getFirmwareInfo(self):
        return self.command("AT+CGMR")  # Identical command: AT+GMR

    # Function for getting hardware info
    def getHardwareInfo(self):
        return self.command("AT+CGMM")  # Identical command: AT+GMM
    
    
    #******************************************************************************************
    #*** SIM Related Functions ****************************************************************
    #****************************************************************************************** 

    # Function returns Mobile Subscriber Identity(IMSI)
    def getIMSI(self):
        return self.command("AT+CIMI")

    # Functions returns Integrated Circuit Card Identifier(ICCID) number of the SIM
    def getICCID(self):
        return self.command("AT+QCCID")

    # Function returning Manufacturer Identification 
    def getManufacturerInfo(self):
        return self.command("AT+CGMI")  # Identical command: AT+GMI
 

    # Fuction for getting signal quality
    def getSignalQuality(self):
        return self.command("AT+CSQ")

    # Function for getting network information
    def getQueryNetworkInfo(self):
        return self.command("AT+QNWINFO")

    # Function for connecting to base station of operator
    def connectToOperator(self):
        print("Trying to connect base station of operator...")
        self.command("AT+CGATT=1")
        self.getSignalQuality()
        
    def detachToOperator(self):
        print("Trying to detach base station of operator...")
        self.command("AT+CGATT=0")
        self.getSignalQuality()

    # Fuction to check the Network Registration Status
    def getNetworkRegStatus(self):
        return self.command("AT+CREG?")
    
    # Function to check the Operator
    def getOperator(self):
        return self.command("AT+COPS?")
    
    #AT+CGACT command is used to activate or deactivate context PDP(Packet Data Profile) 
    def activatePDP(self):
        self.command("AT+CGACT=1,1")
        return self.command("AT+CGACT?")
    
    #Traffic Flow Template
    def trafficPDP(self):
        self.command("AT+CGTFT=?")
        return self.command("AT+CGTFT?")
    
    #Traffic Flow Template AT+CGCLASS=?
    def mobileStationClass(self):
        self.command("AT+CGCLASS=?")
        time.sleep(0.5)
        self.command("AT+CGCLASS=\"CG\"")
        time.sleep(0.5)
        return self.command("AT+CGCLASS?")
    
    # +CGPADDR Command: Show PDP Address
    def showPDPaddress(self):
        self.command("AT+CGPADDR")
        time.sleep(0.5)
        #self.command("AT+CGCLASS=\"CG\"")
        #time.sleep(0.5)
        return self.command("AT+CGPADDR=?")
    
    #+CGAUTO Command: Automatic Response
    def autoRep(self):
        self.command("AT+CGAUTO=1")
        time.sleep(0.5)
        return self.command("AT+CGAUTO?")
    
    #+CGED Command: GPRS Cell Environment
    def cellEnvironment(self):
        self.command("AT+CGED=0")
        time.sleep(0.5)
        return self.command("AT+CGED?")
    
    
    #+CGREG Command: GPRS Network Registration Status
    def netRegStatus(self):
        self.command("AT+CGREG=2")
        time.sleep(0.5)
        return self.command("AT+CGREG?")
    
    #+XCEDATA Command: Establish ECM Data Connection
    def ecmDataConnection(self):
        self.command("AT+XCEDATA=1,1")
        time.sleep(0.5)
        return self.command("AT+XCEDATA?")
    
    #+XDNS Command: Dynamic DNS Request
    def dynamicDnsRequest(self):
        self.command("AT+XDNS=1,1")
        time.sleep(0.5)
        return self.command("AT+XDNS?")
    
    #+CGSMS Command: Select Service for MO SMS Messages
    def serviceforMoSms(self):
        self.command("AT+CGSMS=2")
        time.sleep(0.5)
        return self.command("AT+CGSMS?")
    
    # +KUSBCOMP Command: Set USB Composition
    def setUSBcomp(self):
        self.command("AT+KUSBCOMP=2")
        time.sleep(0.5)
        return self.command("AT+KUSBCOMP?")
    
    #+CGQREQ Command: Request Quality of Service Profile
    def requestQoS(self):
        self.command("AT+CGQREQ=1,1,1,2,2,1")
        time.sleep(0.5)
        return self.command("AT+CGQREQ?")
    
    #+CGQREQ Command: Request Quality of Service Profile
    def request3GQoS(self):
        self.command("AT+CGEQREQ=?")
        time.sleep(0.5)
        return self.command("AT+CGEQREQ?")
    
    #+CGEQNEG Command: 3G Negotiated Quality of Service Profile
    def negotiateQoS(self):
        self.command("AT+CGEQNEG=1,1")
        time.sleep(0.5)
        return self.command("AT+CGEQNEG=?")
 
if __name__=="__main__":
     
     node = Gprs(port="/dev/ttyACM0")
     #node.getFirmwareInfo()
     #node.getHardwareInfo()
     #node.getIMEI()
     #node.getManufacturerInfo()
     #node.saveConfigurations()
     #node.activatePDP()
     #time.sleep(1)
     node.negotiateQoS()