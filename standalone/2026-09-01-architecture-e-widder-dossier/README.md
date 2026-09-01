# Architecture E and the E–Widder source criterion

Status: **PROPOSED PROOF-ORIENTED DOSSIER; INDEPENDENT REVIEW REQUIRED; RH REMAINS UNPROVED.**

This standalone packet collects the complete mathematical output of the review and proof passes over PRs #765, #766, #769, #770, and #781, together with the source–Hermite–Stieltjes closure, the scalar E–Widder compression, and the latest finite-height theorem proving more than four trillion complete Widder orders.

No predecessor branch is modified.  No theorem in this packet is to be read as an accepted repository claim before independent proof review.  The all-order arithmetic inequality remains unproved, so the Riemann Hypothesis remains unproved.

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

The all-order endpoint is

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal W_k(u)\ge0
 \quad\hbox{for every }u>0\hbox{ and every }k\ge1.
 }
\]

The reverse implication is Widder's characterization of Stieltjes functions applied in the functional-equation invariant coordinate `u=s(s-1)`.

### New unconditional finite-order theorem

Let

\[
 F_{n,k}(u)=(-1)^nD_u^{n+k}[u^kq(u)].
\]

Using the invariant genus-zero zero product, the exact atom formula

\[
 F_{n,k}(u)
 =2(n+k)!\sum_a\frac{a^k}{(u+a)^{n+k+1}},
 \qquad a=-\rho(\rho-1),
\]

and a new angular lemma for conjugate off-line invariant atoms, the dossier now proves the following height–order theorem:

> If RH is verified through height `H`, then `F_(n,k)(u)>0` for every `u>0` whenever
> 
> \[
>  \max\{k,n+1\}\arctan(1/H)<\pi/2.
> \]

The published Platt–Trudgian verification through

\[
 H=3\cdot10^{12}
\]

therefore gives

\[
 \boxed{
 F_{n,k}(u)>0
 \quad\text{for every }u>0
 \quad\text{whenever}\quad
 \max\{k,n+1\}\le4{,}710{,}000{,}000{,}000.
 }
\]

In particular,

\[
 \boxed{
 \mathcal W_k(u)>0
 \quad
 (u>0,\ 1\le k\le4{,}710{,}000{,}000{,}000).
 }
\]

No simplicity hypothesis is used.  The external zero computation is imported through the repository's existing exact source lock and was not rerun.

The proof also gives the failure-localization rule

\[
 \mathcal W_k(u)<0
 \Longrightarrow
 \text{an off-line zero exists below height }
 \cot\left(\frac\pi{2k}\right).
\]

This is one-way: a zero below that height is not claimed to force a negative complete sum at the same order.

## Euler-safe source form

The Euler-safe expansion is

\[
 q(u)=
 \frac2u
 +\frac{\psi(s/2)-\log\pi}{2x}
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\frac{e^{-x\log n}}x.
\]

The `2/u` term is killed by every Widder differential operator.  Define

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

where every differentiated prime-power series converges absolutely because `s>1`.

Consequently the E–Widder source inequality

\[
 \boxed{
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal L_k(u,\log n)
 < \mathcal G_k(u)
 }
 \tag{EW}
\]

is now proved for every `u>0` and every integer

\[
 1\le k\le4{,}710{,}000{,}000{,}000.
\]

The same inequality for **all** `k` remains open and is RH-equivalent.  The first order not paid by the imported finite-height theorem is `4,710,000,000,001`; that integer has no intrinsic meaning beyond marking the current angular budget.

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

All translation arrows are explicit.  The only conclusion-bearing content still unproved is positivity for unbounded Widder order, equivalently all-order `(EW)`.

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
| Platt–Trudgian | `EXT.XI.PLATT_TRUDGIAN.2021` | rigorous RH verification through `3*10^12` |

## What is imported and what is new

### Imported repository science

The packet imports, without changing status:

- the raw companion innerness/RH equivalence and actual-Xi finite/asymptotic packets from #765;
- the positive-source quotient construction and native off-central-zero counterexamples from #766;
- the explicit ternary Segre/Chow resolution from #769;
- the source-faithfulness and nonorthogonal quotient/gauge barriers from #770;
- the Segre/Gorenstein, deformation-spectrum and Epstein-wall results from #781;
- reviewed low-order safe-line Pick/Stieltjes results already integrated on `main`;
- the rigorous Platt–Trudgian finite-height theorem through `3*10^12`.

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
9. the scalar E–Widder criterion and absolutely convergent source inequality `(EW)`;
10. the exact differential recurrences and normalized Hausdorff microscope;
11. the invariant-atom angular lemma;
12. the general finite-height-to-finite-Widder-cone theorem;
13. the strict `4.71*10^12`-order source inequality and failure-localization corollary;
14. the accompanying proof-boundary and failed-shortcut firewalls.

No external priority claim is made.

## Reading order

1. [`01_FROZEN_SOURCE_REVIEW.md`](01_FROZEN_SOURCE_REVIEW.md)
2. [`02_SOURCE_HERMITE_STIELTJES_CLOSURE.md`](02_SOURCE_HERMITE_STIELTJES_CLOSURE.md)
3. [`03_E_WIDDER_SCALAR_ENDPOINT.md`](03_E_WIDDER_SCALAR_ENDPOINT.md)
4. [`08_FINITE_HEIGHT_WIDDER_CONE.md`](08_FINITE_HEIGHT_WIDDER_CONE.md)
5. [`04_FIREWALLS_AND_SCOPE.md`](04_FIREWALLS_AND_SCOPE.md)
6. [`05_IMPORTED_VS_NEW_CLAIM_LEDGER.md`](05_IMPORTED_VS_NEW_CLAIM_LEDGER.md)
7. [`06_NEXT_ATTACK.md`](06_NEXT_ATTACK.md)
8. [`07_LITERATURE_BOUNDARY.md`](07_LITERATURE_BOUNDARY.md)
9. [`VALIDATION.md`](VALIDATION.md)
10. [`verify_widder_atom.py`](verify_widder_atom.py)
11. [`verify_height_order_geometry.py`](verify_height_order_geometry.py)

## Validation boundary

The included checkers verify finite algebraic identities only.  They do not replay the external zero computation, prove the analytic continuation arguments, establish all-order source-kernel positivity, prove `(EW)` beyond the stated finite order, or prove RH.

```text
Architecture translations                         PROPOSED COMPLETE / REVIEW
E–Widder equivalence                               PROPOSED COMPLETE / REVIEW
Euler-safe source expansion                        PROPOSED COMPLETE / REVIEW
finite-height full Widder cone through 4.71e12     PROPOSED COMPLETE / REVIEW
exact bounded algebra                              283 AUTHORING CHECKS
all-order E–Widder arithmetic inequality           OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```
