import sys
import os
'''
To generate your HEX data:
I.   Set msgType value:

     0: UUID + Major + Minor
     1: URL
     2: NameID + IstanceID

II.  Set "local vars" inside your choice's if

III. Read data from console output

'''
if len( sys.argv ) == 1:
    sys.argv.append( '--help' )

if sys.argv[1] == '--help':
    print( '''
        Help info 
        
        To run script You must set up a few arguments:

        1. Type of message to generate, possible options are:
            0: UUID + Major + Minor
            1: URL
            2: NameID + IstanceID

        2. Arguments depends of first choice:
            For 0:
                e.g. iBeacon.py 0 "63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5" 3000 4567

                - UID
                    16 Byte of two-HEX-character values
                    e.g. "63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5"
                - Major value
                    2 Byte value
                    e.g. 3000
                - Minor value
                    e.g. 4567
            For 1:
                e.g.    iBeacon.py 1 'facebook$me' 1 0
                mean    https//www.facebook.com/me

                - Url
                    Url address to display
                    Max. 16 chars ( $ count as 1 char )
                    Use $ to insert sufix
                    e.g. 'facebook$me' with suffix 0 mean facebook.com/me
                - Url prefix
                    One of options:
                        0:  http://www.
                        1:  https://www.
                        2:  http://
                        3:  https://
                    e.g. 3
                - Url suffix
                    One of options:
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
                    Is used in Url as $
                    e.g. 0
            For 2:
                e.g. iBeacon.py 2 "11 22 33 44 55 66 77 88 99 00" "AA BB CC DD EE FF"

                nameID
                    10 Byte of two-HEX-character values
                    e.g. "11 22 33 44 55 66 77 88 99 00"
                istanceID
                    6 Byte of two-HEX-character values
                    e.g. "AA BB CC DD EE FF"
    '''
    )
    exit()
else:
    msgType = int(sys.argv[1])

def toHEX( byte ):
    return format( byte, '02X') + " "

#msgType = 2


uuid = ""
prefix = ""
data = ""

if msgType == 0:
    #local vars
    
    uid = sys.argv[2]
    major = int( sys.argv[3] )
    minor = int( sys.argv[4] )
    
    
    #global vars
    dataLong = 16
    header = '1A FF'
    corpID = '4C 00'
    preEnd = '02 15'
    txPow = 'C8'
    
    #data initiation
    data += uid + " "
    
    major = format( major, '04X')
    minor = format( minor, '04X')

    data += major[ :2 ] + " "
    data += major[ 2: ] + " "

    data += minor[ :2 ] + " "
    data += minor[ 2: ] + " "

    data += txPow

elif msgType == 1:
    '''
    HTTP Prefix
    0	0x00	http://www.
    1	0x01	https://www.
    2	0x02	http://
    3	0x03	https://

    HTTP Sufix
    0	0x00	.com/
    1	0x01	.org/
    2	0x02	.edu/
    3	0x03	.net/
    4	0x04	.info/
    5	0x05	.biz/
    6	0x06	.gov/
    7	0x07	.com
    8	0x08	.org
    9	0x09	.edu
    10	0x0a	.net
    11	0x0b	.info
    12	0x0c	.biz
    13	0x0d	.gov
    '''
    #local vars
    
    url = sys.argv[2]
    prefUrl = int( sys.argv[3] )
    sufUrl = int( sys.argv[4] )
    

    #added vars
    eddyType = '10'
    
    #global vars
    dataLong = len(url)
    header = '03 03'
    corpID = 'AA FF'
    preEnd = toHEX( 6 + dataLong ) + '16'
    txPow = '00'

    #data initiation
    if dataLong > 16:
        print("Error! Too long url :(")
        exit()

    data += 'AA' + " "
    data += 'FE' + " "

    data += eddyType + " "

    data += txPow + " "

    data += toHEX( prefUrl )

    for let in url:
        if let == '$':
            data += toHEX( sufUrl )
        else:
            data += toHEX( ord( let ) )

    for i in range( 16 - dataLong ):
        data += toHEX( 0 )

elif msgType == 2:
    #local vars

    nameID = sys.argv[2]
    istanceID = sys.argv[3]

    #added vars
    eddyType = '00'

    #global vars
    dataLong = 16
    header = '03 03'
    corpID = 'AA FF'
    preEnd = toHEX( 6 + dataLong ) + '16'
    txPow = '00'
    
    #data initiation
    data += 'AA' + " "
    data += 'FE' + " "

    data += eddyType + " "

    data += toHEX( 0 )

    data += nameID + " "
    data += istanceID + " "

    data += txPow
else:
    print( "Error! Bad Argument!" )
    exit()

#prefix

prefix += toHEX( 14 + dataLong )

#const discoverable
prefix += toHEX( 2 )
prefix += toHEX( 1 )
prefix += toHEX( 6 )

prefix += header + " "

prefix += corpID + " "

prefix += preEnd + " "
#end prefix

print( "hcitool -i hci0 cmd 0x08 0x0008 " + prefix + data )

cmmd = "hcitool -i hci0 cmd 0x08 0x0008 "
cmmd += prefix
cmmd += data

os.system( cmmd )
os.system( 'hciconfig hci0 leadv 3' )
