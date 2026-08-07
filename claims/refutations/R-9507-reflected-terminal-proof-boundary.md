# R-9507 — The reflected Selberg identity is exact, but it does not close the local packet or terminal contraction

Claim ID: `R-9507`  
Title: The frozen reflected Selberg–Möbius proposal has independent localization, balanced-packet, packet-source, and terminal-boundary gaps  
Status: **ADVERSARIAL REVIEW / FULL-PROOF DERIVATION REJECTED; EXACT REFLECTED ALGEBRA RETAINED**  
Reviewer: `gpt56-pro`  
Created: 2026-08-07  
Frozen object: PR #226 at `63a4d7c0f482a57893db420e64b22f6a605c72e6`  
Primary targets: `L-9516`, `L-9517`, `T-9509`, `X-9514`

## 1. Review disposition

The new reflected coefficient identity is a valid and useful exact identity. It
solves one algebraic mismatch:

```text
one twist:                 H(z)^2
two conjugate twists:      H(z) overline(H(z))
```

The finite Laurent-polynomial replay correctly checks that algebra.

It does **not**, however, prove the terminal contraction or RH. The frozen
proposal has several independent load-bearing gaps before the advertised
endpoint-count hinge `L-9517.5`.

The review classifications are:

```text
L-9516 general coefficient identity                 VERIFIED WITH A SIGN FIX
L-9516 reflected two-twist identity                  VERIFIED
L-9516 diagonal vertical Plancherel identity         VERIFIED WITH SCOPE FIX
L-9516 identification with one unit block            REJECTED
X-9514 finite Laurent regression                     VERIFIED WITH DECLARED SCOPE
finite Möbius resolvent                              VERIFIED AT ITS SCALAR SCOPE
balanced packet elimination in L-9517                REJECTED
terminal interior null-quotient claim                GAP/BLOCKED
packet-specific Selberg absorption                   GAP/BLOCKED
absolute endpoint-coordinate bound L-9517.5          GAP/BLOCKED
derivation L-9517.5 => L-9517.7                       REJECTED
q0=2 terminal-to-Mertens packet decoder              GAP/BLOCKED
conditional scale recurrence => RH                   VERIFIED
T-9509 as a proof of RH                              REJECTED
RH                                                    UNPROVED
```

This refutation does not assert that the target terminal or balanced estimates
are false. It rejects the claimed derivation at the frozen head.

## 2. Exact sign correction in the generalized Selberg identity

Let

\[
A(s)=\sum_n a(n)n^{-s},
\qquad
B(s)=A(s)^{-1}=\sum_n b(n)n^{-s}.
\]

If

