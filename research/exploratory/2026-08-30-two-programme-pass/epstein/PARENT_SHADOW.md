# E5 — Parent–shadow note (mode 7): Z_z inside the real-analytic Eisenstein series

NON_DIRECTED_HIGH_PRECISION; dps=45 for the checks below; rh_established: false.

## How Z_z sits inside E(z,s)

With E_1(z,s) = (1/2) sum_{gcd(m,n)=1} y^s / |mz+n|^{2s} (the gcd=1 Eisenstein series,
= (1/2) sum_{gcd=1} Q_z(m,n)^{-s}), stratifying the full lattice sum by d = gcd(m,n) gives

    Z_z(s) = 2 zeta(2s) E_1(z,s),        equivalently   Lambda_z(s) = 2 xi(2s) E_1(z,s) = 2 E*(z,s),

where xi(u) = pi^{-u/2} Gamma(u/2) zeta(u) and E* is the completed Eisenstein series with
Fourier expansion

    E*(z,s) = xi(2s) y^s + xi(2s-1) y^{1-s}
              + 4 sqrt(y) sum_{n>=1} n^{s-1/2} sigma_{1-2s}(n) K_{s-1/2}(2 pi n y) cos(2 pi n x).

**Numerically verified here** (not assumed):

- Z_z(s) = 2 zeta(2s) E_1(z,s) with E_1 evaluated by a direct coprime lattice sum:
  - z = 0.13 + 1.070000000 i, s = 6.25 + 1.3 i: **23.7 digits** (coprime cutoff Q <= 20000, stated tail bound 1.9e-23)
  - z = 0.5 + 0.866025404 i, s = 6.0 + 2.4 i: **22.9 digits** (coprime cutoff Q <= 25000, stated tail bound 7.8e-23)
- Lambda_z(s) = 2 E*(z,s) against the full Fourier/Bessel expansion (independent engine):
  - z = 0.13 + 1.07 i, s = 0.6 + 7.3 i: **44.8 digits**
  - z = 0.0 + 1.31 i, s = 0.5 + 13.4 i: **41.3 digits**

## Constant term and scattering

The constant term of E* is xi(2s) y^s + xi(2s-1) y^{1-s}: the incoming/outgoing pair of
the continuous spectrum on SL2(Z)\H with scattering "matrix"
phi(s) = xi(2s-1)/xi(2s). On the critical line Re s = 1/2, phi is unimodular:
measured ||phi(1/2 + 3.7 i)| - 1| = 0.00e+00. The poles/zeros of
phi are governed by xi(2s-1) and xi(2s) — the Riemann xi itself is the scattering content
of the parent. Zeros of Lambda_z(s) = 2 xi(2s) E_1(z,s) with xi(2s) zero-free in
0 < Re(2s) < 2 off zeta's critical line Re(2s)=1... more precisely: in the s-strip
0.3 < Re s < 0.7 relevant here, xi(2s) has its zeros on Re s = 1/2 exactly when zeta's
zeros lie on Re(2s) = 1 — which is a zero-free line region known unconditionally only as
Re(2s)=1 itself (zeta(1+it) != 0); so off-line zeros of Lambda_z in this strip away from
Re s = 1/2 are zeros of E_1(z, s) (numerically: every off-line zero found in E3/E4 was
re-checked to be a zero of Lambda_z, hence of xi(2s) E_1(z,s) with xi(2s) != 0 there).

## Survival-ladder reading (parent-shadow mode 7)

- **L6 everywhere**: the functional equation Lambda_z(s) = Lambda_z(1-s) holds at EVERY
  point z of moduli space (oracle O3 verifies it numerically at z=i and at a generic z);
  it is inherited from the parent E(z,s) (Maass–Selberg), not from arithmetic.
- **L2 on a measure-zero locus**: an Euler product for Z_z exists exactly at the
  arithmetic factorization points (CM points such as z=i, z_hex, where Z_z splits as
  (scale) * zeta(s) * L(s, chi_D) — oracle O2), a measure-zero subset of moduli space.
- The measured zero-geometry consequence (E2/E3/E4): at the arithmetic points every
  low-height zero sits on the line to 12 digits (E2 — consistent with GRH numerically);
  moving off the arithmetic locus, finitely many low-height pairs collide and depart at
  the certified (tau*, t*, z*) events of E3, and the departure radius around z=i is
  direction-dependent (E4). Off-line zeros remain density zero: Bombieri–Hejhal show
  (under standard hypotheses) that almost all Epstein zeros lie on the line, and Ki and
  Y. Lee give unconditional on-line proportion/density results — so the FE-only rung of
  the ladder still pins almost all zeros to the line, while the Euler-product rung at the
  CM points pins (numerically, at low height) ALL of them. The departures measured here
  are the finitely many low-height exceptions, not a bulk phenomenon.

## Positioning w.r.t. the literature (mandatory)

Off-line zeros of Epstein zetas (class number > 1, or non-arithmetic) are classical:
Davenport–Heilbronn; Potter–Titchmarsh; real/near-real zeros: Bateman–Grosswald, Stark.
Zero trajectories and collision-spawned off-critical branches in ONE-parameter Epstein
families are published with local singular analysis: Arenstorf–Brewer (1993),
Travenec–Samaj (arXiv:1909.07112), Betermin–Samaj–Travenec (arXiv:2110.09368).
This lab's contribution is limited to: (1) the two-parameter full-moduli atlas over the
fundamental domain; (2) argument-principle certification with stated precision of each
event; (3) k-indexing of which zero pairs depart where; (4) correlating departure radius
with geometric invariants of the lattice (distance to CM points along directions — E4);
(5) the parent-shadow survival-ladder reading above. No claim beyond these; no theorems;
RH and GRH remain open and nothing here bears on them beyond finite-precision numerics.
