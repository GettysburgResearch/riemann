#!/usr/bin/env python3
"""Finite arithmetic and editorial checks; not an analytic-proof verifier.

Run with Python 3.10+: python -I -S -B verify_paper.py
No repository checkout, network, third-party Python package, or assertion
statement is needed. All acceptance guards remain active under python -O.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
import json
import re

ROOT = Path(__file__).resolve().parent
checks: list[str] = []

def require(ok: bool, name: str) -> None:
    if not ok:
        raise RuntimeError("FAILED: " + name)
    checks.append(name)

def density_df(s: F) -> F:
    q = 2*s-1
    if s <= F(2,3):
        delta = q/(4-6*q)
    elif s <= F(11,12):
        delta = q*(36*q-6*(6*s-2)+3)/(36*q*(3-2*s)-24*s+2)
    else:
        delta = (8*s*s-10*s+3)/(1-24*(1-s)**2)
    return 1-delta

def density_fourth(s: F) -> F:
    return (468*s*s-741*s+271)/(6*(36*s*s-75*s+31))

def comparison(kappa: F) -> dict[str, F]:
    delta, x, alpha, a = F(7,18), F(1,2), F(5,6), F(25,36)
    c = 2/(3*kappa)
    D, P = 3-(1+c)*x, (2-c*x)*(1-x)
    J = (alpha-delta)*D+delta*P
    t = 1+delta*P/(2*J)
    r = ((2-c*x)*t-x*(1-c/2))/D
    m = t-r
    R = 1-delta+(alpha-delta)*delta*P/(2*J)
    def e(b: F, ell: F) -> F:
        ly, h = (1+b-ell)/2, (1+b+3*ell)/2
        return a-a*ly-ell/2+x*delta*ell+h*(R+delta/2-F(1,6))-F(87,100)
    eb, el = e(F(1),F(0))-e(F(0),F(0)), e(F(0),F(1))-e(F(0),F(0))
    l0 = F(14,75)
    emin = e(1-l0,l0)
    require(eb <= 0 and el-eb >= 0, f"triangle_nonnegative_coefficients_{kappa}")
    require(emin > F(1,40), f"positive_model_gap_{kappa}")
    return dict(t=t,r=r,m=m,zM=(1-r)/2,zS=(1-2*m)/(6*kappa),R=R,Eb=eb,El=el,Emin=emin)

def main() -> None:
    a,h,theta=F(21,50),F(29,50),F(21,100)
    margins=[]
    for j in range(850):
        s=F(63,100)+F(j,2500)
        tau=s+F(1,2500)
        g=density_fourth(s) if F(7,10)<=s<=F(9,10) else density_df(s)
        margin=theta-(h*(2*tau+g)+a-F(3,2))
        require(margin>0,f"middle_class_{j}")
        margins.append(margin)
    require(min(margins)==F(96266833,858608062500),"exact_middle_margin")
    require(margins.index(min(margins))==411,"exact_binding_middle_index")
    require(density_fourth(F(3,4))==F(43,60),"selected_fourth_density")
    require(F(5,6)+a/6==F(271,300),"mellin_boundary_arithmetic")
    old=comparison(F(3,4)); relaxed=comparison(F(37,50))
    require(tuple(old[k] for k in ('t','r','m','zM','zS','R')) ==
            (F(443,394),F(141,197),F(161,394),F(28,197),F(8,197),F(2363,3546)),"old_witness_tuple")
    require(old['Emin']==F(7003,265950),"old_minimum")
    require(relaxed['R']==F(2075,3114) and relaxed['Emin']==F(6139,233550),"relaxed_minimum")
    require(F(2075,3114)-F(214,337)==F(32879,1049418),"missing_count_saving")
    ranges={}
    for s,root,squared in [(F(3,4),F(1,4),F(1,6)),(F(5,6),F(2,5),F(3,10))]:
        rr=(s-F(1,2))/(F(5,2)-2*s)
        sr=(s-F(1,2))/((5-4*s)*(F(3,2)-s))
        require(rr==root and sr==squared,f"growing_mollifier_ranges_{s}")
        ranges[str(s)]={'root':str(rr),'squared':str(sr)}
    require(2-2*F(13,84)==F(71,42),"pointwise_to_tail_exponent")
    require(F(84,71)*F(71,42)==2,"complete_frequency_cutoff")
    r=F(2323,50000)
    require(r-r*r/9-F(4621,100000)==F(228671,22500000000),"negative_edge_variance_barrier")
    rho=F(1,10**50)
    rounded=[('direct22','1.155e-92','2.320e-38'),('direct24','1.518e-90','5.857e-37'),('direct26','1.194e-87','8.859e-35'),('incremental24','4.499e-90','1.749e-36'),('incremental26','1.231e-87','9.236e-35')]
    for name,beta,L in rounded:
        require(F(L)<1 and F(beta)+F(L)*rho<rho,"rounded_Banach_budget_"+name)
    require((1+F(1,3)/(2-F(3,2)))/2==F(5,6),"conditional_recurrence_fixed_point")
    require(F(5,2)-2*F(5,6)==F(5,6),"quadratic_family_scale_5_6")
    require(F(5,2)-2*F(1,2)==F(3,2),"quadratic_family_scale_RH")
    require(min(F(1,10),F(1,6),F(4,15)-F(1,6))==F(1,10),"second_inverse_cap_error_1_6")
    require(min(F(1,10),F(1,4),F(4,15)-F(1,4))==F(1,60),"second_inverse_cap_error_1_4")
    texfiles=[ROOT/'main.tex']+sorted((ROOT/'sections').glob('*.tex'))
    text='\n'.join(p.read_text(encoding='utf-8') for p in texfiles)
    labels=re.findall(r'\\label\{([^}]+)\}',text)
    require(len(labels)==len(set(labels)),"unique_labels")
    references=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',text)
    require(set(references)<=set(labels),"resolved_cross_references")
    citations=[]
    for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',text):
        citations.extend(group.split(','))
    bbl=(ROOT/'main.bbl').read_text(encoding='utf-8')
    bibkeys=re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',bbl)
    require(len(bibkeys)==len(set(bibkeys)),"unique_bibliography_keys")
    require(set(citations)<=set(bibkeys),"resolved_citations")
    require(set(bibkeys)==set(re.findall(r'@\w+\{([^,]+),',(ROOT/'references.bib').read_text())),"bib_bbl_key_agreement")
    for include in re.findall(r'\\input\{([^}]+)\}',text):
        file=ROOT/include
        if not file.suffix:
            file=file.with_suffix('.tex')
        require(file.is_file(),"local_include_"+include)
    lock=json.loads((ROOT/'SOURCE_LOCK.json').read_text())
    require(len(lock['sources'])==26,"twenty_six_frozen_research_sources")
    for source in lock['sources']:
        require(bool(re.fullmatch('[0-9a-f]{40}',source['commit'])),"source_pin_"+str(source['pr']))
        require(source['commit'] in bbl,"source_pin_linked_"+str(source['pr']))
    require('arXiv submission' in text and 'No independent mathematical referee' in text,"review_and_submission_boundary")
    require(r'\pagestyle{plain}' in text, 'page_number_only_headers')
    require('Gettysburg Research' in text and 'Agentic Polymath project' in text, 'project_credit')
    main_source=(ROOT/'main.tex').read_text()
    require(main_source.count('Gideon Freund')==2, 'name_only_author_and_pdf_metadata')
    require('Gideon Freund' not in '\n'.join(p.read_text() for p in (ROOT/'sections').glob('*.tex')), 'no_author_name_in_body_or_running_headers')
    require(main_source.index('GPT 6 Pro')>main_source.index(r'\input{main.bbl}'), 'named_AI_acknowledgment_at_end')
    require(F(11,12)-F(6267001,37500000)/4==F(43744333,50000000), 'conditional_1005_boundary')
    require(F(8748867,10000000)-F(43744333,50000000)==F(1,25000000), 'conditional_1005_gain')
    require((1+F(29991,40000))/2==F(69991,80000), 'preceding_stage_license_arithmetic')
    stages=[(F(13,20),F(37,120),F(23,24)), (F(35,54),F(5,18),F(25,27)),
      (F(2,3),F(1,4),F(11,12)), (F(17,25),F(23,100),F(91,100)),
      (F(41,60),F(9,40),F(109,120)),(F(15,22),F(5,22),F(10,11)),
      (F(37,54),F(2,9),F(49,54))]
    for shift,power,boundary in stages:
        require(shift+power==boundary,'historical_mellin_'+str(boundary))
    require(F(8,11)-F(43,60)==F(7,660),'fourth_density_gain')
    for T in (3,5,10,100):
        v,B=F(1,20),F(1,2)
        u=(T*T-B*B)/(v*(T*T+B*B)**2)
        y=-2*T*B/(v*(T*T+B*B)**2)
        require(4*y*y==16*T*T*B*B/(v*v*(T*T+B*B)**4),'finite_pair_mass_'+str(T))
        require(u>0 and y*y<=u*u,'finite_pair_envelope_'+str(T))
    report={'status':'PASS','finite_predicates':len(checks),'middle_classes':850,
      'minimum_middle_margin':str(min(margins)),'binding_middle_index':411,
      'failed_087_old_minimum':str(old['Emin']),'failed_087_relaxed_minimum':str(relaxed['Emin']),
      'mollifier_ranges':ranges,'rounded_certificate_budgets_checked':5,
      'latex_files':len(texfiles),'labels':len(labels),'bibliography_entries':len(bibkeys),
      'source_pins':len(lock['sources']),'infinite_proofs_verified':False,'theta_source_rebuilt':False,
      'new_zero_free_region_proved_by_revision':False,'conditional_1005_claim_reported':True,'arxiv_submitted':False}
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
