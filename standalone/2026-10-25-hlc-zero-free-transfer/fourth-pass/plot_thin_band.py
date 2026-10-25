#!/usr/bin/env python3
"""Illustrate the proved uniform exponent margins; no zero data are plotted.

The acceptance certificates use rational arithmetic in the companion
checkers. Floating point is used here only to draw those formulas.
"""

from fractions import Fraction as F
from itertools import product
from pathlib import Path
import os
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) /
                                        'riemann-fourth-pass-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
matplotlib.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 10,
    'svg.fonttype': 'none', 'svg.hashsalt': 'riemann-fourth-pass-thin-band',
    'axes.spines.top': False, 'axes.spines.right': False,
})

corners = list(product([F(473,1024),F(487,1024)],
                       [F(49,100),F(1,2)],
                       [F(29,25),F(117,100)]))
alpha = F(1,250)
mesh = [F(7,10)+F(11,100)*j/660 for j in range(661)]
low, high = [], []
for m in mesh:
    low_gaps, high_gaps = [], []
    for delta, x, r in corners:
        g = delta*x
        baseline = (1+5*r)/6-delta*r
        c = r-m
        low_gaps.append(baseline-(1-2*delta*c-F(4,9)*g*(1-2*c)))
        high_gaps.append(min(baseline-(1-g-(delta-g)*(m-alpha)),
                             alpha*(F(5,6)-delta)))
    low.append(float(min(low_gaps)))
    high.append(float(min(high_gaps)))

x = np.array([float(m) for m in mesh])
low, high = np.array(low), np.array(high)
best = np.maximum(low,high)

fig, ax = plt.subplots(figsize=(10.7,5.8), constrained_layout=False)
fig.subplots_adjust(left=.10, right=.97, bottom=.25, top=.77)
fig.suptitle('The remaining original-product band', x=.10, y=.965,
             ha='left', fontsize=19, fontweight='bold')
fig.text(.10,.885,
         'Uniform bounds on the critical parameter box, with the separate cutoff α = 0.004.\n'
         'These are source-qualified exponent estimates, not computed zeta zeros.',
         fontsize=10.5, color='#404b59', linespacing=1.45,va='top')

ax.axvspan(.735,.773,color='#fff0cf',alpha=1,zorder=0)
ax.axhline(.001,color='#a3342b',lw=1.6,ls=(0,(5,3)),label='Required count saving: 0.001')
ax.axhline(0,color='#b6bec7',lw=.8)
ax.plot(x,low,color='#276d9b',lw=1.25,alpha=.65,label='Ordinary fourth-moment margin')
ax.plot(x,high,color='#25806b',lw=1.25,alpha=.65,label='Marked inverse-moment margin')
ax.plot(x,best,color='#172d42',lw=2.6,label='Better of these two uniform bounds')
ax.axvline(.735,color='#b49142',lw=1,ls=':')
ax.axvline(.773,color='#b49142',lw=1,ls=':')
ax.text(.754,.0138,'Unresolved signed band',ha='center',fontsize=10,
        color='#79581c',fontweight='bold')
ax.text(.754,.0109,'0.735 < logᵤ Nm < 0.773',ha='center',fontsize=10,
        color='#79581c')
ax.scatter([.735,.773],[23/16000,371959/307200000],s=35,
           color=['#276d9b','#25806b'],zorder=5)
ax.annotate('0.0014375',(.735,23/16000),xytext=(-58,22),
            textcoords='offset points',fontsize=9,color='#276d9b',
            arrowprops={'arrowstyle':'-','color':'#276d9b','lw':.8})
ax.annotate('0.001210804…',(.773,371959/307200000),xytext=(17,28),
            textcoords='offset points',fontsize=9,color='#25806b',
            arrowprops={'arrowstyle':'-','color':'#25806b','lw':.8})
ax.set_xlim(.70,.81)
ax.set_ylim(-.011,.020)
ax.set_xlabel('Cutoff exponent for the returned product, logᵤ Nm',labelpad=10)
ax.set_ylabel('Saving below the old witness-count exponent',labelpad=9)
ax.grid(axis='y',color='#e4e8ed',lw=.7)
ax.legend(loc='lower left',bbox_to_anchor=(0,-.36),frameon=False,ncol=2,
          handlelength=2.8,columnspacing=2.0,fontsize=9)
fig.text(.10,.025,
         'The full smooth band is U⁰·⁷³⁵ < Nm < 2U⁰·⁷⁷³; fixed factors disappear at exponent scale.\n'
         'The high component also uses its longer-inverse endpoint, whose proved margin is 1099/768000.',
         color='#586373',fontsize=9,linespacing=1.45)
fig.savefig(HERE/'THIN_BAND.svg',metadata={'Date':None})
fig.savefig(HERE/'THIN_BAND.png',dpi=160,metadata={'Software':'matplotlib'})
plt.close(fig)
print('Wrote THIN_BAND.svg and THIN_BAND.png; analytic status unchanged.')
