"""Assemble matrix/MATRIX.md + matrix.json from the built world records.
(The workflow assembler was lost to session limits; this inline assembler
replaces it. Mechanical cross-tabulation only, no editorializing.)"""
import json, sys
sys.path.insert(0, '.')
from core.worlds import load_worlds, LADDER, MECHANISMS, validate_world

W = load_worlds('worlds')
W = {k: v for k, v in W.items() if k != 'epstein_pair_data'}
ABBR = {'HOLDS':'H','FAILS':'F','OPEN':'O','CONJECTURAL':'C','NOT_APPLICABLE':'-'}
RAB = {'PROVED_HERE':'p','IMPORTED_THEOREM':'i','EXACT_WITNESS':'w',
       'REFUTED_BY_WITNESS':'r','NON_DIRECTED_NUMERIC':'n',
       'SYNTHETIC_CONTROL':'s','OPEN':'o'}
problems = {k: validate_world(v) for k, v in W.items()}
lines = ["# Cross-world survival/mechanism matrix (as built, 2026-08-30)", "",
         "12 of 13 planned world records built (native_imports lost to session",
         "limits; deferred). Cell = STATUS(rigor): H/F/O/C/- with p=proved-here,",
         "i=imported, w=exact-witness, r=refuted-by-witness, n=numeric, s=synthetic,",
         "o=open. Witness index below. rh_established=false throughout.", ""]
for title, keys in (("Ladder view (#764)", LADDER), ("Mechanism view (#763)", MECHANISMS)):
    lines.append(f"## {title}\n")
    hdr = "| world | " + " | ".join(k.split('_')[0] for k in keys) + " | critical line |"
    lines += [hdr, "|" + "---|" * (len(keys) + 2)]
    for wid in sorted(W):
        w = W[wid]
        blk = w['ladder'] if keys is LADDER else w['mechanisms']
        row = [f"{ABBR[blk[k]['status']]}({RAB[blk[k]['rigor']]})" for k in keys]
        cl = w['critical_line']['status']
        lines.append(f"| {wid} | " + " | ".join(row) + f" | {cl} |")
    lines.append("")
lines.append("## Witness index (every FAILS / REFUTED_BY_WITNESS cell)\n")
for wid in sorted(W):
    w = W[wid]
    for blkname in ('ladder', 'mechanisms'):
        for k, c in w[blkname].items():
            if c['status'] == 'FAILS' or c['rigor'] == 'REFUTED_BY_WITNESS':
                wit = (c.get('witness') or c.get('citation'))[:220].replace('\n',' ')
                lines.append(f"- **{wid}.{k}** [{c['rigor']}]: {wit}")
lines.append("\n## Mechanical ablation cross-tabulation\n")
for m in MECHANISMS:
    holds = [k for k in sorted(W) if W[k]['mechanisms'][m]['status']=='HOLDS']
    fails = [k for k in sorted(W) if W[k]['mechanisms'][m]['status']=='FAILS']
    fails_line_false = [k for k in fails if W[k]['critical_line']['status']=='FALSE']
    holds_line_thm  = [k for k in holds if W[k]['critical_line']['status']=='THEOREM']
    lines.append(f"- **{m}**: HOLDS in {holds or '[]'}; FAILS in {fails or '[]'}; "
                 f"FAILS with line FALSE: {fails_line_false or '[]'}; "
                 f"HOLDS with line THEOREM: {holds_line_thm or '[]'}")
line_thm = [k for k in sorted(W) if W[k]['critical_line']['status']=='THEOREM']
pp_thm = [k for k in line_thm if W[k]['mechanisms']['POSITIVITY_PURITY']['status']=='HOLDS']
lines.append(f"\n- worlds with critical line THEOREM: {line_thm}; of these, "
             f"POSITIVITY_PURITY HOLDS in {pp_thm} — co-occurrence "
             f"{'EXACT (all)' if pp_thm==line_thm else 'PARTIAL'} in this corpus")
lines.append(f"\nValidation problems: " +
             (json.dumps({k:v for k,v in problems.items() if v}) or "none") )
open('matrix/MATRIX.md','w').write("\n".join(lines)+"\n")
json.dump({'worlds': {k: {'ladder': {kk: vv['status'] for kk,vv in v['ladder'].items()},
                          'mechanisms': {kk: vv['status'] for kk,vv in v['mechanisms'].items()},
                          'critical_line': v['critical_line']['status']} for k,v in W.items()},
           'validation_problems': {k:v for k,v in problems.items() if v},
           'rh_established': False}, open('matrix/matrix.json','w'), indent=1)
print("worlds:", len(W), "| validation problems:", {k:len(v) for k,v in problems.items() if v} or "NONE")
print("line THEOREM worlds:", line_thm, "| purity holds in:", pp_thm)
