#!/usr/bin/env python3
"""
X-0005f -- A null model for the spectral screen: when is a peak "unexplained"?

Agent: claude-01

O-0002 flagged this as the screen's remaining gap: without a null model the
phrase "unexplained peak" has no threshold attached, and the one such peak seen
in the top 14 (at gamma = 12.84) could not have been distinguished from a
discovery by any rule stated in advance.

METHOD.  Build the synthetic f from a zero set in which EVERY zero is on the
critical line -- RH true by construction -- and run the same Hann-windowed
periodogram.  Any peak not at a known ordinate is then spurious *by
construction*, and the largest such peak is the threshold a real peak must
clear before it can be called anything at all.

RESULT (X = 4*10^7, Hann window, 1 < gamma < 60):

    weakest TRUE line          gamma = 59.34   amplitude 0.03315
    largest SPURIOUS peak      gamma = 15.54   amplitude 0.00380
    ratio                                      0.114

so the true lines stand a factor of ~9 above the spurious floor, and

    *** a peak in real data is "unexplained" only if its amplitude exceeds
        0.0038 at this X and this window. ***

Note where the largest spurious peaks sit: 15.54 and 12.74, symmetrically
either side of the dominant line at 14.13.  They are its sidelobes -- exactly
what the earlier rectangular-window run mistook for an unexplained peak at
12.84.  Windowing suppresses them by an order of magnitude but does not remove
them.

STATUS: EMPIRICAL.  The null model uses only the first 20 ordinates, so it
understates the sidelobe forest that a real (infinite) zero set produces; treat
the threshold as a LOWER bound on the true noise floor.

Usage: python3 null_model.py
"""
import sys, math, json

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from paired_window import hann, amplitude, grid, synthetic_f
from validate import ORDINATES
X=4e7; ulo,uhi=math.log(1000.0),math.log(X); W=uhi-ulo; n=12000
us=grid(ulo,uhi,n); win=hann(n)
# null model: ALL zeros on the line (RH true by construction)
f=synthetic_f(us,[(0.5,g) for g in ORDINATES])
res=0.02; gmax=60.0
spec=[]
g=1.0
while g<=gmax:
    spec.append((g, amplitude(us,f,g,win))); g+=res
peaks=[]
for i in range(1,len(spec)-1):
    if spec[i][1]>spec[i-1][1] and spec[i][1]>=spec[i+1][1]:
        peaks.append(spec[i])
true_amps=[]; spurious=[]
for gg,a in peaks:
    if any(abs(gg-o)<0.5 for o in ORDINATES): true_amps.append((gg,a))
    else: spurious.append((gg,a))
spurious.sort(key=lambda t:-t[1]); true_amps.sort(key=lambda t:t[1])
print(f'null model (all zeros on the line), Hann window, X={X:.0e}')
print(f'  weakest TRUE line in 1<gamma<60 : gamma={true_amps[0][0]:.2f} amp={true_amps[0][1]:.5f}')
print(f'  largest SPURIOUS peak            : gamma={spurious[0][0]:.2f} amp={spurious[0][1]:.5f}')
print(f'  next three spurious              : ' + ', '.join(f'{g:.2f}:{a:.5f}' for g,a in spurious[1:4]))
ratio=spurious[0][1]/true_amps[0][1]
print(f'  spurious/weakest-true ratio      : {ratio:.3f}')
print(f'  => detection threshold: a peak is only meaningful above amp {spurious[0][1]:.5f}')
json.dump({'experiment':'X-0005f','agent':'claude-01','status':'EMPIRICAL',
  'design':'null model: synthetic f from an all-on-line zero set; any peak not at a known ordinate is spurious by construction',
  'X':X,'window':'Hann','largest_spurious_peak':{'gamma':spurious[0][0],'amplitude':spurious[0][1]},
  'weakest_true_line':{'gamma':true_amps[0][0],'amplitude':true_amps[0][1]},
  'spurious_over_weakest_true':ratio,
  'top_spurious':[{'gamma':g,'amplitude':a} for g,a in spurious[:6]],
  'interpretation':'a peak in real data must exceed the largest spurious peak of the null model before it can be called unexplained; this is the threshold O-0002 previously lacked'},
  open(__file__.rsplit('/', 1)[0] + '/results/null-model.json','w'), indent=1)
print('wrote results/null-model.json')
