# Universal selectors for fixed-order Hecke families

**Status:** Elementary fixed-order selector and operator counterexamples, with additional squarefree-source counterexamples conditional on the cited lower-bound preprints. They concern broad arbitrary-ideal slot interfaces; they do not refute a prime-only physical slot estimate or prove a zero-free region. No priority claim is made.

Fix n≥2, a number field K containing μ_n, and a fixed finite bad-prime set S containing primes above n. For n≥3 use the n-th-order family χ_a(b) of [De Faveri §§1–2](https://arxiv.org/abs/2610.04045v1); for n=2 use the standard quadratic-residue family with the same order-two and zero-extension properties. The row index a and source b are integral ideals away from S; the character is zero at primes dividing its original modulus, including the row ideal. Let A>0 and `0≤s<1/n`. For every positive early mesh choose a fixed width `0<w<mesh`, and a fixed width floor at most w. For sufficiently large Z put `X=Z^w` and let p range over good prime ideals with `R≤Np≤2R`, where `R=X^(1/n)/2`. If their number is N, define

    Q_Z(a) = N^(−1/2) Σ_p χ_a(p^n).                     (1)

The ordinary slot sources p^n have norm at most X and coefficient squared mass one. By source multiplicativity and the zero extension,

    χ_a(p^n)=1_(p∤a).                                   (2)

Indeed χ_a has order dividing n at good primes not dividing a, and vanishes at p|a. The prime ideal theorem gives `N≫X^(1/n)/log X`, whereas any row with `Na≤Z^A` has at most `A log Z/log R=O(A/w)` prime divisors in the window. Uniformly on **every** such row,

    |Q_Z(a)|² ≫ X^(1/n)/log X ≥ X^s                   (3)

for sufficiently large Z. The width, floor, source set and coefficient vector respect the original order of choices: the mesh precedes w, and w precedes the growing parameter Z. The slots are n-th powers of primes, not prime-only slots. Source masks and any fixed row ray class are retained.

Consequently, no uniform broad-source selected operator estimate

    ||K_{F,Sources}||² ≪ Z^ε (L+Y^(1−s)L^s)             (4)

can hold at `0<s<1/n` even if F is restricted to n-th-power-free or squarefree good ideals of norm at most Y=Z. Take F to be the good prime ideals of norm ≤Y, for which `#F≫Y/log Y`, and take the unit ideal as sole dual source, L=1. Every prime row is selected by (3), and its unit-source matrix entry is one. The squared norm is `#F`, contradicting (4) for any `ε<s`. This argument is entirely elementary apart from prime ideal counting and applies for every fixed n≥2. It does not assert anything about rows satisfying additional detector-zero constraints.

At the balanced dual scale there is also a source-independent rank-one obstruction: take as dual sources `q^n` for good prime ideals q with `Nq≤(Y/4)^(1/n)`, and take rows to be good prime ideals a with `Y/2≤Na≤Y`. All these pairs are coprime for large Y, so (2) makes the matrix identically one. Its squared norm is

    ≫ Y^(1+1/n)/(log Y)²,                                (5)

whereas the right side of (4) at L=Y is `O(Z^ε Y)`. Thus the balanced estimate fails for any small enough loss even with squarefree prime rows, without using a sharp large sieve. This also includes the endpoint s=0, unlike the unit-source contradiction.

## Balanced counterexamples with squarefree dual sources

In three standard families, a stronger structural point follows from known **squarefree-row and squarefree-column** lower bounds. The universal selector (1) selects all of the rows in those lower-bound matrices, while their dual sources are already squarefree. Therefore (4) fails at L=Y even if arbitrary n-th-power dual sources are forbidden:

* Cubic characters over Q(ζ₃): de Faveri–Dunn–Hoffstein, [*Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*, arXiv:2607.07911](https://arxiv.org/abs/2607.07911), give squared operator norm `≫_ε Y^(4/3−ε)` for the Heath-Brown family. The exact family and bound are also quoted as (1.6) in [De Faveri](https://arxiv.org/abs/2610.04045v1).
* Quartic characters over Q(i): the same preprint gives `≫_ε Y^(5/4−ε)` for its natural quartic family, quoted as De Faveri (1.7).
* Sextic characters over Q(√−3): [Xu–Sang, arXiv:2610.17675v2, Theorem 1.1](https://arxiv.org/abs/2610.17675v2) give `≫_ε Y^(7/6−ε)` for their squarefree matrix. Their Remark 2.1 identifies its primary family with De Faveri's selected conventions.

Here n=3,4,6 respectively, and all three have exponent `1+1/n`. The first two lower bounds are stated for the specific source families, not for an arbitrary fixed-order family or arbitrary choice of S; the third is for the fixed good-prime set in its theorem. Each source's family orientation, character labels, and zero masks must be used as stated. The squarefree lower bounds are recent preprints, not independently verified here. They show that discarding high-power **dual** sources alone cannot repair the broad selected-norm conjecture at these low slopes: the damaging sixth/n-th-power structure can instead reside in the selecting slot.

**Independent review:** A second researcher checked the uniform power-slot selector, fixed-width quantifier order, unit and balanced rank-one obstructions, and the precise cubic, quartic and sextic source families and squarefree lower bounds. The cited lower-bound preprints themselves were not independently established.
