import {Curve,Field,legend,fmt,colors} from './charts.js';
import {labModules,labFields,labMarkup,mountLab} from './labs.js';
import {storedDesk} from './datasets.js';
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const modules={
 ...labModules,
 datasets:{icon:'▥',name:'Stored data',title:'Large data. Exact coordinates.',description:'Persistent multiresolution summaries with independent gaps and event indices.',defaults:{}},
 geometry:{icon:'ζ',name:'Complex geometry',title:'Explore the critical strip',description:'Follow a phase landscape into a numerical slice. Pin a sample, change the object, and compare what survives.',defaults:{function:'zeta',re_min:-1,re_max:2,t_min:10,t_max:35,sigma:.5,grid:40,samples:384,dps:30}},
 primes:{icon:'π',name:'Prime counting',title:'Look beneath the main term',description:'Exact integer counts, classical approximations, and their residuals. Every integer is computed before display reduction.',defaults:{limit:2000,buckets:240}},
 euler:{icon:'∏',name:'Euler products',title:'Watch the primes accumulate',description:'Build a finite Euler product one local factor at a time. Compare the trajectory and its cutoff sensitivity with ζ(s).',defaults:{sigma:1.5,t:14.134725,limit:1000,omit_prime:0,dps:30}},
 mobius:{icon:'μ',name:'Möbius prefix',title:'Where did the cancellation go?',description:'Inspect the literal Möbius source, then open a finite interaction matrix that retains every signed cross term.',defaults:{limit:10000,kernel_n:48,width:.5,buckets:240}},
 zeros:{icon:'γ',name:'Zero spacing',title:'From individual zeros to gaps',description:'Explore the first indexed zeros and their local spacing. Select an event to inspect its high-precision numerical ordinate.',defaults:{zero_count:24,dps:30}},
 height:{icon:'T+δ',name:'Exact-height desk',title:'Tiny windows. Enormous heights.',description:'Navigate imported fine brackets without rounding away their coordinates. Exact anchors never become JavaScript numbers.',defaults:{height_record:1}}
};
const state={request:{module:'cancellation',...modules.cancellation.defaults},result:null,baseline:null,selection:null,notes:'',name:'First exploration',job:null,generation:0,busy:false,error:'',dirty:false,plots:[],connected:false,refinements:[],capabilities:null,lab:null,storeDesk:null,datasetScene:null,artifactNotice:''};
const fields={
 ...labFields,
 datasets:[],
 geometry:[['function','Object','select',['zeta','eta','xi','beta','chi3']],['re_min','σ minimum','number'],['re_max','σ maximum','number'],['t_min','t minimum','number'],['t_max','t maximum','number'],['sigma','Slice σ','number'],['grid','Grid side','number'],['samples','Slice samples','number'],['dps','Working digits','number']],
 primes:[['limit','Maximum x','number'],['buckets','Display buckets','number']],
 euler:[['sigma','Re(s)','number'],['t','Im(s)','number'],['limit','Prime cutoff','number'],['omit_prime','Omit prime','select',[0,2,3,5,7]],['dps','Working digits','number']],
 mobius:[['limit','Mertens prefix','number'],['kernel_n','Kernel prefix','number'],['width','Log-kernel width h','number'],['buckets','Display buckets','number']],
 zeros:[['zero_count','Number of zeros','number'],['dps','Working digits','number']], height:[['height_record','Imported record','select',[1,2]]]
};
const objectNames={zeta:'ζ(s) · Riemann zeta',eta:'η(s) · Dirichlet eta',xi:'ξ(s) · completed zeta',beta:'β(s) · L(χ₄,s)',chi3:'L(χ₃,s) · mod 3'};
function build(){
 $('app').innerHTML=`<aside class="sidebar"><div class="brand"><span class="brand-mark">ℛ</span><div>RIEMANN<br><small>OBSERVATORY</small></div></div><p class="eyebrow">RESEARCH WORKSPACES</p><nav aria-label="Mathematical workspaces">${Object.entries(modules).map(([id,m])=>`<button data-module="${id}" class="nav-button"><span class="nav-symbol">${m.icon}</span>${m.name}</button>`).join('')}</nav><div class="sidebar-foot"><div class="status-dot"></div><span id="connection">Connecting locally</span><p>v0.4 preview · Linked investigations<br>Numerical scouts, not certificates.</p><a href="/api/openapi.json" target="_blank" rel="noopener">API schema ↗</a></div></aside><main id="workspace"><header class="topbar"><div><span class="crumb">AGENTIC POLYMATH</span><span class="divider">/</span>RESEARCH DESK</div><div class="top-actions"><button id="save">Save investigation</button><button id="export">Export experiment ↓</button><label class="button" for="import">Import artifact ↑</label><select id="import-mode" aria-label="Import behavior"><option value="inspect">Inspect saved data</option><option value="replay">Recompute request(s)</option></select><button id="capture">Scene + images ↓</button><input type="file" id="import" accept="application/json,.json" class="visually-hidden"></div></header><section class="intro"><div><div class="eyebrow" id="workspace-label"></div><h1 id="title"></h1><p id="description"></p></div><span class="evidence-badge">SCOUT / NOT CERTIFIED</span></section><section class="parameters" aria-label="Experiment parameters"><div id="controls"></div><div class="run-row"><button class="primary" id="run">▶ Run experiment</button><button id="cancel" disabled>Cancel</button><span id="run-status" role="status" aria-live="polite">Ready</span><button id="pin">Pin baseline</button><button id="clear-baseline" hidden>Clear baseline</button></div></section><div id="error" role="alert" hidden></div><div id="artifact-notice" class="source-banner" hidden></div><div id="result"></div><div id="comparison"></div><div id="refinements"></div><section class="notebook"><div><div class="eyebrow">PRESERVE THE QUESTION</div><h2>Experiment notebook</h2><p>Save the request, selection, observation, and result identity. Export includes both compared artifacts and refinements. Import can inspect without recomputing, or explicitly replay.</p><label>Experiment name<input id="experiment-name" maxlength="120" value="First exploration"></label><label>Observation / next question<textarea id="notes" maxlength="12000" placeholder="What caught your attention? Which parameter change would challenge it?"></textarea></label></div><div><h3>Durable local investigations</h3><p>Stored on this machine, independently of the browser. Both comparisons and refinements are retained.</p><div id="shelf"></div><h3>Agent-readable scene</h3><p>The scene describes the displayed result, not uncomputed edits. All values below share its result identity.</p><details><summary>Inspect structured scene</summary><pre id="scene"></pre></details></div></section><footer>No telemetry. No external assets. No arbitrary code execution. <span id="scene-id"></span></footer></main>`;
 document.querySelectorAll('[data-module]').forEach(b=>b.onclick=()=>selectModule(b.dataset.module));
 $('run').onclick=()=>run();$('cancel').onclick=()=>cancel();$('pin').onclick=()=>{if(!state.result)return;state.baseline=state.result;renderResult();};$('clear-baseline').onclick=()=>{state.baseline=null;renderResult();};
 $('experiment-name').oninput=e=>state.name=e.target.value;$('notes').oninput=e=>{state.notes=e.target.value;updateScene();};
 $('save').onclick=()=>save().catch(e=>showError(e.message));$('capture').onclick=()=>download('observatory-scene-capture.json',JSON.stringify(capture()),'application/json');$('export').onclick=()=>download('riemann-experiment.json',JSON.stringify(exportExperiment(),null,2),'application/json');
 $('import').onchange=async e=>{const f=e.target.files[0];if(!f)return;try{if(f.size>16*1024*1024)throw Error('Import is limited to 16 MiB.');const snapshot=JSON.parse(await f.text());await ($('import-mode').value==='replay'?replay(snapshot):inspectArtifact(snapshot));}catch(ex){showError(ex.message);}e.target.value='';};
 renderControls();renderShelf();renderResult();
}
function renderControls(){
 const m=modules[state.request.module];$('title').textContent=m.title;$('description').textContent=m.description;$('workspace-label').textContent='EXPERIMENT / '+m.name.toUpperCase();
 document.querySelectorAll('[data-module]').forEach(b=>b.classList.toggle('active',b.dataset.module===state.request.module));
 $('controls').innerHTML=fields[state.request.module].map(([key,label,type,options])=>`<label>${label}${type==='select'?`<select data-key="${key}" aria-label="${label}">${options.map(v=>`<option value="${v}" ${String(v)===String(state.request[key])?'selected':''}>${esc(objectNames[v]||v)}</option>`).join('')}</select>`:`<input data-key="${key}" type="${type==='number'?'number':'text'}" step="any" aria-label="${label}" value="${esc(state.request[key])}">`}</label>`).join('');
 document.querySelectorAll('[data-key]').forEach(input=>input.onchange=()=>{const field=fields[state.request.module].find(f=>f[0]===input.dataset.key),type=field[2];state.request[input.dataset.key]=type==='csv'?input.value.split(',').map(s=>Number(s.trim())):type==='text'||(type==='select'&&typeof field[3][0]==='string')?input.value:Number(input.value);state.dirty=true;updateStatus('Parameters changed — run to apply.');updateScene();});applyBounds();
}
function applyBounds(){const schema=state.capabilities?.provider_schemas?.[state.request.module];if(!schema)return;document.querySelectorAll('[data-key]').forEach(input=>{const p=schema.properties[input.dataset.key];if(!p)return;if(p.minimum!==undefined)input.min=p.minimum;if(p.maximum!==undefined)input.max=p.maximum;if(p.type==='integer')input.step='1';input.title=p.description||[p.minimum!==undefined?'min '+p.minimum:'',p.maximum!==undefined?'max '+p.maximum:''].filter(Boolean).join(' · ');});}
function updateStatus(message){$('run-status').textContent=message;$('run').disabled=state.busy||state.request.module==='datasets';$('cancel').disabled=!state.busy;$('save').disabled=!state.result;$('export').disabled=!state.result;$('pin').disabled=!state.result;}
function showError(message){state.error=message;$('error').hidden=!message;$('error').textContent=message;}
async function api(path,options={}){const r=await fetch(path,{...options,headers:{'Content-Type':'application/json','X-Observatory-Client':'v0.1',...options.headers}});const b=await r.json();if(!r.ok)throw Error(typeof b.detail==='string'?b.detail:JSON.stringify(b.detail||b));return b;}
async function cancel(){state.generation++;const key=state.job;state.job=null;state.busy=false;if(key){try{await api('/api/jobs/'+key,{method:'DELETE'});}catch(e){showError(e.message);}}updateStatus('Cancelled. The previous displayed result is unchanged.');}
async function run(request=state.request,attach=false){
 if(request.module==='datasets'){renderResult();return;}
 const retainedView=attach?{selection:structuredClone(state.selection),viewports:scene().viewports}:null;
 await cancel();showError('');const generation=++state.generation;const submitted=structuredClone(request);state.busy=true;state.dirty=false;updateStatus('Computing in an isolated worker…');
 let key;
 try{
   const job=await api('/api/jobs',{method:'POST',body:JSON.stringify(submitted)});key=job.job_id;
   if(generation!==state.generation){await api('/api/jobs/'+key,{method:'DELETE'});return;}
   state.job=key;
   while(generation===state.generation){
     const reply=await api('/api/jobs/'+key);
     if(generation!==state.generation)return;
     if(reply.status==='done'){
       if(attach){state.refinements.push(reply.result);state.refinements=state.refinements.slice(-16);}else{state.result=reply.result;state.selection=null;state.refinements=[];}state.artifactNotice='';state.job=null;state.busy=false;
       // Never relabel old results with subsequently edited controls.
       state.dirty=attach?state.dirty:JSON.stringify(submitted)!==JSON.stringify(state.request);
       renderResult();if(retainedView){restoreView(retainedView);updateScene();}updateStatus(`Ready · ${reply.elapsed_seconds}s · ${state.dirty?'controls changed; result uses submitted parameters':'result '+reply.result.result_id.slice(0,10)}`);return reply.result;
     }
     if(reply.status!=='running')throw Error(reply.error||`Computation ${reply.status}.`);
     updateStatus(`Computing · ${reply.elapsed_seconds}s · Cancel is available`);await new Promise(resolve=>setTimeout(resolve,250));
   }
 }catch(e){if(generation===state.generation){state.busy=false;state.job=null;showError(e.message);updateStatus('Not completed. Reduce the workload or correct the parameters.');}}
 finally{if(generation!==state.generation&&key){try{await api('/api/jobs/'+key,{method:'DELETE'});}catch{/* It may already have expired. */}}}
}
async function selectModule(id){await cancel();state.storeDesk?.destroy();state.storeDesk=null;state.datasetScene=null;state.refinements=[];state.artifactNotice='';state.request={module:id,...modules[id].defaults};state.result=null;state.baseline=null;state.selection=null;renderControls();renderResult();if(id==='datasets'){updateStatus('Stored-data mode');return;}await run();}
function card(id,title,description,wide=false){return `<section class="panel ${wide?'wide':''}"><div class="panel-heading"><div><h2>${esc(title)}</h2><p>${esc(description)}</p></div><button data-export-plot="${id}" aria-label="Export ${esc(title)} as PNG">PNG ↓</button></div><div id="${id}" class="plot"></div><div id="${id}-legend" class="legend"></div></section>`;}
function baseline(series){if(!state.baseline||state.baseline.request.module!==state.result.request.module||!state.baseline.series?.length)return series;return [...series,{...state.baseline.series[0],label:`Pinned ${state.baseline.request.function}: ${state.baseline.series[0].label}`,dashed:true,color:'#cad4dd'}];}
function registerCurve(id,series,options={}){const c=new Curve($(id),series,{...options,onView:options.onView||updateScene,onSelect:options.onSelect||(x=>inspectX(x,id,series))});state.plots.push(c);legend($(id+'-legend'),series);return c;}
function renderResult(){
 state.storeDesk?.destroy();state.storeDesk=null;state.lab=null;state.plots.forEach(p=>p.destroy());state.plots=[];$('comparison').replaceChildren();$('refinements').replaceChildren();$('artifact-notice').hidden=!state.artifactNotice;$('artifact-notice').textContent=state.artifactNotice;$('clear-baseline').hidden=!state.baseline;
 if(state.request.module==='datasets'){const generation=state.generation;storedDesk($('result'),{api,plots:state.plots,onScene:v=>{state.datasetScene=v;updateScene();},download,error:showError}).then(d=>{if(generation===state.generation&&state.request.module==='datasets')state.storeDesk=d;else d.destroy();}).catch(e=>showError(e.message));return;}
 const r=state.result;if(!r){$('result').innerHTML='<div class="empty"><span class="empty-symbol">ζ</span><h2>An instrument for asking better questions.</h2><p>Run an experiment to see its field, components, and numerical record.</p></div>';updateScene();return;}
 const q=r.request,s=r.series||[];let panels=labModules[q.module]?labMarkup(r,card):'';
 if(q.module==='geometry')panels=card('field','Phase landscape',objectNames[q.function]+' · sampled grid')+card('primary','Vertical slice',`σ = ${q.sigma}; Hardy Z, when present, stays on σ = 1/2`);
 if(q.module==='primes')panels=card('primary','Counts & main terms','Computed on every integer in the requested prefix')+card('secondary','Counting residuals','Small differences, not overlaid large main terms')+card('tertiary','Prime-power structure','Two normalized Chebyshev residuals',true);
 if(q.module==='euler')panels=card('primary','Accumulating local factors','Horizontal axis is prime cutoff P')+card('secondary','Distance to ζ(s)','This distance is not a rigorous tail bound')+card('tertiary','Argand trajectory','Each vertex is the next partial product; no point decimation',true);
 if(q.module==='mobius')panels=card('primary','Mertens cancellation','Exact M(x), then sample-preserving display reduction')+card('field','Signed interactions',`Complete kernel prefix 1..${q.kernel_n}; not the larger curve prefix`)+card('secondary','Harmonic balance','Signed harmonic source versus total variation',true);
 if(q.module==='zeros')panels=card('primary','Consecutive gaps','Each point uses two indexed, approximate zeros')+card('secondary','Locally normalized gaps','Midpoint local density, explicitly defined below');
 if(q.module==='height')panels=card('primary','Imported fine interval','Axis shows local offsets δ, never the enormous anchor',true);
 $('result').innerHTML=`<div class="result-heading"><div><span class="eyebrow">COMPUTED ARTIFACT</span><span class="hash">${r.result_id.slice(0,12)}</span></div><span>${esc(r.evidence)}</span></div><div class="panel-grid">${panels}</div><div class="detail-grid"><section class="panel"><h2>Numerical inspector</h2><p>Click a chart, cell, or event. Curve values are nearest retained samples, not interpolated evaluations.</p><pre id="inspector">Select a sample to inspect it.</pre><button id="refine-selected" hidden>Refine selected point</button><details><summary>Metrics & exact values</summary><div class="metrics">${Object.entries(r.metrics||{}).map(([k,v])=>`<div><span>${esc(k)}</span><strong>${esc(typeof v==='number'?fmt(v):v)}</strong></div>`).join('')}</div></details></section><section class="panel"><h2>Definition & numerical boundary</h2><div class="formula">${esc(r.formula)}</div>${r.warnings.map(w=>`<p class="warning">${esc(w)}</p>`).join('')}<p class="provider">${esc(r.provider)}<br>${esc(r.precision.working_note)}</p>${state.baseline?`<p class="warning">Pinned baseline ${state.baseline.result_id.slice(0,10)}. Inspect both requests in the structured scene; both artifacts are retained; the comparison panel below uses matched observables.</p>`:''}</section></div><section class="panel event-panel"><h2>Event layer <span class="count">${r.events.length}</span></h2><p>Kept separately from line reduction. Registered events are not a completeness claim.</p><div id="events" class="events"></div></section>`;
 if(labModules[q.module]){state.lab=mountLab(r,{curve:registerCurve,plots:state.plots,select:selectLab,run:request=>window.observatory.run(request),getSelection:()=>state.selection,viewChanged:updateScene});}
 else if(q.module==='geometry'){
   const field=new Field($('field'),r.grid,{onSelect:(col,row)=>inspectCell(col,row)});state.plots.push(field);
   registerCurve('primary',baseline(s),{xlabel:'t',events:r.events});
 }else if(q.module==='primes'){
   registerCurve('primary',baseline(s.slice(0,3)),{xlabel:'x'});registerCurve('secondary',s.slice(3,5),{xlabel:'x'});registerCurve('tertiary',s.slice(5),{xlabel:'x'});
 }else if(q.module==='euler'){
   registerCurve('primary',baseline(s.slice(0,3)),{xlabel:'Prime cutoff P'});registerCurve('secondary',s.slice(3),{xlabel:'Prime cutoff P'});
   const a=r.argand;registerCurve('tertiary',[{label:'E_P(s), in increasing P',points:a.real.map((x,i)=>[x,a.imag[i]]).filter(p=>p[0]!=null&&p[1]!=null)}],{xlabel:'Re E_P',ylabel:'Im E_P'});
 }else if(q.module==='mobius'){
   registerCurve('primary',baseline(s.slice(0,1)),{xlabel:'x'});state.plots.push(new Field($('field'),r.grid,{onSelect:(col,row)=>inspectCell(col,row)}));registerCurve('secondary',s.slice(2),{xlabel:'x'});
 }else if(q.module==='zeros'){
   registerCurve('primary',baseline(s.slice(0,1)),{xlabel:'Zero index n'});registerCurve('secondary',s.slice(1),{xlabel:'Zero index n'});
 }else{
   const e=r.events[0],span=(e.x1-e.x0)*3;
   registerCurve('primary',[{label:'Offset axis only — no Z values',points:[[e.x0-span,0],[e.x1+span,0]]}],{xlabel:'δ in t = T + δ',events:r.events});
   $('inspector').textContent=JSON.stringify(r.metrics,null,2);$('primary-legend').append(document.createTextNode('Anchor T = '+r.record.anchor));
 }
 $('events').replaceChildren();r.events.forEach((e,i)=>{const b=document.createElement('button');b.className='event';b.textContent=e.index?`γ${e.index} · ${e.decimal}`:`[${fmt(e.x0)}, ${fmt(e.x1)}] · ${e.kind}`;b.onclick=()=>{state.selection={kind:'event',index:i,...e};$('inspector').textContent=JSON.stringify(state.selection,null,2);if(q.module==='geometry')state.plots.forEach(p=>p.setSelection((e.x0+e.x1)/2));updateScene();};$('events').append(b);});
 if(!r.events.length)$('events').textContent='No event producer in this workspace. This does not mean no mathematical events exist.';
 renderComparison();renderRefinements();$('refine-selected').onclick=()=>refineSelected();
 document.querySelectorAll('[data-export-plot]').forEach(b=>b.onclick=()=>{const canvas=$(b.dataset.exportPlot).querySelector('canvas');const a=document.createElement('a');a.download=`${q.module}-${b.dataset.exportPlot}-${r.result_id.slice(0,8)}.png`;a.href=canvas.toDataURL();a.click();});
 updateScene();
}
function selectLab(selection){state.selection=selection;if($('inspector'))$('inspector').textContent=JSON.stringify(selection,null,2);updateScene();}
function inspectX(x,id,series){
 const r=state.result;const values=series.map(s=>{const pts=s.points.filter(p=>p[1]!=null);const nearest=pts.reduce((a,b)=>!a||Math.abs(b[0]-x)<Math.abs(a[0]-x)?b:a,null);return {series:s.label,retained_sample:nearest};});
 state.selection={kind:'curve',view:id,x,values};$('inspector').textContent=JSON.stringify(state.selection,null,2);
 if(r.request.module==='geometry')state.plots.forEach(p=>p.setSelection(x));updateScene();
}
function inspectCell(col,row){const g=state.result.grid,k=row*g.n+col;state.selection=g.kind==='complex'?{kind:'sampled grid cell',sigma:g.x[col],t:g.y[row],real:g.real[k],imag:g.imag[k],phase:g.phase[k],log1p_modulus:g.magnitude[k]}:{kind:'signed interaction',m:g.x[col],n:g.y[row],value:g.values[k]};$('inspector').textContent=JSON.stringify(state.selection,null,2);if(g.kind==='complex'){state.plots.forEach(p=>p.setSelection(g.y[row]));$('refine-selected').hidden=false;}updateScene();}
function scene(){const r=state.result;return {schema_version:2,application:'Riemann Observatory 0.4 preview',dataset:state.datasetScene,artifact_notice:state.artifactNotice,refinement_ids:state.refinements.map(r=>r.result_id),result_id:r?.result_id||null,evidence:r?.evidence||'no result',displayed_request:r?.request||null,uncomputed_controls:state.dirty?state.request:null,baseline:state.baseline?{result_id:state.baseline.result_id,request:state.baseline.request}:null,selection:state.selection,formula:r?.formula||null,metrics:r?.metrics||null,views:(r?.series||[]).map(s=>({label:s.label,computed_samples:s.input_count,display_vertices:s.points.length,missing_samples:s.missing_count,contract:s.contract})),viewports:state.plots.map(p=>({id:p.host.id,kind:p instanceof Curve?'curve':'field',x_range:p.view||[p.grid.x[0],p.grid.x.at(-1)],selected_cell:p instanceof Field?p.selection:null})),event_count:r?.events.length||0,notes:state.notes};}
function updateScene(){if(!$('scene'))return;const obj=scene();$('scene').textContent=JSON.stringify(obj,null,2);$('workspace').dataset.sceneId=obj.result_id||'none';$('scene-id').textContent=obj.result_id?'Scene '+obj.result_id.slice(0,12):'';}
function exportExperiment(){
 if(!state.result)throw Error('Compute a result first.');
 return {schema_version:2,name:state.name,notes:state.notes,result:structuredClone(state.result),comparison:structuredClone(state.baseline),refinements:structuredClone(state.refinements),selection:structuredClone(state.selection),viewports:scene().viewports,comparison_view:null};
}
async function save(){
 if(!state.result)return;
 const receipt=await api('/api/investigations',{method:'POST',body:JSON.stringify(exportExperiment())});
 try{localStorage.setItem('observatory-last-investigation',receipt.investigation_id);}catch{/* disk persistence does not depend on browser storage */}
 await renderShelf();updateStatus('Saved to local disk: both artifacts, notes, view and refinements.');return receipt;
}
async function renderShelf(){
 try{const {items}=await api('/api/investigations');$('shelf').replaceChildren();if(!items.length){$('shelf').textContent='No saved investigations yet.';return;}
 for(const item of items){const b=document.createElement('button');b.className='saved-experiment';b.textContent=`${item.name} · ${item.created} ↗`;b.onclick=()=>openInvestigation(item.investigation_id).catch(e=>showError(e.message));$('shelf').append(b);}}
 catch(e){$('shelf').textContent='Store unavailable: '+e.message;}
}
async function openInvestigation(key){const saved=await api('/api/investigations/'+key);await adopt(saved.experiment,saved.trust);return saved;}
async function adopt(snapshot,notice){
 await cancel();state.storeDesk?.destroy();state.datasetScene=null;state.result=snapshot.result;state.baseline=snapshot.comparison||null;state.refinements=snapshot.refinements||[];
 state.request=structuredClone(state.result.request);state.name=String(snapshot.name||'Imported investigation').slice(0,120);state.notes=String(snapshot.notes||'').slice(0,12000);state.selection=null;state.artifactNotice=notice;state.dirty=false;
 $('experiment-name').value=state.name;$('notes').value=state.notes;renderControls();renderResult();restoreView(snapshot);updateScene();updateStatus('Loaded stored artifacts without recomputing.');
}
async function inspectArtifact(snapshot){
 if(snapshot?.schema_version!==2||!snapshot.result)throw Error('Offline inspection expects a v2 result bundle. Choose “Recompute request(s)” for a v1 or request-only experiment.');
 const receipt=await api('/api/investigations',{method:'POST',body:JSON.stringify(snapshot)});await openInvestigation(receipt.investigation_id);await renderShelf();
}
async function replay(snapshot){
 const request=snapshot?.result?.request||snapshot?.request||snapshot;
 if(!request||!modules[request.module]||request.module==='datasets')throw Error('Expected a supported numerical experiment request.');
 const companion=snapshot?.comparison;
 const refinements=snapshot?.refinements||[];
 await cancel();state.request=structuredClone(request);state.name=String(snapshot.name||'Replayed investigation').slice(0,120);state.notes=String(snapshot.notes||'').slice(0,12000);state.result=null;state.baseline=null;state.selection=null;state.datasetScene=null;
 $('experiment-name').value=state.name;$('notes').value=state.notes;renderControls();renderResult();
 // Recompute both requests, not just the currently selected side.
 let newComparison=null;
 if(companion){newComparison=await run(companion.request);if(!newComparison)return;}
 const result=await run(request);if(!result)return;
 state.baseline=newComparison;
 for(const old of refinements){if(old.request?.module==='refine')await run(old.request,true);}
 renderResult();restoreView(snapshot);updateScene();
 const oldId=snapshot?.result?.result_id||snapshot?.result_id;
 if((oldId&&result.result_id!==oldId)||(companion&&newComparison.result_id!==companion.result_id))showError('Recomputed artifact identities differ. Producer versions, environment or numerical data changed; saved originals were not overwritten.');
 return result;
}
function capture(){
 if(state.busy)throw Error('Finish or cancel the computation before capturing a scene.');
 state.plots.forEach(p=>p.draw());
 return {schema_version:1,scene:scene(),images:state.plots.map(p=>({view_id:p.host.id,result_id:state.result?.result_id||null,png_data_url:p.canvas.toDataURL('image/png')}))};
}
function renderComparison(){
 const a=state.baseline,b=state.result;
 if(!a||!b)return;
 const compatible=a.request.module===b.request.module&&a.series?.[0]&&b.series?.[0]&&a.series[0].label===b.series[0].label;
 $('comparison').innerHTML=`<section class="panel comparison-panel"><h2>Preserved experiment comparison</h2><p>Both complete artifacts are exported and stored. The following panels compare their first matching observable; no interpolation or tail estimate is inferred.</p><div class="comparison-requests"><div><h3>Pinned · ${a.result_id.slice(0,10)}</h3><pre>${esc(JSON.stringify(a.request,null,2))}</pre></div><div><h3>Current · ${b.result_id.slice(0,10)}</h3><pre>${esc(JSON.stringify(b.request,null,2))}</pre></div></div>${compatible?`<div class="comparison-plots">${card('compare-left','Pinned observable',a.series[0].label)}${card('compare-right','Current observable',b.series[0].label)}</div>${card('compare-delta','Current − pinned','Only identical retained x coordinates are paired; mismatched samples are not interpolated.')}`:'<p>These artifacts do not expose the same first observable. Their data and requests are retained, but no numerical subtraction is shown.</p>'}</section>`;
 if(compatible){registerCurve('compare-left',[a.series[0]]);registerCurve('compare-right',[b.series[0]]);const map=new Map(a.series[0].points);const points=b.series[0].points.filter(p=>map.has(p[0])).map(([x,y])=>[x,y===null||map.get(x)===null?null:y-map.get(x)]);registerCurve('compare-delta',[{label:'Matched retained-sample difference',points}]);}
}
function renderRefinements(){
 $('refinements').innerHTML=state.refinements.length?`<section class="panel comparison-panel"><h2>Retained point refinements</h2><p>These are separate, source-identified artifacts attached to this investigation.</p>${state.refinements.map(r=>`<details><summary>${esc(r.formula)} · ${r.result_id.slice(0,10)}</summary><pre>${esc(JSON.stringify({evidence:r.evidence,request:r.request,point:r.point},null,2))}</pre></details>`).join('')}</section>`:'';
}
async function refineSelected(){
 const s=state.selection;
 if(!state.result||s?.kind!=='sampled grid cell'){showError('Select a complex grid sample first.');return;}
 return run({module:'refine',function:state.result.request.function,real:s.sigma.toFixed(17),imag:s.t.toFixed(17),dps:80,backend:'mpmath'},true);
}
function restoreView(snapshot){
 for(const view of Array.isArray(snapshot.viewports)?snapshot.viewports.slice(0,24):[]){const plot=state.plots.find(p=>p.host.id===view.id);if(plot instanceof Field&&Array.isArray(view.selected_cell)&&view.selected_cell.length===2&&view.selected_cell.every(v=>Number.isInteger(v)&&v>=0&&v<plot.grid.n)){plot.selection=[...view.selected_cell];plot.draw();}if(!(plot instanceof Curve)||!Array.isArray(view.x_range)||view.x_range.length!==2||!view.x_range.every(Number.isFinite))continue;const [lo,hi]=view.x_range;if(lo>=plot.full[0]&&hi<=plot.full[1]&&hi>lo){plot.view=[lo,hi];plot.draw();}}
 const sel=snapshot.selection;if(!sel||typeof sel!=='object')return;
 if(state.lab){state.lab.restore(sel);return;}
 if(sel.kind==='curve'&&Number.isFinite(sel.x)){const plot=state.plots.find(p=>p.host.id===sel.view);if(plot instanceof Curve&&sel.x>=plot.full[0]&&sel.x<=plot.full[1])plot.pick(sel.x);}
 else if(sel.kind==='event'&&Number.isInteger(sel.index)&&state.result.events[sel.index]){const e=state.result.events[sel.index];state.selection={kind:'event',index:sel.index,...e};$('inspector').textContent=JSON.stringify(state.selection,null,2);}
 else if(state.result.grid){const g=state.result.grid;const col=g.x.indexOf(g.kind==='complex'?sel.sigma:sel.m),row=g.y.indexOf(g.kind==='complex'?sel.t:sel.n);if(col>=0&&row>=0){const field=state.plots.find(p=>p instanceof Field);field.selection=[col,row];field.draw();inspectCell(col,row);}}
}
function download(name,content,type){const url=URL.createObjectURL(new Blob([content],{type}));const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
window.observatory={scene,capture,save,openInvestigation,inspectArtifact,refineSelected,result:()=>structuredClone(state.result),exportExperiment,replay,run:async request=>{if(request){if(!modules[request.module])throw Error('Unknown module');await cancel();state.request={...modules[request.module].defaults,...structuredClone(request)};const same=state.result?.request.module===request.module;state.result=null;if(!same)state.baseline=null;state.datasetScene=null;renderControls();renderResult();}return run();},cancel};
build();
api('/api/health').then(async()=>{state.connected=true;$('connection').textContent='Local engine connected';state.capabilities=await api('/api/capabilities');applyBounds();return run();}).catch(e=>{showError(e.message);$('connection').textContent='Engine unavailable';});
