import zlib
import re
with open("main.pdf", "rb") as f:
    data = f.read()
streams = re.findall(b'stream\n(.*?)endstream', data, re.S)
found = False
for s in streams:
    try:
        decoded = zlib.decompress(s)
        if b"Rafailov" in decoded or b"Direct" in decoded:
            found = True
            print("FOUND IN STREAM!")
            break
    except:
        pass
if not found:
    print("NOT FOUND IN PDF!")
