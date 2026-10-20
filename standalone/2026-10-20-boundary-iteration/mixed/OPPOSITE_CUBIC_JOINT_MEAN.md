# A joint mean for opposite cubic conductor orientations

20 October 2026. **Proposed source-dependent auxiliary theorem, with a
complete absorption argument. Independent review requested.** This is
a different family from the quadratic/sextic pair. It improves the
separately averaged cubic-sieve envelope in its balanced range. No
claim of literature priority, improved zero-free boundary, or RH is made.

The inputs are Dunn--Radziwill, [2109.07463v3, Section 5](https://arxiv.org/html/2109.07463v3),
the exact finite-profile and divisor-resummation proofs in this packet,
and de Faveri, [2610.04045v1, Proposition 8.1](https://arxiv.org/html/2610.04045v1).
The uniform angular argument uses `../type_i/ANGULAR_UNIFORMITY.md`.
This proof does not use a zero-free theorem or the recursive inverse
moment from the supplied quasi-Riemann-hypothesis framework.

## 1. Family, completion and estimate

Work in the Eisenstein field with the primary and zero-extension
conventions of the finite-profile proof. Let `r,S` be squarefree,
coprime to each other and to the fixed bad primes. Write
`chi_T(c)=(c/T)_3`, and let `ell` be a nonzero integer. For each of
the four ramified profiles `kappa`, put

\[
 Q_{r,S,\kappa}(s;\ell)=
 Z_{rS}(3s-1/2,3\ell)
 \sum_c \widetilde g(c)\kappa(c)
       \overline{\chi_r(c)}\chi_S(c)\alpha(c)^\ell(Nc)^{-s},
 \tag{OC1}
\]

where the full incomplete Hecke factor is

\[
 Z_{rS}(3s-1/2,3\ell)
 =\sum_{(d,rS)=1}\alpha(d)^{3\ell}(Nd)^{1/2-3s}.
 \tag{OC2}
\]

All fixed ramified factors belong to their specified scalar channels.
The cube character in (OC2) is untwisted because `chi_S^3=1` on
units, and it remains zero when `d` meets `rS`. The vector `Q` includes
all four profiles and both angular signs.

Let `r` range over `Nr<=R` and `S` over `H<NS<=2H`, with all original
masks retained. Put

\[
 M=\min(R,H),\quad N=\max(R,H),\quad Y_0=R^{1/2}H,
\]
\[
 F_\delta(R,H)=RH+
 M^{2/3}N^{1/3}Y_0^{1-2\delta}
 +M^{1/3}N^{2/3}Y_0^{2/3-2\delta}.
 \tag{OC3}
\]

For every fixed `0<delta<2/9` and `epsilon>0`, the proposed bound is

\[
 \boxed{\quad
 \sum_{\substack{Nr\le R,\ H<NS\le2H\\(r,S)=1}}^{*}
  \|\mathbf Q_{r,S}(1/2+\delta+it;\ell)\|^2
 \ll_{\delta,\epsilon}(RH)^\epsilon F_\delta(R,H)
                 (1+|\ell|+|t|)^{2-4\delta+\epsilon}.
 \quad}                                                   \tag{OC4}
\]

The field and finite bad-place data are fixed. Constants do not depend
on the two conductors or angular order. Angular order zero is excluded:
this positive cubic character does not supply the odd quadratic guard
that removes spherical theta residues.

At `R=H=N`, (OC3) is comparable to

\[
                     N^2+N^{5/2-3\delta}.                \tag{OC5}
\]

In particular `delta=1/6` is allowed and gives the natural-count
`N^(2+epsilon)` mean on `Re s=2/3`. This is not a central-line
Lindelof mean. More generally, when `R>=H`, (OC3) is comparable to
`RH+R^(5/6-delta)H^(5/3-2delta)`. Its second term is at most `RH`
if `R^(1/6+delta)>=H^(2/3-2delta)`.

## 2. Exact self-reflection at the positive cubic conductor

Use the same periodic-twist reflection as in
`QUADRATIC_PAIR_ABSORPTION.md`, now with `eta=chi_S` instead of
`xi_S chi_S^j`. The primitive Fourier transform at `S`, the inversion
of its nonzero Fourier variable, and the local Kubota factor replace
`eta` by

\[
                    \overline{\eta\chi_S}=\chi_S.
 \tag{OC6}
\]

Thus the positive cubic conductor is a fixed point of reflection.
The two primitive local Gauss factors have characters `chi_S` and
`bar chi_S`. Their product has modulus `NS` (indeed the usual
compatible additive normalization gives `chi_S(-1) NS=NS`), with
any CRT convention contributing only a unit phase. Character zeros
keep the Fourier variable coprime to `S`.

At `r`, the negative cubic character still cancels the local Kubota
factor and produces the full signed Ramanujan sum. The exact divisor
resummation in `../type_i/DUAL_RESUMMATION.md` therefore applies at
every prime of `r`. Since `chi_S^3=1`, its complementary Euler
parameters have the untwisted cube phase of (OC2). It restores that
entire factor, including its deleted Euler factors, and replaces `r`
only by divisors `k|r`. The coprimality `(k,S)=1` survives.

The three-cusp extraction minor remains invertible: the additional
unit character `chi_S(omega)` only shifts its integer phase index.
The ramified geometric ratio has the extra factor
`chi_S(lambda)^3=1`. The full 27-cusp reflection and subsequent
four-profile extraction are exactly the mechanism previously audited;
no invariant four-dimensional Fourier-coefficient space is assumed.

Consequently, with `L=1+|ell|+|t|` and any small `eta>0`,

\[
 \|\mathbf Q_{r,S}(1/2-\delta+it;\ell)\|
 \ll L^{4\delta}(NS)^{2\delta}(Nr)^{-1/2+2\delta+\eta}
       \sum_{k\mid r}(Nk)^{1/2-\delta}
       \|\mathbf Q_{k,S}(1/2+\delta-it;\ell)\|.
 \tag{OC7}
\]

The vector includes the reflected angular sign. The archimedean factor
is the uniformly bounded gamma quotient already proved in the angular
uniformity note. Nonzero angular order makes every completed component
entire. All common-prime masks and local phases are retained before
taking this norm inequality.

## 3. The original side uses the actual joint cubic sieve

After fixing finitely many ray classes, cubic reciprocity changes the
column character in (OC1) to

\[
                  \chi_c(S)\overline{\chi_c(r)}
                         =\chi_c(Sr^2).
 \tag{OC8}
\]

This is exactly the kernel of de Faveri's Proposition 8.1 with
`a=S,b=r`. The proposition allows arbitrary squarefree column
coefficients. Restricting its positive row sum to squarefree coprime
`r,S` is legitimate; the fixed ray classes are handled separately.
The norm, angular, Gauss and ramified-profile column factors are all
independent of the two rows after that fixed partition.

For a squarefree column dyad of length `D`, the squared coefficient
norm on `Re s=1/2+delta` is `O(D^(-2 delta))`. Dyadic summation gives
the following original-side bound for the Gaussian free-split integral
at any `Y>=1`:

\[
 \mathcal I(R,H;Y)\ll(RHY)^\eta
 \{RH+M^{2/3}N^{1/3}Y^{1-2\delta}
                +M^{1/3}N^{2/3}Y^{2/3-2\delta}\}.
 \tag{OC9}
\]

Both nonconstant column powers are positive in the stated delta range.
This is a conductor-ordered joint operator estimate, rather than a
product of two independent sieves.

Completion causes no extra power. For each cube `d`, its coefficient
in norm is `(Nd)^(-1-3 delta)` and its squarefree column length is
`Y/(Nd)^3`. Minkowski for the three terms in (OC9) gives cube exponents

\[
                   -1-3\delta,\qquad -5/2,\qquad -2,
 \tag{OC10}
\]

all absolutely summable over ideals. For each fixed `d`, the row
condition `(rS,d)=1` is retained as a positive restriction and the
cube angular phase has modulus one. No cube tail is discarded.

## 4. Divisor closure and absorption

Square (OC7), sum multiples of each divisor, and then sum the positive
`S` rows. With `A_+` denoting the joint right-line mean, the left mean
is bounded by

\[
 H^{4\delta}L^{8\delta}R^{4\delta+\eta}
 \sum_{H<NS\le2H}^{*}\sum_{Nk\le R,(k,S)=1}^{*}
       (Nk)^{-2\delta}
       \|\mathbf Q_{k,S}(1/2+\delta-it;\ell)\|^2.
 \tag{OC11}
\]

The exponents of `R` in the three terms of (OC3) are

| Range | Row powers |
| --- | --- |
| `R<=H` | `1`, `7/6-delta`, `2/3-delta` |
| `R>=H` | `1`, `5/6-delta`, `1-delta` |

Every power is strictly greater than `2 delta` when `delta<2/9`.
Each term is continuous at `R=H`. Partial summation, splitting there
if necessary, therefore costs at most a fixed constant times
`R^(-2 delta) F_delta(R,H)`. This checks the divisor closure for
all ratios of the two conductor lengths.

Normalize a supremum over finite conductor and angular cutoffs, and
all heights, by the right side of (OC4). It is finite before absorption:
the right absolute line is uniformly bounded, the exact reflection on
a preliminary line `Re s=-eta` gives a fixed conductor polynomial
times `L^(2+4 eta)`, and Gaussian three-lines gives initial height
degree `L^(1-2 delta+2 eta)` for each component. Taking `eta` sufficiently
small puts its square below the chosen final height allowance. This
uses scalar extraction on the left and the convergent full cusp
expansion only on the reflected right absolute line.

The shifted Gaussian integral, using (OC11), contributes relative to
this supremum at most a constant times

\[
       Y^{-4\delta}R^{2\delta+\eta}H^{4\delta}L^{8\delta}.
 \tag{OC12}
\]

Choose

\[
                    Y=C_0(RH)^\theta R^{1/2}H L^2.
 \tag{OC13}
\]

Choose the sieve and divisor losses below `4 delta theta`, then take
the fixed `C0` sufficiently large for a contraction for every `R,H>=1`.
Choose `theta` inside the final epsilon allowance. Substitution in
(OC9) gives (OC3); its largest angular power is `L^(2-4 delta)`.
The Gaussian convolution is uniform because shifting height by `v`
costs at most a fixed power of `1+|v|`. Reflection fixes `S`, decreases
`r`, and changes only an included angular sign, so every finite cutoff
closes. The supremum is bounded independently of the cutoffs. Letting
them increase proves (OC4).

## 5. A licensed free-column consequence and comparison

For arbitrary jointly chosen `|b(r,S)|<=1`, fixed smooth radial tests,
and squarefree coprime outer rows, define

\[
 T(A,R,H)=\sum_{r\asymp R,S\asymp H}^{*}b(r,S)
 \sum_u\widetilde g(ur)\chi_S(ur)\alpha(ur)^\ell
       W_A(Nu/A)W_R(Nr/R)W_H(NS/H).
 \tag{OC14}
\]

The `u` sum is unrestricted apart from its natural arithmetic zeros.
Exact cubic Gauss multiplicativity extracts the outer unit factors and
leaves precisely (OC1). Mellin inversion, absolute convergence of the
inverse cube factor on `Re s=1/2+delta`, and Cauchy in `(r,S)` give

\[
 |T(A,R,H)|\ll (ARH)^\epsilon
 (1+|\ell|)^{1-2\delta+\epsilon}
 A^{1/2+\delta}\{RH F_\delta(R,H)\}^{1/2}.
 \tag{OC15}
\]

Only fixed radial seminorms are required. At `A=R=H=N`, choosing
`delta=1/6` gives `N^(8/3+epsilon)` with angular cost
`(1+|ell|)^(2/3+epsilon)`. In terms of `X=ARH=N^3`, the exponent is
`8/9`. For a line arbitrarily close to `1/2`, the corresponding
exponent is `11/12`. The inner variable cannot be restricted to primes
or assigned an arbitrary arithmetic multiplier by this argument.

For comparison, in the smaller range `0<delta<1/6`, the separate
cubic-in-r sieve and this same reflection give, after summing `S`,

\[
 RH+R^{1/2-\delta}H^{2-2\delta}
            +R^{1-\delta}H^{5/3-2\delta}.
 \tag{OC16}
\]

The restriction `delta<1/6` is needed for that separate proof's divisor
partial summation: its row power `1/2-delta` must exceed `2 delta`.
At `R=H=N` the largest term of (OC16) in this range is
`N^(8/3-3 delta)`. The joint estimate is strictly stronger throughout
this comparison range. Its valid endpoint `delta=1/6` follows from
the new joint proof, not from inserting an endpoint into (OC16).

The source-overlap check must distinguish the present positive cubic
row from the positive sextic partner of `JOINT_PAIR_UNEQUAL_CUTOFFS.md`.
In rStation paper 5's sextic notation the present row is `z=S^2`,
not `z=S`, and its fourth-power label is `f=r`. Thus its all-row
scale is `K=H^2`. Even retaining the powerful-row stratum in equation
(11.3), with powerful-part norm `H^2`, gives after undoing the label
normalization the completed bound
`RH+R^2 H^3/D`. At `R=H=N`, combining this with the joint original
sieve crosses at `D=N^2`, producing a peak `N^(3-4 delta)`, which
does not recover (OC5) in the stated range. The generic (11.4) bound
is weaker still. This checks those specific supplied interfaces; it
is not an exhaustive literature comparison or a priority claim.

The physical boundary-determining terminal contains a quadratic/sextic
conductor and row-dependent marks. Its character is not (OC8).
Consequently (OC4) and (OC15) do not lower the current numerical
zero-free boundary, and do not resolve the remaining short-common-
divisor or coherent prime-column problems.
