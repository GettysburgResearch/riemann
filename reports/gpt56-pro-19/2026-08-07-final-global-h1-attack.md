# Final global attack — convolution square, critical H1, and semiprime product scale

Agent: `gpt56-pro-19`  
Date: 2026-08-07  
Issue: #223  
Stacked on: draft PR #222

## 1. Full-problem comparison

The newest global routes are different coordinates of the same obstruction:

- PR #202: square-screw negative growth;
- PR #208: the same scalar in the constant D-0001 coordinate;
- PR #216: prime-only Hardy `H2` energy;
- PR #219: prime-power convex-polygon deficit;
- PR #218: one Haar screw defect / Stieltjes hierarchy;
- PR #222: signed balanced semiprime Type-II cells.

The finite matrix, Schur, and source machinery is no longer the main obstacle.
The load-bearing global statement is cancellation in one prime-supported
identity orbit.

This pass asks whether the final two-prime geometry can be removed entirely by
squaring the analytic signal before returning to arithmetic.

## 2. Main result

Let

\[
 F(z)=\widehat H(z)P_1(1/2+z)
\]

be the prime-only analytic signal of `T-21502`. Then

\[
 F\in H^2(C_\sigma)
 \iff F^2\in H^1(C_\sigma)
\]

with exact norm identity

\[
 \|F^2\|_{H^1}=\|F\|_{H^2}^2.
\]

The inverse Laplace transform of `F^2` is

\[
 (Q*Q)(x)
 =\sum_{p,q}
 {\log p\log q\over\sqrt{pq}}
 (H*H)(x-\log(pq)).
\]

Grouping by `n=pq` yields one one-dimensional signal supported on prime squares
and squarefree semiprimes. The squarefree coefficient is exactly

\[
 \Lambda_2(pq)=2\log p\log q.
\]

For the full von Mangoldt signal, the coefficient is

\[
 (\Lambda*\Lambda)(n)
 =\Lambda_2(n)-\Lambda(n)\log n.
\]

Thus the nonlinear Selberg channel is now an explicit one-dimensional source,
not a two-factor ratio matrix.

Subject to independent review of the parent prime-only transfer,

\[
 \mathrm{RH}
 \iff
 \widehat H(z)^2P_1(1/2+z)^2
 \in H^1(C_\sigma)
 \quad\text{for every }\sigma>0.
\]

## 3. Literature connection

The standard Dirichlet Hardy embedding places `mathscr H^2` in the conformally
invariant half-plane Hardy space at `Re s=1/2`; see Brevig,
arXiv:1606.03101. The required prime value is on the untwisted `Re s=0`
identity orbit, exactly one half-plane farther left.

The analytic square belongs to the Dirichlet weak product

\[
 \mathscr H^2_0\odot\mathscr H^2_0,
\]

which connects the problem to multiplicative Hankel forms and the weak-product
programme of Brevig--Perfekt, arXiv:1510.02019. Those results also warn that
Bohr-torus product norms and one-parameter boundary traces are very different.

`R-22301` proves the relevant universal embedding is impossible: normalized
Dirichlet polynomials supported on `[N,2N]` have coefficient norm one but
identity-orbit mass of order `N` on a fixed interval. The same example has
weak-product norm at most one after squaring.

Therefore abstract Hardy or weak-product membership cannot finish RH. A proof
must be restricted to the single prime-supported arithmetic ray.

## 4. Stronger one-dimensional sufficient theorem

`L-22302` gives an actionable sufficient condition. Put

\[
 C=Q*Q,
 \qquad
 c_\sigma=e^{-\sigma x}C(x).
\]

If

\[
 c_\sigma\in W^{1,2}(\mathbb R)
\]

for every `sigma>0`, then

\[
 \|\widehat{c_\sigma}\|_1
 \le\pi\sqrt2
 \left(\|c_\sigma\|_2^2+\|c_\sigma'\|_2^2\right)^{1/2}<\infty,
\]

and RH follows through `T-22301`.

Both required `L2` quantities are explicit one-dimensional semiprime mean
squares with windows

\[
 W=H*H,
 \qquad
 W'-\sigma W.
\]

This is stronger than necessary, but it is a conventional dispersion target
and has independent pair/product producers.

## 5. What was attempted

The pass tested the following possible closures:

1. the standard `mathscr H^2` local embedding;
2. weak-product membership of the analytic square;
3. universal weighted boundary evaluation at `Re s=0`;
4. ordinary coefficient `l2` estimates for the semiprime series;
5. direct Fourier `L1` from time-domain `L1`;
6. absolute semiprime and cellwise sieve estimates;
7. product-variable Sobolev estimates from known PNT errors;
8. Selberg's coefficient identity after separating its two terms.

Items 1--3 fail by the exact half-plane/no-go argument. Items 4--6 lose an
exponential factor. Items 7--8 require a mean-square cancellation strong enough
to contain the RH statement itself.

No valid proof of the critical embedding was found.

## 6. Exact checker

`X-22301` verifies with `Fraction` arithmetic:

- direct convolution equals grouped product convolution;
- exact diagonal/off-diagonal recombination;
- ordered cross coefficients combine with the factor of two;
- `|z^2|=|z|^2` on rational complex samples;
- coefficient norm one can coexist with identity point mass `N`.

Retained proof-object SHA-256:

```text
4db99b1c11db3400fa0256102217228716c945d4a10305fc338b1a741408f500
```

Eight central/mutation tests are committed. This is synthetic exact algebra,
not Riemann data.

## SERIOUS RESOLUTION PATH

A serious final path is present:

```text
prime-only Hardy exponent
-> analytic square
-> one-dimensional semiprime convolution
-> restricted critical H1/Carleson estimate
-> RH.
```

The first three arrows are exact in the proposed stack. The smallest exact
blocker is:

\[
 \boxed{
 \int_{\mathbb R}
 |\widehat H(\sigma+it)|^2
 |P_1(1/2+\sigma+it)|^2dt<\infty
 \quad\text{for every }\sigma>0.}
\]

Equivalently, prove the two semiprime Sobolev estimates of `L-22302`.

This is not another finite surrogate. It is the global RH-bearing identity
orbit itself, expressed with ordinary primes and one product variable.

## 7. Honest status

```text
H2/H1 square equivalence                    PROPOSED / exact
product-scale semiprime convolution         PROPOSED / exact
full Selberg one-dimensional forcing        PROPOSED / exact
universal critical embedding shortcut       REFUTED
semiprime Sobolev sufficient condition      PROPOSED / exact transfer
restricted prime-ray H1 estimate            OPEN
Riemann Hypothesis                           UNPROVED
```
