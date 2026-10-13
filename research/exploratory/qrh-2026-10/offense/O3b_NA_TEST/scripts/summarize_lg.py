#!/usr/bin/env python3
"""O3b round 2: summarize the W_G (log-Gaussian row weight) runs results/kublg_Q*.json. EMPIRICAL, floating point."""
import json, math, glob, sys, os
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'results', 'kublg_Q*.json')), key=lambda p: int(p.split('_Q')[1].split('.')[0])):
    d = json.load(open(f)); nB = d['normB']
    print(f"Q={d['Q']} Z={d['Z']} CMAX={d['CMAX']} ({d['CMAX']/d['Z']:.1f} Z) #m={d['nM']}")
    for r in d['recs']:
        if r['Y'] < 10000: continue
        ex = r['gram'] - r['gram_diag']
        R = [r['T'][i] / (math.sqrt(ex) * nB[i]) for i in range(5)]
        snr = [r['T'][i] / r['RW'][i] for i in range(5)]
        fl = r['RW'][0] / (math.sqrt(ex) * nB[0])
        print(f"  Y={r['Y']:6d} R(theta,mu1,pm1,cph,mph)=" + ' '.join(f'{x:.4f}' for x in R) + f"  floor={fl:.4f}  SNR=" + ' '.join(f'{x:.2f}' for x in snr)
              + f"  | noxi SNR theta={r['T_noxi'][0]/r['RW_noxi'][0]:.2f} mu1={r['T_noxi'][1]/r['RW_noxi'][1]:.2f}")
