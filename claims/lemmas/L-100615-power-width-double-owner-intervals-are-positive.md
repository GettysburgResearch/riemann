# L-100615 — Double-owner cubic intervals are positive throughout every subcritical prime-power width

Claim ID: `L-100615`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC INTERVAL THEOREM**  
Created: 2026-08-20  
Depends on: `L-100613`; Mertens' theorem for prime reciprocals  
RH status: **not assumed**

Let `K_(p,q)=(I-U_p)(I-U_q)Psi` and retain the source-normalized interior-prime
bound from `L-100613`:

\[
\ell^{-1/2}K_{p,q}(y/\ell)
\le\frac4{3\ell}K_{p,q}(y).
\tag{L-100615.1}
\]

Fix a real exponent

\[
1<A<e^{3/4}.
\]

Mertens' theorem gives, uniformly for primes `p<q<=p^A`,

\[
\sum_{p<\ell<q\atop\ell\ {m prime}}\frac1\ell
\le
\log\frac{\log q}{\log p}+o_{p\to\infty}(1)
\le
\log A+o_{p\to\infty}(1).
\tag{L-100615.2}
\]

Since

\[
\frac43\log A<1,
\]

there is `p_0(A)` such that

\[
\boxed{
\frac43
\sum_{p<\ell<q}\frac1\ell<1
\qquad
(p\ge p_0(A),\ q\le p^A).
}
\tag{L-100615.3}

Apply the adjacent-level argument of `L-100613` to the complete interior Euler
product. It yields

\[
\boxed{
\prod_{p<\ell<q}
(I-\ell^{-1/2}U_\ell)
(I-U_p)(I-U_q)\Psi(y)
\ge0
}
\tag{L-100615.4}
\]

for every `y>0`, every sufficiently large endpoint prime `p`, and every prime
`q` satisfying `p<q<=p^A`.

Thus the proved positive region is not merely a fixed ratio-eight shell. It
contains every prime interval whose upper endpoint is below

\[
p^{e^{3/4}-o(1)}.
\]

Numerically,

\[
e^{3/4}=2.117000\ldots.
\]

The exact constant is the conjunction of two independent facts:

```text
cubic double-difference Harnack cost       4/3;
prime-harmonic interval mass               log A.
```

The remaining Schur matrix may therefore be restricted to genuinely
supercritical endpoint separation

\[
\log q>(e^{3/4}-o(1))\log p,
\]

plus finitely many low-prime exceptional rows and columns. This is a much
sparser region than the raw long-interval condition `q/p>8`.

The theorem does not estimate that supercritical region.