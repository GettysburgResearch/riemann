#!/usr/bin/env python3
"""Run the actual-chain and dependency regressions; no network or research code.

Default also checks both complete pinned historical registries and all current
integration decisions. --fixture-only is explicitly narrower and never emits
an actual-registry or full-checkout PASS.
"""
from __future__ import annotations
import argparse
import copy
import importlib.util
import json
import ntpath
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m

v=module('graph_resolver',HERE.parent/'validate.py')
h=module('source_hardening',HERE.parent/'hardening/verify.py')
F=v.load(HERE/'actual_chain.json')
A='API.CONJUNCTIVE.SPARSITY_ENERGY'
N='OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS'
M='API.MELLIN.SUBPOWER_NEGATIVE_MASS'


def unsafe_closure(claims,edges):
    # The pre-fix closure, including the old status-only edge interpretation.
    reach={r['semantic_id'] for r in claims if r['final_verdict'] in v.PROVEN
           and not r['semantic_id'].startswith('OPEN.') and r['semantic_id']!='RH'}
    while True:
        previous=set(reach)
        for e in edges:
            if e['final_verdict'] in v.RELATIONS and set(json.loads(e['premise_ids']))<=reach:
                reach.add(e['conclusion_id'])
        if reach==previous:return reach


def claim(name,status='VERIFIED'):
    return {'semantic_id':name,'source_claim_id':'','final_verdict':status}


