#!/usr/bin/env python3
"""Patch the reference producer to use one correctly-rounded MPFR call.

The reference implementation evaluates each exact-input log/sqrt twice and
sine/cosine twice per direction.  This script replaces those helpers by:

- one correctly rounded nearest log or square root, bracketed by its immediate
  predecessor and successor;
- one correctly rounded `mpfr_sin_cos` value at the phase midpoint, bracketed by
  immediate neighbors and then widened by the rigorous phase radius.

Each replacement still contains the exact elementary-function value.  Its
midpoint-Lipschitz sine/cosine enclosure need not contain the reference
implementation's different over-enclosure, so cross-backend intervals are
expected to overlap around the exact value but are not asserted to be nested.
The replacement substantially reduces special-function work.
"""
from pathlib import Path
import argparse

LOG = r'''static void logiv(iv*o,const iv*a){if(mpfr_cmp(a->lo,a->hi)!=0){fprintf(stderr,"logiv requires exact input\n");exit(2);}mpfr_log(tmpv[15],a->lo,MPFR_RNDN);mpfr_set(o->lo,tmpv[15],MPFR_RNDN);mpfr_nextbelow(o->lo);mpfr_set(o->hi,tmpv[15],MPFR_RNDN);mpfr_nextabove(o->hi);}'''
SQRT = r'''static void sqrtiv(iv*o,const iv*a){if(mpfr_cmp(a->lo,a->hi)!=0){fprintf(stderr,"sqrtiv requires exact input\n");exit(2);}mpfr_sqrt(tmpv[15],a->lo,MPFR_RNDN);mpfr_set(o->lo,tmpv[15],MPFR_RNDN);mpfr_nextbelow(o->lo);mpfr_set(o->hi,tmpv[15],MPFR_RNDN);mpfr_nextabove(o->hi);}'''
SINCOS = r'''static void sincosiv(iv*s,iv*c,const iv*x){mpfr_add(tmpv[8],x->lo,x->hi,MPFR_RNDN);mpfr_div_2ui(tmpv[8],tmpv[8],1,MPFR_RNDN);mpfr_sub(tmpv[9],tmpv[8],x->lo,MPFR_RNDU);mpfr_sub(tmpv[14],x->hi,tmpv[8],MPFR_RNDU);if(mpfr_cmp(tmpv[14],tmpv[9])>0)mpfr_set(tmpv[9],tmpv[14],MPFR_RNDU);mpfr_sin_cos(tmpv[10],tmpv[12],tmpv[8],MPFR_RNDN);mpfr_set(tmpv[11],tmpv[10],MPFR_RNDN);mpfr_nextbelow(tmpv[10]);mpfr_nextabove(tmpv[11]);mpfr_sub(s->lo,tmpv[10],tmpv[9],MPFR_RNDD);mpfr_add(s->hi,tmpv[11],tmpv[9],MPFR_RNDU);mpfr_set(tmpv[13],tmpv[12],MPFR_RNDN);mpfr_nextbelow(tmpv[12]);mpfr_nextabove(tmpv[13]);mpfr_sub(c->lo,tmpv[12],tmpv[9],MPFR_RNDD);mpfr_add(c->hi,tmpv[13],tmpv[9],MPFR_RNDU);if(mpfr_cmp_si(s->lo,-1)<0)mpfr_set_si(s->lo,-1,MPFR_RNDD);if(mpfr_cmp_si(s->hi,1)>0)mpfr_set_si(s->hi,1,MPFR_RNDU);if(mpfr_cmp_si(c->lo,-1)<0)mpfr_set_si(c->lo,-1,MPFR_RNDD);if(mpfr_cmp_si(c->hi,1)>0)mpfr_set_si(c->hi,1,MPFR_RNDU);}'''

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('source',type=Path)
    parser.add_argument('output',type=Path)
    args=parser.parse_args()
    lines=args.source.read_text().splitlines()
    found={'log':False,'sqrt':False,'sincos':False}
    out=[]
    for line in lines:
        if line.startswith('static void logiv('): out.append(LOG); found['log']=True
        elif line.startswith('static void sqrtiv('): out.append(SQRT); found['sqrt']=True
        elif line.startswith('static void sincosiv('): out.append(SINCOS); found['sincos']=True
        else: out.append(line)
    if not all(found.values()): raise SystemExit(f'missing replacement target: {found}')
    args.output.write_text('\n'.join(out)+'\n')
if __name__=='__main__': main()
