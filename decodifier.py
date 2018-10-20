# spacechem unlevelcodeifier
import base64
import json
import gzip

def decode(stri):
    debased = base64.b64decode(stri)
    decompressed = gzip.decompress(debased).decode('utf-8')
    return json.loads(decompressed)