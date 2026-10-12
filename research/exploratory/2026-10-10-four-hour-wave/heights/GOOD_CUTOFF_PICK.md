# Integer-count cutoffs: global Pick order 1,142,000

**Status:** native endpoint-selection and complete-source quantitative proof,
submitted for independent review. The global conclusion additionally imports
the published critical-line census through `3000175332800`, which is larger
than `H0+20`. No RH or all-order full-kernel conclusion is asserted.

**Scope:** the actual xi source kernel on arbitrary distinct positive nodes;
and cofinally growing orders for complete tails at explicitly proved
selectable cutoffs. The cutoff is a property of the complete zero count,
independent of the nodes. Its existence is proved; no numerical value of the
selected cutoff is claimed.

**Exact dependencies:** [DENSITY_RATIONAL_REFINEMENT.md](DENSITY_RATIONAL_REFINEMENT.md),
[VOLTERRA_RATIONAL_REFINEMENT.md](VOLTERRA_RATIONAL_REFINEMENT.md), their complete
xi source/node congruence, classical strip and pointwise count inputs; and
the newly imported unconditional Turing-integral theorem recorded in
[TRUDGIAN_TURING_SOURCE_RECORD.md](../literature/TRUDGIAN_TURING_SOURCE_RECORD.md).
The primary theorem used here is Trudgian, *Improvements to Turing's Method*,
arXiv:0903.1885v3, Theorem 2.2, not a conjectural small value of `S(H0)`.

**What was run:** exact uniform scalar guards, integer-sawtooth integral
controls and normal/-O rational replays in `verify_good_cutoff.py`. The
published Turing bound and census are imported, not rerun.

## Q1. Count convention and imported integral

Throughout `N_+(t)=#{rho:0<Im rho<=t}`, with all analytic multiplicities,
is right-continuous. Set

\[
 \mathcal M(t)=\frac{t}{2\pi}\log\frac{t}{2\pi}
                 -\frac{t}{2\pi}+\frac78,\qquad
 \Delta(t)=N_+(t)-\mathcal M(t).
\]

The native Gamma/count calculation gives, away from zero ordinates,

\[
 \Delta(t)=S(t)+\epsilon(t)/\pi,\qquad |\epsilon(t)|<1/t,
                                                        \tag{Q1}
\]

where `S` is the complete continued argument on
`2 -> 2+it -> 1/2+it`, divided by pi. Isolated-point conventions for `S`
do not change its integral. Import the exact unconditional theorem

\[
 \left|\int_a^bS(t)dt\right|
 \le\frac{2067}{1000}+\frac{59}{1000}\log b,
 \qquad b>a>168\pi.                                    \tag{Q2}
\]

Consequently every interval `[a,b]` with `a>=H0` has

\[
 \left|\int_a^b\Delta(t)dt\right|
 <\frac{2067}{1000}+\frac{59}{1000}\log b
                      +\frac{b-a}{3a}.                 \tag{Q3}
\]

The count identity uses the native positive-ordinate normalization, rather
than the inconsistent introductory count prose in the cited 2010 preprint.
Only its literal argument-integral theorem is imported.

## Q2. A count which misses zero cannot have a small signed integral

Let `[a,b]` lie above `H0`. The smooth main term has

`mathcal M'>4`, `mathcal M''>0`.

Indeed `logt>28`, `log(2pi)<2`, `pi<22/7` imply
`mathcal M'>91/22>4`. On intervals with no zero ordinate, `Delta` strictly
decreases; at every zero ordinate it jumps upward by a positive integer.
There are finitely many such jumps on a compact interval.

If `Delta(t)` never equals zero on the whole interval, its sign can change
at most once, from negative to positive. A positive-to-negative change
would either occur continuously between ordinates, giving an actual zero,
or occur at an upward jump, which is impossible. This remains true when
a one-sided limit is zero but the right-continuous value is not zero.

On an interval `[a,a+L]` of uniform positive sign, integer-valuedness gives
`N_+(t)>=ceil mathcal M(t)` almost everywhere. On an interval of negative
sign it gives `N_+(t)<=floor mathcal M(t)` almost everywhere. Thus respectively

