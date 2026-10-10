#!/usr/bin/env python3
"""Independent marked-subset, removal and dyadic-tail controls."""
from fractions import Fraction as Q
from itertools import combinations
import unittest
from flint import arb,ctx
from exclusion_moments import ExclusionMoments
from exclusion_tail import certify_positive_tail
from verify_horizon_stitch import as_arb
from weighted_moments import normalized_level_bounds

ctx.prec=192

class ExclusionControls(unittest.TestCase):
    def test_marked_prefix_against_direct_products(self):
        limit=40000
        for a in map(Q,['1.1','1.15']):
            engine=ExclusionMoments(a,limit)
            direct={k:([arb(0)]*7,[arb(0)]*7) for k in [2,4,6]}
            counts={k:0 for k in direct}
            def visit(start,product,used,depth):
                if depth in direct:
                    counts[depth]+=1
                    mass=arb(product)**(-as_arb(a));root=arb(product).sqrt()
                    for j in range(7):
                        direct[depth][0][j]+=mass
                        direct[depth][1][j]+=mass*used
                        mass*=root
                if depth==6:return
                for i in range(start,len(engine.labels)):
                    q=engine.labels[i]
                    if product*q>limit:break
                    visit(i+1,product*q,used+arb(q)**(-as_arb(a)),depth+1)
            visit(0,1,arb(0),0)
            self.assertGreater(counts[6],0)
            for level in direct:
                result=engine.marked_cumulative(level,limit)
                for j in range(7):
                    self.assertTrue(result.ordinary[j].overlaps(direct[level][0][j]))
                    self.assertTrue(result.marked[j].overlaps(direct[level][1][j]))

    def test_used_label_identity_and_duplicate_67(self):
        labels=[2,3,5,7,67,67];a=Q('1.15')
        weights=[arb(q)**(-as_arb(a)) for q in labels]
        elementary=[arb(0)]*7; marked=[arb(0)]*7
        elementary[0]=arb(1)
        for k in range(1,7):
            for indices in combinations(range(6),k):
                product=arb(1);used=arb(0)
                for i in indices:product*=weights[i];used+=weights[i]
                elementary[k]+=product;marked[k]+=product*used
        V=sum(weights,arb(0))
        for k in range(1,6):
            self.assertTrue(((V*elementary[k]-marked[k])/(k+1)).overlaps(elementary[k+1]))
        pairs=list(combinations(range(6),2))
        self.assertEqual(sum(labels[i]*labels[j]==4489 for i,j in pairs),1)
        self.assertEqual(sum(labels[i]*labels[j]==134 for i,j in pairs),2)

    def test_kernel_removal_and_marked_kernel_bounds(self):
        m=Q('1.3');a=(m+1)/2;endpoint=40000
        engine=ExclusionMoments(a,endpoint)
        for k in [2,4,6]:
            vector=engine.marked_cumulative(k,endpoint)
            lower,upper=normalized_level_bounds(m,endpoint,vector.marked)
            self.assertTrue(bool(lower>0));self.assertTrue(bool(upper>lower))
        for n,q,x in [(1,2,2),(2,3,6),(67,67,4489),(30,11,10000)]:
            left=(4*(arb(x)/(n*q)).sqrt()-3)**as_arb(m)/arb(q).sqrt()
            right=(4*(arb(x)/n).sqrt()-3)**as_arb(m)*arb(q)**(-as_arb(a))
            self.assertTrue(bool(left<right))

    def test_dyadic_cap_and_rejection_guards(self):
        # Positive quadratic centered in the domain; Bernstein subdivision
        # is needed even though the polynomial itself is strictly positive.
        n=10000000;cap=(1/arb(n).sqrt()).upper();center=cap/2
        polynomial=[center**2+cap**2/100,-2*center,arb(1)]
        result=certify_positive_tail(polynomial,n)
        self.assertGreater(result['bernstein_leaf_count'],1)
        for leaf in result['leaves']:
            for value in leaf['z_interval']:
                self.assertTrue(arb(value).is_exact())
        with self.assertRaises(ValueError):certify_positive_tail([arb(-1)],n,max_depth=1)
        engine=ExclusionMoments(Q('1.15'),100)
        with self.assertRaises(ValueError):engine.marked_cumulative(3,100)
        with self.assertRaises(ValueError):engine.marked_cumulative(2,101)

if __name__=='__main__':unittest.main()
