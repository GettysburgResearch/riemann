import unittest
import mpmath as mp

from packet_blocks import (
    box_sinc,
    carrier_kernel,
    correct_dimensionless_prime_kernel,
    legendre_basis_value,
    naive_fractional_divided_difference,
    off_lattice_arch_entry,
    off_lattice_frequency_kernel,
    off_lattice_gram,
    off_lattice_pole_entry,
    overlap_matrix,
    sinc,
)


class PacketBlockTests(unittest.TestCase):
    def test_overlap_endpoints_and_parity(self):
        with mp.workdps(60):
            k0 = overlap_matrix(6, mp.mpf(0))
            k1 = overlap_matrix(6, mp.mpf(1))
            for m in range(7):
                for n in range(7):
                    self.assertLess(abs(k0[m, n] - (1 if m == n else 0)), mp.mpf("1e-55"))
                    self.assertLess(abs(k1[m, n]), mp.mpf("1e-55"))
            k = overlap_matrix(6, mp.mpf("0.37"))
            for m in range(7):
                for n in range(7):
                    self.assertLess(abs(k[n, m] - (-1) ** (m + n) * k[m, n]), mp.mpf("1e-55"))

    def test_overlap_against_direct_quadrature(self):
        with mp.workdps(70):
            s = mp.mpf("0.381")
            k = overlap_matrix(5, s)
            for m, n in [(0, 0), (1, 4), (3, 2), (5, 5)]:
                direct = mp.sqrt((2*m+1)*(2*n+1))/2 * mp.quad(
                    lambda x: mp.legendre(m, x-2*s) * mp.legendre(n, x),
                    [-1+2*s, 1],
                )
                self.assertLess(abs(k[m, n] - direct), mp.mpf("1e-55"))

    def test_carrier_kernel_is_real_symmetric(self):
        with mp.workdps(50):
            b = carrier_kernel(7, mp.mpf("0.29"), mp.mpf("123.456"))
            for m in range(8):
                for n in range(8):
                    self.assertLess(abs(b[m,n]-b[n,m]), mp.mpf("1e-45"))
                    self.assertEqual(mp.im(b[m,n]), 0)

    def test_scalar_kernel_recovery(self):
        with mp.workdps(60):
            s = mp.mpf("0.314")
            phase = mp.mpf("8.7")
            b = carrier_kernel(0, s, phase)[0,0]
            self.assertLess(abs(b - (1-s)*mp.cos(phase)), mp.mpf("1e-55"))

    def test_legendre_basis_is_real_on_real_axis_and_orthogonal(self):
        with mp.workdps(50):
            delta = mp.mpf("1.7")
            T = mp.mpf("4.25")
            for n in range(5):
                value = legendre_basis_value(n, mp.mpf("2.1"), T, delta)
                self.assertLess(abs(mp.im(value)), mp.mpf("1e-45"))
            for m in range(4):
                for n in range(4):
                    inner = mp.quad(
                        lambda eta: mp.sqrt((2*m+1)/delta)*mp.legendre(m,2*eta/delta)
                        * mp.sqrt((2*n+1)/delta)*mp.legendre(n,2*eta/delta),
                        [-delta/2, delta/2],
                    )
                    self.assertLess(abs(inner-(1 if m==n else 0)), mp.mpf("1e-45"))

    def test_off_lattice_frequency_formula_against_support_integral(self):
        with mp.workdps(55):
            delta = mp.mpf("0.83")
            ti = mp.mpf("2.3")
            tj = mp.mpf("-0.7")
            xi = mp.mpf("0.21")
            direct = mp.re(mp.quad(
                lambda eta: mp.exp(-2*mp.pi*mp.j*ti*eta)
                * mp.exp(2*mp.pi*mp.j*tj*(eta-xi)) / delta,
                [-delta/2+xi, delta/2],
            ))
            closed = off_lattice_frequency_kernel(ti,tj,xi,delta)
            self.assertLess(abs(direct-closed), mp.mpf("3e-45"))

    def test_scalar_arch_and_pole_forms_are_finite(self):
        with mp.workdps(45):
            L = mp.log(13)
            a = off_lattice_arch_entry(mp.mpf("3.2"), mp.mpf("3.2"), L)
            p = off_lattice_pole_entry(mp.mpf("3.2"), mp.mpf("3.2"), L)
            self.assertTrue(mp.isfinite(a))
            self.assertTrue(mp.isfinite(p))

    def test_integer_lattice_bridge_and_fractional_adversary(self):
        with mp.workdps(60):
            u = mp.mpf("0.271")
            for x, y in [(2,5),(3,8)]:
                correct = correct_dimensionless_prime_kernel(x,y,u)
                naive = naive_fractional_divided_difference(x,y,u)
                self.assertLess(abs(correct - (-1)**(x-y)*naive), mp.mpf("1e-55"))
            x = mp.mpf("2.125")
            y = mp.mpf("5.375")
            correct = correct_dimensionless_prime_kernel(x,y,u)
            naive = naive_fractional_divided_difference(x,y,u)
            self.assertGreater(abs(correct-naive), mp.mpf("0.01"))

    def test_off_lattice_gram(self):
        with mp.workdps(50):
            delta=mp.mpf("0.91")
            self.assertEqual(off_lattice_gram(3,3,delta),1)
            self.assertLess(abs(off_lattice_gram(2,5,delta)-sinc(3*mp.pi*delta)),mp.mpf("1e-45"))


if __name__ == '__main__':
    unittest.main()