def edge(name,ps,target,missing='',kind='HYPEREDGE',status='CONDITIONAL_EXACT'):
    return {'edge_id':name,'premise_ids':json.dumps(ps),'conclusion_id':target,
            'first_missing_premise':missing,'edge_type':kind,'final_verdict':status}


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.cs=copy.deepcopy(F['claims']);self.es=copy.deepcopy(F['edges'])

    def test_actual_chain_reproduces_old_false_path(self):
        self.assertIn(N,unsafe_closure(self.cs,self.es))
        self.assertIn('RH',unsafe_closure(self.cs,self.es))

    def test_actual_chain_repaired_in_both_views(self):
        cs,es,r=v.resolve(self.cs,self.es,[])
        for key in ('base_reachable_ids','current_reachable_ids'):
            self.assertIn(A,r[key]);self.assertIn(M,r[key])
            self.assertNotIn(N,r[key]);self.assertNotIn('RH',r[key])
        self.assertFalse(es[0]['current_traversable'])
        self.assertTrue(es[1]['current_traversable'])
        self.assertIn('NOT_AN_APPLICATION_EDGE',json.loads(es[0]['current_block_reasons']))
        self.assertIn('UNRESOLVED_SELF_DEPENDENCY',json.loads(es[0]['current_block_reasons']))
        self.assertEqual(es[0]['historical_premise_ids'],self.es[0]['premise_ids'])
        self.assertIn(N,json.loads(es[0]['premise_ids']))
        self.assertEqual(cs[2]['final_verdict'],'OPEN_SUFFICIENT_FOR_RH')

    def test_source_records_remain_unchanged(self):
        v.resolve(self.cs,self.es,[])
        self.assertEqual(self.cs,F['claims']);self.assertEqual(self.es,F['edges'])

    def test_verified_api_is_still_not_an_application(self):
        self.es[0]['final_verdict']='VERIFIED'
        self.assertNotIn(N,v.resolve(self.cs,self.es,[])[2]['current_reachable_ids'])

    def test_cleared_missing_column_does_not_activate_api(self):
        self.es[0]['first_missing_premise']=''
        self.assertNotIn(N,v.resolve(self.cs,self.es,[])[2]['current_reachable_ids'])

    def test_retyping_api_does_not_drop_missing_estimate(self):
        self.es[0]['edge_type']='HYPEREDGE'
        self.assertNotIn(N,v.resolve(self.cs,self.es,[])[2]['current_reachable_ids'])

    def test_retyping_and_deleting_premise_still_triggers_rh_guard(self):
        self.es[0]['edge_type']='HYPEREDGE';self.es[0]['first_missing_premise']=''
        with self.assertRaisesRegex(ValueError,'reviewed-only graph reaches RH'):
            v.resolve(self.cs,self.es,[])

    def test_missing_premise_is_conjunctive_not_comment(self):
        cs=[claim('FACT'),claim('API'),claim('OPEN.P','OPEN_SUFFICIENT_FOR_RH'),
            claim('OPEN.Q','OPEN_SUFFICIENT_FOR_RH'),claim('TARGET','GAP_BLOCKED'),F['claims'][0]]
        es=[edge('one',['FACT'],'OPEN.P'),edge('apply',['API'],'TARGET','OPEN.P|OPEN.Q')]
        c,e,r=v.resolve(cs,es,[])
        self.assertIn('OPEN.P',r['current_reachable_ids'])
        self.assertNotIn('TARGET',r['current_reachable_ids'])
        self.assertEqual(json.loads(e[1]['premise_ids']),['API','OPEN.P','OPEN.Q'])
        es.append(edge('two',['FACT'],'OPEN.Q'))
        self.assertIn('TARGET',v.resolve(cs,es,[])[2]['current_reachable_ids'])

    def test_real_implication_may_derive_an_open_label(self):
        cs=[claim('FACT'),claim('OPEN.NEW','OPEN_SUFFICIENT_FOR_RH'),F['claims'][0]]
        result=v.resolve(cs,[edge('proof',['FACT'],'OPEN.NEW')],[])[2]
        self.assertIn('OPEN.NEW',result['current_reachable_ids'])

    def test_closure_does_not_hide_rh(self):
        cs=[claim('FACT'),F['claims'][0]];es=[edge('bad',['FACT'],'RH')]
        self.assertIn('RH',v.graph_closure(cs,v.typed_edges(cs,es)))
        with self.assertRaisesRegex(ValueError,'reviewed-only graph reaches RH'):
            v.resolve(cs,es,[])

    def test_cycle_cannot_bootstrap_unproved_nodes(self):
        cs=[claim('X','GAP_BLOCKED'),claim('Y','GAP_BLOCKED'),F['claims'][0]]
        es=[edge('xy',['X'],'Y'),edge('yx',['Y'],'X')]
        self.assertEqual(v.resolve(cs,es,[])[2]['current_reachable_ids'],[])

    def test_blocked_current_node_cannot_reenter_by_implication(self):
        cs=[claim('FACT'),claim('TARGET'),F['claims'][0]]
        es=[edge('e',['FACT'],'TARGET')]
        d=[{'id':'test','base_semantic_ids':['TARGET'],'base_source_claims':[],
            'block_original_graph_use':True,'correction':'blocked','evidence':[]}]
        result=v.resolve(cs,es,d)[2]
        self.assertIn('TARGET',result['base_reachable_ids'])
        self.assertNotIn('TARGET',result['current_reachable_ids'])

    def test_structural_use_does_not_inhabit_conditional_api(self):
        cs=[claim('AMPLITUDE'),claim('API','CONDITIONAL_EXACT'),F['claims'][0]]
        es=[edge('struct',['AMPLITUDE'],'API','API','STRUCTURAL_USE')]
        self.assertNotIn('API',v.resolve(cs,es,[])[2]['current_reachable_ids'])

    def test_unknown_edge_type_is_rejected(self):
        self.es[0]['edge_type']='NEW_TYPE'
        with self.assertRaisesRegex(ValueError,'unknown or absent edge type'):v.resolve(self.cs,self.es,[])

    def test_missing_edge_type_is_rejected(self):
        del self.es[0]['edge_type']
        with self.assertRaisesRegex(ValueError,'unknown or absent edge type'):v.resolve(self.cs,self.es,[])

    def test_dangling_hidden_prerequisite_is_rejected(self):
        self.es[0]['first_missing_premise']='UNKNOWN'
        with self.assertRaisesRegex(ValueError,'missing prerequisite'):v.resolve(self.cs,self.es,[])

    def test_dangling_explicit_prerequisite_is_rejected(self):
        self.es[0]['premise_ids']='["UNKNOWN"]'
        with self.assertRaisesRegex(ValueError,'dangling inherited endpoint'):v.resolve(self.cs,self.es,[])

    def test_empty_premise_list_is_rejected(self):
        self.es[0]['premise_ids']='[]'
        with self.assertRaisesRegex(ValueError,'bad inherited hyperedge'):v.resolve(self.cs,self.es,[])

    def test_duplicate_edges_are_rejected(self):
        self.es.append(copy.deepcopy(self.es[0]))
        with self.assertRaisesRegex(ValueError,'duplicate inherited edge'):v.resolve(self.cs,self.es,[])

    def test_duplicate_premises_are_rejected(self):
        self.es[0]['premise_ids']=json.dumps([A,A])
        with self.assertRaisesRegex(ValueError,'duplicate inherited premise'):v.resolve(self.cs,self.es,[])

    def test_bad_missing_declarations_are_rejected(self):
        for bad in (True,None,'|'+N,N+'|',N+'|'+N):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                es=copy.deepcopy(self.es);es[0]['first_missing_premise']=bad
                v.resolve(self.cs,es,[])

    def test_false_relation_not_rehabilitated(self):
        self.es[1]['final_verdict']='FALSE'
        self.assertFalse(v.resolve(self.cs,self.es,[])[1][1]['current_traversable'])

    def test_untyped_edges_cannot_be_passed_to_closure(self):
        with self.assertRaisesRegex(ValueError,'requires a typed edge'):v.graph_closure(self.cs,self.es)

    def test_windows_link_lookup_uses_git_posix_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'docs').mkdir()
            texts={'docs/start.md':'# Start\n[Read](../README.md#hello)\n', 'README.md':'# Hello\n'}
            tree={}
            for name,text in texts.items():
                (root/name).write_bytes(text.encode('utf-8'))
                tree[name]=('100644','blob',h.blob(text.encode()))
            # Simulate Windows path normalization without claiming a Windows run.
            with mock.patch.object(h.os,'path',ntpath):
                report=h.check_links(root,tree,('docs/start.md',))
            self.assertEqual(report['local_links_and_anchors'],1)


