// Rendering is deliberately separate from numerical providers and experiment state.
export const colors = ['#5cddd4','#efba67','#ac9eff','#ef8297','#96c97b','#98bedc'];
export const fmt = x => !Number.isFinite(x) ? '—' : (Math.abs(x)>=1e5 || (Math.abs(x)>0 && Math.abs(x)<0.001) ? x.toExponential(3) : Number(x.toPrecision(6)).toString());
const pad = {l:65,r:22,t:24,b:45};
function setup(host,label) {
  const canvas=document.createElement('canvas'); canvas.tabIndex=0; canvas.setAttribute('role','img'); canvas.setAttribute('aria-label',label);
  const toolbar=document.createElement('div');toolbar.className='plot-tools';
  host.replaceChildren(toolbar,canvas);
  const context=canvas.getContext('2d');
  const fit=()=>{const w=Math.max(260,host.clientWidth),h=300;const dpr=Math.min(2,window.devicePixelRatio||1);canvas.width=w*dpr;canvas.height=h*dpr;canvas.style.width='100%';canvas.style.height=h+'px';context.setTransform(dpr,0,0,dpr,0,0);return [w,h];};
  return {canvas,toolbar,context,fit};
}
function button(parent,text,label,action) {const b=document.createElement('button');b.textContent=text;b.setAttribute('aria-label',label);b.onclick=action;parent.append(b);return b;}
function stamp(ctx,w,h){ctx.fillStyle='#91aabd';ctx.font='8px ui-monospace, monospace';ctx.textAlign='right';ctx.fillText('SCOUT · '+(window.observatory?.scene().result_id||'').slice(0,8),w-8,h-6);}
function ticks(ctx,w,h,xlim,ylim,xlabel,ylabel) {
  ctx.fillStyle='#0d1622';ctx.fillRect(0,0,w,h);ctx.lineWidth=1;ctx.font='11px ui-monospace, monospace';
  for(let i=0;i<=4;i++) {
    const x=pad.l+(w-pad.l-pad.r)*i/4, y=h-pad.b-(h-pad.t-pad.b)*i/4;
    ctx.strokeStyle='#213043';ctx.beginPath();ctx.moveTo(x,pad.t);ctx.lineTo(x,h-pad.b);ctx.moveTo(pad.l,y);ctx.lineTo(w-pad.r,y);ctx.stroke();
    ctx.fillStyle='#92a6bb';ctx.textAlign='center';ctx.fillText(fmt(xlim[0]+(xlim[1]-xlim[0])*i/4),x,h-pad.b+19);
    ctx.textAlign='right';ctx.fillText(fmt(ylim[0]+(ylim[1]-ylim[0])*i/4),pad.l-9,y+4);
  }
  ctx.fillStyle='#b6c7d9';ctx.textAlign='center';ctx.fillText(xlabel,w/2,h-6);ctx.textAlign='left';ctx.fillText(ylabel,pad.l,14);
}
export class Curve {
  constructor(host,series,{label='Data plot',xlabel='x',ylabel='',events=[],onSelect=()=>{},selection=null,onView=()=>{}}={}) {
    Object.assign(this,setup(host,label));Object.assign(this,{host,series,xlabel,ylabel,events,onSelect,selection,onView});
    const xs=series.flatMap(s=>s.points.map(p=>p[0])).filter(Number.isFinite).concat(events.flatMap(e=>[e.x0,e.x1]));
    let lo=xs.length?xs.reduce((a,b)=>Math.min(a,b),Infinity):0,hi=xs.length?xs.reduce((a,b)=>Math.max(a,b),-Infinity):1;if(lo===hi){lo-=.5;hi+=.5;}
    this.full=[lo,hi];this.view=[lo,hi];
    button(this.toolbar,'−','Zoom out',()=>this.zoom(1.7));button(this.toolbar,'+','Zoom in',()=>this.zoom(.6));button(this.toolbar,'Reset','Reset plot viewport',()=>{this.view=[...this.full];this.draw();this.onView();});
    const hint=document.createElement('span');hint.textContent='Drag to zoom · click to inspect · arrows to step';this.toolbar.append(hint);
    this.canvas.onpointerdown=e=>{this.down=e.offsetX;this.canvas.setPointerCapture(e.pointerId);};
    this.canvas.onpointerup=e=>{if(this.down==null)return;const a=this.toX(this.down),b=this.toX(e.offsetX);if(Math.abs(e.offsetX-this.down)>12){this.view=[Math.min(a,b),Math.max(a,b)];this.draw();this.onView();}else this.pick(b);this.down=null;};
    this.canvas.ondblclick=()=>{this.view=[...this.full];this.draw();this.onView();};
    this.canvas.onkeydown=e=>{if(!['ArrowLeft','ArrowRight','+','-'].includes(e.key))return;e.preventDefault();if(e.key==='+')this.zoom(.6);else if(e.key==='-')this.zoom(1.7);else{const pts=this.series[0]?.points||[];if(!pts.length)return;let k=pts.findIndex(p=>p[0]>=(this.selection??this.view[0]));k=Math.max(0,Math.min(pts.length-1,k+(e.key==='ArrowLeft'?-1:1)));this.pick(pts[k][0]);}};
    this.observer=new ResizeObserver(()=>this.draw());this.observer.observe(host);this.draw();
  }
  toX(px){const w=this.width||500;return this.view[0]+Math.max(0,Math.min(1,(px-pad.l)/(w-pad.l-pad.r)))*(this.view[1]-this.view[0]);}
  zoom(factor){let mid=(this.view[0]+this.view[1])/2,span=(this.view[1]-this.view[0])*factor;span=Math.min(span,this.full[1]-this.full[0]);let lo=Math.max(this.full[0],Math.min(mid-span/2,this.full[1]-span));this.view=[lo,lo+span];this.draw();this.onView();}
  pick(x){this.selection=x;this.draw();this.onSelect(x);}
  setSelection(x){this.selection=x;this.draw();}
  destroy(){this.observer.disconnect();}
  draw(){
    const [w,h]=this.fit();this.width=w;const ctx=this.context,[lo,hi]=this.view;
    const values=this.series.flatMap(s=>s.points.filter(p=>p[0]>=lo&&p[0]<=hi&&Number.isFinite(p[1])).map(p=>p[1]));
    let ymin=values.length?values.reduce((a,b)=>Math.min(a,b),Infinity):0,ymax=values.length?values.reduce((a,b)=>Math.max(a,b),-Infinity):1;
    let margin=(ymax-ymin)*.08 || Math.max(Math.abs(ymin)*.1,1);ymin-=margin;ymax+=margin;
    const px=x=>pad.l+(x-lo)/(hi-lo)*(w-pad.l-pad.r),py=y=>h-pad.b-(y-ymin)/(ymax-ymin)*(h-pad.t-pad.b);
    ticks(ctx,w,h,[lo,hi],[ymin,ymax],this.xlabel,this.ylabel);
    ctx.save();ctx.beginPath();ctx.rect(pad.l,pad.t,w-pad.l-pad.r,h-pad.t-pad.b);ctx.clip();
    for(const e of this.events){ctx.fillStyle='#efba6733';ctx.fillRect(px(e.x0),pad.t,Math.max(1,px(e.x1)-px(e.x0)),h-pad.t-pad.b);}
    this.series.forEach((s,i)=>{
      const color=s.color||colors[i%colors.length];ctx.strokeStyle=color;ctx.lineWidth=1;ctx.globalAlpha=.18;
      for(const e of s.envelopes||[]){if(e.x1<lo||e.x0>hi)continue;ctx.beginPath();ctx.moveTo(px((e.x0+e.x1)/2),py(e.min));ctx.lineTo(px((e.x0+e.x1)/2),py(e.max));ctx.stroke();}
      ctx.globalAlpha=1;ctx.lineWidth=s.dashed?1.2:1.5;ctx.setLineDash(s.dashed?[5,4]:[]);ctx.beginPath();let active=false;
      for(const [x,y] of s.points){if(y===null||!Number.isFinite(y)){active=false;continue;}if(active)ctx.lineTo(px(x),py(y));else ctx.moveTo(px(x),py(y));active=true;}ctx.stroke();ctx.setLineDash([]);
    });
    if(Number.isFinite(this.selection)){ctx.strokeStyle='#d9e6f1aa';ctx.setLineDash([3,4]);ctx.beginPath();ctx.moveTo(px(this.selection),pad.t);ctx.lineTo(px(this.selection),h-pad.b);ctx.stroke();ctx.setLineDash([]);}
    ctx.restore();stamp(ctx,w,h);
  }
}
export class Field {
  constructor(host,grid,{label='Sampled field',onSelect=()=>{}}={}) {
    Object.assign(this,setup(host,label));Object.assign(this,{host,grid,onSelect});
    const hint=document.createElement('span');hint.textContent=grid.kind==='complex'?'Hue: phase · brightness: log(1+|f|) · click a sample':'Signed interaction · gold positive / cyan negative · click a cell';this.toolbar.append(hint);
    this.canvas.onclick=e=>{const col=Math.max(0,Math.min(grid.n-1,Math.floor((e.offsetX-pad.l)/(this.width-pad.l-pad.r)*grid.n)));const row=grid.n-1-Math.max(0,Math.min(grid.n-1,Math.floor((e.offsetY-pad.t)/(300-pad.t-pad.b)*grid.n)));this.selection=[col,row];this.draw();onSelect(col,row);};
    this.canvas.onkeydown=e=>{if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key))return;e.preventDefault();let [col,row]=this.selection||[0,0];col=Math.max(0,Math.min(grid.n-1,col+(e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0)));row=Math.max(0,Math.min(grid.n-1,row+(e.key==='ArrowUp'?1:e.key==='ArrowDown'?-1:0)));this.selection=[col,row];this.draw();onSelect(col,row);};
    this.observer=new ResizeObserver(()=>this.draw());this.observer.observe(host);this.draw();
  }
  setSelection(x){this.t=x;this.draw();}
  destroy(){this.observer.disconnect();}
  draw(){
    const [w,h]=this.fit();this.width=w;const ctx=this.context,g=this.grid,n=g.n;
    ticks(ctx,w,h,[g.x[0],g.x.at(-1)],[g.y[0],g.y.at(-1)],g.kind==='complex'?'Re(s) = σ':'m',g.kind==='complex'?'Im(s) = t':'n');
    const cw=(w-pad.l-pad.r)/n,ch=(h-pad.t-pad.b)/n,max=g.kind==='interaction'?(g.scale_max??Math.max(...g.values.map(Math.abs))):1;
    for(let row=0;row<n;row++)for(let col=0;col<n;col++){
      const k=row*n+col;let fill='#455164';
      if(g.kind==='complex'&&g.phase[k]!=null&&g.magnitude[k]!=null){const hue=(g.phase[k]*180/Math.PI+360)%360;const bright=20+44*(1-Math.exp(-g.magnitude[k]));fill=`hsl(${hue} 70% ${bright}%)`;}
      if(g.kind==='interaction'){const v=g.values[k],a=Math.sqrt(Math.abs(v)/(max||1));fill=`hsl(${v>=0?38:175} ${45+35*a}% ${7+65*a}%)`;}
      ctx.fillStyle=fill;ctx.fillRect(pad.l+col*cw,pad.t+(n-1-row)*ch,cw+.3,ch+.3);
    }
    if(g.split){ctx.strokeStyle='#ffffff99';ctx.lineWidth=1;const sx=pad.l+g.split*cw,sy=pad.t+(n-g.split)*ch;ctx.beginPath();ctx.moveTo(sx,pad.t);ctx.lineTo(sx,h-pad.b);ctx.moveTo(pad.l,sy);ctx.lineTo(w-pad.r,sy);ctx.stroke();}
    if(g.kind==='complex'&&this.t>=g.y[0]&&this.t<=g.y.at(-1)){const y=h-pad.b-(this.t-g.y[0])/(g.y.at(-1)-g.y[0])*(h-pad.t-pad.b);ctx.strokeStyle='#fff9';ctx.beginPath();ctx.moveTo(pad.l,y);ctx.lineTo(w-pad.r,y);ctx.stroke();}
    if(this.selection){const [c,r]=this.selection;ctx.strokeStyle='#fff';ctx.lineWidth=1.5;ctx.strokeRect(pad.l+c*cw,pad.t+(n-1-r)*ch,cw,ch);}
    stamp(ctx,w,h);
  }
}
export function legend(host,series){host.replaceChildren();series.forEach((s,i)=>{const item=document.createElement('span'),dot=document.createElement('i');dot.style.background=s.color||colors[i%colors.length];item.append(dot,document.createTextNode(s.label));host.append(item);});}
