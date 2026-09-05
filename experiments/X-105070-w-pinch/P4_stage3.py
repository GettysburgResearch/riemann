import numpy as np, math, json, sys
# Stage 3: robustness of beta fits (widths, cmin, jackknife), per-window ratio & phase lock.
D=json.load(open('stage1_big.json'))
rows=np.array(D['rows'])
u=rows[:,0]; W=rows[:,2]; V=rows[:,3]; msamp=rows[:,4]
L=np.log(u); dL=np.gradient(L)
g1=14.134725141734695
ph=np.exp(-1j*g1*L)
def proj(A,width,step=0.25):
    cs=[];amps=[];phs=[]
    c=L[0]+width/2
    while c+width/2<=L[-1]+1e-9:
        w=(L>=c-width/2)&(L<c+width/2)
        if w.sum()>10:
            a=np.sum(A[w]*ph[w]*dL[w])/np.sum(dL[w])
            cs.append(c);amps.append(abs(a));phs.append(np.angle(a))
        c+=step
    return np.array(cs),np.array(amps),np.array(phs)
def beta(cs,amps,cmin):
    sel=(cs>=cmin)&(amps>0)
    x=np.log(cs[sel]);y=np.log(amps[sel])
    A=np.vstack([np.ones_like(x),x]).T
    coef,_,_,_=np.linalg.lstsq(A,y,rcond=None)
    r=y-A@coef
    # jackknife over blocks of 4
    nb=len(x)//4; bs=[]
    for i in range(nb):
        mask=np.ones(len(x),bool); mask[4*i:4*i+4]=False
        c2,_,_,_=np.linalg.lstsq(A[mask],y[mask],rcond=None)
        bs.append(-c2[1])
    return -coef[1], float(np.std(bs)*math.sqrt(max(nb-1,1))), len(x)
out={}
print('width cmin   beta_W (jk se)     beta_V (jk se)     beta_m_grid')
for width in [1.5,2.0,3.0]:
    for cmin in [3.0,3.5,4.5]:
        cW,aW,pW=proj(np.sqrt(u)*W,width)
        cV,aV,_=proj(np.sqrt(u)*V,width)
        cm,am,pm=proj(np.sqrt(u)*msamp,width)
        bW=beta(cW,aW,cmin);bV=beta(cV,aV,cmin);bm=beta(cm,am,cmin)
        out[f'{width}_{cmin}']={'W':bW,'V':bV,'m':bm}
        print('%.1f  %.1f   %+.3f+-%.3f (%d)  %+.3f+-%.3f  %+.3f+-%.3f'%(width,cmin,bW[0],bW[1],bW[2],bV[0],bV[1],bm[0],bm[1]))
# per-window amplitude ratio & phase difference (width 2.0)
cW,aW,pW=proj(np.sqrt(u)*W,2.0)
cm,am,pm=proj(np.sqrt(u)*msamp,2.0)
n=min(len(cW),len(cm))
ratio=aW[:n]/am[:n]
dphi=np.angle(np.exp(1j*(pW[:n]-pm[:n])))
print('per-window amp ratio aW/am: mean=%.4f sd=%.4f (predict 0.2468)'%(ratio.mean(),ratio.std()))
print('per-window phase diff (rad, predict pi=sign flip): mean=%.3f sd=%.3f'%(np.mean(np.abs(dphi)),np.std(np.abs(dphi))))
print('windows (c, aW, am, ratio):')
for i in range(0,n,4):
    print('  %.2f  %.5f  %.5f  %.3f'%(cW[i],aW[i],am[i],ratio[i]))
json.dump({'grid_scan':out,'ratio_mean':float(ratio.mean()),'ratio_sd':float(ratio.std()),
 'absdphi_mean':float(np.mean(np.abs(dphi)))},open('stage3.json','w'))
print('wrote stage3.json')
