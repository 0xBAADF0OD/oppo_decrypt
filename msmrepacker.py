#!/usr/bin/env python3
# OnePlus MSM repacker by craznazn@xda
# Based on work by B.Kerler
# Licensed under MIT License
"""


Usage:
    msmrepacker.py <source_ops> <target_ops>
"""

import opscrypto as ops

def extract_source_xml():
    path = sys.argv[1]
    try:
        mbox = mbox4
        xml = extractxml(filename, key)
    except:
        try:
            mbox = mbox5
            xml = extractxml(filename, key)
        except:
             print("Unsupported key !")
             exit(0)


#Extract source settings.xml
#Extract target settings.xml
#Modify target settings as needed

#Locate target xml offset, eg 0x1693d2000
#dd xml offset to eof, call it xml+footer.enc
#   dd if=target.ops of=xmlfooter.enc bs=$((0x1693d2000)) skip=1

#Save the ops footer
#wc -c xmlfooter.enc.dec, footer is at offset of output-0x200
#dd if=xmlfooter.enc bs=$((97280-512)) of=opsfooter skip=1

#decrypt with python3 opscrypto.py encryptfile xmlfooter.enc.dec
#check if xml

#save new setting
#python3 opscrypto.py encryptfile mod-settings.xml
#dd if=mod-settings.xml.enc of=mod-settings.xml.enc.padded bs=$((97280-512)) conv=sync

#add footer
#cat opsfooter >> mod-settings.xml.enc.padded
#modify file at opsfooter offset to correct filesize

#truncate target ops and finish
#truncate -s $((0x1693d2000)) billie8_14_E.01_210128.ops
#cat mod-settings.xml.enc.padded >> billie8_14_E.01_210128.ops