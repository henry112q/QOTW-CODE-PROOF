import os
code = 'print("hello world") \nfor x in range(0,10):\n  print(x)'

a = open(r"QOTW-ITTERATION-WITHOUT-LOOPS/testing.py",'w')
a.write(code)
a.close()

os.system(r"python.exe H:\QOTW-CODE-PROOF\QOTW-ITTERATION-WITHOUT-LOOPS\testing.py")

