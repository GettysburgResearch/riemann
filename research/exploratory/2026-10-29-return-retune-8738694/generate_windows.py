"""Generate altered window declarations in an isolated Return source tree."""
import argparse, hashlib
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--windows',required=True,help='Pristine PR94 Windows.lean')
p.add_argument('--source',required=True,help='Isolated Return source directory')
a=p.parse_args()
b=Path(a.windows).read_bytes()
assert hashlib.sha256(b).hexdigest()=='3d436434bf8a76f2246f12bb942840f33e4d8ce3d2155660e4572dccab15a799'
s=b.decode().replace('import Submissions.arvi_density.Return.Rows.Admission31\n','import Submissions.arvi_density.Return.Rows.Admission31\nimport Submissions.arvi_density.Return.Rows.Admission32\n')
old='''def returnWindow09 : ReturnCountWindow where
 branch := .weakC7
 nonold := by decide
 deltaLo := (51/128:ℝ)
 deltaHi := (27/64:ℝ)
 pLo := (7/16:ℝ)'''
new='''def returnWindow09 : ReturnCountWindow where
 branch := .weakC7
 nonold := by decide
 deltaLo := (397/1000:ℝ)
 deltaHi := (27/64:ℝ)
 pLo := (43/100:ℝ)'''
assert s.count(old)==1
s=s.replace(old,new)
entry='''def returnWindow32 : ReturnCountWindow where
 branch := .capC
 nonold := by decide
 deltaLo := (39/100:ℝ)
 deltaHi := (3971/10000:ℝ)
 pLo := (43/100:ℝ)
 deltaBounds := by norm_num
 pBounds := by norm_num
 certificate := admission32_all
'''
s=s.replace('def returnWindows : List ReturnCountWindow := [',entry+'def returnWindows : List ReturnCountWindow := [')
s=s.replace('returnWindow30,returnWindow31]','returnWindow30,returnWindow31,returnWindow32]')
out=Path(a.source)/'Windows.lean';out.write_text(s)
print('generated',out)
