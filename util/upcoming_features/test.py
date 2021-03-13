import os.path, time

print("Last modified: %s" % time.ctime(os.path.getmtime("./empty.txt")))
print("Created: %s" % time.ctime(os.path.getctime("./empty.txt")))