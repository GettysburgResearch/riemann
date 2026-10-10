import os, re, sys, json
root = sys.argv[1]; start = sys.argv[2:]
imp_re = re.compile(r'^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([\w.«»\-]+)', re.M)
seen = {}; ext = {}
stack = list(start)
while stack:
    m = stack.pop()
    if m in seen: continue
    path = os.path.join(root, *m.split('.')) + '.lean'
    if not os.path.exists(path):
        top = m.split('.')[0]
        ext[top] = ext.get(top, set()); ext[top].add(m)
        seen[m] = None
        continue
    src = open(path, encoding='utf-8').read()
    # strip block comments crudely
    src2 = re.sub(r'/-.*?-/', '', src, flags=re.S)
    head = src2.split('\n')
    imps = []
    for line in head:
        s = line.strip()
        if not s or s.startswith('--'): continue
        mm = re.match(r'^(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?(\S+)', s)
        if mm: imps.append(mm.group(1)); continue
        if s.startswith('module') or s.startswith('prelude'): continue
        break
    seen[m] = (path, src.count('\n'))
    stack.extend(imps)
local = {k:v for k,v in seen.items() if v}
print("local modules:", len(local), "lines:", sum(v[1] for v in local.values()))
for k,v in sorted(ext.items()):
    print("external", k, len(v), sorted(v)[:5] if k!='Mathlib' else '')
json.dump(sorted(local), open(sys.argv[0]+'.out.json','w'))
