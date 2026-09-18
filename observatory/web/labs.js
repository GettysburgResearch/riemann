// New research desks share the legacy renderer, job transport and saved state.
import {Curve, Field, legend, fmt} from './charts.js';
const $ = id => document.getElementById(id);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const sources = ['mobius','magnitude','random_signs','shuffled','liouville','alternating'];
export const labModules = {
 cancellation: {icon:'Δμ',name:'Linked cancellation',title:'Follow a discrepancy to its source',description:'Compare complete finite sources. Change the split and width, inspect the cross term, and follow a matrix entry or eigenmode back to its contributors.',defaults:{n:64,start:1,split:32,width:.5,exponent:.5,source_a:'mobius',source_b:'magnitude',seed_a:17,seed_b:29}},
 explicit: {icon:'↔',name:'Prime–zero formula',title:'Two sides. One specified identity.',description:'A Gaussian Weil explicit formula, with all finite terms visible. Move the log-center, change smoothing and cutoffs, then inspect the contributing prime powers and zero band.',defaults:{a:.015,b_min:0,b_max:5,focus_b:2.302585092994046,samples:81,prime_cutoff:5000,zero_count:24,band_first:1,band_last:8,gamma_cutoff:100,quadrature_order:24,dps:30}},
 sweep: {icon:'⌕',name:'Disagreement search',title:'Search here. Test somewhere else.',description:'Search a bounded width × split grid, freeze its winner, then evaluate once on a disjoint held-out window. Negative findings remain part of the investigation.',defaults:{n:48,train_start:1,holdout_start:1001,source_a:'mobius',source_b:'random_signs',seed_a:17,seed_b:29,exponent:.5,width_min:.05,width_max:2,width_steps:12,split_steps:9}},
 family: {icon:'L',name:'Quadratic L-families',title:'Compare members without losing their arithmetic',description:'Real quadratic characters, primitive conductors and induced members. The local factors removed by induction remain explicit.',defaults:{discriminants:[-4,-3,5],multiplier:1,sigma:.5,t_min:0,t_max:40,samples:96,dps:25}},
 hierarchy: {icon:'Σ',name:'Reciprocal families',title:'Thin a sequence. Inspect what remains.',description:'Repeated prime-index selection, reciprocal sums and a separate fractional sequence. Index cutoffs and value cutoffs are never silently identified.',defaults:{limit:20000,depth:3,alpha:.5,buckets:360}},
 refine: {icon:'⊙',name:'Point refinement',title:'Refine the point, not the whole screen',description:'Decimal-string coordinates and a higher-precision evaluation. Precision agreement is a check, not a certified error bound.',defaults:{function:'zeta',real:'0.5',imag:'14.134725141734693790457251983562',dps:60,backend:'mpmath'}}
};
export const labFields = {
 cancellation:[['n','Window length','number'],['start','Starting integer','number'],['split','Block split (count)','number'],['width','Log-kernel width h','number'],['exponent','Weight exponent α','number'],['source_a','Source A','select',sources],['source_b','Control B','select',sources],['seed_a','Seed A','number'],['seed_b','Seed B','number']],
 explicit:[['a','Gaussian a','number'],['b_min','b minimum','number'],['b_max','b maximum','number'],['focus_b','Focused b = log x','number'],['samples','b samples','number'],['prime_cutoff','Prime-power cutoff','number'],['zero_count','Positive zero count','number'],['band_first','Zero band first','number'],['band_last','Zero band last','number'],['gamma_cutoff','Gamma |t| cutoff','number'],['quadrature_order','Quadrature order','select',[16,24,32]],['dps','Zero working digits','number']],
 sweep:[['n','Window length','number'],['train_start','Training start','number'],['holdout_start','Holdout start','number'],['source_a','Source A','select',sources],['source_b','Control B','select',sources],['seed_a','Seed A','number'],['seed_b','Seed B','number'],['exponent','Weight exponent α','number'],['width_min','Minimum h','number'],['width_max','Maximum h','number'],['width_steps','Width trials','number'],['split_steps','Split trials','number']],
 family:[['discriminants','Discriminants (comma separated)','csv'],['multiplier','Induced modulus multiplier','select',[1,2,3,4]],['sigma','Slice σ','number'],['t_min','t minimum','number'],['t_max','t maximum','number'],['samples','Samples','number'],['dps','Working digits','number']],
 hierarchy:[['limit','Integer / index cutoff','number'],['depth','Selection depth','number'],['alpha','Fractional exponent α','number'],['buckets','Display buckets','number']],
 refine:[['function','Object','select',['zeta','eta','xi','beta','chi3']],['real','Exact Re(s) decimal','text'],['imag','Exact Im(s) decimal','text'],['dps','Working digits','number'],['backend','Refinement backend','select',['mpmath','flint']]]
};

