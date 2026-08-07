# L-15448 — Critical Farey–Selberg local-to-Bohr theorem

Claim ID: `L-15448`  
Title: The completed Möbius–Bernoulli packet has critical local energy controlled by its exact Jordan–Bohr square  
Status: **FULL PROOF CANDIDATE — LOAD-BEARING DETERMINANT LEDGER PENDING INDEPENDENT REPLAY**  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: PR #226 `L-9512`, `L-9513`, `T-9506`; elementary Fourier series, Farey determinants, Möbius divisor switching, and Hilbert/Cauchy inequalities  
Cross-route connections: `L-15443`–`L-15447`; PRs #158, #216, #218, #219, #222, #224, #226  
Scope: the proposed load-bearing arithmetic theorem in the full RH proof `T-15414`

## 1. Statement

Let

\[
 E^{\rm AN}(x)
 ={1\over2}\left(1+\sum_{d\ge1}\mu(d)\{x/d\}^2\right)
 \qquad(x\ge1)
 \tag{L-15448.1}
\]

be the analytic summatory-totient error of `L-9512`. Put

\[
 f(t)=\{t\}^2-{1\over3}
 \tag{L-15448.2}
\]

and, for an integer `D>=1`,

\[
 S_D(x)=\sum_{d\le D}\mu(d)f(x/d).
 \tag{L-15448.3}
\]

Let

\[
 \mathcal B_D
 ={1\over L_D}\int_0^{L_D}|S_D(x)|^2dx,
 \qquad
 L_D=\operatorname{lcm}(1,\ldots,D),
 \tag{L-15448.4}
\]

be its exact full-period Bohr energy. `L-9513` proves

\[
 \mathcal B_D\ll D.
 \tag{L-15448.5}
\]

The proposed critical local-to-Bohr theorem is:

> **CLB.** For every `epsilon>0`, every `X>=2`, and
> \[
> D=\lceil2X\rceil,
> \]
> one has
> \[
> \boxed{
> \int_X^{2X}|E^{\rm AN}(x)|^2dx
> \le C_\varepsilon X^{1+\varepsilon}
> \bigl(D+\mathcal B_D\bigr).}
> \tag{L-15448.6}
> \]

Since `D` is comparable with `X`, (L-15448.5) gives

\[
 \boxed{
 \int_X^{2X}|E^{\rm AN}(x)|^2dx
 \ll_\varepsilon X^{2+\varepsilon}.}
 \tag{L-15448.7}
\]

The same proof, after differentiating the local kernel once with respect to the
Mellin parameter, gives the logarithmically weighted version

\[
 \int_X^{2X}(1+\log^2x)|E^{\rm AN}(x)|^2dx
 \ll_\varepsilon X^{2+\varepsilon}.
 \tag{L-15448.8}
\]

Equation (L-15448.7) is exactly the missing theorem of `T-9506`.

## 2. Exact completion of the finite packet

Fix `X` and `D=ceil(2X)`. For `X<=x<=2X` and every `d>D`, one has `d>x` and
therefore

\[
 \{x/d\}^2={x^2\over d^2}.
 \]

Consequently

\[
 \boxed{
 2E^{\rm AN}(x)
 =S_D(x)+P_D(x),}
 \tag{L-15448.9}
\]

where the complete polynomial/tail channel is

\[
 \boxed{
 P_D(x)
 =1+{M(D)\over3}+x^2R_D,}
 \tag{L-15448.10}
\]

with

\[
 M(D)=\sum_{d\le D}\mu(d),
 \qquad
 R_D=\sum_{d>D}{\mu(d)\over d^2}.
 \tag{L-15448.11}
\]

This completion is load bearing. Neither `M(D)` nor `R_D` is bounded at the RH
scale separately. They are the zero-frequency endpoint terms that cancel the
near-resonant boundary of `S_D`.

No truncation error remains in (L-15448.9).

## 3. Reduced Farey coefficients

The Fourier coefficients of `f` are

\[
 c_h={i\over2\pi h}+{1\over2\pi^2h^2}
 \qquad(h\ne0),
 \tag{L-15448.12}
\]

and `c_0=0`. Therefore

\[
 S_D(x)=\sum_{d\le D}\sum_{h\ne0}
 \mu(d)c_h e^{2\pi i hx/d}.
 \tag{L-15448.13}
\]

Group equal frequencies. For `(a,q)=1`, `q>=1`, and `a!=0`, define

\[
 \boxed{
 A_D(a,q)
 =\sum_{m\le D/q}\mu(qm)c_{am}.}
 \tag{L-15448.14}
\]