def check_actual_registries():
    records=[]
    for prefix,count in (('claims',139),('edges',36)):
        path=ROOT/F[prefix+'_path']
        v.require(v.blob(path.read_bytes())==F[prefix+'_blob'],'actual historical '+prefix+' blob mismatch')
        _,data=v.rows(path);v.require(len(data)==count,'actual '+prefix+' row count')
        index={r['semantic_id' if prefix=='claims' else 'edge_id']:r for r in data}
        for row in F[prefix]:
            key=row['semantic_id' if prefix=='claims' else 'edge_id']
            v.require(all(index[key][k]==value for k,value in row.items()),'actual chain projection drift: '+key)
        records.append(data)
    cs,es=records
    v.require('RH' in unsafe_closure(cs,es),'historical real-data counterexample no longer reproduced')
    decisions=v.load(ROOT/'integration/2026-09-06/DECISIONS.json')
    _,fixed,report=v.resolve(cs,es,decisions)
    v.require(N not in report['base_reachable_ids'] and N not in report['current_reachable_ids'],
              'open native estimate was manufactured')
    api=next(e for e in fixed if e['edge_id']=='EDGE.CONJ.SPARSITY_ENERGY')
    v.require(not api['current_traversable'],'API promotion survived')
    return {'claims':len(cs),'edges':len(es),'decisions':len(decisions),
            'historical_literal_false_rh_path_reproduced':True,
            'base_reachable':report['base_reachable'],'current_reachable':report['current_reachable'],
            'reviewed_only_path_to_rh':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fixture-only',action='store_true')
    args=parser.parse_args()
    result=unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromTestCase(GraphTests))
    if not result.wasSuccessful():return 1
    actual=None if args.fixture_only else check_actual_registries()
    print(json.dumps({'marker':'PASS_ACTUAL_CHAIN_FIXTURE_SCOPE' if args.fixture_only else 'PASS_PINNED_ACTUAL_GRAPH_REGRESSION',
        'tests':result.testsRun,'actual_registries':actual,'whole_checkout_validated':False,
        'native_windows_execution':sys.platform=='win32','rh_proved':False},sort_keys=True,indent=2))
    return 0

if __name__=='__main__':sys.exit(main())
