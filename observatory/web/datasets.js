// Stored samples are queried by ordinal index. Exact coordinates stay in strings.
import {Curve, legend, fmt} from './charts.js';
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export async function storedDesk(host,{api,plots,onScene,download,error}){
 let generation=0,active=true, current=null, curve=null;
 host.innerHTML=`<section class="panel"><h2>Stored-data observatory</h2><p>Import sampled curves once, then query persistent multiresolution summaries. The horizontal coordinate is sample index. Exact anchor + offset strings remain available on inspection.</p><div class="store-controls"><label>Dataset<select id="dataset-select" aria-label="Stored dataset"></select></label><label>First index<input id="dataset-start" type="number" min="0" value="0"></label><label>Stop index (exclusive)<input id="dataset-stop" type="number" value="1000"></label><label>Bucket target<input id="dataset-budget" type="number" min="8" max="1024" value="256"></label><button id="dataset-load">Load viewport</button><button id="dataset-full">Full range</button></div><div class="result-tools"><label class="button" for="dataset-import">Import series JSON ↑</label><input id="dataset-import" type="file" accept=".json,application/json" class="visually-hidden"><button id="dataset-demo">Import 4,096-point adversarial demo</button><button id="dataset-export">Export view manifest</button></div><div id="dataset-status" class="store-status"></div><div id="stored-curve" class="plot"></div><div id="stored-legend" class="legend"></div><h3>Exact selected sample</h3><pre id="stored-inspector">Select a sample to inspect its exact coordinate and original value.</pre><h3>Independent registered events</h3><div id="stored-events" class="events"></div><details><summary>Coverage, gaps and summary contract</summary><pre id="stored-contract"></pre></details></section>`;
 const $=id=>document.getElementById(id);
 let items=[];
 async function refresh(key=null){
   items=(await api('/api/datasets')).items;
   if(!active)return;
   $('dataset-select').innerHTML=items.map(i=>`<option value="${i.dataset_id}">${esc(i.name)} · ${i.sample_count} samples</option>`).join('');
   if(key)$('dataset-select').value=key;
   $('dataset-status').textContent=items.length?'Choose a range, or load the full stored dataset.':'No datasets yet. Import your data or the adversarial demo.';
 }
 async function pick(index){
   const mine=generation,key=current?.dataset.dataset_id;if(!key)return;
   const row=await api(`/api/datasets/${key}/sample/${Math.max(current.start,Math.min(current.stop-1,Math.round(index)))}`);
   if(!active||mine!==generation)return;
   $('stored-inspector').textContent=JSON.stringify(row,null,2);publish(row);
 }
 function publish(selection=null){if(current)onScene({dataset_id:current.dataset.dataset_id,name:current.dataset.name,start:current.start,stop:current.stop,buckets:Number($('dataset-budget').value),anchor:current.dataset.anchor,selection,event_count:current.events.length,gap_count:current.gaps.length,summary_level:current.level});}
 async function load(start=null,stop=null,key=null){
   const mine=++generation,selectedKey=key||$('dataset-select').value;
   if(!selectedKey){error('Import a dataset first.');return;}
   start=start??Number($('dataset-start').value);stop=stop??Number($('dataset-stop').value);
   $('dataset-status').textContent='Querying stored summaries…';
   try{
     const data=await api(`/api/datasets/${selectedKey}/view?start=${start}&stop=${stop}&buckets=${Number($('dataset-budget').value)}`);
     if(!active||mine!==generation)return;
     current=data;$('dataset-select').value=selectedKey;$('dataset-start').value=data.start;$('dataset-stop').value=data.stop;
     if(curve){curve.destroy();const i=plots.indexOf(curve);if(i>=0)plots.splice(i,1);}
     const s=[{label:data.dataset.name,points:data.points}];
     curve=new Curve($('stored-curve'),s,{xlabel:'original sample index',events:data.events.map(e=>({x0:e.index,x1:e.index})),onSelect:index=>pick(index).catch(e=>error(e.message)),onView:()=>{const [lo,hi]=curve.view;load(Math.max(0,Math.floor(lo)),Math.min(data.dataset.sample_count,Math.ceil(hi)+1)).catch(e=>error(e.message));}});plots.push(curve);legend($('stored-legend'),s);
     $('dataset-status').textContent=`${data.finite_count} finite + ${data.missing_count} missing samples · ${data.points.length} vertices · stored level ${data.level} · ${data.raw_rows_read} boundary rows read · signed sum ${fmt(data.signed_sum)}`;
     $('stored-contract').textContent=JSON.stringify({metadata:data.dataset,contract:data.contract,gaps:data.gaps,signed_sum:data.signed_sum,absolute_sum:data.absolute_sum},null,2);
     $('stored-events').replaceChildren();for(const event of data.events){const b=document.createElement('button');b.className='event';b.textContent=`${event.index}: ${event.label} · ${event.status}`;b.onclick=()=>pick(event.index).catch(e=>error(e.message));$('stored-events').append(b);}
     publish();
   }catch(e){if(active&&mine===generation){$('dataset-status').textContent='Viewport was not loaded.';error(e.message);}}
 }
 $('dataset-load').onclick=()=>load();
 $('dataset-full').onclick=()=>{const item=items.find(v=>v.dataset_id===$('dataset-select').value);if(item)load(0,item.sample_count);};
 $('dataset-import').onchange=async e=>{const f=e.target.files[0];if(!f)return;try{if(f.size>24*1024*1024)throw Error('Import is limited to 24 MiB.');$('dataset-status').textContent='Validating and indexing the dataset…';const out=await api('/api/datasets',{method:'POST',body:await f.text()});await refresh(out.dataset_id);await load(0,out.sample_count,out.dataset_id);}catch(ex){error(ex.message);}e.target.value='';};
 $('dataset-demo').onclick=async()=>{try{const count=4096,data={name:'Alternating source, spike, gaps and huge exact anchor',provenance:'Deterministic synthetic UI control; NOT mathematical zero data.',anchor:'763173730199776587433631628770',samples:Array.from({length:count},(_,i)=>({offset:(i/1000000).toFixed(6),value:i>=2047&&i<2050?null:i===3011?75:(i%2?-1:1)})),events:[{index:3011,label:'Injected spike',status:'synthetic control'},{index:2047,label:'Missing interval starts',status:'coverage marker'}]};$('dataset-status').textContent='Building stored summaries…';const out=await api('/api/datasets',{method:'POST',body:JSON.stringify(data)});await refresh(out.dataset_id);await load(0,count,out.dataset_id);}catch(e){error(e.message);}};
 $('dataset-export').onclick=()=>{if(current)download('observatory-dataset-view.json',JSON.stringify({schema_version:1,dataset_id:current.dataset.dataset_id,start:current.start,stop:current.stop,buckets:Number($('dataset-budget').value),dataset:current.dataset},null,2),'application/json');};
 await refresh();
 return {load,destroy:()=>{active=false;generation++;}};
}
