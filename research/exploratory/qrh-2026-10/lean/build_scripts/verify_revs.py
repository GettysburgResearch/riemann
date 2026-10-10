import json, subprocess, sys, os
P = sys.argv[1]
m = json.load(open(os.path.join(P, 'lake-manifest.json')))
bad = 0
for p in m['packages']:
    name = p['name']
    d = os.path.join(P, '.lake', 'packages', name.strip('«»'))
    if not os.path.isdir(d):
        print('MISSING', name); bad += 1; continue
    head = subprocess.run(['git', '-C', d, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(['git', '-C', d, 'status', '--porcelain', '--untracked-files=no'], capture_output=True, text=True).stdout.strip()
    ok = head == p['rev']
    bad += (not ok)
    print(('OK   ' if ok else 'BAD  ') + f"{name:32s} {head} {'(locally patched: %d files)' % len(dirty.splitlines()) if dirty else ''}")
print('mismatches:', bad)
