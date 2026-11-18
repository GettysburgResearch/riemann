"""Independent integer replay of AF RowCert.checkRows, not an enclosure/proof-kernel check.
Usage: python experiments/code/formal_row_check.py /path/to/zeta-23-lean
"""
import pathlib,re,sys,json,hashlib
p=pathlib.Path(sys.argv[1])/'Zeta23/PairCeiling/LawN256.lean';s=p.read_text();block=s.split('encl := [',1)[1].split(']\n  tn',1)[0];rows=[tuple(map(int,x)) for x in re.findall(r'\((\d+),\s*(\d+)\)',block)]
get=lambda n:int(re.search(r'\b'+n+r' := (\d+)',s).group(1))
N,K,tn,td,dn,dd=map(get,['N','K','tn','td','dn','dd'])
assert N>0 and K>0 and td>0 and dd>0 and len(rows)==N
all_ordered=all(l<=h for l,h in rows)
checks=[]
for j,(l,h) in enumerate(rows,1):
 if j<N:checks.extend([abs(N*l-j*K)*td<=tn*K,abs(N*h-j*K)*td<=tn*K])
for vals in zip(*rows):checks.append(abs(2*sum(vals)-K*N)*dd<=dn*2*K*N)
print(json.dumps({'kind':'independent_exact_integer_replay_of_row_checker_only','file_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rows':len(rows),'scale_is_2_pow_140':K==2**140,'positive_sizes_and_matching_length':True,'ordered_intervals':all_ordered,'all_checks_pass':all(checks),'integer_inequality_checks':len(checks),'scope_limit':'Does not establish EnclOK or existence of the advertised marked configuration law; those require external witness and validated trigonometric enclosures. Does not run Lean.'},indent=2))
