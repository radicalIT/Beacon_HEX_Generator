# -*- coding: utf-8 -*-
import os

print( '''
    Welcome in iBeacon Message generator
    1. Choose message type:
        0: UUID + Major + Minor
        1: URL
        2: NameID + IstanceID
'''
)
msgTypes = [ "0: UUID + Major + Minor", "1: URL", "2: NameID + IstanceID" ]

msgType = input()
while msgType not in [ 0, 1, 2 ]:
    print( "Error! Bad argument" )
    print( "Try again:" )
    msgType = input()
msgType = int( msgType )
print( "You type " + msgTypes[ msgType ] )

if msgType == 0:
    print( '''
        Great! Now type your UID
        UID is a 16 Byte of two-HEX-character values separated by spaces
	!!! Insert your id into ' ' !!!
        e.g. '63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5'
    ''' )
    uid = input()
    while len( uid) != 47 :
        print( "Error! You input bad UID" )
        print( "Try again:" )
        uid = input()
    
    print( '''
        Nice! Now you can type your Major value
        Value ‭must be in range from 0 to 65535‬
        e.g. 3849
    ''' )
    major = int( input() )
    while major < 0 or major > 65535:
        print( "Error! You input bad Major value" )
        print( "Try again:" )
        major = int( input() )


    print( '''
        Good! Now you can type your Minor value
        Value ‭must be in range from 0 to 65535‬
        e.g. 3849
    ''' )
    minor = int( input() )
    while minor < 0 or minor > 65535:
        print( "Error! You input bad Minor value" )
        print( "Try again:" )
        minor = int( input() )

    mssg = 'python iBeacon.py 0 \"' + uid + "\" " + str( major ) + " " + str( minor )
    #print( mssg )
    os.system( mssg )
if msgType == 1:
    print( '''
        Great! Now type your url suffix
        Choose one of options:
            0:	.com/
            1:	.org/
            2:	.edu/
            3:	.net/
            4:	.info/
            5:	.biz/
            6:	.gov/
            7:	.com
            8:	.org
            9:	.edu
            10:	.net
            11:	.info
            12:	.biz
            13:	.gov
        e.g. 0
    ''' )
    suffix = int( input() )
    while suffix < 0 or suffix > 13:
        print( "Error! Bad argument" )
        print( "Try again:" )
        suffix = int( input() )

    print( '''
        Nice! Now type your url address
        Max. 16 chars ( $ count as 1 char )
        Use $ to insert sufix (".com",".net")
	!!! Insert your url into ' ' !!!
        e.g. 'facebook$me' with suffix 0 mean facebook.com/me
    ''' )
    url = input()
    while len( url) > 16 :
        print( "Error! You input too long Url" )
        print( "Try again:" )
        url = input()

    print( '''
        Great! Now type your url prefix
        Choose one of options:
            0:  http://www.
            1:  https://www.
            2:  http://
            3:  https://
        e.g. 0
    ''' )
    prefix = int( input() )
    while prefix < 0 or prefix > 3:
        print( "Error! Bad argument" )
        print( "Try again:" )
        prefix = int( input() )


    mssg = 'python iBeacon.py 1 \'' + url + "\' " + str( prefix ) + " " + str( suffix )
    #print( mssg )
    os.system( mssg )
if msgType == 2:
    print( '''
        Great! Now type your NameID
        NameID is a 10 Byte of two-HEX-character values separated by spaces
	!!! Insert your id into ' ' !!!
        e.g. "11 22 33 44 55 66 77 88 99 00"
    ''' )
    name = input()
    while len( name) != 29:
        print( "Error! You input bad nameID" )
        print( "Try again:" )
        name = input()
    
    print( '''
        OK! Now type your IstanceID
        NameID is a 6 Byte of two-HEX-character values separated by spaces
	!!! Insert your id into ' ' !!!
        e.g. "AA BB CC DD EE FF"
    ''' )
    istance = input()
    while len( istance) != 17:
        print( "Error! You input bad istanceID" )
        print( "Try again:" )
        istance = input()

    mssg = 'python iBeacon.py 2 \"' + name + "\" \"" + istance + "\""
    #print( mssg )
    os.system( mssg )