function table(headings, rows) {
 return `<div class="table-scroll"><table><thead><tr>${headings.map(h=>`<th>${esc(h)}</th>`).join('')}</tr></thead><tbody>${rows.map(row=>`<tr>${row.map(v=>`<td>${esc(typeof v==='number'?fmt(v):v)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
}
function energy(label, e) {
 return `<section class="panel energy-panel"><h2>${esc(label)}</h2><div class="energy-strip">${[['Block A',e.A],['Block B',e.B],['2 × cross',e.cross],['Full energy',e.total]].map(([k,v])=>`<div class="${v<0?'negative':''}"><span>${k}</span><strong>${fmt(v)}</strong></div>`).join('')}</div><p>Diagonal ${fmt(e.diagonal)} · off-diagonal ${fmt(e.off_diagonal)} · identity residual ${fmt(e.identity_residual)}</p></section>`;
}
export function labMarkup(r, card) {
 const q=r.request;
 if(q.module==='cancellation')return energy('SOURCE A · '+q.source_a,r.experiments.a.energy)+energy('CONTROL B · '+q.source_b,r.experiments.b.energy)+
 card('matrix-a','Source A interactions','Full finite matrix; a common color scale is used for A and B')+card('matrix-b','Control B interactions','Click a cell: both sources and the difference are inspected together')+
 card('difference','B − A: term-by-term discrepancy','Signed difference, not a difference between separately reduced energies')+card('rows','Where the difference accumulates','Click an integer to rank its contributing terms')+
 `<section class="panel wide"><h2>Contributing terms</h2><p id="trace-summary">Select a row or cell to trace it.</p><div id="trace"></div></section>`+
 card('prefix','Full-prefix energy','Every added integer brings its diagonal and both off-diagonal orientations',true)+
 card('eigenvalues','Kernel spectrum','No tiny negative eigenvalue is clipped; unstable modes remain labeled')+
 `<section class="panel"><h2>Eigenmode → test function</h2><label>Selected eigenmode<select id="mode-select" aria-label="Selected eigenmode"></select></label><div id="mode-details"></div></section>`+
 card('mode-vector','Mode coefficients and source projections','vₙ, aₙvₙ, bₙvₙ; a selected mode is not an RH witness')+card('mode-function','The corresponding kernel section','f(u)=Σvₙ exp(−(u−log n)²/(2h²)); u is log-coordinate');
 if(q.module==='explicit')return card('explicit-sides','Finite identity comparison','Select b on either curve; use “Inspect this b” to recompute the term ledger')+
 card('explicit-error','Discrepancy & selected band','The residual includes omitted tails and numerical errors, not just zero truncation')+
 card('explicit-components','Pole, logπ, gamma, and prime-power terms','Each plotted term uses the displayed normalization',true)+
 `<section class="panel wide"><div class="focus-row"><h2>Term ledger at b=${fmt(r.focus.b)} · x=${fmt(r.focus.x)}</h2><button id="focus-explicit">Inspect selected b</button><span id="focus-proposal"></span></div>${table(['Pole','−logπ','Gamma','−Prime powers','RHS','Zero sum','RHS − zeros'],[[r.focus.pole,r.focus.logpi,r.focus.gamma,r.focus.prime,r.focus.rhs,r.focus.zeros,r.focus.discrepancy]])}<div class="ledger-grid"><div><h3>Prime-power contributions · largest magnitudes first</h3>${table(['p^k','p','k','Signed contribution'],[...r.focus.prime_terms].sort((a,b)=>Math.abs(b.contribution)-Math.abs(a.contribution)).slice(0,80).map(t=>[t.n,t.prime,t.power,t.contribution]))}<p>Top 80 shown; ALL ${r.focus.prime_terms.length} terms are retained in the artifact. Finite prime total ${fmt(r.focus.prime)}.</p></div><div><h3>Every selected zero pair</h3>${table(['Index','γ (approximate)','Pair contribution'],r.focus.zero_terms.map(t=>[t.index,t.gamma,t.contribution]))}</div></div><h3>Truncation and error ledger</h3>${table(['Boundary','Status'],Object.entries(r.boundaries).map(([k,v])=>[k,v===null?'UNKNOWN — no bound supplied':v]))}<details><summary>Cutoff and quadrature consistency checks</summary><pre>${esc(JSON.stringify({cutoffs:r.cutoff_checks,quadrature_change:r.focus.quadrature_order_change},null,2))}</pre></details></section>`;
 if(q.module==='sweep')return card('sweep-curve','Best training effect at each width','Selection is training-only; the holdout is not scanned')+
 `<section class="panel"><h2>Frozen detector</h2><div class="energy-strip"><div><span>Training best</span><strong>${fmt(r.metrics.training_best_score)}</strong></div><div><span>Held out · once</span><strong>${fmt(r.metrics.frozen_holdout_score)}</strong></div></div><pre>${esc(JSON.stringify(r.detector,null,2))}</pre><button id="open-holdout">Inspect frozen holdout terms</button></section>`+
 `<section class="panel wide"><h2>Training grid · click a trial to investigate</h2><p>Every trial is preserved. Opening a nonwinning trial does not inherit the winner’s holdout result.</p><div id="sweep-grid" class="sweep-grid"></div><pre id="sweep-selection"></pre><button id="open-trial">Open selected training comparison</button></section>`;
 if(q.module==='family')return card('family-curves','Member comparison','Raw ordinates t; no automatic universal unfolding',true)+`<section class="panel wide"><h2>Arithmetic member metadata</h2>${table(['D','Conductor','Modulus','Primitive','Parity','Removed local primes','L(1/2)','Induction residual'],r.members.map(m=>[m.D,m.conductor,m.modulus,String(m.primitive),m.parity,m.removed_euler_primes.join(', ')||'none',m.central_value_s_half,m.induction_residual_at_midpoint]))}<details><summary>Exact character tables & completion conventions</summary><pre>${esc(JSON.stringify(r.members,null,2))}</pre></details></section>`;
 if(q.module==='hierarchy')return card('hierarchy-sums','Reciprocal sums by value cutoff x','Exact selected memberships; floating reciprocal sums')+card('hierarchy-counts','Selected family counts','A member’s rank is taken within the previous family')+card('fractional','Fractional sequence by INDEX cutoff N',r.fractional.coordinate,true)+`<section class="panel wide"><h2>Membership inspector</h2>${table(['Depth','Count','Reciprocal sum','First members'],r.families.map(f=>[f.depth,f.count,f.harmonic_sum,f.initial_members.join(', ')]))}</section>`;
 if(q.module==='refine')return `<section class="panel wide"><h2>Point refinement result</h2>${table(['Quantity','Value'],Object.entries(r.point))}<p>Only the displayed point was evaluated. Saved refinements travel with their parent investigation.</p></section>`;
 return '';
}

export function mountLab(r, tools) {
 const {curve, plots, select, run, getSelection, viewChanged}=tools, q=r.request;
 const bindCurve=(id,series,options={})=>curve(id,series,options);
 const inspect=obj=>{select(obj);};
 let restore=()=>{};
 if(q.module==='cancellation'){
   const n=q.n, A=r.experiments.a, B=r.experiments.b;
   const scale=Math.max(...A.matrix.map(Math.abs),...B.matrix.map(Math.abs));
   const fields=[];
   const trace=(row,col=null)=>{
     const terms=r.indices.map((m,j)=>({m,n:r.indices[row],a:A.matrix[row*n+j],b:B.matrix[row*n+j],delta:r.grid.values[row*n+j],block:(row<q.split?'A':'B')+(j<q.split?'A':'B'),coefficient_a:A.coefficients[j],coefficient_b:B.coefficients[j],row_coefficient_a:A.coefficients[row],row_coefficient_b:B.coefficients[row],weight_m_a:A.weights[j],weight_n_a:A.weights[row],weight_m_b:B.weights[j],weight_n_b:B.weights[row],kernel_value:Math.exp(-.5*((Math.log(m)-Math.log(r.indices[row]))/q.width)**2)}));
     terms.sort((a,b)=>Math.abs(b.delta)-Math.abs(a.delta));
     const sum=terms.reduce((s,t)=>s+t.delta,0);
     $('trace-summary').textContent=`Row n=${r.indices[row]} · cₙ(A)=${A.coefficients[row]}, cₙ(B)=${B.coefficients[row]} · all ${n} terms · sum(B−A)=${fmt(sum)}. Cross-block entries occur in both matrix orientations; this row lists one orientation.`;
     $('trace').innerHTML=table(['m','n','Block','cₘ(A)','cₘ(B)','A term','B term','B − A'],terms.map(t=>[t.m,t.n,t.block,t.coefficient_a,t.coefficient_b,t.a,t.b,t.delta]));
     const selected=col===null?null:terms.find(t=>t.m===r.indices[col]);
     if(col!==null)fields.forEach(f=>{f.selection=[col,row];f.draw();});
     inspect({kind:'cancellation trace',row,col,integer:r.indices[row],row_difference:sum,selected_term:selected,contributor_count:n});
   };
   for(const [id,values,common] of [['matrix-a',A.matrix,true],['matrix-b',B.matrix,true],['difference',r.grid.values,false]]){
     const g={...r.grid,values,...(common?{scale_max:scale}:{}),split:q.split};
     const f=new Field($(id),g,{label:id,onSelect:(col,row)=>trace(row,col)});plots.push(f);fields.push(f);
   }
   bindCurve('rows',r.series.slice(2),{xlabel:'integer n',onSelect:x=>trace(Math.max(0,Math.min(n-1,Math.round(x)-q.start)))});
   bindCurve('prefix',r.series.slice(0,2),{xlabel:'last included integer'});
   let modePlots=[];
   const setMode=mode=>{
     mode=Math.max(0,Math.min(n-1,mode));$('mode-select').value=String(mode);
     const S=r.spectrum, v=S.vectors[mode], lambda=S.eigenvalues[mode];
     const projectionA=v.map((value,i)=>value*A.weights[i]),projectionB=v.map((value,i)=>value*B.weights[i]);
     const xs=Array.from({length:192},(_,i)=>r.kernel.logs[0]+(r.kernel.logs.at(-1)-r.kernel.logs[0])*i/191);
     const f=xs.map(x=>v.reduce((total,value,j)=>total+value*Math.exp(-.5*((x-r.kernel.logs[j])/q.width)**2),0));
     modePlots.forEach(p=>{p.destroy();const i=plots.indexOf(p);if(i>=0)plots.splice(i,1);});
     modePlots=[bindCurve('mode-vector',[{label:'vₙ',points:v.map((x,i)=>[r.indices[i],x])},{label:'aₙvₙ',points:projectionA.map((x,i)=>[r.indices[i],x])},{label:'bₙvₙ',points:projectionB.map((x,i)=>[r.indices[i],x])}],{xlabel:'integer n'}),bindCurve('mode-function',[{label:'Kernel section f(u)',points:xs.map((x,i)=>[x,f[i]])}],{xlabel:'u = log coordinate'})];
     $('mode-details').innerHTML=table(['Quantity','Value'],[['Eigenvalue',lambda],['λ(v·a)²',S.mode_energy_a[mode]],['λ(v·b)²',S.mode_energy_b[mode]],['Eigenpair residual (full Frobenius)',S.residual_frobenius],['Numerical rank',S.numerical_rank],['Status',Math.abs(lambda)<=S.numerical_rank_threshold?'UNRESOLVED / near numerical floor':'Finite numerical mode']]);
     inspect({kind:'kernel mode',mode,eigenvalue:lambda,projection_a:S.projection_a[mode],projection_b:S.projection_b[mode],energy_a:S.mode_energy_a[mode],energy_b:S.mode_energy_b[mode]});
   };
   $('mode-select').innerHTML=r.spectrum.eigenvalues.map((v,i)=>`<option value="${i}">Mode ${i+1} · λ=${fmt(v)}</option>`).join('');
   $('mode-select').onchange=e=>setMode(Number(e.target.value));
   bindCurve('eigenvalues',[{label:'Eigenvalue',points:r.spectrum.eigenvalues.map((v,i)=>[i+1,v])}],{xlabel:'mode index',onSelect:x=>setMode(Math.round(x)-1)});
   setMode(n-1);trace(Math.min(q.split-1,n-1));
   restore=selection=>{if(selection?.kind==='kernel mode'&&Number.isInteger(selection.mode))setMode(selection.mode);else if(selection?.kind==='cancellation trace'&&Number.isInteger(selection.row)&&selection.row>=0&&selection.row<n)trace(selection.row,Number.isInteger(selection.col)&&selection.col>=0&&selection.col<n?selection.col:null);};
 }
 if(q.module==='explicit'){
   let selected=q.focus_b;
   const choose=x=>{selected=Math.min(q.b_max,Math.max(q.b_min,x));$('focus-proposal').textContent=`Selected b=${fmt(selected)}`;inspect({kind:'explicit focus proposal',b:selected});};
   bindCurve('explicit-sides',r.series.slice(0,2),{xlabel:'b = log center',onSelect:choose});
   bindCurve('explicit-error',r.series.slice(2,4),{xlabel:'b = log center',onSelect:choose});
   bindCurve('explicit-components',r.series.slice(4),{xlabel:'b = log center',onSelect:choose});
   $('focus-explicit').onclick=()=>run({...q,focus_b:selected});
   restore=s=>{if(s?.kind==='explicit focus proposal'&&Number.isFinite(s.b))choose(s.b);};
 }
 if(q.module==='sweep'){
   let chosen=r.winner_index;
   const pick=i=>{chosen=i;const trial=r.trials[i];$('sweep-selection').textContent=JSON.stringify(trial,null,2);document.querySelectorAll('[data-trial]').forEach(b=>b.classList.toggle('selected',Number(b.dataset.trial)===i));inspect({kind:'training trial',index:i,...trial});};
   const max=Math.max(...r.trials.map(t=>t.score),1e-30);
   $('sweep-grid').style.gridTemplateColumns=`repeat(${r.splits.length},minmax(45px,1fr))`;
   $('sweep-grid').innerHTML=r.trials.map((t,i)=>`<button data-trial="${i}" title="h=${t.width}, split=${t.split}, score=${t.score}" aria-label="Trial ${i+1}: width ${fmt(t.width)}, split ${t.split}, score ${fmt(t.score)}">${fmt(t.score)}</button>`).join('');
   document.querySelectorAll('[data-trial]').forEach(b=>{b.style.background=`hsl(175 35% ${10+28*r.trials[Number(b.dataset.trial)].score/max}%)`;b.onclick=()=>pick(Number(b.dataset.trial));});
   bindCurve('sweep-curve',r.series,{xlabel:'kernel width h'});
   $('open-trial').onclick=()=>{const t=r.trials[chosen];run({module:'cancellation',n:q.n,start:q.train_start,split:t.split,width:t.width,exponent:q.exponent,source_a:q.source_a,source_b:q.source_b,seed_a:q.seed_a,seed_b:q.seed_b});};
   $('open-holdout').onclick=()=>run(r.holdout.request);
   pick(chosen);restore=s=>{if(s?.kind==='training trial'&&Number.isInteger(s.index)&&r.trials[s.index])pick(s.index);};
 }
 if(q.module==='family')bindCurve('family-curves',r.series,{xlabel:'t'});
 if(q.module==='hierarchy'){
   bindCurve('hierarchy-sums',r.series,{xlabel:'value cutoff x'});bindCurve('hierarchy-counts',r.families.map(f=>f.count_curve),{xlabel:'value cutoff x'});bindCurve('fractional',[r.fractional.series],{xlabel:'INDEX cutoff N (not value cutoff x)'});
 }
 if(q.module==='refine')inspect({kind:'refined point',request:q,point:r.point});
 return {restore};
}
