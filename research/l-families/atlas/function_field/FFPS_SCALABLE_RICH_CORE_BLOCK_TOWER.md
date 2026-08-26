# A scalable native rich-core block tower

Status: **exact all-rank source identity on the declared rich subsource,
exact formal leverage/density frontier; no varying-place complex, signed
family estimate, complement bound in the full FFPS source, RH, or GRH**

Exact bounded replay:
[`ffps_scalable_rich_core_block_tower.py`](ffps_scalable_rich_core_block_tower.py).

The source locks are the four blobs recorded in
`FFPS_FOUR_PHASE_RICH_CORE_SOURCE.md`; the all-rank theorem iterates that
same every-divisor argument and introduces no new source assumption.

## 0. Outcome

The four-phase construction is not an isolated trick.  It extends to an
arbitrarily high block rank inside one native current.

Let

\[
 N=Pg^2c^2,\qquad M=Qg^2d^2
\]

be one clean bilateral source atom.  Put

\[
 \omega_1(n)=\#\{p\mid n:p\equiv1\pmod4\}.
\]

On the rank-`r` rich subsource

\[
 \omega_1(c)\ge r,\qquad\omega_1(d)\ge r,
\tag{0.1}
\]

choose the first `r` eligible divisors on each side,

\[
 \ell_1,\ldots,\ell_r\mid c,
 \qquad
 \rho_1,\ldots,\rho_r\mid d.
\]

The upstream squarefree common-core extraction and owner/core renewal imply
that every `ell_i` divides `N` but not `M`, and every `rho_i` divides `M` but
not `N`.  Multiplying the `2r` nonzero prime Ramanujan identities gives

\[
 \boxed{(-1)^{2r}=1.}
\tag{0.2}
\]

All phases occur before one common square.  Pair them crosswise into blocks

\[
 \tau_i=\epsilon_{\ell_i}(Qd^2)
         \epsilon_{\rho_i}(Pc^2),\qquad 1\le i\le r.
\tag{0.3}
\]

For every nonempty `S subset {1,...,r}`, the quotient mode
`tau_S=product_(i in S)tau_i` contains at least one nonprincipal phase on
each source side.  The full selected quotient `C_2^r` is therefore bilateral.

Each block contracts by

\[
 L_{p,q}={4(p-1)(q-1)\over5pq+p+q+1}<{4\over5},
\tag{0.4}
\]

so the formal hard leverage obeys

\[
 \boxed{L_r=\prod_{i=1}^rL_{\ell_i,\rho_i}<\left({4\over5}\right)^r.}
\tag{0.5}
\]

More surprisingly, `r` can grow with the core range in the ambient
logarithmic measure.  If

\[
 r=\lfloor\alpha\log\log x\rfloor,
 \qquad0<\alpha<{1\over2},
\tag{0.6}
\]

then the relative logarithmic mass of squarefree cores failing (0.1) is at
most

\[
 \boxed{(\log x)^{-c(\alpha)+o(1)},\qquad
 c(\alpha)={1\over2}-\alpha+\alpha\log(2\alpha)>0,}
\tag{0.7}
\]

while

\[
 \boxed{L_r<(\log x)^{-\alpha\log(5/4)+o(1)}.}
\tag{0.8}
\]

Thus the formal architecture can obtain a genuine power-of-log leverage gain
on an ambient log-density-one subsource, while, for each **fixed** common
place degree `e`, the separate equal-degree path model has only
`O_e((log log x)^2)` normalized selected-energy rank.

This is the first scalable source construction in the branch.  It remains a
candidate, not an RH estimate: the full Boolean source may correlate with
factor richness, and the signed varying-place trace is still open.

## 1. Exact all-rank source identity

The four-phase packet proves the divisor extension carefully.  In brief,
the pre-extraction squarefree cores are `a=gc,b=gd`, with

\[
 (g,cd)=(c,d)=1,
 \qquad(c,Q)=(d,P)=1.
\tag{1.1}
\]

Therefore every selected divisor on the `c` side supplies a nonzero phase
against `M`, and conversely on the `d` side.  Choosing the first `r` eligible
divisors is canonical and introduces no phase-choice multiplicity.

At all `2r` moduli one retains the owner quadratic-sector labels

\[
 \kappa_{\ell_i}(Q)=\sigma_i,
 \qquad\kappa_{\rho_i}(P)=\tau_i^{\rm owner}.
\tag{1.2}
\]

These make each physical orientation a function of `Qd^2` or `Pc^2`, not of
an owner presentation.  The selected block characters in (0.3) use one
factor from each side.  Products of blocks preserve that property, proving
the bilateral assertion for all `2^r-1` modes.

No tensor product of already-squared currents appears.  The operation order
is

```text
one source atom
 -> 2r nonzero Ramanujan phases
 -> complete 2r-fold Mellin transform
 -> hard C2^r quotient restriction
 -> one common square / Wick cleanup.
```

## 2. Uniform contraction

The two-prime block formula is exact.  Comparing it to `4/5` gives

\[
 5\cdot4(p-1)(q-1)
 <4(5pq+p+q+1)
\]

because the right side minus the left side is
`4(6p+6q-4)>0`.  This proves (0.4), uniformly over all eligible primes.
Multiplicativity of disjoint block leverage then proves (0.5).

The bound is sharp as a uniform asymptotic statement: `L_(p,q)` approaches
`4/5` as both primes tend to infinity.  A stronger constant cannot hold for
all blocks.

## 3. Growing-rank density theorem

For `0<t<1`, the positive squarefree Euler product and Mertens in the two
reduced classes modulo four give, uniformly for `0<=t<=1`,