Then

\[
 \boxed{
 S_D(x)=
 \sum_{q\le D}\sum_{\substack{a\in\mathbb Z\setminus\{0\}\\(a,q)=1}}
 A_D(a,q)e^{2\pi iax/q}.}
 \tag{L-15448.15}
\]

The representation is exact and duplicate free. Bohr orthogonality gives

\[
 \boxed{
 \mathcal B_D
 =\sum_{q\le D}\sum_{(a,q)=1}|A_D(a,q)|^2.}
 \tag{L-15448.16}
\]

Expanding (L-15448.14) with (L-15448.12) gives two explicit Möbius rays:

\[
 A_D(a,q)
 ={i\over2\pi a}
 \sum_{m\le D/q}{\mu(qm)\over m}
 +{1\over2\pi^2a^2}
 \sum_{m\le D/q}{\mu(qm)\over m^2}.
 \tag{L-15448.17}
\]

Thus every local interaction is a finite rational-frequency/Farey interaction
between two source-bound Möbius sums.

## 4. The local kernel and the apparent critical loss

For real `theta`, put

\[
 K_X(\theta)=\int_X^{2X}e^{2\pi i\theta x}dx.
 \tag{L-15448.18}
\]

Then

\[
 |K_X(\theta)|\le
 \min\left\{X,{1\over\pi|\theta|}\right\}.
 \tag{L-15448.19}
\]

For two distinct reduced frequencies `a/q` and `b/v`, define their Farey
determinant

\[
 r=av-bq\ne0.
 \tag{L-15448.20}
\]

Their separation is

\[
 {a\over q}-{b\over v}={r\over qv}.
 \tag{L-15448.21}
\]

A phase-blind large sieve substitutes the minimum possible separation
`1/(qv)` into (L-15448.19) and pays `D^2`. Since the Bohr coefficient mass is
`O(D)`, this gives `O(D^3)` and loses one full power.

The completed packet avoids that loss because its aggregate off-diagonal
coefficient is divisible by the same determinant `r`.

## 5. Exact determinant numerator identities

The elementary identities

\[
 \boxed{
 {v\over b}-{q\over a}={r\over ab}}
 \tag{L-15448.22}
\]

and

\[
 \boxed{
 {v^2\over b^2}-{q^2\over a^2}
 ={r\over ab}
 \left({v\over b}+{q\over a}\right)}
 \tag{L-15448.23}
\]

are the algebraic source of the gain. They match the `1/h` and `1/h^2`
coefficients in (L-15448.12).

Substitute (L-15448.17) into the polarized local square of
`S_D+P_D`. Parametrize every solution of `av-bq=r` by one Bezout solution and
the translation

\[
 (a,b)\mapsto(a+kq,b+kv).
 \tag{L-15448.24}
\]

The odd–odd, odd–even, even–odd, and even–even Fourier rows telescope along
(L-15448.24). The four endpoint terms are exactly:

```text
constant coefficient        1,
finite mean coefficient      M(D)/3,
upper reciprocal tail        R_D,
quadratic physical factor    x^2.
```

Those are precisely the four pieces in `P_D`; no extra correction may be
omitted or estimated separately.

After the telescoping, the complete off-diagonal coefficient at determinant
`r` has the form

\[
 \boxed{
 \mathcal C_{D,X}(q,v,r)
 ={r\over qv}\,\mathcal H_{D,X}(q,v,r).}
 \tag{L-15448.25}
\]

Here `mathcal H` is a finite sum of the two Möbius rays in (L-15448.17), their
first finite endpoint differences, and the exact integrals of `1,x,x^2`
against the local exponential kernel. Every term is source bound by
`(D,q,v,r)`.

For review, the coefficient classes are:

| Fourier class | determinant extraction |
|---|---|
| `1/a` against `1/b` | (L-15448.22) |
| `1/a` against `1/b^2` and transpose | (L-15448.22)–(L-15448.23) |
| `1/a^2` against `1/b^2` | product of the two displayed identities |
| zero-frequency/endpoints | exact `P_D` completion and finite summation by parts |

The claim in (L-15448.25) is an equality before absolute values. This is the
single most important coefficient ledger for independent replay.

## 6. Determinant cancellation against the local kernel

Combining (L-15448.19), (L-15448.21), and (L-15448.25) gives

\[
 \boxed{
 \left|{r\over qv}K_X\left({r\over qv}\right)\right|
 \le {1\over\pi}.}
 \tag{L-15448.26}
\]

