# Independent skeptical reconstruction: coalescing simple roots

Reviewer: spectral/history agent. Date2026-11-17. Task received only the polynomial, triangular reciprocal definition and proposed norm formula. The equivalence-track proof was not read. The director's existing adjudication file was opened only after the coefficient calculation and parent message reporting the independent result; its clustered-root paragraph concerns the compatible optimum Gram calculation. This is a scoped elementary review, not an audit of a source paper.

## Setup made explicit

Let θ∈R, q=e^(−iθ), Pθ(z)=(1−z)(1−qz), N≥1 integer. In H² of the unit disk, use normalized boundary norm so monomials are orthonormal. The reciprocal Taylor coefficients are a_n=∑_(j=0)^n q^j, including q=1 by continuity (then a_n=n+1). Define

    W_N(z)=∑_(n=0)^(N−1) (1−n/N)a_n z^n.

Including n=N with zero weight is identical. Let S_N=∑_(k=1)^N q^k.

## Exact coefficient reconstruction

The recurrence a_n−(1+q)a_(n−1)+q a_(n−2)=0 and the identity (1+q)a_(n−1)−2q a_(n−2)=1+q^n give

    1−Pθ W_N=(1/N)∑_(n=1)^N(1+q^n)z^n−(S_N/N)z^(N+1).

The n=N boundary term follows by using weight zero for a_N; the n=N+1 term is −q a_(N−1)/N. There is no constant residual because a_0=1. Parseval therefore gives exactly

    ||1−Pθ W_N||² = [2N+2Re S_N+|S_N|²]/N².

This independently confirms the claimed formula, with no division by1−q and therefore no missing repeated-root case.

## θ=c/N limit and adversarial cases

For fixed c∈R, the Riemann sum S_N/N→∫_0^1e^(−icx)dx=e^(−ic/2)sinc(c/2), where sinc(x)=sin(x)/x with sinc(0)=1. Consequently

    ||1−P_(c/N) W_N||²→sinc(c/2)².

The 2N and2ReS_N terms are O(N), whereas |S_N|² can be orderN².

- **c=0 / θ=0:** q=1, S_N=N and the exact squared norm is1+4/N. The limit1 is correct. The roots coincide and are no longer simple.
- **c→0 after N→∞:** sinc(c/2)²→1. Arbitrarily close distinct roots can therefore preserve a large limiting triangular error. This does not require using the repeated-root theorem hypothesis incorrectly.
- **c=2π:** for N≥2, q is a nontrivial Nth root of unity, so S_N=0 and the exact squared error is2/N. The triangular construction succeeds on this exceptional scaling. For N=1, q=1; S_1=1 and the squared norm is5, so claiming2/N without excluding N=1 is false.
- **c=2πm≠0:** the vanishing-limit exception also occurs for each fixed nonzero integer m once N does not divide m. Thus one cannot claim every coalescing scaling fails.
- **Fixed θ not a multiple of2π:** S_N stays bounded, so squared error=2/N+Oθ(N^(−2)). The hidden constant blows up asθ→0; this is exactly the nonuniformity being exposed.

## Independent optimal-approximation check

Restrict Q to degree≤N−1. A residual R=1−PθQ has degree≤N+1. For distinct roots it is feasible iff R(1)=R(q^(−1))=1. Put d=N+2 and

    T=∑_(k=0)^(N+1)e^(ikθ).

The two evaluation vectors have Gram diagonal d and off-diagonal T or its conjugate. Since the roots are distinct, |T|<d. Minimizing the coefficient norm under the two linear evaluation constraints yields

    min_Q ||1−PθQ||²=(2d−2ReT)/(d²−|T|²).

For θ=c/N with fixed c≠0,

    N·min_Q ||1−PθQ||² →
    [2−2sin(c)/c] / [1−sinc(c/2)²].

This is finite for every fixed c≠0 and tends4 as c→0. Hence the **optimal squared error is O_c(1/N)** even where the triangular squared error tends a positive constant. The optimal norm itself is O_c(N^(−1/2)), not O(1/N); terminology must preserve this distinction.

For the exact repeated-root case, feasibility is R(1)=1,R′(1)=0. With coefficients indexed0,…,d−1, the Gram entries are d, d(d−1)/2 and d(d−1)(2d−1)/6. Solving the2×2 normal equations gives

    min_Q ||1−(1−z)²Q||²=2(2d−1)/[d(d+1)], d=N+2,

again asymptotic4/N. This also verifies that the confluent limit of the distinct-root optimizer is well behaved.

At c=2π the optimal limit coefficient is2, matching triangular performance to first order. The optimal coefficient function is not necessarily confined to[2,4]: near c just above2π, sin(c)>0 while the denominator differs from1 only quadratically, so the ratio can be below2. No monotonicity claim was needed or established.

## Verdict and limits

Finding class: **independently checked with no issue found in the inspected portion**, after explicit qualification of exceptional c and norm versus squared norm. This is a nonuniform-family obstruction to extending a fixed-polynomial asymptotic uniformly as two roots merge. It is not an error in a theorem that fixes a polynomial with simple roots, and it is not yet a claim about the zeta Nyman–Beurling space. A publishable transfer would need a justified map from its actual approximation geometry to this clustered-root local model, with uniform control of all remaining factors.
