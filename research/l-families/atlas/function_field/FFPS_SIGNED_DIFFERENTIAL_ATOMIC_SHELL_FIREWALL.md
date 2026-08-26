# The extra-notched signed differential has an exact negative dyadic shell

Status: **exact signed-measure theorem for a deleted Wick-disjoint prime
shell of the literal `D_out` polynomial; parent outer-adapter mismatch
exposed, and no theorem yet for the explicit outer current, complete recombined
FFPS gate, RH, or GRH**

Bounded exact replay:
[`ffps_signed_differential_atomic_shell_firewall.py`](ffps_signed_differential_atomic_shell_firewall.py).

Frozen comparison point: corrected PR #751 commit
`49a5b4180d7c2ba582764750dc8178e2d5498b4c`, especially `L-102701`,
`L-102740`, `L-106133--L-106134`, `R-106150`, and `T-106150`.  This is
the signed-operator sequel to
`FFPS_HALF_SOURCE_COHERENT_SHELL_FIREWALL.md`.

## 0. Outcome

The literal fourth-order polynomial `D_out` displayed in `T-106150` does
**not** erase the coherent prime shell.  Applied to `A *_M A` in logarithmic
coordinate, it gives a compact finite signed measure with five exact dyadic
atoms.  The atoms at ratios `2` and `8` are negative:

\[
\begin{array}{c|ccccc}
X/n&1&2&4&8&16\\ \hline
\text{atomic coefficient}
&5&-10-10\sqrt2&15+20\sqrt2&-20-10\sqrt2&10.
\end{array}
\tag{0.1}
\]

On the odd, Wick-disjoint prime shell of the preceding packet, distinct
dyadic layers cannot meet: their `2`-adic valuations differ.  The exact
negative atomic variation per unit positive translate is therefore

\[
\boxed{30+20\sqrt2.}
\tag{0.2}
\]

For singleton cores, the Beta square contributes

\[
\int_0^1(1-\theta)\theta^2\,d\theta={1\over12}.
\tag{0.3}
\]

Consequently the atomic part of the deleted Wick shell has exact negative
variation

\[
\boxed{
 \left({5\over2}+{5\sqrt2\over3}\right)
 \sum_{\substack{p\ne q,\ a\ne b\\
                   p,q\in\mathcal P_Z,
                   \ a,b\in\mathcal A_Z}}
 {1\over\sqrt{pq}\,ab}
 \asymp {Z\over(\log Z)^4}
 =Y^{1/10-o(1)}.}
\tag{0.4}
\]

The total Jordan negative variation is at least (0.4), because an absolutely
continuous part cannot cancel point masses.  Its free source diagonal is only
`Y^(-1/5+o(1))`.  Thus this extra-notched signed differential, by itself,
gives no source-blind or deletion-stable route from the free diagonal to the
literal polynomial estimate written in `WKSFSC106150`.

There is a load-bearing three-way parent mismatch.  With

\[
 q(s)=1-\sqrt2\,2^{-s},\qquad r(s)=1-2^{-s},
\]

the actual common mother has `q(s)^2r(s)^2`, whereas the outer construction
written before the final equality in `L-102740` has only `q(s)r(s)^2`.
Moreover the explicit piecewise kernel of `L-102880` differs from the
`L-102740` construction by the stable first-order filter

\[
 V={5D+3/2\over4}.
\]

Therefore the kernel audited here is

\[
\boxed{K_{\rm extra}=QV K_{\rm exp},}
\tag{0.5}
\]

where `Q=I-sqrt(2)S_2` is the single dyadic notch,
`(S_2f)(X)=f(X/2)`, and `K_exp` is the explicit derivative kernel printed in
`L-102880`.  Equivalently, if `K_740` denotes the derivative of the
`L-102740` construction, then

\[
 K_{740}=VK_{\rm exp},\qquad K_{\rm extra}=QK_{740}.
\]

