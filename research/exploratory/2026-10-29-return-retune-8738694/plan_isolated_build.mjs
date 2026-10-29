// No-execution import/rebuild plan. Usage: node plan_isolated_build.mjs RETUNE_SRC ACTIVE_SRC IMPORT_PARSER OUTPUT_JSON
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { resolve, join } from 'node:path';
import { pathToFileURL } from 'node:url';
const [retuneArg, activeArg, parserArg, outArg] = process.argv.slice(2);
if (!outArg) throw Error('four positional arguments required');
const root=resolve(retuneArg), active=resolve(activeArg);
const { leanImports }=await import(pathToFileURL(resolve(parserArg)).href);
const hash=b=>createHash('sha256').update(b).digest('hex');
const deps={}, order=[], visiting=new Set(), done=new Set(), retuneHash={}, activeHash={};
function visit(name) {
 if(done.has(name))return;
 if(visiting.has(name))throw Error('cycle '+name);
 visiting.add(name);
 const rel=name.replaceAll('.','/')+'.lean', path=join(root,rel);
 if(!existsSync(path))throw Error('missing source '+name);
 const bytes=readFileSync(path);retuneHash[name]=hash(bytes);
 const reference=join(active,rel);activeHash[name]=existsSync(reference)?hash(readFileSync(reference)):null;
 deps[name]=leanImports(bytes.toString()).filter(x=>x==='Candidate'||x.startsWith('Candidate.')||x==='Submissions'||x.startsWith('Submissions.'));
 for(const d of deps[name])visit(d);
 visiting.delete(name);done.add(name);order.push(name);
}
visit('Candidate.Main');
const changed=order.filter(n=>retuneHash[n]!==activeHash[n]);
const affected=new Set();
for(const n of order)if(changed.includes(n)||deps[n].some(d=>affected.has(d)))affected.add(n);
const payload={status:'dependency plan only; no compilation',root_module:'Candidate.Main',retune_source_root:root,active_source_root:active,reachable_count:order.length,changed_count:changed.length,affected_count:affected.size,changed,affected_build_order:order.filter(n=>affected.has(n)),module_dependencies:Object.fromEntries(order.filter(n=>affected.has(n)).map(n=>[n,deps[n]])),source_sha256:Object.fromEntries(order.map(n=>[n,retuneHash[n]]))};
writeFileSync(outArg,JSON.stringify(payload,null,2)+'\n');
console.log('reachable',order.length,'changed',changed.length,'affected',affected.size,'output',outArg);
