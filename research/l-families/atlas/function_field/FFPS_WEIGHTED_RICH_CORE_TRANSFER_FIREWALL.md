# The weighted rich-core transfer firewall

Status: **exact Boolean-coefficient and physical-shell obstruction to an
automatic ambient-density transfer; uniform coefficient-majorant Rankin bound
proved; no bound for the fully observed FFPS complementary current, RH, or
GRH**

Bounded replay:
[`ffps_weighted_rich_core_transfer_firewall.py`](ffps_weighted_rich_core_transfer_firewall.py).

Frozen arithmetic source: PR #751 at `98af0db6e`, especially `L-106080`,
`L-102884`, `L-106120--L-106121`, `L-106132--L-106133`, and
`T-106140`.

## 0. Outcome

The ambient logarithmic-density theorem in
`FFPS_SCALABLE_RICH_CORE_BLOCK_TOWER.md` does **not** automatically transfer to
the frozen weighted Boolean FFPS source.

The mismatch is exact.  The ambient theorem uses

\[
 {\mu^2(c)\mu^2(d)\over cd}
\tag{0.1}
\]

over cumulative core ranges.  The frozen balanced source instead carries the
cutoff-dependent coefficient

\[
 b_U=a_U\star a_U\star\mu_{\rm sf},
 \qquad
 a_U=\varepsilon-\mu_U\star\mathbf1_{\rm sf},
 \qquad U=\lfloor Y^{1/6}\rfloor,
\tag{0.2}
\]

then common-core extraction, owner weights, a ratio-eight physical shell,
Boolean representation/depth labels, carrier and renewal masks, and a
Hilbert-valued observation.  PR #751 supplies a subpower pointwise bound for
the resulting `gamma_omega`; it supplies no factor-richness Carleson estimate
for that observed measure.

Indeed, poor cores are literal nonzero balanced-source atoms.  If every prime
in a squarefree support `S` exceeds `U`, then

\[
 \boxed{b_U(S)=1+(-1)^{|S|}.}
\tag{0.3}
\]

In particular, a product of two large primes congruent to three modulo four
has `b_U=2` but has no eligible prime at all.  Section 2 gives an exact clean
pair of such cores in one legal physical shell.

There is a useful positive result at the coefficient-majorant level.  Uniformly
in `U`,

\[
 \boxed{|b_U(n)|\le5^{\omega(n)}}.
\tag{0.4}
\]

A weighted Rankin argument then gives a power-of-log saving for the poor set
relative to the corresponding `5^omega` majorant.  That is not yet a transfer
to the actual physical source: a `Y^{o(1)}` observation weight or a retained
depth/shell selector can concentrate on the poor sector and erase any fixed
logarithmic saving.

The correct next theorem is therefore a source-weighted, shell-uniform
richness estimate after the actual Boolean/depth recombination—not another
ambient Euler-product calculation.

## 1. Exact rough-support coefficient

Work in the labelled squarefree Boolean algebra.  If `S` is nonempty and
every `p in S` exceeds `U`, the only divisor of `S` below the cutoff is the
empty divisor.  Hence

\[
 a_U(S)=-1,
 \qquad a_U(\varnothing)=0.
\tag{1.1}
\]

Now expand

\[
 b_U(S)=
 \sum_{A\sqcup B\sqcup C=S}
 a_U(A)a_U(B)(-1)^{|C|}.
\tag{1.2}
\]

Only `A,B` nonempty survive.  Give the three boxes weights `1,1,-1`.
Inclusion--exclusion for the conditions `A != empty`, `B != empty` gives

\[
 (1+1-1)^{|S|}
 -(1-1)^{|S|}
 -(1-1)^{|S|}
 +(-1)^{|S|}
 =1+(-1)^{|S|},
\]

proving (0.3).  This is the actual cutoff-dependent coefficient from
`L-106080` and `L-106132`, not an arbitrary replacement weight.

For a general support of size `k`,

\[
 |a_U(S)|\le2^k.
\]