\[
-\frac{A'}{A}(s)=\sum_n\Lambda_A(n)n^{-s},
\]

then, because

\[
A'(s)=-\sum_n a(n)\log n\,n^{-s},
\]

the correct coefficient identity is

\[
\boxed{\Lambda_A=b*(a\log),}
\]

not

\[
\Lambda_A=-b*(a\log)
\]

as written in the prose of `L-9516`.

The subsequent boxed identity is nevertheless correct:

\[
\boxed{
b*(a\log^2)
=
\Lambda_A\log+\Lambda_A*\Lambda_A.
}
\]

Indeed its Dirichlet series is

\[
\frac{A''}{A}
=
-\left(-\frac{A'}{A}\right)'
+
\left(-\frac{A'}{A}\right)^2.
\]

`X-9514` implements the correct positive sign, so this is a notation/prose
repair rather than a failure of the finite regression.

## 3. The reflected coefficient identity is exact

For independent real twist parameters `t` and `s`, define

\[
A_t(w)=\zeta(w+it),
\qquad
A_{-s}(w)=\zeta(w-is).
\]

Write the corresponding coefficient sequences as

\[
a_t(n)=n^{-it},
\qquad
b_t(n)=\mu(n)n^{-it},
\qquad
\Lambda_t(n)=\Lambda(n)n^{-it},
\]

and similarly for `-s`.

Applying the generalized Selberg identity to

\[
A_t,\qquad A_{-s},\qquad A_tA_{-s}
\]

and subtracting the two individual identities from the product identity gives

\[
\boxed{
\mathcal C_{t,-s}
-\mathcal C_t
-\mathcal C_{-s}
=
2\Lambda_t*\Lambda_{-s}.
}
\tag{R-9507.1}
\]

The frozen `L-9516` is the diagonal specialization `s=t`. On a real line
`Re(w)=sigma>1`,

\[
2\left|-\frac{\zeta'}{\zeta}(\sigma+it)\right|^2
=
\mathcal C_{t,-t}(\sigma)
-\mathcal C_t(\sigma)
-\mathcal C_{-t}(\sigma).
\]

This part is verified.

## 4. The diagonal vertical integral is a global weighted energy, not a block energy

Let

\[
Q_H(x)
=
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}H(x-\log n),
\]

with `H` real and compactly supported, and let

\[
L(z)=-\frac{\zeta'}{\zeta}\left(\frac12+z\right).
\]

For `alpha>1/2`,

\[
F_\alpha(t)
:=
\widehat H(\alpha+it)L(\alpha+it)
\]

is the Fourier transform of

\[
x\longmapsto e^{-\alpha x}Q_H(x).
\]

Plancherel gives the exact identity

\[
\boxed{
\int_{\mathbb R}
|\widehat H(\alpha+it)|^2
|L(\alpha+it)|^2\,dt
=
2\pi\int_{\mathbb R}
e^{-2\alpha x}|Q_H(x)|^2\,dx.
}
\tag{R-9507.2}
\]

Thus `L-9516.5` produces the **all-line exponentially weighted Hardy energy**.

It does not produce, for a fixed logarithmic block,

\[
\mathcal B_J
=
\int_J^{J+1}|Q_H(x)|^2\,dx.
\]

The left side of `L-9516.5` contains no parameter `J`.

Compact support of the inverse Fourier transform of

\[
|\widehat H(\alpha+it)|^2
\]

restricts the ratio of two arithmetic indices. It does not restrict their
common/product scale. Consequently the resulting arithmetic series is a
finite-ratio packet, but not a finite endpoint packet.

This invalidates the statement in `T-9509` that the single vertical integral is
already the exact unit-block energy in product-scale coordinates.

## 5. Why a unit block requires two independent vertical frequencies

Fourier inversion gives

\[
e^{-\alpha x}Q_H(x)
=
\frac1{2\pi}
\int_{\mathbb R}F_\alpha(t)e^{itx}\,dt.
\]

For an interval `I=[J,J+1]`,

\[
\boxed{
\begin{aligned}
\int_I|Q_H(x)|^2dx
=
\frac1{(2\pi)^2}
\iint_{\mathbb R^2}
&F_\alpha(t)\overline{F_\alpha(s)}
\\
&\times
\Phi_{I,\alpha}(t-s)\,dt\,ds,
\end{aligned}
}
\tag{R-9507.3}
\]

where

\[
\Phi_{I,\alpha}(\omega)
=
\int_Ie^{2\alpha x}e^{i\omega x}\,dx.
\]

The local block therefore requires the product

\[
L(\alpha+it)L(\alpha-is)
\]

for independent `t,s`, not only the diagonal `s=t`.

`L-9518` supplies the exact two-frequency reflected identity and block adapter.
It repairs this algebraic interface, but does not prove a packet estimate.

## 6. The proposal imports an open balanced Type-II theorem as though it were finite induction

Section 3 of `L-9517` says that the finite induction of `L-23203` removes both

```text
balanced rows
reduced-complexity rows
```

and leaves only terminal rows.

Finite complexity induction can eliminate already-proved same-scale
lower-complexity inequalities. It cannot prove the arithmetic inequality for a
balanced Type-II packet.

The corrected dependency `L-23203` now states this explicitly:

```text
a balanced row must already satisfy a source-specific lower-scale estimate;
the balanced estimate is BTP(K), and it remains open.
```

The corrected PR #233 status likewise says:

```text
terminal Type-I Euler family       proposed complete
balanced Type-II theorem BTP(K)    open
RH                                 unproved
```

This is not a cosmetic dependency update. It is an independent RH-bearing
obligation. The exact Möbius-core decoder `L-15159` proves that, after any fixed
finite packetization, at least one destination retains the full Möbius block
exponent.

Therefore the statement that `L-9517.5` is the single decisive hinge is false.
A balanced source-specific recurrence remains necessary.

## 7. The null quotient does not automatically annihilate a finite arithmetic packet

The high-order window does annihilate the full continuous densities

\[
u^r\,du,
\qquad
u^re^{u/2}\,du,
\qquad
0\le r\le K.
\]

That is the exact content of the high-order null quotient.

A finite resolvent packet contains additional data:

```text
Möbius coefficients
residual divisor coefficients r_V(n)
integer-lattice support
truncated divisor ranges
first-crossing indicators
factor-boundary step functions
```

These sources are not polynomial-exponential densities merely because one
restricts to a polyhedral cell in logarithmic coordinates.

The source dependency `L-15155` explicitly warns that truncated factor ranges
and shifted step boundaries are not automatically null modes. They must remain
in the packet or be removed by a separate source certificate.

A correct terminal lattice row can be closed by Euler summation only after all
Möbius/divisor signs have been frozen into a short prefix and the remaining
large variable runs over a complete integer lattice with polynomial logarithmic
coefficient. That is the terminal theorem on PRs #235/#233. It does not imply
the balanced estimate.

`L-9517` never emits the exact source map proving that every claimed terminal
interior has this normal form.

## 8. Scalar Selberg positivity does not control packet self-energies without a source map

The reflected identity is an identity for the complete aggregate source.

After decomposing that source into packet fields,

\[
Q=\sum_\tau Q_\tau,
\]

the block energy is

\[
\|Q\|^2
=
\sum_{\tau,\upsilon}
\langle Q_\tau,Q_\upsilon\rangle.
\]

Aggregate positivity does not bound each diagonal

\[
\|Q_\tau\|^2.
\]

The elementary model

\[
Q_1=v,
\qquad
Q_2=-v
\]

has aggregate source zero and individual energy sum `2||v||^2`.

The corrected dependency `L-23204` records exactly this packet-source firewall:
a scalar Selberg equation may be used for packet energies only after one
supplies either

1. an exact packet source map with every induced cross term, or
2. a coupled vector/matrix Selberg equation.

`L-9517.5` supplies neither. The two-frequency identity of `L-9518` gives the
correct aggregate normal orientation, but a coupled balanced-packet coercive
inequality remains open.

## 9. Terminal geometry permits linearly many short coordinates

The proposed reason for

\[
\#\{\text{free endpoint divisor coordinates}\}\le C_*
\tag{R-9507.4}
\]

is not valid. Fixed spline degree does not bound the dimension of a divisor
face.

Expand one resolvent factor as

\[
\mu_V*r_V^{*j},
\qquad
r_V(n)
=
-\sum_{\substack{d\mid n\\d\le V}}\mu(d),
\]

and write each residual variable as

\[
n_i=d_im_i,
\qquad
d_i\le V.
\]

Fix `delta=1/5`. For large `K`, take

\[
j_K=\left\lfloor\frac K5\right\rfloor-1.
\]

Choose `j_K` short residual factors in cells

\[
V<n_i\le cV
\]

for one fixed `c>1`. Their complete product has scale

\[
X^{j_K/K+o(1)}
<
X^{1/5}.
\]

One additional unrestricted quotient fills the remaining scale and is terminal
large.

After Abel/Euler summation in that long variable, its endpoint face is still
parametrized by the short residual/divisor coordinates

\[
d_1,\ldots,d_{j_K}.
\]

Thus the natural terminal face has

\[
j_K=\Omega(K)
\]

free short divisor coordinates.

`X-9515` records this exact scale mutation.

This does not rule out a miraculous signed cancellation after complete
recombination. It proves that the absolute bound (R-9507.4) does not follow from

```text
terminality
fixed spline degree
null moments
finite complexity
```

as asserted. A new exact cancellation ledger would be required.

## 10. Endpoint coordinate counting is not sufficient even if the face collapses

Abel summation of a genuinely arithmetic long coefficient gives a boundary
partial sum. Schematically,

\[
\sum_{n\le y}c(n)f(n)
=
C(y)f(y)
-
\int C(u)f'(u)\,du,
\qquad
C(u)=\sum_{n\le u}c(n).
\]

If `c(n)` retains a Möbius source, `C(u)` is Mertens-like. Null moments for
continuous polynomial densities do not bound it.

The proposal's own `q_0=2` mutation identifies the surviving scalar as

\[
G_K(D)=\Delta_{2/3}^K M(D).
\]

For every fixed `K`, the estimate

\[
G_K(D)=O_\varepsilon(D^{1/2+\varepsilon})
\]

is RH-equivalent by exact geometric inversion.

Therefore there is a sharp dichotomy:

```text
the long terminal variable has coefficient 1/polynomial:
    Euler cancellation closes it unconditionally;

the long terminal variable retains the Möbius coefficient:
    its boundary is an RH-equivalent Mertens partial sum.
```

Counting how many short endpoint coordinates remain does not estimate that
Mertens boundary. Even `C_*=0` would not by itself prove a square-root bound for
`G_K`.

Hence the implication

\[
\text{endpoint coordinate count}
\Longrightarrow
\text{L-9517.7}
\]

is rejected.

## 11. The claimed q0=2 packet decoder is not supplied

The scalar theorem `L-23202` proves:

\[
G_K=\Delta_{2/3}^K M
\quad\text{has the RH exponent for every fixed }K.
\]

Its corrected proof boundary explicitly says:

```text
No exact map is asserted from G_K to the terminal or balanced packet families.
Such a packet decoder must be constructed separately.
```

`L-9517` asserts that the `q_0=2` terminal packet *becomes* `G_K`, but provides
no tuple-level map, no cutoff ledger, and no equality of block kernels.

Moreover, once genuine terminal Type-I rows are closed by complete-lattice
Euler cancellation, `L-15159` implies that at least one **balanced** destination
retains the full fixed-`q_0` Möbius exponent. The RH-bearing slice cannot be
made terminal-small by bookkeeping alone.

Thus `L-9517.8` is not an independently passed mutation. It restates the missing
arithmetic estimate.

## 12. No coercive coefficient is computed in the proposed “absorption”

`L-9516` gives an equality

\[
2E=F.
\]

After decomposing `F`, `L-9517` says that a surviving Hermitian diagonal is
“moved to the energy side.”

To obtain an estimate one needs an exact ledger such as

\[
2E
=
\kappa E+R,
\qquad
\kappa<2,
\]

or a correctly signed inequality with a strict reserve.

No coefficient `kappa`, sign, or packet matrix is computed. If the surviving
diagonal is exactly `2E`, moving it cancels the identity and yields no bound.
If it is a packet diagonal, the source-map problem of Section 8 applies.

Endpoint counting cannot substitute for this missing coercivity.

## 13. Conditional deductions that survive

If one independently proves a valid finite auxiliary recurrence

\[
M_K(J)
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+
M_K((1-\delta)J+O_K(1))
\right]
\]

with

\[
\eta_K\to0,
\]

then the exponent calculation is correct:

\[
\lambda_K
\le
\eta_K+(1-\delta)\lambda_K,
\qquad
\lambda_K\le\frac{\eta_K}{\delta}.
\]

Together with the safe-filter Hardy transfer, letting `K` increase gives
`Theta_zeta=0` and RH.

Likewise, a proved estimate for `G_K` transfers to `M` through the exact
geometric inversion.

These deductions are conditional. The required recurrence and `G_K` estimate
are not proved by `L-9517`.

## 14. Corrected frontier

The durable continuation is:

```text
exact reflected Selberg algebra
-> two-frequency local-block reflected identity L-9518
-> exact finite signed packetization
-> direct complete-lattice terminal Euler closure
-> coupled signed balanced Type-II normal-Gram theorem
-> strict lower-scale recurrence
-> RH.
```

The remaining theorem must control the actual balanced packet vector, including
the exact fixed-`q_0=2` Möbius core. It cannot be replaced by endpoint dimension
counting or aggregate scalar positivity.

## 15. Frozen verdict

\[
\boxed{
\text{PR #226 at }63a4d7c0\ldots
\text{ is REJECTED as a proof of RH.}
}
\]

Retained:

```text
exact analytic-totient/Jordan/Mellin spine
exact one- and two-frequency Selberg coefficient algebra
finite Möbius resolvent
safe-filter Hardy transfer
conditional scale-contraction deduction
```

Open:

```text
local block packet estimate
balanced Type-II contraction
packet-source/coercivity ledger
Mertens-bearing boundary estimate
RH
```
