import os
images = {}
ilist = []
for root, dirs, files in os.walk("./Templates"):
    for filename in files:
        folder = root.split("/")
        name = filename.split('.')
        images[name[0]] = folder[2]
        # ilist.append(folder[2])

print(ilist)