Applying this in (1.2) and summing the absolute partition weights gives

\[
 |b_U(S)|
 \le(2+2+1)^k=5^k,
\]

which proves (0.4), uniformly in the moving cutoff.

## 2. Exact clean physical-shell counterfixture

Take

\[
 P=5\cdot7=35,
 \qquad Q=13\cdot17=221,
\]

and

\[
 c=103\cdot107=11021,
 \qquad d=79\cdot83=6557.
\]

All eight prime labels are distinct.  Thus `(c,d)=1`, `(c,Q)=1`, `(d,P)=1`,
and the clean reduced pair has `g=1`.  Put

\[
 N=Pc^2=4,251,185,435,
 \qquad
 M=Qd^2=9,501,729,029,
\]

and

\[
 Y=\lceil M/8\rceil=1,187,716,129,
 \qquad U=\lfloor Y^{1/6}\rfloor=32.
\]

Then exactly

\[
 Y<N<M\le8Y,
\tag{2.1}
\]

so both products lie in one sharp ratio-eight physical horizon.  Every core prime
exceeds `U`, while all four are three modulo four.  Therefore

\[
 \boxed{
 \omega_1(c)=\omega_1(d)=0,
 \qquad b_U(c)=b_U(d)=2.}
\tag{2.2}
\]

This obeys the squarefree, common-core, cross-coprimality, owner and shell
conditions used by the frozen bilateral source.  It proves that poor cores
are not removed by the Boolean coefficient or by the physical shell.

The phenomenon is asymptotic, not a small-number accident.  Keep `P,Q`
fixed and choose four distinct primes congruent to three modulo four in a
short fixed-ratio interval `[Z,(1+epsilon)Z]`.  For sufficiently small fixed
`epsilon`,

\[
 {1\over8}<{Pc^2\over Qd^2}<8.
\]

The associated horizon has `U asymp Z^(2/3)`, so all four primes exceed `U`
for large `Z`; each two-prime core again has coefficient two and eligible
count zero.  The prime number theorem in progressions supplies infinitely
many such clean pairs.

More sharply, the Boolean source retains depth labels before the final
recombination.  On the rough two-prime-core depth sector, (0.3) is constantly
two.  Once `r>=3`, **every** atom in that sector fails the rank-`r` richness
condition, irrespective of residue class.  Thus no richness estimate can be
uniform over the inherited depth coordinate.  The depth rows have to be
recombined, or their total contribution separately paid, before a
density-one statement is used.

This is not a proof that the fully recombined frozen FFPS source is dominated
by poor cores.  It is a proof that the ambient law plus the currently frozen
pointwise source bounds cannot exclude such concentration.

## 3. The strongest automatic weighted Rankin bound

Let

\[
 \omega_1(n)=\#\{p\mid n:p\equiv1\pmod4\},
 \qquad r=\lfloor\alpha\log\log x\rfloor,
 \qquad0<\alpha<1/2.
\]

For `0<t<1`, (0.4), positivity and Mertens in the two reduced residue classes
give

\[
\begin{aligned}
 &\sum_{\substack{n\le x\\\mu^2(n)=1\\\omega_1(n)<r}}
 { |b_U(n)|\over n}\\
 &\quad\le
 t^{-(r-1)}
 \prod_{\substack{p\le x\\p\equiv1(4)}}
 \left(1+{5t\over p}\right)
 \prod_{\substack{p\le x\\p\not\equiv1(4)}}
 \left(1+{5\over p}\right)\\
 &\quad\ll
 (\log x)^{\frac52(1+t)-\alpha\log t+o(1)}.
\end{aligned}
\tag{3.1}
\]

The optimizing value is `t=2alpha/5`, so

\[
 \boxed{
 \sum_{\omega_1(n)<r}{|b_U(n)|\over n}
 \ll
 (\log x)^{E_5(\alpha)+o(1)},}
\tag{3.2}
\]

where

