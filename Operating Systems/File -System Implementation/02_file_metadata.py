import os
import time

filename = "sample.txt"

with open(filename, "w") as file:
    file.write("Operating System File System Practice")

info = os.stat(filename)

print("File Name:", filename)
print("File Size:", info.st_size, "bytes")

print("Last Modified:",
      time.ctime(info.st_mtime))