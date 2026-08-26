# The coherent half-source shell firewall

Status: **asymptotically exact prime-shell countermodel to any subpower-loss
diagonal-to-positive-observation inequality based only on injectivity,
compact ratio-eight support and Wick disjointness; no counterexample to the
signed native differential/reflection kernel, RH, or GRH**

Bounded exponent replay:
[`ffps_half_source_coherent_shell_firewall.py`](ffps_half_source_coherent_shell_firewall.py).

Frozen interfaces: PR #751 `L-106133--L-106134`, `R-106150`, and
`T-106150`.  The exact half-source coefficient is supplied by
`FFPS_BOOLEAN_HALF_SOURCE_DIAGONAL_GAIN.md`.

## 0. Outcome

The free owner--core source diagonal is polynomially saving, but it cannot be
interpolated to the observed half-field by injectivity and compact support.
There is an explicit coherent prime shell on which the gap is a positive
power.

Let `Z` tend to infinity and set

\[
 Y=Z^{10},
 \qquad U=\lfloor Y^{1/6}\rfloor=\lfloor Z^{5/3}\rfloor.
\]

Choose owner primes and half-core primes in disjoint fixed-ratio intervals

\[
 p\in\mathcal P_Z=[Z,(1+\varepsilon)Z],
 \qquad
 a\in\mathcal A_Z=[Z^2,(1+\varepsilon)Z^2],
\tag{0.1}
\]

with `epsilon>0` fixed and sufficiently small.  Then `a>U`, so the exact
rough-singleton formula gives

\[
 \boxed{f_U(a)=-1.}
\tag{0.2}
\]

Every half-source atom has physical size

\[
 pa^2\asymp Z^5=Y^{1/2},
\tag{0.3}
\]

and every product of two half-atoms has size `asymp Z^10=Y`.  Taking
`(1+epsilon)^6<8` puts the whole two-half shell inside one ratio-eight window.

The prime number theorem gives

\[
 M_P:=|\mathcal P_Z|\asymp {Z\over\log Z},
 \qquad
 M_A:=|\mathcal A_Z|\asymp {Z^2\over\log Z},
\]

so the number of injective half-atoms is

\[
 N_Z=M_PM_A\asymp {Z^3\over(\log Z)^2}.
\tag{0.4}
\]

Their free diagonal is

