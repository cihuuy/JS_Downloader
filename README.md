# JS_Downloader
JavaScript powershell based Download &amp; Execute + Obfuscator &amp; Encoder

=== PRIVATE ===

Usage of obfuscator.exe (can also use the invoke_obfuscator_script):

1) Through CMD cd to the directory where the EXE is.

2) type: obfuscator.exe url dropfilename

(for example: obfuscator.exe http://example.com/test.exe test.exe)

3) Code should get copied to clipboard


Usage of encoder.py:

1) Copy code from clipboard into encoder

2) Read output.txt file

3) Copy output.txt Code to clipboard

Usage of build_powershell.js:

1) Replace SHELLCODEHERE with the code you have in clipboard

2) Save :)


invoke_obfuscator_native: generates code from EXE (needs to be compiled)
invoke_obfuscator_script: generates code from the string given in code (requiers AutoIT)

=== PRIVATE ===
