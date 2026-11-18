import sys, json, time
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # the run copy inserted the scratchpad path instead
from adj_U3_lzz_predicate import test_d
lst = json.load(open(sys.argv[1]))
k = int(sys.argv[2])
out = []
for d, pl in lst[:k]:
    t0 = time.time()
    r = test_d(int(d))
    r["P_all_minus1"] = pl
    r["seconds"] = round(time.time() - t0, 1)
    print(r, flush=True)
    out.append(r)
json.dump(out, open(sys.argv[3], 'w'))
