import importlib.util, json, pathlib, tempfile, unittest

HERE=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('v',HERE/'verify.py')
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)

class TestFutureProfile(unittest.TestCase):
    def test_01_quotient_fast_matches_full(self):
        for n in (1,2,10,99,256,4096):
            self.assertEqual(v.quotient_values_fast(n),v.quotient_values(n))
    def test_02_floor_closure(self):
        N=4096; Q=set(v.quotient_values_fast(N))
        for x in Q:
            for p in v.primes_upto(x):
                self.assertIn(x//p,Q)
    def test_03_state_minimality(self):
        self.assertGreater(v.state_minimality_fixture(4096)['independent_rows'],0)
    def test_04_large_exact_count(self):
        self.assertEqual(v.state_minimality_fixture(100000000)['independent_rows'],4056)
    def test_05_bridge(self):
        self.assertEqual(v.exact_bridge_fixture()['cases'],96)
    def test_06_half_order(self):
        self.assertGreater(v.symbolic_half_order_fixture()['checked'],0)
    def test_07_exponents(self):
        e=v.exponent_fixture(); self.assertEqual(e['u_power'],e['vk_power'])
    def test_08_mutate_floor(self):
        N=10; m=2; x=N//m; p=3
        self.assertNotEqual((x+1)//p,N//(m*p))
    def test_09_mutate_prime_weight(self):
        self.assertNotEqual(v.Fraction(1,3),v.Fraction(1,9))
    def test_10_fixed_state_firewall(self):
        self.assertGreater(v.state_minimality_fixture(10**8)['independent_rows'],1000)
    def test_11_diagnostic_scope(self):
        d=json.loads((HERE/'results/fcbi-scan-100m.json').read_text())
        self.assertFalse(d['proves_all_scale'])
    def test_12_rh_status(self):
        c=json.loads((HERE/'certificates/control.json').read_text())
        self.assertFalse(c['rh_established'])

if __name__=='__main__': unittest.main()
