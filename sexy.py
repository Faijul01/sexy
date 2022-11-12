
#-------------------Dont Edit This Script-----------------#
import os,platform,time

bitt=platform.architecture()[0]

if bitt=="32bit":
    print('[!] Your Device is 32 bit');time.sleep(1);print('\n\n[!] Your Python Version :');time.sleep(1);os.system('python --version')
    time.sleep(2)
    import bcz32.Faijul


elif bitt=="64bit":
    os.system('clear');print('[!] Your Device is 64 bit');time.sleep(1);print('\n\n[!] Your Python Version :');time.sleep(1);os.system('python --version')
    time.sleep(2)
    import bcz64.Faijul

else:
    print('\nUNKNOWN DEVICE')

#---------------------------------------------------------#
#                    THIS TOOL OWNED BY
#                  • FAIJUL ISLAM
#---------------------------------------------------------#