import unittest

import mpmath as mp

from correction_bound import correction_bound


def _autocorrelations(v):
    K = len(v)
    out = []
    for d in range(K):
        out.append(sum(v[j + d] * mp.conj(v[j]) for j in range(K - d)))
    out.append(mp.mpc(0))
    return out


def _r_value(t, L, cvals):
    K = len(cvals) - 1
    H = 2 * L / K
    if t >= 2 * L:
        return cvals[K]
    d = min(int(mp.floor(t / H)), K - 1)
    theta = (t - d * H) / H
    return (1 - theta) * cvals[d] + theta * cvals[d + 1]


def _b_value(t):
    if t == 0:
        return mp.mpf(1) / 4
    return mp.exp(-t / 4) / (1 - mp.exp(-t)) - 1 / t


class ResidualIdentityTests(unittest.TestCase):
    def test_compact_and_residual_forms_agree(self):
        with mp.workdps(60):
            cutoff = 13
            T = mp.mpf("37.5")
            L = mp.log(cutoff)
            A = 2 * L
            K = 3
            raw = [mp.mpc(1, 2), mp.mpc(-2, 1), mp.mpc(3, -1)]
            norm = mp.sqrt(sum(abs(x) ** 2 for x in raw))
            v = [x / norm for x in raw]
            cvals = _autocorrelations(v)
            H = A / K
            omega = T / 2
            rprime0 = (cvals[1] - cvals[0]) / H
            cprime0 = mp.re(rprime0)

            def C(t):
                return mp.re(mp.exp(-1j * omega * t) * _r_value(t, L, cvals))

            def original_integrand(t):
                if t == 0:
                    return -mp.mpf(5) / 4 - cprime0
                return (mp.exp(-t) - C(t)) / t - _b_value(t) * C(t)

            def residual_integrand(t):
                if t == 0:
                    return -mp.mpf(1) / 4 - cprime0
                return (mp.cos(omega * t) - C(t)) / t - _b_value(t) * C(t)

            points = [d * H for d in range(K + 1)]
            i_original = sum(
                mp.quad(original_integrand, [points[d], points[d + 1]])
                for d in range(K)
            )
            i_residual = sum(
                mp.quad(residual_integrand, [points[d], points[d + 1]])
                for d in range(K)
            )
            original = (i_original + mp.e1(A) - mp.log(mp.pi)) / (2 * mp.pi)
            residual = (
                mp.log(T / (2 * mp.pi))
                - mp.ci(T * L)
                + i_residual
            ) / (2 * mp.pi)
            self.assertLess(abs(original - residual), mp.mpf("1e-48"))

            bound = correction_bound(cutoff, float(T), K)
            self.assertLess(
                abs(original - mp.log(T / (2 * mp.pi)) / (2 * mp.pi)),
                bound.archimedean_bound,
            )


if __name__ == "__main__":
    unittest.main()
