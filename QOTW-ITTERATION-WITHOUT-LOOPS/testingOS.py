import os
code = 'import os \ncode = "for x in range(0,10): print(x)"\na=open("H:/QOTW-CODE-PROOF/QOTW-ITTERATION-WITHOUT-LOOPS/test1.py","w") \na.write(code) \na.close()\nos.system("python.exe H:QOTW-CODE-PROOF/QOTW-ITTERATION-WITHOUT-LOOPS/test1.py")'

a = open(r"H:\QOTW-CODE-PROOF\QOTW-ITTERATION-WITHOUT-LOOPS\testing.py",'w')
a.write(code)
a.close()
for x in range(4):
    os.system(r"python.exe H:\QOTW-CODE-PROOF\QOTW-ITTERATION-WITHOUT-LOOPS\testing.py")