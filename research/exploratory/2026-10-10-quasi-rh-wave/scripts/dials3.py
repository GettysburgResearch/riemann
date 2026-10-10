exec(open('dials2.py').read().split('print("paper check')[0])
import numpy as np
print("baseline:", bestB())
for c in [0.25, 0.3, 0.4, 0.5, 1.0]:
    print(f"c={c:.2f} (plain capacity zP=c(1-2m)):", bestB(c=c))
for s in [0.6, 0.75, 1.0]:
    print(f"sM={s:.2f} (inverse capacity zM=sM(1-r)):", bestB(sM=s))
for a,c,s in [(0.6,0.5,1.0),(0.7,1.0,1.0)]:
    print(f"combo alpha={a},c={c},sM={s}:", bestB(alpha=a,c=c,sM=s))
for fs in [0.1, 0.25, 0.5, 0.75]:
    print(f"floor_save={fs} ideal counts  :", bestB(ideal=True, floor_save=fs))
for fs in [0.1, 0.25, 0.5]:
    print(f"floor_save={fs} baseline counts:", bestB(floor_save=fs))
# ideal counts + floor_save needed to reach 3/4: ell=2/3 requires C0 - fs*h <= 0 with b->0: -1/4+5/6 - fs*(1+2)/2 <= 0 -> fs >= (7/12)/(3/2) = 7/18
print("floor_save needed for ell=2/3 (b=0):", (-1/4 + 5*(2/3)/4)/((1+3*(2/3))/2))