\[
 \int_a^{a+L}\Delta(t)dt\ge L/2-\frac1{8\mathcal M'(a)},
 \qquad
 \int_a^{a+L}\Delta(t)dt\le-L/2+\frac1{8\mathcal M'(a)}. \tag{Q4}
\]

**Proof of the sawtooth estimate.** Change variable `u=mathcal M(t)` and
let `g(u)=1/mathcal M'(mathcal M^(-1)(u))`; `g` is positive and decreasing.
Both `ceil u-u-1/2` and `floor u-u+1/2` equal `1/2-{u}` off integers.
Their continuous periodic primitive is

`F(u)={u}(1-{u})/2`, with `0<=F<=1/8`.

Integration by parts yields
`integral (1/2-{u})g(u)du=F(v)g(v)-F(u)g(u)-integral F g'`.
Since `g'<=0`, this quantity lies between `-g(u)/8` and `g(u)/8`.
The constant `1/2` part integrates to `L/2`. This proves (Q4), with no
assumption about zero spacing or multiplicity. \(\square\)

## Q3. An exact good cutoff occurs within twenty height units

There exists a real `T_*` in `[H0,H0+20]` such that

\[
 \boxed{\Delta(T_*)=0}.                                 \tag{Q5}
\]

**Proof.** If no such point exists, the sign rule in Q2 makes at least one
of the two ten-unit halves have uniform sign almost everywhere. By (Q4),
the absolute integral on that half is greater than `5-1/32`.
But `log(H0+20)<30` (for instance `e>8/3` and
`H0+20<(8/3)^30`), so (Q3) bounds that same integral by less than

`2067/1000+(59/1000)*30+10/(3H0)<4`,

a contradiction. All comparisons are strict rational guards in the replay.
The selected point may be a zero ordinate. Its right-continuous count is
the one in (Q5), which is precisely the endpoint value needed below.
No favorable numerical value of `S(H0)` has been presumed. \(\square\)

## Q4. Good cutoffs occur cofinally, with a short selectable buffer

More generally, for every `B>=H0`, put `L=ceil(log B)`. Then some

\[
 \boxed{T\in[B,B+2L]\quad\text{satisfies}\quad\Delta(T)=0.} \tag{Q6}
\]

Here `L>=29` and `L<=B/2`, so `B+2L<=2B` and
`log(B+2L)<logB+1<=L+1`. Formula (Q3) on either half gives an upper bound
less than `3.126+.059L`, whereas (Q4) gives `L/2-1/32` for a uniform-sign
half. Their difference is positive already at `L=29`, and increases with
`L`. The same sign argument proves (Q6). The elementary `L<=B/2` follows
from monotonicity of `B/2-logB-1` for `B>2` and its positivity at `H0`.

## Q5. The complete-source endpoint cost now disappears

At any good cutoff `T>=H0`, keep exactly the logarithmically weighted
proper rational norm and constants from the density packet:

`d=3191/5000`, `C1=6383/10000`, `C2=2037/5000`,
`c_*=232/1000`, `m_*=(113/355)(1-1838/28729)`, `U_*=106/333`.

For every denominator dimension `n>=850000`, put `q=n^2/T`. Integrate by
parts on `(T,infinity)`. The endpoint is exactly zero by `Delta(T)=0`:

\[
 \left|2\int_{(T,\infty)}|R|^2d\Delta\right|
 \le2\int_T^\infty|\Delta|\,|(|R|^2)'|db
 \le4c_*d qB_R=\ell_g qB_R,\quad
 \boxed{\ell_g=92539/156250}.                            \tag{Q7}
\]

The interval excludes every atom at `T`; the integration-by-parts boundary
uses the right-continuous value of `Delta(T)`. If `T` is itself an ordinate,
its entire source atom is assigned to the below-or-at-`T` part.
The bound holds for every complex numerator, so it applies to all `D^jP`
in the full variable-displacement series. Consequently the reference lower
bound is `(m_*-ell_g q)B_R` and sampling upper bound
`S_g(q)B_R=(U_*+ell_g q)B_R`.

## Q6. Displacements and exact strict source payment

Keep the actual independent vertical displacements `|a_b|<=1/2`, their
Taylor depths, both signed-pole classes, and all conjugate/multiplicity
groups, as in V5–V7. When `q<=87/200`,

`(d+2/n)q<13881/50000`,

and a rational exponential upper bound proves

`exp(13881/50000)<kappa_g=33/25`.

The unchanged derivative coefficients `C1,C2` and discrete Minkowski
therefore give the complete conjugate-source loss

`(C2+C1^2) kappa_g^2 q^2 S_g(q)B/4`.

Subtracting from the reference gives the strictly positive uniform gap

\[
 m_*-\ell_g q-\tfrac14(C_2+C_1^2)\kappa_g^2q^2(U_*+\ell_g q)
 \ge\boxed{\frac{38543369070455868447007920769}
                  {23584713437500000000000000000000}>0}. \tag{Q8}
\]

The minimum is at `q=87/200`, since all subtracted coefficients are positive.
The gap is about `0.00163425`. Complete source sums and remainders converge
by the same proper-rational decay and complete count bounds already proved.

## Q7. Global and cofinal consequences

At any good cutoff, the exact arbitrary-node congruence proves strict tail
positive definiteness for every even `n>=850000` with

\[
 \boxed{200n^2\le87T}.                                  \tag{Q9}
\]

Principal submatrices cover smaller sizes. The cofinal choices in (Q6)
therefore give increasing tail orders `sqrt(87T/200)+O(1)`.
This is a selectable-cutoff theorem, not the same inequality at every
predetermined cutoff. The all-cutoff 900,000 density theorem is unchanged.

For the global theorem use (Q5). The published critical-line verification
extends through `3000175332800>H0+20`, so every source below or at `T_*`
is a nonnegative critical-pair Gram source. Also

`200*(1142000)^2 < 87*H0 <=87*T_*`.

Adding that complete critical source to the strictly positive tail gives
global Pick order **1,142,000**, at the stated imported census scope. It
uses the existence of one common cutoff, independent of the nodes; no
uncomputed gap is discarded. A finite global order and cofinal orders for
changing tail kernels do not imply RH.
