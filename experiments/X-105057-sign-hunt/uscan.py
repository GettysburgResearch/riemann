import json, fast_O
rows = []
mu = fast_O.mobius_np(fast_O.UN_for((4700**3*2))[1] + 10)
for U in range(2700, 4701, 25):
    X = U**3 + ((U+1)**3 - U**3)//2   # mid-cell
    Uc, N = fast_O.UN_for(X)
    h = fast_O.build_h(Uc, N, mu)
    O, D = fast_O.band_O_D(Uc, N, h)
    rows.append({'U':Uc,'X':X,'N':N,'O':O,'D':D})
    print('U=%d O=%+.4f' % (Uc, O), flush=True)
json.dump(rows, open('out_uscan.json','w'))
