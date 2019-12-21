#!/bin/bash python3.7
ssh -p 222 localhost /home/s/studio3f/.local/bin/python3 /home/s/studio3f/test2.studiovector.art/sitecelitel/1C_utils/from1CsaveJSON.py
ssh -p 222 localhost /home/s/studio3f/.local/bin/python3 /home/s/studio3f/test2.studiovector.art/sitecelitel/manage.py organ
ssh -p 222 localhost /home/s/studio3f/.local/bin/python3 /home/s/studio3f/test2.studiovector.art/sitecelitel/manage.py del_price
ssh -p 222 localhost /home/s/studio3f/.local/bin/python3 /home/s/studio3f/test2.studiovector.art/sitecelitel/manage.py service