Thus neither the construction nor the common-mother differential equals the
explicit kernel.  Until a complete-source adapter or a terminal-safe inverse
repairs that edge, this packet has no direct conclusion-facing implication to
the explicit outer current or RH.  The full frozen-interface proof is in
`FFPS_COMMON_MOTHER_OUTER_NOTCH_MISMATCH.md`.

The second qualification is also decisive: the intended RH-bearing current is
the **complete undeleted Boolean source** plus its inherited closed sectors.
Other source sectors may cancel these atoms before the negative part is taken.
Equation (0.4) neither proves nor disproves that global cancellation.

## 1. Exact kernel calculation

Write `x=log X`, `t=log y`, `L=log 2`, and let lower-case letters denote
logarithmic kernels.  We use the frozen convention

\[
 \widehat f(s)=\int_{\mathbb R}f(e^t)e^{-st}\,dt,
 \qquad D={d\over dt}=X{d\over dX}.
\]

Thus `widehat(Df)(s)=s widehat(f)(s)` for compact distributions; this fixes
the sign of every factor below.  The positive ratio-four spline has Mellin
transform

\[
\widehat A(s)=
{(1-2^{-s})(1-\sqrt2\,2^{-s})\over s(s-1/2)}.
\tag{1.1}
\]

Its logarithmic representative is explicitly

\[
a(t)=
\begin{cases}
2(e^{t/2}-1),&0<t<L,\\
\sqrt2(2-e^{t/2}),&L<t<2L,\\
0,&\text{otherwise}.
\end{cases}
\tag{1.2}
\]

It is continuous and piecewise smooth with derivative jumps.  Hence `a''`
is a finite signed measure and `(a*a)''''=a''*a''` is a finite signed
measure.  Every lower derivative occurring below is also a finite measure.

The literal polynomial used in `T-106150` is

\[
\mathcal D_{\rm out}
={1\over2}D(D-1)(5D+3/2)(2D-1).
\tag{1.3}
\]

For the extra-notched kernel

\[
K=\mathcal D_{\rm out}(A*_M A),
\]

finite-measure Mellin transformation gives

\[
\begin{aligned}
\widehat K(s)
&={1\over2}s(s-1)(5s+3/2)(2s-1)\widehat A(s)^2\\
&=(1-2^{-s})^2(1-\sqrt2\,2^{-s})^2
 { (s-1)(5s+3/2)\over s(s-1/2)}\\
&=(1-2^{-s})^2(1-\sqrt2\,2^{-s})^2
 \left(5+{3\over s}-{4\over s-1/2}\right).
\end{aligned}
\tag{1.4}
\]

By contrast, the literal first multiplier line of `L-102740` gives the
undifferentiated constructed outer current

\[
 \widehat R_{740}(s)
 =q(s)r(s)^2{(s-1)(5s+3/2)\over s^2(s-1/2)}.
\tag{1.5}
\]

Applying the final `D` in the frozen definition `K_740=D R_740` therefore
gives

\[
 \widehat K_{740}(s)
 =q(s)r(s)^2{(s-1)(5s+3/2)\over s(s-1/2)}.
\tag{1.6}
\]

Direct integration of the three explicit cells in `L-102880` instead gives

\[
 \widehat K_{\rm exp}(s)
 ={4q(s)r(s)^2(s-1)\over s(s-1/2)}.
\tag{1.7}
\]

Consequently

\[
 K_{740}=VK_{\rm exp},\qquad
 QR_{740}
 ={1\over2}(D-1)(5D+3/2)\Phi_*.
\]

Applying `D` gives (0.5).  Equivalently, equation (1.4) has one additional
factor `q(s)` relative to (1.6), while (1.6) itself has the additional stable
factor `(5s+3/2)/4` relative to (1.7).  Since
`widehat(S_2f)(s)=2^(-s)widehat(f)(s)`, this proves the typing identity (0.5)
and isolates the parent adapter mismatch.  The remainder of this packet
concerns `K_extra` only.

The inverse transform of the last factor is

\[
5\delta_0+(3-4e^{t/2})1_{t\ge0}\,dt.
\tag{1.8}
\]

