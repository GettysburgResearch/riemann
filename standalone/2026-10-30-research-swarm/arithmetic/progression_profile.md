# Constructive continuation: an arithmetic profile compensator

Status: **PROVED IDENTITIES AND FIXED-SCALE ASYMPTOTIC; target-strip error estimate open.**  
This extends the frozen `report.md` (SHA256 `eb23e9351638b31ac19ff581e176473412208687142929d647447bbe2d91bbae`). It does not revise its proofs or claim a zero-free improvement. The standard external analytic inputs for the new fixed-scale asymptotic are the prime number theorem in each fixed reduced progression and Brun–Titchmarsh. They are stated where used; neither RH nor a uniform square-root progression estimate is assumed.

## 1. The safe convergence range is actually Re s>1

The exact character identity is

$$D_q(s)=-\varphi(q)\sum_{n\equiv1\ (q)}\Lambda(n)n^{-s},\qquad \Re s>1.$$

For σ>1, Λ(n)≤log n and n=mq+1 give

$$
|D_q(s)|\le q^{1-\sigma}
\left[(\log q+\log(3/2))\zeta(\sigma)-\zeta'(\sigma)\right].
$$

Here mq+1≤(3/2)mq for q≥2 and m≥1. Therefore, uniformly in Im s,

$$
T_Q(s)=\frac1{Q-1}\sum_{q=2}^{Q}D_q(s)
=\begin{cases}
O_\sigma(Q^{1-\sigma}\log Q),&1<\sigma<2,\\
O(\log^2Q/Q),&\sigma=2,\\
O_\sigma(1/Q),&\sigma>2.
\end{cases}
$$

This is convergence of the normalized finite average. It does not assert that the unnormalized infinite sum over q converges for 1<σ≤2. The shifted-zeta sum in the original report still has absolute convergence domain Re s>2.

## 2. Exact removal of the known real pole

Write ψ(x;q,1)=Σ_{n≤x,n≡1 mod q}Λ(n), and define

$$
\Psi_Q(x)=\frac1{Q-1}\sum_{q=2}^{Q}\varphi(q)\psi(x;q,1),
\qquad
M_Q^{(0)}(x)=\frac1{Q-1}\sum_{q=2}^{Q}(x-q)_+.
$$

The terms q>x vanish in both definitions: n≡1 mod q has no nonzero von Mangoldt term at n≤q. Thus this is a causal cutoff, with no silently omitted large moduli.

Put

$$
C_Q^{(0)}(s)=\frac1{Q-1}\sum_{q=2}^{Q}\frac{q^{1-s}}{s-1},
\qquad R_Q^{(0)}(s)=T_Q(s)+C_Q^{(0)}(s).
$$

Every D_q has residue −1 at 1. Every compensator summand has residue +1 there. Consequently R_Q^(0) is regular at 1 and retains all the positive zero residues elsewhere in Re s>0. For Re s>1, Stieltjes integration and integration by parts give the exact identity

$$
\boxed{\displaystyle
R_Q^{(0)}(s)=-s\int_1^\infty
[\Psi_Q(x)-M_Q^{(0)}(x)]x^{-s-1}\,dx.}
$$

The individual version is

$$
D_q(s)+\frac{q^{1-s}}{s-1}
=-s\int_1^\infty
[\varphi(q)\psi(x;q,1)-(x-q)_+]x^{-s-1}\,dx.
$$

All boundary terms vanish: the bracket is zero at 1 and O_q(x) at infinity, while σ>1.

### Exact small-x switching

When 2≤x≤Q+1, every divisor of n−1 is at most Q. Hence

$$
(Q-1)\Psi_Q(x)=\sum_{n\le x}(n-2)\Lambda(n).
$$

Let r(x)=ψ(x)−x and v={x}. A direct partial summation gives

$$
\boxed{\displaystyle
(Q-1)[\Psi_Q(x)-M_Q^{(0)}(x)]
=(x-2)r(x)-\int_2^x r(y)\,dy
-\frac x2+1+\frac{v^2-v}{2}.}
$$

This treats q>x exactly and obtains cancellation before applying any progression estimate. In particular, if |r(y)|≤E(y), the absolute error is at most

$$
\frac{xE(x)+\int_2^xE(y)dy+x/2+2}{Q-1}.
$$

For x=uQ with fixed 0<u≤1, ordinary PNT gives error o(Q). This is a genuine averaged bound unavailable from replacing each individual progression by its full main term x/φ(q) before its first possible prime.

## 3. The first transition reveals a deterministic drift

The naive cutoff is not the complete arithmetic main term when x and Q are comparable. The missing divisor sum is exactly

$$
\sum_{n\le x}\Lambda(n)\sum_{\substack{q\mid n-1\\q>Q}}\varphi(q)
=\sum_{k<(x-1)/Q}\ \sum_{Q<q\le(x-1)/k}\varphi(q)\Lambda(kq+1).
$$

This suggests computing weighted primes along the fixed linear polynomial kq+1.

### Lemma: fixed-k weighted prime asymptotic

For every fixed positive integer k,

$$
\sum_{m\le Y}\varphi(m)\Lambda(km+1)
=\frac{C(k)}2Y^2+o_k(Y^2),
$$

where

$$
A=\prod_p\left(1-\frac1{p(p-1)}\right),\qquad
C(k)=A\prod_{p\mid k}\frac{p^2-1}{p^2-p-1}.
$$

The constant A is the usual Artin Euler product. No primitive-root conjecture is being assumed here.

**Proof.** Proper prime powers contribute O_k(Y^(3/2)log²Y), which is o(Y²). For prime values, expand

$$\varphi(m)=m\sum_{d\mid m}\frac{\mu(d)}d.$$

For each fixed d, the prime number theorem in the progression 1 modulo kd and partial summation yield

$$
\sum_{\substack{m\le Y\\d\mid m\\km+1\ \mathrm{prime}}}
m\log(km+1)
\sim\frac{kY^2}{2\varphi(kd)}.
$$

To justify the infinite d-sum, first fix a cutoff D. For D<d≤√Y, Brun–Titchmarsh gives the upper bound O_k(Y²/φ(kd)) for the inner sum, uniformly in this range. The weighted tail is therefore bounded by

$$O_k\left(Y^2\sum_{d>D}\frac1{d\varphi(d)}\right),$$

which tends to zero relative to Y² as D→∞. We used φ(kd)≥φ(k)φ(d). For d>√Y, the elementary bound Λ(km+1)≤log(kY+1) gives a total O_k(Y^(3/2)logY+Ylog²Y)=o(Y²). These estimates justify first sending Y→∞ with D fixed, then D→∞.

Thus C(k)=kΣ_d μ(d)/(dφ(kd)). Factoring this absolutely convergent sum prime by prime gives the displayed product. For p dividing k, the factor relative to A is (p²−1)/(p²−p−1). ∎

### The fixed-scale profile

For every fixed real u>0,

$$
\boxed{\displaystyle
\frac{\Psi_Q(uQ)}Q\longrightarrow
P(u)=\frac12\left[u^2-\sum_{1\le k<u}
C(k)\left(\frac{u^2}{k^2}-1\right)\right].}
$$

**Proof.** The complete divisor sum has main term (uQ)²/2. Its missing part is the preceding exact switched sum, involving finitely many k<u. Apply the fixed-k lemma to the interval (Q,uQ/k]. Divide by Q(Q−1). Integer endpoint effects are o(1) after normalization. ∎

**Compact uniformity.** The convergence is uniform for 0≤u≤B for each fixed B: both normalized cumulative functions are nondecreasing in u, P is continuous, and a finite grid from uniform continuity sandwiches every intermediate value. This uses no estimate for u growing with Q. Consequently, for any fixed 0<a<b<∞, the Mellin transform of the corrected error restricted to aQ≤x≤bQ is o(Q^(1−Re s)), uniformly when s ranges over a fixed compact set. The two unbounded endpoint regions remain separate obligations.

For 0<u≤1, P(u)=u²/2. For 1<u≤2,

$$P(u)=\frac{(1-A)u^2+A}{2}.$$

Meanwhile M_Q^(0)(uQ)/Q→u−1/2 for u≥1. Their difference on this first transition is

$$
P(u)-(u-1/2)=\frac{(u-1)[(1-A)u-(1+A)]}{2}.
$$

It is strictly negative immediately after u=1. For example, at the fixed scale u=1+A∈(1,2), it equals −A²(1+A)/2. Therefore the naive progression compensator has an **unconditional error of order Q** on part of the first transition interval. One cannot assume it is already o(Q) throughout x≈Q.

This identifies and removes a concrete false target before investing in a much harder cancellation estimate.

## 4. An explicit compensator matching the arithmetic profile

Let

$$
\mathcal C(s)=\sum_{k\ge1}\frac{C(k)}{k^s}
=A\zeta(s)G(s),\qquad
G(s)=\prod_p\left(1+\frac{p^{1-s}}{p^2-p-1}\right).
$$

The Dirichlet-series identity initially holds for Re s>1. The auxiliary Euler product G converges absolutely and locally uniformly for Re s>0, so the right-hand side continues meromorphically there, with only the possible pole at 1. Zeros of G are harmless; no reciprocal of G or ζ occurs.

Two exact normalizations are

$$\operatorname{Res}_{s=1}\mathcal C(s)=1,
\qquad \mathcal C(2)=\sum_{k\ge1}\frac{C(k)}{k^2}=1.$$

Both follow by multiplying the positive Euler factors. The latter identity rewrites the profile as

$$
P(u)=\frac12\left[u^2\sum_{k\ge u}\frac{C(k)}{k^2}
+\sum_{k<u}C(k)\right],
\qquad
P'(u)=u\sum_{k\ge u}\frac{C(k)}{k^2}
$$

away from integer u. In particular P is continuous and increasing. To justify growth without a Tauberian assumption, write C(k)=AΣ_{d|k}g(d), where g is nonnegative, supported on squarefree integers, and g(p)=p/(p²−p−1). Then Σ_d g(d)/d=G(1)=1/A. Consequently Σ_{k≤v}C(k)≤v exactly, and dominated convergence gives Σ_{k≤v}C(k)∼v. Partial summation in the displayed profile even yields P(u)≤u. Thus all model integrals below have the stated convergence. For 1<Re s<2, Tonelli/absolute convergence gives

$$
\int_0^\infty u^{-s}\,dP(u)
=\frac{\mathcal C(s)}{2-s}.
$$

To match the lower integration limit 1, define

$$
M_Q^*(x)=QP(x/Q)-\frac1{2Q},\qquad x\ge1,
$$

so M_Q^*(1)=0. Its Mellin–Stieltjes transform is

$$
\boxed{\displaystyle
C_Q^*(s)=\frac{Q^{1-s}\mathcal C(s)-Q^{-1}}{2-s}.}
$$

The transform identity is initially obtained for 1<Re s<2. The subtraction removes the contribution of 0<x<1, where QP(x/Q)=x²/(2Q). At s=2 the apparent singularity is removable because C(2)=1. Analytic continuation through that removable point identifies the same transform on the full half-plane Re s>1, where the integral from 1 converges. At s=1 the residue is +1. Apart from that known real pole, C_Q^* is holomorphic on Re s>0. In particular, it has no pole at a nontrivial zeta zero.

Thus

$$R_Q^*(s)=T_Q(s)+C_Q^*(s)$$

is regular at 1 and retains the same positive zero residues as T_Q. It tends to zero on compact subsets of Re s>1. For Re s>1 its exact source is

$$
\boxed{\displaystyle
R_Q^*(s)=-s\int_1^\infty
[\Psi_Q(x)-M_Q^*(x)]x^{-s-1}\,dx.}
$$

For every fixed u>0, the error in brackets at x=uQ is o(Q). The order-Q first-transition drift of the naive compensator is gone by an explicit, source-derived correction. This statement includes the finite k divisor switches; it does not silently replace them by a continuum prime model.

## 5. What remains and why it is a useful target

The limiting profile is unconditional. It supplies no power saving or uniform control when u grows with Q, and fixed-u o(Q) is not enough to move the Mellin estimate below Re s=1. At σ<1 an o(Q) transition error can still produce o(Q^(1−σ)), which need not tend to zero.

The remaining task is therefore precise: control the Mellin transform of

$$\Psi_Q(x)-QP(x/Q)+1/(2Q)$$

uniformly on the desired contours, with the small-x block, each fixed-ratio transition, and the unbounded x/Q tail all retained. A suitable contour bound below the integer zero-count threshold from `report.md` would exclude a zeta zero. The correction itself does not provide that bound, and analytic continuation of its defining integral cannot be assumed from the fixed-scale asymptotic.

This is a concrete arithmetic detector with the known pole and its nontrivial divisor profile explicitly removed. Its auxiliary Euler product is absolutely convergent throughout Re s>0, while the entire unresolved signed content remains in an identified progression-error source. That gives a more specific next attack than an unspecified family average.

## 6. Finite-scale experiment

`profile_experiment.py` uses ordinary floating-point von Mangoldt weights and an Artin product truncated at primes up to 1,000,000. It is illustrative, not an interval certificate. The exact infinite product, rather than its decimal approximation, defines the theorem.

For Q=20,000 the observed normalized progression statistic gives:

| u | Ψ_Q(uQ)/Q | Arithmetic profile P(u) | Error from naive cutoff model |
|---|---:|---:|---:|
| 1.25 | 0.675445 | 0.676075 | −0.074505 |
| 1.50 | 0.888098 | 0.891278 | −0.111852 |
| 1.75 | 1.145463 | 1.145608 | −0.104487 |
| 2.00 | 1.439018 | 1.439066 | −0.060932 |

The new profile removes the large deterministic drift in this finite example. The complete output also includes smaller Q, u up to 4, and the fixed-k weighted-prime constants. These measurements are not used to prove convergence or a power-saving error; the proof in Section 3 is the source for the fixed-scale limit.
