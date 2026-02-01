def tiny_hash(s: str) -> int:
    h = 0
    for i, ch in enumerate(s):
        h += ord(ch) * (i+1)
        
    return h % 256

r1 = tiny_hash("hello")
r2 = tiny_hash("hellx")
r3 = tiny_hash("hellp")
print(r1, "\t", r2, "\t", r3)
#############################

seen = {}

for i in range(32, 127):   # printable ASCII
    for j in range(32, 127):
        s = chr(i) + chr(j)
        h = tiny_hash(s)

        if h in seen and seen[h] != s:
            print("print collision found!")
            print(seen[h], "->", h)
            print(s, "->", h)
            print("Same hash is founded")
            #raise SystemExit
        
        seen[h] = s

target = 143

for i in range(32, 127):
    for j in range(32, 127):
        s = chr(i) + chr(j)
        if tiny_hash(s) == target:
            print("Found preimage:", s)
            break

########################

import secrets
import string

def random_string():
    return ''.join(secrets.choice(string.ascii_letters) for _ in range(5))

seen = set()

for i in range(1, 50):
    s = random_string()
    h = tiny_hash(s)

    if h in seen:
        print(f"Collission after {i} hashes")
        break

    seen.add(h)