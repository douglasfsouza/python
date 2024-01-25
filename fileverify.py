import os
filename = os.environ.get('hello.py')
if filename:
    print("filename")
else:
    print("not filename")

if os.path.isfile(filename):
    print("isfile")
else:
    print("not isfile")

if filename and os.path.isfile(filename):
    print("existe hello.py")
else:
    print("not found")