\[
 E_5(\alpha)
 ={5\over2}+\alpha-\alpha\log(2\alpha/5).
\tag{3.3}
\]

Against the full coefficient majorant

\[
 \sum_{n\le x}{\mu^2(n)5^{\omega(n)}\over n}
 \asymp(\log x)^5,
\]

the saving exponent is

\[
 \boxed{
 c_5(\alpha)
 ={5\over2}-\alpha+\alpha\log(2\alpha/5)>0.}
\tag{3.4}
\]

The same exponent controls a pair when either `c` or `d` is poor: drop
coprimality and use the union bound.  Under common-square extraction,

\[
 |b_U(gc)b_U(gd)|
 \le25^{\omega(g)}5^{\omega(c)+\omega(d)},
\]

and the exact `g^-2` source weight pays

\[
 \sum_g{\mu^2(g)25^{\omega(g)}\over g^2}<\infty.
\tag{3.5}
\]

Owner exclusions, coprimality and indicator-valued shell deletions can only
decrease this positive majorant.

Equations (3.1)--(3.5) are uniform in `U`.  They are the maximum automatic
transfer presently justified.  They do **not** prove the desired FFPS
complement bound because:

1. the reference measure is the artificial `5^omega` majorant, not the
   signed or Hilbert-valued FFPS current;
2. the frozen `gamma_omega(t)=Y^{o(1)}` bound is not a uniform fixed power of
   `log Y`, so it can exceed the saving in (3.4);
3. the physical observation and retained depth/incidence coordinates can
   correlate with factor richness, as Section 2 demonstrates;
4. taking absolute values before the complete conductor/source recombination
   is forbidden by `R-106123` and `T-106140`.

## 4. Exact no-go and the next theorem target

The following implication is false under the currently recorded source
hypotheses:

```text
ambient mu^2(n)/n richness
  + pointwise gamma_omega=Y^o(1)
  + ratio-eight support
  => power-log small observed poor-core current.
```

The rough two-prime rows give nonzero legal source atoms, and a coefficient
packet supported on those rows satisfies the frozen pointwise and support
bounds while having poor-core mass ratio one.  This is a logical countermodel
to a deduction from the stated hypotheses; it is not a counterexample to an
additional theorem about the one fixed fully recombined FFPS coefficient.

The smallest useful new statement is:

```text
FFPS-RICH-CARLESON(alpha):
  after summing the actual Boolean representation and depth coordinates,
  uniformly in every physical owner/shell block that remains before the
  common square, the total variation (or the exact source-dual Hilbert norm)
  of atoms with omega_1(c)<r or omega_1(d)<r is smaller by a fixed power of
  log Y than the declared full-source reference norm.
```

An alternative is a direct signed theorem for the fully recombined
complementary current.  Either version must keep the conductor recombination
required by `T-106140`; a depthwise or fixed-fibre positive estimate cannot
work.

## 5. Proof ledger

Proved exactly:

- the rough-support Boolean formula (0.3);
- the uniform Boolean majorant (0.4);
- a clean, cross-coprime, ratio-eight poor-core source fixture;
- the existence of asymptotic rough two-prime poor rows;
- the weighted coefficient-majorant Rankin bound (3.1)--(3.5);
- the logical failure of automatic transfer from the frozen pointwise source
  hypotheses.

Not proved:

- `FFPS-RICH-CARLESON(alpha)`;
- a power-log bound for the fully observed complementary FFPS current;
- the signed rich-current trace estimate, principal individualization, RH,
  or GRH.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_weighted_rich_core_transfer_firewall.py --check
python -B -O research/l-families/atlas/function_field/ffps_weighted_rich_core_transfer_firewall.py --check
python -B -m unittest tests.test_ffps_weighted_rich_core_transfer_firewall
python -B -O -m unittest tests.test_ffps_weighted_rich_core_transfer_firewall
```

The replay evaluates labelled Boolean partitions through support size eight
and one exact integer shell fixture.  It enumerates no source family,
conductor family, curve, or point.
