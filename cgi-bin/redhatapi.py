#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi 

print('''<style>
pre{
color: black;
font-weight:bold;
font-size:20px
}
</style>
''')

db = cgi.FieldStorage()

cmd =db.getvalue("cmd")
output=sp.getstatusoutput("sudo {}" .format(cmd))
output= output 

print("<body style='padding :40px;'>")
print('<h1 style ="color:#df405a;">Output</h1>')
print("<pre>{}</pre>".format(output))
print("</body>")
