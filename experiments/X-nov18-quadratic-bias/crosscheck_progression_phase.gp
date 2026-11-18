\\ Independent ordinary-precision check of the phase at zero for class one.
\\ The directed bounds are produced by classify_progressions.py.
default(realprecision,38);
character_phase(q)={
  my(group=znstar(q,1), base=lfuncreate(1), primitive, conductor, g, chi, lf);
  my(total=Euler-1/2-eulerphi(q)/2-lfun(base,2,1)/lfun(base,2));
  for(m=2,q,if(gcd(m,q)==1,
    conductor=znconreyconductor(group,znconreylog(group,m),&primitive);
    if(type(conductor)=="t_VEC",conductor=conductor[1]);
    g=znstar(conductor,1);
    chi=znconreychar(g,znconreyexp(g,primitive));
    lf=lfuncreate([g,chi]);
    total+=lfun(lf,1,1)/lfun(lf,1)-lfun(lf,2,1)/lfun(lf,2);
  ));
  if(abs(imag(total))>1.e-28,error("conjugate-character cancellation failed"));
  return(real(total));
}
cyclotomic_phase(q)={
  my(lf=lfuncreate(polcyclo(q)), jet=lfun(lf,1+t+O(t^5)));
  return(polcoef(jet,0)/polcoef(jet,-1)-eulerphi(q)/2-1/2-lfun(lf,2,1)/lfun(lf,2));
}
check_phase(q)={
  my(value=character_phase(q),roots=sum(a=1,q,lift(Mod(a,q)^2)==1));
  if(q!=120 && abs(value-cyclotomic_phase(q))>1.e-26,error("cyclotomic cross-check failed"));
  if(value>=-2*roots/3,error("threshold not crossed"));
  print(q," ",value," < ",-2*roots/3);
}
for(i=1,11,check_phase([11,21,22,28,36,40,42,48,60,84,120][i]));
