from __future__ import annotations
import math
import unittest
from run import first_ca_numbers, segmented_primes, scan_ca_transitions, simple_primes, transition_boundary

class PrimeGenerationTests(unittest.TestCase):
    def test_simple_and_segmented_sieves_agree(self):
        expected=[2,3,5,7,11,13,17,19,23,29]
        self.assertEqual(simple_primes(30), expected)
        self.assertEqual(list(segmented_primes(30, segment_odds=3)), expected)
    def test_edges(self):
        self.assertEqual(list(segmented_primes(1)), [])
        self.assertEqual(list(segmented_primes(2)), [2])
        self.assertEqual(list(segmented_primes(3)), [2,3])
        self.assertEqual(list(segmented_primes(4)), [2,3])

class TransitionTests(unittest.TestCase):
    def test_boundary_decreases_with_exponent(self):
        for p in (2,3,5,97):
            xs=[transition_boundary(p,a) for a in range(1,8)]
            self.assertTrue(all(x>y>0 for x,y in zip(xs,xs[1:])))
    def test_boundary_decreases_with_prime(self):
        xs=[transition_boundary(p,1) for p in simple_primes(200)]
        self.assertTrue(all(x>y for x,y in zip(xs,xs[1:])))
    def test_initial_ca_sequence(self):
        expected=[2,6,12,60,120,360,2520,5040,55440,720720,1441440,4324320,
                  21621600,367567200,6983776800,160626866400,321253732800,
                  9316358251200,288807105787200,2021649740510400,
                  6064949221531200,224403121196654400]
        self.assertEqual(first_ca_numbers(len(expected), prime_limit=100), expected)

class ScanTests(unittest.TestCase):
    def test_small_scan(self):
        result=scan_ca_transitions(10_000, top_k=5, segment_odds=127)
        self.assertEqual(result.status, "EMPIRICAL")
        self.assertEqual(result.prime_count, len(simple_primes(10_000)))
        self.assertEqual(result.distinct_primes, result.prime_count)
        self.assertEqual(result.near_ties, [])
        self.assertIsNotNone(result.best_ratio)
        self.assertLess(result.best_ratio, 1.0)
        self.assertGreater(result.log_n, math.log(5040))
        self.assertEqual(len(result.top_events), 5)

    def test_stream_matches_naive_event_sort(self):
        p_max=2_000
        b_min=transition_boundary(p_max,1)
        events=[]
        for p in simple_primes(p_max):
            for a in range(1,64):
                boundary=transition_boundary(p,a)
                if boundary < b_min:
                    break
                events.append((boundary,p,a))
        events.sort(reverse=True)
        exponents={}
        log_n=0.0
        log_i=0.0
        best=-1.0
        for boundary,p,a in events:
            self.assertEqual(a,exponents.get(p,0)+1)
            exponents[p]=a
            log_p=math.log(p)
            log_n += log_p
            x=math.exp(-a*log_p)
            log_i += math.log1p(-x/p)-math.log1p(-x)
            if log_n > math.log(5040):
                ratio=math.exp(log_i)/(math.exp(0.5772156649015328606)*math.log(log_n))
                best=max(best,ratio)
        streamed=scan_ca_transitions(p_max,top_k=3,segment_odds=31)
        self.assertEqual(streamed.event_count,len(events))
        self.assertEqual(streamed.best_ratio,best)

if __name__ == "__main__": unittest.main()
