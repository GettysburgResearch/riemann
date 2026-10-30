exec(open('corner.py').read().split('for b in')[0].replace('3001','601'))
for b in [.935,.94,.945,.95]:
 best=(-1,None)
 C=.14
 for d in np.linspace(0,C,11):
  for k in np.linspace(0,min(d,(C-d)/1.2),6):
   for g in np.linspace(0,C-d-1.2*k,6):
    for v in np.linspace(0,b/2,41):
     rr=val(b,v,d,k,g)
     if rr[0]>best[0]:best=(rr[0],(d,k,g,v,rr[1:]))
 print(b,best,flush=True)