\[
 \sum_{n\le x}{\mu^2(n)t^{\omega_1(n)}\over n}
 \ll(\log x)^{(1+t)/2}.
\tag{3.1}
\]

If `omega_1(n)<r`, then

\[
 1\le t^{-(r-1)}t^{\omega_1(n)}.
\]

Choose `r` as in (0.6) and `t=2alpha`.  After division by

\[
 \sum_{n\le x}{\mu^2(n)\over n}
 \asymp\log x,
\]

the logarithm of the upper bound, divided by `log log x`, is

\[
 -{1-2\alpha\over2}-\alpha\log(2\alpha)+o(1)
 =-c(\alpha)+o(1).
\]

This proves (0.7).  The function is positive on `(0,1/2)` and vanishes at
the natural mean boundary `alpha=1/2`.

For coprime pairs `(c,d)`, dropping coprimality upper-bounds the union of the
two bad events, while the squarefree coprime-pair denominator is
`asymp (log x)^2`.  Hence the same exponent applies when both sides are
required to be rich.

Substituting (0.6) into (0.5) proves (0.8).

## 4. The formal density/leverage frontier

Two exponents compete:

\[
 c(\alpha)={1\over2}-\alpha+\alpha\log(2\alpha),
 \qquad
 \lambda(\alpha)=\alpha\log(5/4).
\tag{4.1}
\]

Balancing them gives the diagnostic point

\[
 \alpha_*\approx0.274064461784,
 \qquad c(\alpha_*)=\lambda(\alpha_*)\approx0.061155717291.
\tag{4.2}
\]

The fixture records a higher-precision bounded solve.  This is not an
optimization theorem for FFPS: it ignores Betti growth, the sizes of the
selected phase primes, conductor recombination, and the complementary
current.  It is a clean target for a future joint analytic budget.

## 5. Complexity and atomic ledgers

The quotient has `2^r-1` selected modes.  Exponential mode count is not by
itself the normalized cohomological cost.  In the separate endpoint-disjoint
equal-degree path model, the exact averages are

\[
 \overline b_1=er-2+{er\over2^r-1},
 \qquad
 \overline{b_1^2}
 =e^2r^2+(e^2-4e)r+4+O_e(r^2 2^{-r}).
\tag{5.1}
\]

For fixed `e` and `r asymp log log x`, the latter is
`O_e((log log x)^2)`.  This is only a complexity candidate: the native phase
places have varying degrees and have not been assembled into that path
complex.  No bound uniform in their degrees, nor any comparison between
those degrees and `x`, is asserted.

There is a favorable formal atomic check.  The product of all selected phase
primes divides `cd`, so under the natural generalized source-dual weight

\[
 g^2\prod_i\ell_i\rho_i
\]

the principal atomic coefficient is at most

\[
 {C_r\over g^2cdPQ},
 \qquad
 C_r=\prod_{p\text{ selected}}{p+1\over p-1}.
\tag{5.2}
\]

The `2r` selected primes are distinct.  The product is largest on the first
`2r` primes congruent to one modulo four.  Mertens and the prime number
theorem in that progression give

\[
 \boxed{C_r\ll\log(2r).}
\tag{5.3}
\]

Indeed, `log C_r` is `2 sum 1/p+O(1)` over those primes, hence
`log log p_(2r)+O(1)`, while `p_(2r) asymp r log r`.  At
`r asymp log log x`, this is only `O(log log log x)`, far smaller than a
power of `log x`.

The generalized source-dual moment and its global summation have not been
proved, so (5.2)--(5.3) are an acceptance test rather than a claimed FFPS
estimate.  They do show that the obvious principal-weight product does not
algebraically erase the leverage gain.

The off-coset interferometer itself is literally atom-free.  The harder
obstruction is its positive selected energy and the weight-two countermodel:
the three, then exponentially many, selected modes must remain in one signed
trace rather than be bounded separately.

## 6. What this opens

The scalable theorem turns the next RH-facing question into a quantitative
one:

> Can the complete rich-core relative trace be bounded with a loss smaller
> than the power-of-log gain in (0.8), while the complementary current costs
> no more than (0.7)?

An affirmative answer still needs principal extraction, but the exact
identity `P=C-S` already supplies the algebraic subtraction once both objects
live on a common source base.

The most useful next experiments are:

1. construct the `2r`-place function-field trace complex for slowly growing
   `r`, with irreducible-place projectors included;
2. determine whether its relative hard-minus-selected class has Betti cost
   polynomial in `r` after common invariant cancellation;
3. prove an FFPS-weighted analogue of (0.7) for the actual Boolean source;
4. test whether the product of the first `r` eligible phase primes introduces
   a hidden source-dual loss not visible in the ambient count.

## 7. Proof ledger

Proved exactly or by the stated standard Mertens input:

- the all-rank source partition and `2r`-phase identity;
- bilateral support of every selected quotient mode;
- the uniform leverage bound (0.5);
- the ambient growing-rank density exponent (0.7);
- the formal power-of-log leverage (0.8);
- the density/leverage diagnostic frontier.

Not proved:

- rich-core density in the fully weighted FFPS source;
- the generalized source-dual moment;
- a common varying-place complex or uniform Betti theorem;
- the signed family estimate, complement bound, principal theorem, RH, or
  GRH.

## 8. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_scalable_rich_core_block_tower.py --check
python -B -O research/l-families/atlas/function_field/ffps_scalable_rich_core_block_tower.py --check
python -B -m unittest tests.test_ffps_scalable_rich_core_block_tower
python -B -O -m unittest tests.test_ffps_scalable_rich_core_block_tower
```

The replay evaluates eight exact rational block factors and an 80-step scalar
bisection.  It enumerates no source atoms, conductors, curves, or points.
