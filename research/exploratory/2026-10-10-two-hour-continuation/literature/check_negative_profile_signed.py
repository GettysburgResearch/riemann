"""Exact directed reweighting of a complete imported source trace census."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import argparse,hashlib,json,re


def need(ok,why):
    if not ok: raise ArithmeticError(why)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scalar_bounds(s):
    m=re.fullmatch(r'\[([0-9.e+\-]+) \+/- ([0-9.e+\-]+)\]',s)
    need(m is not None,'exact midpoint/radius ball')
    a,b=map(F,m.groups());need(b>=0,'nonnegative radius')
    return a-b,a+b


def complex_bounds(s):
    m=re.fullmatch(r'(\[[^\]]+\]) \+ (\[[^\]]+\])j',s)
    need(m is not None,'complete printed complex ball')
    return scalar_bounds(m[1]),scalar_bounds(m[2])


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();here=Path(__file__).resolve();base=here.parent
    guards={
        'FULL_SIGNED_COMPACT_WITNESS.md':'1c0a1718080e6f763a3531f9f9a8f8fcd31868c48d241290406fe4cef61644ca',
        'check_full_signed_compact.py':'ace0ec9a10deef974d3cae842590bc46c2d048e65dfa5b14b659cbc7c380dc50',
        'check_fourier_compact_trace.py':'dddf8f7c12fe022e54e19d9994da6092fd7a3a7e9da1d1d67b6daf6f5c27c598',
        'FOURIER_COMPACT_BALANCED_TRACE.md':'480cb96c363ddddf5d35306b0b25739c110b6f407e8101a43aaddae04605f120',
        'FULL_SIGNED_COMPACT_WITNESS_INDEPENDENT_REVIEW.md':'5084650971b3af4d5dbb30ed169ecc5f30a4ce463f064edb6bcca3d5ce13d008',
        'independent-full-signed-compact-normal.json':'46e642fa1c4774f1d31166de547731762fa7f89ac3f0a3ce6b0c500f91571d93',
        'independent-full-signed-compact-optimized.json':'46e642fa1c4774f1d31166de547731762fa7f89ac3f0a3ce6b0c500f91571d93',
        'independent-fourier-compact-trace-normal.json':'fa2e817911ebaee9411f3b617149fa55ad98e9b7abc6e604dd6b3a1d6cc6aae8'}
    for name,h in guards.items():need(digest(base/name)==h,'frozen source trace binding '+name)
    source=Path('/workspace/.riemann-research/moment-sources/914/standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md')
    source_sha='c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983'
    need(digest(source)==source_sha,'literal critical-sector source')
    receipt=json.loads((base/'independent-full-signed-compact-normal.json').read_text())
    lead_receipt=json.loads((base/'independent-fourier-compact-trace-normal.json').read_text())
    need(receipt['D']==30 and receipt['H']==40,'physical common scales')
    records={}
    for r in receipt['records']:
        key=tuple(r['exponents']),tuple(r['principal_mask'])
        need(key not in records,'unique complete character/mask record')
        records[key]=r
    need(len(records)==178,'all imported neutral character groups')
    q=(7,7,13,13,19,19,31,31);selected=(0,1,4,5)
    charges=tuple((a-1)//6 for a in q)

    def classification(t):
        l=Counter(t[:2]);r=Counter(t[2:]);g1=g2=1
        for i in range(8):
            if l[i]+r[i]==1:g1*=q[i]
            if l[i]+r[i]==2 and (l[i]-r[i])%6:g2*=q[i]
        es=tuple((l[i]-r[i])%6 for i in range(8))
        mask=tuple(i for i in range(8) if l[i]+r[i] and es[i]==0)
        return g1!=1 and g1*g1*g2>1600,(es,mask)

    old=Counter();critical=Counter();leading=Counter()
    for t in product(range(8),repeat=4):
        yes,key=classification(t)
        if yes:old[key]+=1
    need(sum(old.values())==3696 and len(old)==1092,'complete original critical classifier')
    for key,m in old.items():
        neutral=sum(e*c for e,c in zip(key[0],charges))%6==0
        need((key in records)==neutral,'complete exact unit-orbit killed/neutral partition')
        if neutral:need(records[key]['multiplicity']==m,'imported record exact original multiplicity')
    for t in product(selected,repeat=4):
        yes,key=classification(t)
        if yes:
            critical[key]+=1
            if len(set(t))==4:leading[key]+=1
    need(sum(critical.values())==168 and len(critical)==54,'complete four-column critical census')
    need(sum(leading.values())==24,'all four-distinct ordered leading tuples')
    need(sum(k in records for k in critical)==12,'new complete neutral group census')
    need(sum(m for k,m in critical.items() if k in records)==48,'new complete neutral tuple census')

    def aggregate(counts):
        lo=hi=ilo=ihi=F(0)
        for key,m in counts.items():
            if key not in records:continue
            (a,b),(c,d)=complex_bounds(records[key]['row_trace_ball'])
            lo+=m*a;hi+=m*b;ilo+=m*c;ihi+=m*d
        need(ilo<=0<=ihi,'complete aggregate imaginary interval contains zero')
        return lo,hi
    full=aggregate(critical);lead=aggregate(leading)
    # Reweighting only removes tuples and all remaining weights equal one,
    # so the complete old tuplewise perturbation budgets still apply.
    need(F(2645,1000)**2<7,'exact sqrt7 lower bound')
    error=F(3696*2*40*34693*90*1000,2645*10**12)
    lead_error=scalar_bounds(lead_receipt['smooth_error_bound'])[1]
    need(error<F(7,20),'complete source Schwartz error below .35')
    need(full[1]+error<F(-947,2),'actual source full critical R2 below -473.5')
    need(lead_error<F(1,1000) and lead[1]+lead_error<-3,'actual source leading face below -3')

    # Independent exact auxiliary spatial control, not a Fourier-compact
    # source recomputation. All actual prime ideals and nonunit masks kept.
    def norm(z):return z[0]*z[0]-z[0]*z[1]+z[1]*z[1]
    fields=[]
    for a in (7,19):
        for root in (r for r in range(a) if (r*r+r+1)%a==0):
            gen=next(g for g in range(2,a) if len({pow(g,j,a) for j in range(a-1)})==a-1)
            logs={pow(gen,j,a):j for j in range(a-1)}
            c=logs[(1+root)%a]//((a-1)//6)
            need(logs[(1+root)%a]%((a-1)//6)==0,'native sixth-root embedding')
            inv=pow(c,-1,6);fields.append((a,root,{x:logs[x]*inv%6 for x in range(1,a)}))
    need(len(fields)==4,'four distinct actual prime ideals')
    bound=isqrt(160//3)
    rows=[(a,b) for a,b in product(range(-bound,bound+1),repeat=2) if 0<norm((a,b))<=40]
    need(len(rows)==150,'complete auxiliary row disk')
    units=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
    symbols=[[None if (a+b*root)%p==0 else table[(a+b*root)%p] for p,root,table in fields] for a,b in rows]
    disk=[0,0];disk_lead=[0,0];moment=0
    for row in symbols:
        a=b=0
        for e in row:
            if e is not None:
                x,y=units[e];a+=x;b+=y
        moment+=norm((a,b))**2
    for t in product(range(4),repeat=4):
        yes,_=classification(tuple(selected[i] for i in t))
        if not yes:continue
        trace=[0,0]
        for row in symbols:
            if any(row[i] is None for i in t):continue
            e=(row[t[0]]+row[t[1]]-row[t[2]]-row[t[3]])%6
            a,b=units[e];trace[0]+=a;trace[1]+=b
        for i in range(2):
            disk[i]+=trace[i]
            if len(set(t))==4:disk_lead[i]+=trace[i]
    need(disk[1]==0 and disk_lead[1]==0 and moment>=0,'exact real auxiliary complete forms')
    record=dict(status='PASS_EXACT_SOURCE_REALIZABLE_NEGATIVE_PROFILE_SIGNED_WITNESS',
        D=30,H=40,source_norm_profile_samples={'7':1,'13':0,'19':1,'31':0},
        nonnegative_smooth_source_profile=True,source_prime_columns=4,all_ordered_tuples=256,
        critical_tuples=168,critical_groups=54,neutral_groups=12,neutral_critical_tuples=48,
        leading_tuples=24,full_compact_R2_lower_exact=str(full[0]),full_compact_R2_upper_exact=str(full[1]),
        full_compact_R2_approx=str(float(sum(full)/2)),leading_compact_R2_lower_exact=str(lead[0]),
        leading_compact_R2_upper_exact=str(lead[1]),leading_compact_R2_approx=str(float(sum(lead)/2)),
        complete_full_Schwartz_error_rational_upper_bound=str(error),
        actual_Schwartz_full_R2_strict_upper_bound='-473.5',actual_Schwartz_leading_R2_strict_upper_bound='-3',
        auxiliary_spatial_rows=150,auxiliary_spatial_full_critical_R2=disk,
        auxiliary_spatial_leading_R2=disk_lead,auxiliary_spatial_full_fourth_moment=moment,
        imported_source_sha256=guards,literal_sector_source_sha256=source_sha,
        proof_sha256=digest(base/'NEGATIVE_PROFILE_SIGNED_WITNESS.md'),checker_sha256=digest(here),
        new_native_row_integration_performed=False,imported_complete_directed_row_traces=True,
        full_moment_negative=False,asymptotic_cancellation_proved=False,rh_proved=False)
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n');print(record['status'])


if __name__=='__main__':main()
