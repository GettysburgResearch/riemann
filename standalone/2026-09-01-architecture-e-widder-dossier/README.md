# Architecture E and the E–Widder source criterion

Status: **PROPOSED PROOF-ORIENTED DOSSIER; INDEPENDENT REVIEW REQUIRED; RH REMAINS UNPROVED.**

This standalone packet collects the complete mathematical output of the review and proof passes over PRs #765, #766, #769, #770, and #781, together with the source–Hermite–Stieltjes closure developed in the successor work and the latest scalar compression to an all-order Widder inequality.

No predecessor branch is modified.  No theorem in this packet is to be read as an accepted repository claim before independent proof review.  In particular, the final arithmetic inequality is not proved here, so the Riemann Hypothesis remains unproved.

## Current leading state

Put

\[
 \xi_{\rm R}(s)
 =\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad
 u=s(s-1),
\]

and, for `u>0`,

\[
 x=\sqrt{u+\frac14},
 \qquad
 s=\frac12+x>1.
\]

Define the safe invariant logarithmic derivative

\[
 \boxed{
 q(u)=
 \frac1{\sqrt{u+\frac14}}
 \frac{\xi_{\rm R}'}{\xi_{\rm R}}
 \left(\frac12+\sqrt{u+\frac14}\right).
 }
\]

The actual positive theta kernel makes `q(u)>0` unconditionally.  For every integer `k>=1`, set

\[
 \boxed{
 \mathcal W_k(u)
 =(-1)^{k-1}
 \frac{d^{2k-1}}{du^{2k-1}}
 \bigl[u^kq(u)\bigr].
 }
\]

The latest proposed endpoint theorem is

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal W_k(u)\ge0
 \quad\hbox{for every }u>0\hbox{ and every }k\ge1.
 }
\]

The reverse implication is Widder's characterization of Stieltjes functions applied in the functional-equation invariant coordinate `u=s(s-1)`.  Under RH,

\[
 q(u)=2\sum_{\gamma>0}
 \frac{m_\gamma}{u+\gamma^2+1/4},
\]

and hence

\[
 \mathcal W_k(u)
 =2(2k-1)!
 \sum_{\gamma>0}m_\gamma
 \frac{(\gamma^2+1/4)^k}
 {(u+\gamma^2+1/4)^{2k}}>0.
\]

The Euler-safe expansion is

\[
 q(u)=
 \frac2u
 +\frac{\psi(s/2)-\log\pi}{2x}
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\frac{e^{-x\log n}}x.
\]

The `2/u` term is killed by every Widder differential operator.  Consequently define

\[
 \mathcal G_k(u)=
 (-1)^{k-1}D_u^{2k-1}
 \left[
  \frac{u^k}{2x}
  \bigl(\psi(s/2)-\log\pi\bigr)
 \right]
\]

and

\[
 \mathcal L_k(u,\ell)=
 (-1)^{k-1}D_u^{2k-1}
 \left[
  \frac{u^k}{x}e^{-\ell x}
 \right].
\]

Then

\[
 \mathcal W_k(u)
 =\mathcal G_k(u)
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
  \mathcal L_k(u,\log n),
\]

where every differentiated prime-power series converges absolutely because `s>1`.  Thus the entire remaining Architecture-E theorem is the source-faithful inequality

\[
 \boxed{
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal L_k(u,\log n)
 \le \mathcal G_k(u)
 \qquad(u>0,\ k\ge1).
 }
 \tag{EW}
\]

`(EW)` is not proved in this packet.  It is exactly the point at which the proof programme remains open.

## Complete architecture

The dossier proves or imports, with exact provenance, the chain

\[
 \begin{array}{c}
 \text{actual theta source }\Phi\\
 \Downarrow\\
 \mathcal A_\Phi(a,b)
 =\frac12\displaystyle\int_{|a+b|}^{\infty}
 \xi H_\xi(a-b)\,d\xi\\
 \Updownarrow\\
 K_0\succeq0\\
 \Updownarrow\\
 \mathcal B_X\succeq0\\
 \Updownarrow\\
 \Theta_\lambda\text{ has zero negative squares}\\
 \Updownarrow\\
 q\text{ is a Stieltjes function}\\
 \Updownarrow\\
 \mathcal W_k(u)\ge0\quad(\forall u,k)\\
 \Updownarrow\\
 \mathrm{RH}.
 \end{array}
\]

All translation arrows are explicit.  The only unproved content is the final positivity assertion, equivalently `(EW)`.

## Frozen review boundary

