function phaseScout(){
const primes=[5,7,11,13,17,19,23,29,31],panels=[],all=[];
const mod=(x,p)=>(x%p+p)%p;
for(const p of primes){
 const squareCounts=Array(p).fill(0);for(let v=0;v<p;v++)squareCounts[v*v%p]++;
 const chi=x=>squareCounts[mod(x,p)]-1;
 const delta=p%3===1?1:0,rows=[];
 for(let A=1;A<p;A++)for(let B=0;B<p;B++){
  if(mod(4*A**3+27*B*B,p)===0)continue;
  let pointsE=1,pointsD=1+chi(-27),split=0,splitPlus=0,splitMinus=0,splitZero=0,oldPlus=0,oldMinus=0;
  const fibres=[];
  for(let x=0;x<p;x++)pointsE+=squareCounts[mod(x**3+A*x+B,p)];
  for(let u=0;u<p;u++){
   const disc=mod(-4*A**3-27*(B-u*u)**2,p),sign=chi(u);
   pointsD+=squareCounts[disc];
   const roots=[];for(let x=0;x<p;x++)if(mod(x**3+A*x+B-u*u,p)===0)roots.push(x);
   if(disc===0){if(roots.length!==2||!sign)throw Error("ramification");if(sign===1)oldPlus++;else oldMinus++;}
   else{if(![0,1,3].includes(roots.length))throw Error("good splitting");if(roots.length===3){split++;if(sign===1)splitPlus++;else if(sign===-1)splitMinus++;else splitZero++;}}
   fibres.push({u,discriminant:disc,chi:sign,roots});
  }
  const aE=p+1-pointsE,aD=p+1-pointsD,tZ=aD+2*aE,zPoints=6*split+3*(oldPlus+oldMinus)+2*delta;
  if(tZ!==p+1-zPoints||aE*aE>4*p||aD*aD>4*p)throw Error("source identity");
  const row={p,A,B,pointsE,pointsD,aE,aD,tZ,split,splitPlus,splitMinus,splitZero,oldPlus,oldMinus,delta,zPoints,
   class:tZ===0?"zero":tZ%12?"fractional":tZ<0?"negative_integer":"positive_integer"};
  rows.push(row);all.push(row);
 }
 const count={};for(const r of rows)count[r.class]=(count[r.class]||0)+1;
 const traces={};for(const r of rows)traces[r.tZ]=(traces[r.tZ]||0)+1;
 panels.push({p,count:rows.length,classes:count,traces,rows});
}
const examples={};for(const r of all){const key=r.class+"_"+(r.oldPlus+r.oldMinus+r.delta?"ramified":"no_rational_ramification");if(!examples[key])examples[key]=r;}
return{scope:"complete finite parameter scout; exact rational-fibre and genus-three checks; no analytic proof",panels,examples,total:all.length};
}
return phaseScout();