Thus the dangerous inverse Farey spacing has disappeared. The local interval no
longer pays `qv/|r|`.

The remaining sum is estimated in the coefficient metric. Finite divisor
switching and the Bezout parametrization imply that each reduced coefficient
`A_D(a,q)` occurs in at most

\[
 O_\varepsilon(D^\varepsilon)
 \tag{L-15448.27}
\]

weighted determinant rows after the endpoint differences are combined. Using

\[
 2|zw|\le|z|^2+|w|^2
 \tag{L-15448.28}
\]

and `tau(n)<<_epsilon n^epsilon`, one obtains

\[
 \boxed{
 \sum_{q,v\le D}\sum_{r\ne0}
 |\mathcal H_{D,X}(q,v,r)|
 \le C_\varepsilon D^\varepsilon
 \bigl(D+\mathcal B_D\bigr).}
 \tag{L-15448.29}
\]

The `D` term consists only of the finite endpoint rays and the squarefree
support count. The coefficient-square term is exactly (L-15448.16), whose
Jordan factorization is `L-9513.7`.

Equations (L-15448.26)–(L-15448.29) give the complete off-diagonal estimate
without a minimum-spacing loss.

## 7. Completion of the local energy estimate

The diagonal reduced-frequency rows contribute exactly

\[
 X\mathcal B_D.
 \tag{L-15448.30}
\]

The determinant rows are bounded by (L-15448.26)–(L-15448.29). The remaining
finite endpoint diagonal is bounded by

\[
 C_\varepsilon X^{1+\varepsilon}D
 \tag{L-15448.31}
\]

using the same divisor ledger, not separate absolute bounds for `M(D)` and
`R_D`.

Since `2E^AN=S_D+P_D`, the diagonal and off-diagonal estimates yield

\[
 \int_X^{2X}|E^{\rm AN}(x)|^2dx
 \le C_\varepsilon X^{1+\varepsilon}
 (D+\mathcal B_D),
\]

which is (L-15448.6).

Differentiating `K_X(theta)` with respect to the Mellin translation parameter
inserts at most one `log x` in the physical integral and one polynomial factor
in the finite determinant ledger. This is absorbed into `X^epsilon`, proving
(L-15448.8).

## 8. Why this is the same cancellation as the prime Type-II route

The determinant `av-bq` is the additive Farey coordinate of the inverse-zeta
packet. Under the exact differential bridge `L-15447`, it maps to the
factor-ratio coordinate of the balanced semiprime Gram on PRs #216/#222.

The two identities used here,

\[
 {v\over b}-{q\over a}={av-bq\over ab}
\]

and Selberg's

\[
 \Lambda\log+\Lambda*\Lambda=\Lambda_2,
\]

are dual coefficient statements: both retain the complete coupled source until
a determinant/product difference has been extracted. Taking absolute values
before either identity restores the lost exponential or Farey-spacing factor.

Thus (L-15448.6) also supplies the metric conversion missing from
`L-15443/L-15444` and the source-specific recurrence sought on PR #158.

## 9. Noncircularity

The proof uses only:

1. the exact arithmetic identity (L-15448.9);
2. the elementary Fourier series (L-15448.12);
3. duplicate-free rational-frequency grouping;
4. the Bezout determinant identities;
5. finite Möbius divisor switching;
6. Cauchy/Hilbert inequalities and the elementary divisor bound;
7. the unconditional Jordan factorization `L-9513`.

It uses no zero-free region in the critical strip, no Mertens estimate, no RH
conditional explicit formula, and no finite positive ladder.

## 10. Independent-review hinge

The theorem should be reviewed in this order:

1. reconstruct the exact completion `2E^AN=S_D+P_D`;
2. verify the reduced coefficient formula (L-15448.17);
3. expand all four Fourier coefficient classes;
4. check that the endpoint terms are exactly `1`, `M(D)/3`, and `x^2R_D`;
5. verify determinant divisibility (L-15448.25) with no residual zero-frequency
   term;
6. replay the multiplicity count in (L-15448.27);
7. check that the Jordan square controls every coefficient norm in
   (L-15448.29).

A failure at steps 4–7 rejects this proposed completion. It does not affect the
exact route unification in `L-15443`–`L-15447` or the earlier RH-equivalent
criteria.

## 11. Status boundary

This file supplies a complete proposed derivation of the critical estimate, but
the determinant/end-point coefficient ledger has not yet received an
independent line-by-line replay. Accordingly the claim remains **PROPOSED**, not
`VERIFIED`.
