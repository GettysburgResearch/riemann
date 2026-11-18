#!/usr/bin/env python3
"""Illustrate proved RH-conditional fixed-band moment formulas, not zero data."""
import json
import hashlib
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

R=Path(__file__).resolve().parents[2]
OUT=R/'experiments/results'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.titlesize':11,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'svg.hashsalt':'riemann-observatory-round11-band-moments'})
b=np.linspace(.002,1/6-1e-5,300);a=b/2
d1=b-a;d2=b*b-a*a;d3=b**3-a**3
mean=np.log(2)-4*d1+2*d3/3
vc=.5*np.log(2)-4*d1*d1+4*d1*d3-4*d3*d3/9
vs=.5*np.log(2)-1.5*d2*d2
k3=-8*d1**3+24*d1*d1*d3-8*d1*d3*d3+16*d3**3/27
fig,axes=plt.subplots(1,3,figsize=(10.4,3.7),layout='constrained')
red='#a43a36';blue='#235d86';gray='#53616a'
axes[0].plot(b,mean,color=red,label='Cosine band')
axes[0].axhline(np.log(2),ls='--',color=gray,label='Independent phases')
axes[0].set(title='Limiting mean',ylabel='Mean')
axes[1].plot(b,vc,color=red,label='Cosine band')
axes[1].plot(b,vs,color=blue,label='Sine band')
axes[1].axhline(.5*np.log(2),ls='--',color=gray,label='Independent phases')
axes[1].set(title='Limiting variance',ylabel='Variance')
axes[2].plot(b,k3/vc**1.5,color=red,label='Cosine band')
axes[2].axhline(0,ls='--',color=gray,label='Any Gaussian')
axes[2].set(title='Nonzero third moment',ylabel='Third centered moment / variance$^{3/2}$')
for ax in axes:
 ax.set_xlabel('Upper exponent $b$');ax.grid(alpha=.18);ax.legend(frameon=False,fontsize=7.5,loc='best')
 ax.set_xlim(0,1/6);ax.tick_params(labelsize=8)
fig.suptitle('Fixed power bands: moments under RH',fontsize=14,fontweight='bold')
fig.supxlabel(r'Band $Y^{b/2}<p\leq Y^b$, with $0<b<1/6$. First take $Y\to\infty$ at each fixed $b$.',fontsize=9)
for suffix in ('png','svg','pdf'):
 fig.savefig(OUT/f'prime_band_round11.{suffix}',dpi=180,metadata={'Creator':'Riemann Observatory'})
plt.close(fig)
(OUT/'prime_band_round11_figure.json').write_text(json.dumps({
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Illustration of exact proved RH-conditional asymptotic formulas. Floating point rendering, no finite-Y zero data or numerical certificate.',
 'source':'audits/adversarial_reviews/director_polynomial_bands_round11.md',
 'band':'a=b/2, 0<b<1/6',
 'witness':{'a':'1/20','b':'1/10','exact_third_cumulant':'-818904257/864000000000'},
 'rows':[dict(b=float(x),mean=float(m),cosine_variance=float(v),sine_variance=float(s),third_cumulant=float(c)) for x,m,v,s,c in zip(b,mean,vc,vs,k3)]},indent=2)+'\n')
print('Rendered prime_band_round11 PNG/SVG/PDF and formula data.')
