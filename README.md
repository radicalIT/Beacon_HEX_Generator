# Beacon_HEX_Generator
        
###        To run script You must set up a few arguments:

        1. Type of message to generate, possible options are:
            0: UUID + Major + Minor
            1: URL
            2: NameID + IstanceID

        2. Arguments depends of first choice:
            For 0:
```python
                e.g. iBeacon.py 0 "63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5" 3000 4567
```
                - UID
                    16 Byte of two-HEX-character values
                    e.g. "63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5"
                - Major value
                    2 Byte value
                    e.g. 3000
                - Minor value
                    e.g. 4567
            For 1:
                e.g.    iBeacon.py 1 "facebook$me" 1 0
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
