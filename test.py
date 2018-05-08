import os
images = {}
for root, dirs, files in os.walk("./Templates"):
    for filename in files:
        folder = root.split("\\")
        name = filename.split('.')
        images[name[0]] = folder[1]

print(images)
