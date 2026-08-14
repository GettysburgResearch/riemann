#!/usr/bin/env python3
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 100
mp.iv.dps = 80
P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
X, Y, PNEW = 871, 13, 67

D=[(1,1)]
for q in P:
    D += [(d*q,-mu) for d,mu in list(D)]
D=sorted((d,mu) for d,mu in D if d<=X)

def sc_sqrt(x): return mp.sqrt(mp.mpf(x))
def sc_log(x): return mp.log(mp.mpf(x))
def iv_sqrt_q(n,d=1): return mp.iv.sqrt(mp.iv.mpf(n)/d)
def iv_log_q(n,d=1): return mp.iv.log(mp.iv.mpf(n)/d)

Hs=[mp.mpf('0')]*(X+1); Ls=[mp.mpf('0')]*(X+1)
Hi=[mp.iv.mpf(0)]*(X+1); Li=[mp.iv.mpf(0)]*(X+1)
for n in range(1,X+1):
    Hs[n]=Hs[n-1]+1/sc_sqrt(n)
    Ls[n]=Ls[n-1]+sc_log(n)/sc_sqrt(n)
    Hi[n]=Hi[n-1]+1/iv_sqrt_q(n)
    Li[n]=Li[n-1]+iv_log_q(n)/iv_sqrt_q(n)

def q_scalar(num,den,row):
    if num < row*den: return mp.mpf('0')
    n=num//den; le=sc_log(mp.mpf(num)/den)
    def h(m): return mp.mpf('0') if m*den>num else sc_log(mp.mpf(num)/(den*m))/sc_sqrt(m)
    hr=h(row); hn=h(row+1); tail=mp.mpf('0')
    if n>=row+2: tail=le*(Hs[n]-Hs[row+1])-(Ls[n]-Ls[row+1])
    return ((row+1)/(row-1))*(hr-hn)+mp.mpf(2*(row+1))/(row*(row-1))*hn+mp.mpf(2)/(row*(row-1))*tail

def q_iv(num,den,row):
    if num < row*den: return mp.iv.mpf(0)
    n=num//den; le=iv_log_q(num,den)
    def h(m): return mp.iv.mpf(0) if m*den>num else iv_log_q(num,den*m)/iv_sqrt_q(m)
    hr=h(row); hn=h(row+1); tail=mp.iv.mpf(0)
    if n>=row+2: tail=le*(Hi[n]-Hi[row+1])-(Li[n]-Li[row+1])
    return (mp.iv.mpf(row+1)/(row-1))*(hr-hn)+mp.iv.mpf(2*(row+1))/(row*(row-1))*hn+mp.iv.mpf(2)/(row*(row-1))*tail

r_s=1/sc_sqrt(PNEW); r_i=1/iv_sqrt_q(PNEW)
sx_s=sc_sqrt(X); sy_s=sc_sqrt(Y); sx_i=iv_sqrt_q(X); sy_i=iv_sqrt_q(Y)
scalar=[]; intervals=[]
for d,mu in D:
    sd_s=sc_sqrt(d); sd_i=iv_sqrt_q(d)
    target_s=4*sx_s/d-3/sd_s; score_s=5*sx_s/d-3/sd_s
    target_i=4*sx_i/d-3/sd_i; score_i=5*sx_i/d-3/sd_i
    if d<=Y:
        target_s-=r_s*(4*sy_s/d-3/sd_s); score_s-=r_s*(5*sy_s/d-3/sd_s)
        target_i-=r_i*(4*sy_i/d-3/sd_i); score_i-=r_i*(5*sy_i/d-3/sd_i)
    rs=[]; ri=[]
    for j in range(2,67):
        vs=q_scalar(X,d,j)/sd_s; vi=q_iv(X,d,j)/sd_i
        if d<=Y:
            vs-=r_s*q_scalar(Y,d,j)/sd_s; vi-=r_i*q_iv(Y,d,j)/sd_i
        rs.append(vs); ri.append(vi)
    scalar.append((d,mu,target_s,score_s,rs)); intervals.append((d,mu,target_i,score_i,ri))

Es=[a for a in scalar if a[1]==1 and a[3]>0]
Os=[a for a in scalar if a[1]==-1 and a[3]>0]
Ei={a[0]:a for a in intervals if a[1]==1}; Oi={a[0]:a for a in intervals if a[1]==-1}

flow=[]; avail=[]; ei=0
for o in Os:
    while ei<len(Es) and Es[ei][0] <= o[0]+8:
        avail.append([Es[ei][0], mp.mpf(Es[ei][3])]); ei+=1
    rem=mp.mpf(o[3]); k=0
    while rem > mp.mpf('1e-90'):
        while k<len(avail) and avail[k][1] <= mp.mpf('1e-90'): k+=1
        if k==len(avail): raise AssertionError('Hall failure')
        e,cap=avail[k]
        if cap < rem:
            flow.append((o[0],e,'CAP')); rem-=cap; avail[k][1]=mp.mpf(0); k+=1
        else:
            flow.append((o[0],e,'DEM')); avail[k][1]-=rem; rem=mp.mpf(0)

cap={e[0]:mp.iv.mpf(Ei[e[0]][3]) for e in Es}
target_gain=mp.iv.mpf(0); row_gain=[mp.iv.mpf(0) for _ in range(65)]
flow_count=0; max_up=0; idx=0
for o in Os:
    rem=mp.iv.mpf(Oi[o[0]][3])
    while idx<len(flow) and flow[idx][0]==o[0]:
        oo,e,kind=flow[idx]; idx+=1
        if kind=='CAP':
            if not (cap[e].b < rem.a): raise AssertionError(f'ambiguous CAP {oo=} {e=}')
            take=cap[e]; rem=rem-take; cap[e]=mp.iv.mpf(0)
        else:
            if not (rem.b <= cap[e].a): raise AssertionError(f'ambiguous DEM {oo=} {e=}')
            take=rem; cap[e]=cap[e]-take; rem=mp.iv.mpf(0)
        ev=Ei[e]; ov=Oi[oo]
        target_gain += take*(ev[2]/ev[3]-ov[2]/ov[3])
        for k in range(65): row_gain[k] += take*(ev[4][k]/ev[3]-ov[4][k]/ov[3])
        flow_count+=1; max_up=max(max_up,e-oo)
    if not (rem.a <= 0 <= rem.b): raise AssertionError(f'unmatched odd demand {o[0]}')
if idx!=len(flow): raise AssertionError('unused flow decisions')

def low(v): return mp.mpf(v.a)
def high(v): return mp.mpf(v.b)
mins=min((low(v),j+2,high(v)) for j,v in enumerate(row_gain))
assert low(target_gain)>0 and mins[0]>0
print('PASS_JOINT_HOSTILE_LEAF_LEFT_GREEDY')
print('flow_count',flow_count)
print('max_upward',max_up)
print('target_gain_lower',mp.nstr(low(target_gain),50))
print('target_gain_upper',mp.nstr(high(target_gain),50))
print('min_row',mins[1])
print('min_row_gain_lower',mp.nstr(mins[0],50))
print('min_row_gain_upper',mp.nstr(mins[2],50))
