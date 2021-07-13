import re
q = input()
w = input()

pattern = re.compile(w)
r = pattern.search(q)

if not r:
    print("(-1, -1)")
    
while r:
    print(f"({r.start()}, {r.end() - 1})")
    r = pattern.search(q, r.start() + 1)