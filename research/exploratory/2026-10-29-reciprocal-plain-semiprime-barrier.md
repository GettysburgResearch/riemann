# Absolute reciprocal–plain convolution has a full-scale semiprime tail

**Status:** Elementary exact obstruction; independently reviewed for the algebra and prime-counting argument. It does not prove a zero-free region, does not rule out cancellation in the signed Dirichlet polynomial, and makes no claim of external novelty.

**Scope:** Sharp truncated and nonnegative annular Möbius and ordinary Dirichlet sums with the same Dirichlet character. The arithmetic input is the prime number theorem in fixed-proportion intervals. The statement is an all-large-scale lower bound on an *absolute coefficient sum*, not a numerical or a zero-density estimate.

## Theorem

For real `2<=A<=B`, let

    M_A(s,chi) = sum_(d<=A) mu(d) chi(d) d^(-s),
    S_B(s,chi) = sum_(m<=B) chi(m) m^(-s),
    a_(A,B)(n) = sum_(d|n, d<=A, n/d<=B) mu(d).

Let `chi` be a Dirichlet character modulo `q`. For all sufficiently large `A`, if at most half the primes in each of `(A/2,A]` and `(B/2,B]` divide `q`, then

    sum_(n>B) |chi(n) a_(A,B)(n)| / sqrt(n)
       >> sqrt(A B) / (log A log B),

with an absolute implied constant. In particular this holds uniformly for `q<=U^C`, `A=U^r`, `B=U^m`, with fixed `0<r<=m`, fixed `C>0`, and sufficiently large `U`.

The finite Dirichlet polynomial identity is

    M_A(s,chi) S_B(s,chi)
      = sum_(n<=AB) chi(n) a_(A,B)(n) n^(-s).

Its coefficients agree with `1` at `n=1` and vanish at `2<=n<=A`; the theorem identifies a large part of the later coefficient tail.

## Proof

Complete multiplicativity of `chi` gives the product identity, including zero values at primes dividing `q`. For `n<=A<=B`, both cutoff conditions hold for every divisor of `n`, hence `a_(A,B)(n)=sum_(d|n)mu(d)`, giving the initial cancellation.

Take distinct primes `p in (A/2,A]` and `r in (B/2,B]`, neither dividing `q`. For large `A`, `pr>AB/4>B` and `pr<=AB`. The divisor `d=1` is excluded by `pr>B`; `d=pr` is excluded by `pr>A`; and `d=p` is allowed. The remaining divisor `d=r` is allowed exactly when `r<=A`. Consequently

    a_(A,B)(pr) = -1 - 1_(r<=A),

and `|chi(pr)|=1`. These coefficients therefore have absolute value at least one. There are at least a positive constant times `(A/log A)(B/log B)` ordered admissible pairs: prime counting supplies that many primes in each interval, at most half are removed by the conductor hypothesis, and deleting the diagonal costs at most the size of the smaller prime set. Each resulting semiprime has at most two ordered representations. Since `1/sqrt(pr)>=1/sqrt(AB)`, summing these distinct terms proves the displayed lower bound.

For `q<=U^C`, the number of distinct prime divisors of `q` is at most `C log U/log 2`. This is negligible compared with the number of primes in either interval when `A=U^r`, `B=U^m` and `r>0` are fixed, so the conductor condition holds uniformly for all large U. Constants and thresholds may depend on `r,m,C`.

## Nonnegative annular windows

Let `V,W` be any fixed nonnegative, nonzero continuous functions with compact support in `(0,infinity)`, and define the annular coefficient

    a_(V,W;A,B)(n) = sum_(d|n) mu(d) V(d/A) W((n/d)/B).

There exist fixed intervals `[v1,v2]` and `[w1,w2]` inside `(0,infinity)` and a constant `c0>0` on which `V` and `W`, respectively, are at least `c0`. For distinct primes `p` in `[v1 A,v2 A]` and `r` in `[w1 B,w2 B]`, the divisors `1` and `pr` contribute zero to `a_(V,W;A,B)(pr)` once `A,B` are large: `V(1/A)=0` and `pr/A` tends uniformly to infinity. The remaining two terms are nonpositive, and the `d=p` term is at most `-c0^2`. Thus

    |a_(V,W;A,B)(pr)| >= c0^2.

The same prime-counting and two-to-one argument now gives

    sum_n |chi(n) a_(V,W;A,B)(n)| / sqrt(n)
       >>_(V,W) sqrt(A B) / (log A log B)

for fixed windows, large scales and the analogous condition that conductor primes remove at most half of either fixed-proportion prime interval. It holds uniformly for polynomially bounded conductors and polynomial scales as above. This does not assume that the two prime intervals are disjoint. It does require nonnegative real windows; arbitrary signed, complex or row-dependent detector profiles can destroy the indicated sign and are not covered.

## Consequence for detector-product arguments

In centrally normalized witnesses of lengths `A=U^r`, `B=U^m`, the direct triangle bound at `s=1/2+it` contains the absolute coefficient sum above, which is at least `U^((r+m)/2-o(1))`. A source normalization `A^(-1/2) W(n/A)` is converted exactly to `n^(-1/2) V(n/A)` by taking `V(x)=sqrt(x) W(x)`; this preserves nonnegativity and compact annular support. Simultaneous lower spikes of the usual form `|M_A|^2 >= U^(delta r-o(1))` and `|S_B|^2 >= U^(delta m-o(1))` require only a product of size `U^(delta(r+m)/2-o(1))`. For fixed `delta<1`, the absolute coefficient bound is asymptotically larger, so *that triangle-inequality route alone* cannot contradict the spikes. Any improvement through the product must retain cancellation in the signed coefficients or their oscillatory phases, use additional arithmetic structure, or change the detector; the theorem does not say such an improvement is impossible.

The sharp-cutoff and nonnegative-window results do not assert such a lower bound for arbitrary signed, complex or row-dependent smooth profiles, nor uniformity when the conductor can include a positive proportion of all primes in a relevant short interval. Their novelty relative to the literature has not been checked.