The apparent half-line tails cancel after the four finite differences in
(1.4), consistently with compact support.  Only the `5 delta_0` term
contributes atoms.  Expanding

\[
(1-z)^2(1-\sqrt2z)^2
=1-(2+2\sqrt2)z+(3+4\sqrt2)z^2
 -(4+2\sqrt2)z^3+2z^4
\tag{1.9}
\]

proves (0.1).  This also proves directly that `K` is nonzero.  Its total mass
vanishes because (1.3) contains `D`; in fact the five atomic coefficients
already sum to zero.

This packet uses the Jordan negative variation of the signed measure in
`dX/X`.  That convention includes the dyadic endpoint atoms of the
extra-notched kernel.  The remaining part of `K_extra` is absolutely
continuous, so it cannot cancel those point masses.  If a consumer removes
endpoint atoms into a separate colour ledger, it must move (0.1) there
explicitly rather than silently treating `K_extra` as an ordinary function.
No claim is made here that the explicit outer endpoint ledger has the same
five atoms.

## 2. The odd prime shell

Fix a small `epsilon>0` and put

\[
\mathcal P_Z=\{p\text{ prime}:Z\le p\le(1+\varepsilon)Z\},
\qquad
\mathcal A_Z=\{a\text{ prime}:Z^2\le a\le(1+\varepsilon)Z^2\}.
\tag{2.1}
\]

For large `Z`, all selected primes are odd and the two intervals are
disjoint.  Set

\[
Y=16(1+\varepsilon)^6Z^{10},
\qquad U=\lfloor Y^{1/6}\rfloor.
\tag{2.2}
\]

If the consumer requires a dyadic horizon, replace the displayed `Y` by the
least dyadic number above it.  This changes `Y` and `U` by fixed factors
only; `U=O(Z^(5/3))<Z^2` and all five atom layers remain inside the new
horizon.  Every exponent below is unchanged.

Then `a>U` and the exact half-source singleton coefficient is

\[
f_U(a)=-1.
\tag{2.3}
\]

Every ordered Wick pair with `p!=q` and `a!=b` has physical product

\[
n=(pa^2)(qb^2),
\tag{2.4}
\]

which is odd and at most `(1+epsilon)^6 Z^10`.  Its negative atoms occur at
`X=2n` and `X=8n`, both below `Y`.  If

\[
2^jn=2^km
\]

for two odd physical products, then comparison of `2`-adic valuations gives
`j=k`.  Thus a negative layer (`j=1,3`) cannot coincide with a positive layer
(`j=0,2,4`).  Coincident representations inside one layer have the same
positive source weight and the same atomic sign, so they reinforce rather
than cancel.

The source coefficient of a pair before the Beta integral is

\[
{\theta^2\over\sqrt{pq}\,ab}>0.
\tag{2.5}
\]

Equations (0.1)--(0.3) therefore give the exact first equality in (0.4).

## 3. Asymptotic size and Wick deletion

Prime number theory in fixed-ratio intervals gives

\[
\sum_{p\in\mathcal P_Z}{1\over\sqrt p}
\asymp {Z^{1/2}\over\log Z},
\qquad
\sum_{a\in\mathcal A_Z}{1\over a}
\asymp {1\over\log Z}.
\tag{3.1}
\]

The unrestricted ordered-pair mass is their product squared, hence
`Z/(log Z)^4`.  Pairs with a shared owner contribute a relative
`O((log Z)/Z)` fraction; pairs with a shared core contribute a relative
`O((log Z)/Z^2)` fraction.  Wick deletion therefore leaves `1-o(1)` of the
weighted mass and proves (0.4).

The corresponding one-half-source diagonal is

\[
\sum_{p,a}{1\over pa^2}
\asymp {Z^{-2}\over(\log Z)^2}=Y^{-1/5+o(1)}.
\tag{3.2}
\]

The negative-atomic-mass/diagonal quotient is consequently

\[
Y^{3/10-o(1)}.
\tag{3.3}
\]