This packet freezes the following exact source states.  Later movement on any source branch is outside the present claims unless separately audited.

| Source | Frozen head | Role |
|---|---|---|
| `main` | `6dda8b5125457ed936330229f8c9eb6491728e76` | branch base |
| PR #765 | `8f01064df805624c045877655893c324a220975d` | actual-Xi companions, theta asymptotics, raw-innerness firewall |
| PR #766 | `17c7624a0bd56c5356d00278b2a846d2efdbdccc` | positive-source quotients and counterexamples, coefficient flags |
| PR #769 | `f36576faf7853a56bd1f64edd29c4df662cae849` | completed ternary Segre/Chow source resolution |
| PR #770 | `9421846721cd788ab01615c8b6d459d9de849df7` | native source faithfulness, quotient/gauge obstructions |
| PR #781 | `ea282c4e73ecd2d8cad44587da5ffa135df67e98` | Segre defect geometry, deformation spectra, Epstein walls |
| PR #783 | `1db60cddb723ea921c1cc73edaa0334b72679156` | proof review and generalized-Schur negative-index theorem |
| PR #784 | `d6d326b21d9526d9c91b18017bf550003f8f4f9b` | source–Hermite–Stieltjes closure and mechanism firewalls |

## What is imported and what is new

### Imported repository science

The packet imports, without changing status:

- the raw companion innerness/RH equivalence and actual-Xi finite/asymptotic packets from #765;
- the positive-source quotient construction and native off-central-zero counterexamples from #766;
- the explicit ternary Segre/Chow resolution from #769;
- the source-faithfulness and nonorthogonal quotient/gauge barriers from #770;
- the Segre/Gorenstein, deformation-spectrum and Epstein-wall results from #781;
- reviewed low-order safe-line Pick/Stieltjes results already integrated on `main`.

### Imported classical mathematics

The proofs use standard canonical products for entire functions, Hermite–Biehler/de Branges kernel algebra, generalized Schur/Pontryagin kernels, Stieltjes transforms, Widder's 1938 real-variable characterization of Stieltjes functions, the functional equation of `xi`, and the absolutely convergent Euler formula for `xi'/xi` on `Re(s)>1`.

### Proposed new or new-in-repository deductions

Subject to independent review, the dossier contributes:

1. the exact companion-Schur/Hermite–Bezout congruence in the present normalization;
2. the distinct-location negative-square count for the Xi Hermite kernel;
3. the explicit source polarization and its double Fourier transform;
4. the identity `A_Phi=4K_0` with the current Weyl kernel;
5. the safe Euler-axis restriction and explicit prime-shift operator formulation;
6. the exact Stieltjes endpoint and two-channel Gram factorization;
7. the Loewner-difference decomposition of the safe Pick matrix;
8. the functional-equation invariant coordinate `u=s(s-1)`;
9. the scalar E–Widder criterion and the absolutely convergent source inequality `(EW)`;
10. the accompanying proof-boundary and failed-shortcut firewalls.

No external priority claim is made.

## Reading order

1. [`01_FROZEN_SOURCE_REVIEW.md`](01_FROZEN_SOURCE_REVIEW.md)
2. [`02_SOURCE_HERMITE_STIELTJES_CLOSURE.md`](02_SOURCE_HERMITE_STIELTJES_CLOSURE.md)
3. [`03_E_WIDDER_SCALAR_ENDPOINT.md`](03_E_WIDDER_SCALAR_ENDPOINT.md)
4. [`04_FIREWALLS_AND_SCOPE.md`](04_FIREWALLS_AND_SCOPE.md)
5. [`05_IMPORTED_VS_NEW_CLAIM_LEDGER.md`](05_IMPORTED_VS_NEW_CLAIM_LEDGER.md)
6. [`06_NEXT_ATTACK.md`](06_NEXT_ATTACK.md)
7. [`verify_widder_atom.py`](verify_widder_atom.py)

## Validation boundary

The included checker verifies finite algebraic identities only.  It does not prove the analytic continuation arguments, the infinite canonical-product identities, source-kernel positivity, the Widder inequalities for Riemann data, or RH.

```text
Architecture translations                 PROPOSED COMPLETE / REVIEW
E–Widder equivalence                       PROPOSED COMPLETE / REVIEW
Euler-safe source expansion                PROPOSED COMPLETE / REVIEW
finite symbolic atom checks                INCLUDED
E–Widder arithmetic inequality (EW)        OPEN / RH-EQUIVALENT
Riemann Hypothesis                         UNPROVED
```
