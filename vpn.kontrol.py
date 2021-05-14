#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN KONTROL")
print("Vpn Kontrol Aracına Hoşgeldiniz   instagram = zumrudu_anka_team")
print("Bu Araç Treangle Tarafından Oluşturulmuştur      ")
hedefip = input("Hedef ip girin : ")
os.system("ike-scan " + hedefip)


