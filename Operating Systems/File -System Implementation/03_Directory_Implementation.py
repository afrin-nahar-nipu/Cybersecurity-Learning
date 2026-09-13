import os
import os

folders = [
    "Documents",
    "Images",
    "Projects"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(folder, "created")

files = os.listdir(".")

print("Directory Contents:")

for file in files:
    print(file)