Unlike the earlier positive-spline firewall, this conclusion is already
after the exact literal differential (1.3).  Because of (0.5), it is not
automatically a statement after the explicit conclusion-bearing outer kernel.

## 4. Exact firewall and remaining escape

Let a proposed proof of the literal `D_out` estimate which `T-106150` names
`WKSFSC106150` be **deletion-stable** if it applies with the same subpower
bound after an arbitrary legal coefficient deletion from the owner--core
half-source.  Here legal means retaining actual half-source atoms with their
coefficients, cutoff and prime labels unchanged before applying the same Wick
projection; it does not mean that the deletion is itself a native source
sector.  No such proof can use only:

```text
the injective physical map (p,a) -> p a^2;
the cutoff a>U;
the free source diagonal;
Boolean/Wick removal of shared labels;
the literal extra-notched differential D_out.
```

The prime shell (2.1) is a counterfixture, with negative atomic variation
`Y^(1/10-o(1))`.

For the literal extra-notched object, this leaves one mathematically
substantial source-side escape:

\[
\boxed{
\text{cancellation must occur across distinct source sectors before
the negative part is taken.}}
\tag{4.1}
\]

That cancellation might come from the exact two-large-Moebius
recombination, the connected additive/Kummer subtraction, or another global
arithmetic identity.  It cannot be inferred from the local kernel or source
diagonal alone.  Separately, removing the `Q` and `V` filters to recover the
explicit outer kernel can change the atomic response; this packet makes no
claim about that response.

In particular, the result does **not** establish any of the following:

- failure of the literal `WKSFSC106150` estimate for the complete frozen
  source;
- failure of the explicit outer-current estimate, `SFSC106150`, or
  `REFSIG106150`;
- failure of `WCADD106140`, `WCKUM106140`, or the selected cyclic gate;
- a lower bound for the complete current after all source sectors combine;
- RH or GRH, or their negations.

Those bullets delimit this packet's theorem; they are not a current-frontier
open ledger.  The later
`FFPS_COMPLETE_BETA_ATOMIC_VARIATION_FIREWALL.md` performs the full
complete-source recombination and proves that the raw complete-beta Jordan
premise fails with an `Omega(sqrt(Y))` lower bound.  It does not retroactively
turn this deleted-shell argument into a proof about the explicit native outer
kernel, so the kernel-typing fences above remain in force.

## 5. Proof ledger

Proved exactly:

- the finite signed-measure nature of the differentiated self-convolution;
- the rational Mellin reduction (1.4);
- the exact typing `K_extra=QV K_explicit` and
  `K_740=V K_explicit` relative to the three frozen multiplier formulas;
- all five dyadic atomic coefficients (0.1);
- the exact negative atomic mass (0.2);
- the singleton Beta weight (0.3);
- `2`-adic separation of positive and negative atom layers;
- the source-diagonal and negative-atomic-variation exponents.

Used asymptotically:

- the prime number theorem in fixed-ratio intervals;
- the `1-o(1)` weighted survival of Wick-disjoint pairs.

Still open:

- repair or retyping of the parent explicit-outer/`D_out` adapter;
- the signed atomic response of the explicit outer kernel;
- within this packet, the cancellation or reinforcement of this shell in the
  complete undeleted Boolean source (settled downstream for the raw complete
  beta current by the separate atomic-variation firewall);
- the endpoint-colour bookkeeping if a consumer excludes the extra-notched
  atoms from its negative-part convention;
- every remaining live-source, native-kernel, or fixed-mollified RH-bearing
  gate listed above, excluding the downstream-refuted raw complete-beta
  premise.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_signed_differential_atomic_shell_firewall.py --check
python -B -O research/l-families/atlas/function_field/ffps_signed_differential_atomic_shell_firewall.py --check
python -B -m unittest tests.test_ffps_signed_differential_atomic_shell_firewall
python -B -O -m unittest tests.test_ffps_signed_differential_atomic_shell_firewall
```

The replay uses exact rational arithmetic in `Q(sqrt(2))`.  It enumerates no
prime interval, source atom, conductor family, curve, or point.