\[
 \boxed{
 D_Z=
 \sum_{p\in\mathcal P_Z}
 \sum_{a\in\mathcal A_Z}{1\over pa^2}
 \asymp {Z^{-2}\over(\log Z)^2}
 =Y^{-1/5+o(1)}.}
\tag{0.5}

But a positive local spline observation adds all coefficients with the same
sign.  Its coherent square has scale

\[
 \boxed{
 C_Z\asymp
 \left(\sum_{p,a}{1\over\sqrt p\,a}\right)^2
 \asymp {Z\over(\log Z)^4}
 =Y^{1/10-o(1)}.}
\tag{0.6}

Therefore

\[
 \boxed{
 {C_Z\over D_Z}
 \asymp {Z^3\over(\log Z)^2}
 =Y^{3/10-o(1)}
 \asymp N_Z.}
\tag{0.7}

Boolean/Wick disjointness does not repair the gap: a proportion

\[
 \left(1-{1\over M_P}\right)
 \left(1-{1\over M_A}\right)=1-o(1)
\tag{0.8}

of ordered atom pairs have disjoint literal supports.

Thus no estimate of the form

\[
 \text{positive local observed energy}
 \le Y^{o(1)}\times\text{free source diagonal}
\tag{0.9}

can follow uniformly from:

```text
the injective map (p,a) -> p a^2;
the cutoff support a>U;
one ratio-eight shell;
the paid free diagonal;
Boolean/Wick deletion of shared labels.
```

This does **not** refute the native FFPS route.  The conclusion kernel is a
signed differential/reflection observation, not the positive local spline
used in the fixture.  Equation (0.7) instead proves that genuine reflection
or arithmetic cancellation is indispensable; a diagonal interpolation
shortcut is impossible.

## 1. Exact scale compatibility

The half-source packet gives

\[
 f_U(a)=-1
\]

for every prime `a>U`.  In (0.1),

\[
 a\ge Z^2>Z^{5/3}\ge U
\]

for large `Z`, so every selected coefficient has the same negative sign.

The two physical scales are exact at the exponent level:

\[
 \deg_Z(pa^2)=1+2\cdot2=5,
 \qquad
 \deg_Z((pa^2)(qb^2))=10=\deg_ZY.
\tag{1.1}
\]

Across the complete Cartesian shell,

\[
 {\max (pa^2qb^2)\over\min(pa^2qb^2)}
 \le(1+\varepsilon)^6.
\tag{1.2}

For example `epsilon=1/100` makes this ratio less than eight by a large
margin.  Owner and half-core intervals are disjoint, so `(p,a)=1` and no
owner label can equal a core label.

The depth dilation in `L-106133` multiplies these singleton half-core
coefficients by `theta`.  Restricting the Beta parameter to any fixed interval
such as `theta in [1/2,3/4]` changes all scales only by constants and has
positive Beta measure.

## 2. Exact diagonal and coherent scales

The half-atom coefficient is

\[
 c_{p,a}={f_U(a)\over\sqrt p\,a}
 =-{1\over\sqrt p\,a}.
\tag{2.1}

Prime number theory in fixed-ratio intervals gives

\[
 \sum_{p\in\mathcal P_Z}{1\over p}
 \asymp {1\over\log Z},
 \qquad
 \sum_{a\in\mathcal A_Z}{1\over a^2}
 \asymp {1\over Z^2\log Z}.
\tag{2.2}

Multiplying proves (0.5).  Likewise,

\[
 \sum_{p\in\mathcal P_Z}{1\over\sqrt p}
 \asymp {Z^{1/2}\over\log Z},
 \qquad
 \sum_{a\in\mathcal A_Z}{1\over a}
 \asymp {1\over\log Z},
\tag{2.3}

which proves (0.6).

To turn (0.6) into an observation fixture, let `A` be any continuous
nonnegative local spline which is positive at one interior point `y_0`.
The frozen half-field kernel of `L-106134` has exactly this property.  There
are `eta,c>0` with

\[
 A(y)\ge c
 \qquad(|y-y_0|<\eta).
\]

Choose `epsilon` small enough and choose `X` so that

\[
 {X\over pa^2}
\]

lies in this positive interval for every atom in the shell.  Since all
coefficients (2.1) have the same sign,

\[
 \left|\sum_{p,a}c_{p,a}A(X/(pa^2))\right|^2
 \ge c^2
 \left(\sum_{p,a}{1\over\sqrt p\,a}\right)^2,
\tag{2.4}

giving the lower bound (0.6).

For the two-half Wick convolution, use the positive interior of
`A *_M A` and the product shell (1.2).  The same argument applies after
removing shared-label pairs because their fraction tends to zero.

## 3. Wick disjointness leaves almost every pair

Index atoms by the Cartesian set

\[
 \mathcal P_Z\times\mathcal A_Z.
\]

Because the two prime intervals are disjoint, two atoms `(p,a)` and `(q,b)`
share a literal label exactly when `p=q` or `a=b`.  The number of ordered
disjoint pairs is therefore

\[
 M_P(M_P-1)M_A(M_A-1).
\tag{3.1}

Against `N_Z^2=M_P^2M_A^2`, the surviving fraction is exactly (0.8).  In
particular, the Wick projection removes only

\[
 O(M_P^{-1}+M_A^{-1})=o(1)
\]

of the coherent mass.  It removes the literal contractions correctly, but it
is not an orthogonality mechanism for distinct products.

## 4. Precise no-go statement

Consider any class of observation operators which includes one continuous
nonnegative compact multiplicative spline with a positive interior interval,
and which is required to obey a uniform estimate for every legal coefficient
deletion of the frozen half-source.  There is no bound

\[
 \|\mathcal O F\|^2
 \ll Y^{o(1)}
 \sum_{p,a}|c_{p,a}|^2
\tag{4.1}

deducible solely from injectivity, fixed-ratio compactness and Wick
disjointness.  The shell (0.1) makes the quotient of the two sides at least
`Y^(3/10-o(1))`.

The same fixture rules out replacing `Y^o(1)` in (4.1) by any loss
`Y^gamma` with `gamma<3/10`, for that positive local class.

The qualifications are load-bearing:

- The fixture is a legal deletion/subfamily countermodel.  It does not prove
  that the complete undeleted FFPS source has the same sign after all source
  sectors are recombined.
- It uses the positive spline `A` and `A *_M A`, before the conclusion-bearing
  differential polynomial is applied.
- The native outer/reflection kernel is signed.  Its derivatives may cancel
  the coherent bulk exhibited here.
- Therefore the fixture does not refute `REFSIG106150`, `WCADD106140`,
  `WCKUM106140`, or RH.  It proves those cancellation gates cannot be replaced
  by a source-diagonal/Bessel assertion.

## 5. Architectural consequence

The current ledger is now sharp:

```text
literal half-source coefficient and cutoff         exact;
owner/core map                                      injective;
free atomic/source diagonal                         power-saving;
shared-label Wick contractions                      removed/closed;
distinct-product coherent shell                     power-sized countermodel;
signed reflection/differential cancellation         open and indispensable.
```

The next work should act on the signed operator itself.  Promising options
are:

1. calculate the reflection-even/odd response of the rough prime shell and
   identify which leading coherent moments the differential polynomial kills;
2. apply the two-large-Moebius representation before the positive spline is
   formed;
3. retain the connected additive/Kummer subtraction of `T-106140` rather
   than estimating the half-field energy.

Any further free-diagonal refinement, by itself, cannot cross (0.7).

## 6. Proof ledger

Proved exactly or from the prime number theorem in fixed-ratio intervals:

- compatibility of the cutoff, half-product and final-product scales;
- the exact rough coefficient sign;
- the atom count and diagonal/coherent asymptotics (0.4)--(0.7);
- the exact Wick-disjoint surviving fraction (0.8);
- the no-go for subpower-loss positive local diagonal-to-observation bounds.

Not proved or claimed:

- positivity of the signed native differential/reflection observation;
- failure of a globally recombined signed FFPS theorem;
- `REFSIG106150`, the family gates, principal individualization, RH, or GRH.

## 7. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_half_source_coherent_shell_firewall.py --check
python -B -O research/l-families/atlas/function_field/ffps_half_source_coherent_shell_firewall.py --check
python -B -m unittest tests.test_ffps_half_source_coherent_shell_firewall
python -B -O -m unittest tests.test_ffps_half_source_coherent_shell_firewall
```

The replay checks the rational scale ledger, one exact rough half-source
coefficient, the ratio-eight inequality and three finite Wick-fraction
panels.  It enumerates no prime interval, source family, conductor family,
curve or point.
