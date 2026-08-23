import json, fast_O
rows = []
Us = [8600, 9000, 9400, 9800, 10200, 10600]
mu = fast_O.mobius_np((Us[-1]+1)**2 + 2*Us[-1] + 10)
for U in Us:
    X = U**3 + ((U+1)**3 - U**3)//2
    Uc, N = fast_O.UN_for(X)
    h = fast_O.build_h(Uc, N, mu)
    O, D = fast_O.band_O_D(Uc, N, h)
    del h
    rows.append({'U':Uc,'X':X,'N':N,'O':O,'D':D})
    print('U=%d X=%.4g O=%+.4f D=%.4f' % (Uc, X, O, D), flush=True)
    json.dump(rows, open('out_uscan12.json','w'))
