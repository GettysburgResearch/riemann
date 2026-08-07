# L-15445 — The analytic totient error is the inverse-zeta metric carrier for the dyadic prime ray

Claim ID: `L-15445`  
Title: One explicit zero-free Mellin multiplier carries the analytic summatory-totient error to the raw dyadic Chebyshev signal  
Status: `PROPOSED — EXACT TRANSFORM IDENTITY; CRITICAL LOCAL MULTIPLIER ESTIMATE OPEN`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `T-15412`; PR #226 `L-9512/T-9506`; the functional equation and Euler product  
Cross-route connections: `L-15443/L-15444`, PRs #216/#222/#224/#226  
Scope: exact identification of the inverse-zeta metric common to the prime and totient routes; this does not prove either critical second-moment bound

## 1. The two transforms

Let

\[
E^{\rm AN}(x)
={1\over2}\left(1+
 \sum_{d\ge1}\mu(d)\{x/d\}^2\right)
\qquad(x\ge1)
\tag{L-15445.1}
\]

be the analytic summatory-totient error of `L-9512`, and put

\[
\boxed{
\mathcal T(s)
=\int_1^\infty E^{\rm AN}(x)x^{-s-1}dx.}
\tag{L-15445.2}
\]

Initially for `Re s>2`,

\[
\boxed{
\mathcal T(s)
=-{\zeta(s-1)\over s(s-1)\zeta(s)}
+{3/\pi^2\over s-2}.}
\tag{L-15445.3}
\]

Let the dyadic Chebyshev signal of `T-15412` be

\[
Q_\diamond(\log Y)
={\psi(Y)-4\psi(Y/4)\over\sqrt Y}.
\tag{L-15445.4}
\]

For `z=s-1/2`, its Laplace transform is

\[
\boxed{
\mathcal Q(s)
:=\mathcal LQ_\diamond(s-1/2)
=-{1-4^{1-s}\over s}
 {\zeta'(s)\over\zeta(s)}.}
\tag{L-15445.5}
\]

## 2. Exact inverse-zeta bridge

Solving (L-15445.3) for `1/zeta(s)` gives

\[
{1\over\zeta(s)}
=-{s(s-1)\over\zeta(s-1)}
 \left[
  \mathcal T(s)-{3/\pi^2\over s-2}
 \right].
\tag{L-15445.6}
\]

Substituting into (L-15445.5) yields the exact identity

\[
\boxed{
\mathcal Q(s)
=\mathfrak M(s)
 \left[
  \mathcal T(s)-{3/\pi^2\over s-2}
 \right],}
\tag{L-15445.7}
\]

where

\[
\boxed{
\mathfrak M(s)
=(1-4^{1-s})(s-1)
 {\zeta'(s)\over\zeta(s-1)}.}
\tag{L-15445.8}
\]

Thus the raw prime signal is not merely RH-equivalent to the totient analytic part. It is obtained from it by one explicit Mellin multiplier after removing its elementary main pole.

## 3. The multiplier is safe in the open critical strip

Consider

\[
{1\over2}<\Re s<1.
\tag{L-15445.9}
\]

### Denominator

The functional equation writes `zeta(s-1)` as a nonzero elementary factor times `zeta(2-s)`. Since

\[
\Re(2-s)>1,
\]

the Euler product gives

\[
\boxed{\zeta(s-1)\ne0}
\tag{L-15445.10}
\]

throughout (L-15445.9).

### Dyadic factor

The zeros of `1-4^(1-s)` lie on

\[
\Re s=1.
\tag{L-15445.11}
\]

Hence this factor never suppresses an open-strip zero.

### Pole at one

Near `s=1`,

\[
1-4^{1-s}=\log4\,(s-1)+O((s-1)^2),
\]

while `zeta'(s)` has a double pole. The two displayed powers of `s-1` in
`(1-4^(1-s))(s-1)` cancel it. Thus `mathfrak M` is regular at the zeta pole.

### Multiplicity at a nontrivial zero

If `rho` is a zero of zeta of multiplicity `m`, then the totient factor in brackets in (L-15445.7) has a pole of order `m`, whereas `zeta'(s)` has a zero of order `m-1`. All other factors are nonzero for an off-line zero in (L-15445.9). Therefore

\[
\boxed{
\mathcal Q(s)
\text{ has one simple pole at every off-line }\rho,}
\tag{L-15445.12}
\]

independently of multiplicity, exactly as required by the logarithmic derivative.

The multiplier introduces no new RH-sensitive divisor. All inverse-zeta geometry is already carried by `mathcal T`.

## 4. Metric interpretation

`L-15443` writes the Selberg operator as

\[
\mathcal M\mathcal L\mathcal M^{-1}
=-m^{-1}\partial_zm,
\qquad
m(z)=(1+z)\zeta(1+z).
\tag{L-15445.13}
\]

The difficult step there is division by `m` when converting the positive gauged form to the physical Chebyshev/Hardy norm.

Equation (L-15445.6) identifies exactly the same division in an independent arithmetic coordinate:

```text
analytic totient error
    = an elementary nonvanishing factor times 1/zeta;

dyadic Chebyshev signal
    = a safe zeta-prime numerator times that inverse-zeta metric.
```

Hence PR #226 does not produce an unrelated RH criterion. Its critical local second moment is a direct candidate norm for the inverse-zeta metric missing from `L-15443/L-15444`.

## 5. Why the Bohr factorizations do not yet compose automatically

PR #226 proves an `O(D)` full-period Jordan-totient square for the truncated Möbius/Farey packet. `L-15444` proves a finite-boundary Bohr lower ledger for the gauged Chebyshev source. Equation (L-15445.7) shows how the two global coefficient pictures are related.

What remains is local and metric-sensitive. On a critical physical interval, the multiplier `mathfrak M(sigma+it)` has polynomial vertical growth, and the relevant inverse-zeta packet contains near-resonant Farey clusters at spacing `D^-2`. Therefore neither of the following is valid without an additional theorem:

```text
Bohr positivity of the gauged numerator
    => local prime Hardy bound;

full-period Jordan factorization of the Möbius packet
    => critical local totient second moment.
```

Both missing implications are the same ray-specific local-to-Bohr transference viewed before and after multiplication by `mathfrak M`.

## 6. Exact common finish line

Any one of the following supplies the missing metric conversion and proves RH through the already stated transfer theorems:

1. the analytic-totient estimate
   \[
   \int_1^X|E^{\rm AN}(x)|^2dx
   \ll_\varepsilon X^{2+\varepsilon};
   \tag{L-15445.14}
   \]
2. the dyadic Chebyshev estimate
   \[
   \int_1^Y
   \left|{\psi(t)\over t}-{\psi(t/4)\over t/4}\right|^2dt
   =Y^{o(1)};
   \tag{L-15445.15}
   \]
3. the restricted signed semiprime/Carleson estimate of PRs #222/#224;
4. a source-specific local multiplier theorem for (L-15445.7) that combines the Möbius Jordan square with the gauged prime square.

The fourth formulation is the direct synthesis suggested by the repository-wide comparison.

## 7. Proof boundary

Closed exactly:

- transform identity (L-15445.7);
- open-strip nonvanishing of `zeta(s-1)`;
- safe dyadic zero geometry;
- multiplicity reduction to one simple logarithmic-derivative pole;
- identification of the common inverse-zeta metric.

Open:

- the critical local multiplier estimate;
- local-to-Bohr transference for the Möbius/Farey packet;
- the signed semiprime/Carleson theorem;
- either critical second-moment bound.

This lemma does not prove RH. It shows that the newest prime and totient attacks have independently reached the same exact missing metric theorem.