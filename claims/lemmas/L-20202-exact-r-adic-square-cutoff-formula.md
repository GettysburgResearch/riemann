# L-20202 — Exact `r`-adic square-cutoff prime formula

Claim ID: `L-20202`  
Title: The critical-mesh integer-dilation defect has one square-cutoff prime sum and an arbitrarily thin negative prefix  
Status: `PROPOSED — COMPLETE ALGEBRAIC CONSEQUENCE OF THE IMPORTED SCREW FORMULA`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `L-19801`; `T-20203`  
Scope: every fixed integer `r>=2` and every integer `n>=2^(r/2)`

## 1. Critical-mesh statistic

Fix an integer `r>=2` and put

\[
 t={2\over r}\log n,
 \qquad
 \mathcal H_r(n)=r^2\Psi(t)-\Psi(rt).
 \tag{1}
\]

The lower bound on `n` ensures `t>=log 2`, so the finite prime/Lerch formula of
`L-19801` applies at both scales. The larger scale is always

\[
 rt=2\log n,
\]

hence every prime term lies below the common square cutoff `n^2`.

Write

\[
 \kappa=\psi(1/4)-\log\pi
\]

and

\[
 \Phi(z)=\Phi(z,2,1/4).
\]

## 2. Complete exact formula

Direct substitution gives

\[
\boxed{
\begin{aligned}
\mathcal H_r(n)={}&
4\left[
 r^2\left(n^{1/r}+n^{-1/r}-2\right)
 -\left(n+n^{-1}-2\right)
\right]\\
&+(r-1)\kappa\log n\\
&+\sum_{q\le n^{2/r}}
 {\Lambda(q)\over\sqrt q}
 \log{q^{r^2-1}\over n^{2(r-1)}}\\
&+\sum_{n^{2/r}<q\le n^2}
 {\Lambda(q)\over\sqrt q}
 \log{n^2\over q}\\
&-{r^2\over4}n^{-1/r}\Phi(n^{-4/r})
 +{1\over4n}\Phi(n^{-4})
 +{r^2-1\over4}\Phi(1).
\end{aligned}}
\tag{2}
\]

Both sums include every prime power, with `Lambda(p^a)=log p`. The threshold
`n^(2/r)` is interpreted as an exact real cutoff; equality is harmless because
the second weight vanishes at `q=n^2`, not at the intermediate cutoff.

## 3. Prime-weight sign geometry

For `q<=n^(2/r)`, the weight is

\[
 w_{r,n}(q)
 =\log{q^{r^2-1}\over n^{2(r-1)}}.
\]

Since `r^2-1=(r-1)(r+1)`,

\[
\boxed{
 w_{r,n}(q)<0
 \iff
 q<n^{2/(r+1)}.}
\tag{3}
\]

It is nonnegative on

\[
 n^{2/(r+1)}\le q\le n^{2/r}.
\]

Every prime power in the outer band

\[
 n^{2/r}<q\le n^2
\]

has the positive weight `log(n^2/q)`. Consequently

\[
\boxed{
\text{all negative prime weight is confined to }
q<n^{2/(r+1)}.}
\tag{4}
\]

The complete manifest remains `q<=n^2`. Thus increasing a fixed `r` makes the
negative prefix exponent `2/(r+1)` arbitrarily small without weakening the RH
criterion of `T-20203`.

For a positive mixture with maximal dilation `R`, sampled at

\[
 t={2\over R}\log n,
\]

the `r`-component can be negative only below

\[
 q<n^{2r/[R(r+1)]}\le n^{2/(R+1)}.
\]

Hence the same thin-prefix statement holds for every positive mixture.

## 4. The polar term is an exact hyperbolic deficit

The first line of (2) is

\[
16\left[
 r^2\sinh^2\!\left({\log n\over2r}\right)
 -\sinh^2\!\left({\log n\over2}\right)
\right].
\tag{5}
\]

Since `sinh(rx)>=r sinh(x)` for `x>=0`,

\[
\boxed{\text{the polar contribution is nonpositive.}}
\tag{6}
\]

At `r=2`, it reduces to the square

\[
 -4\left(\sqrt n+n^{-1/2}-2\right)^2.
\]

## 5. The complete Lerch term is termwise positive

Set

\[
 y_k=n^{-(4k+1)/r},
 \qquad 0<y_k<1.
\]

The final line of (2) equals

\[
\boxed{
 {1\over4}\sum_{k=0}^\infty
 {r^2(1-y_k)-(1-y_k^r)\over(k+1/4)^2}.}
\tag{7}
\]

Now

\[
 1-y^r=(1-y)(1+y+\cdots+y^{r-1})\le r(1-y),
\]

so every numerator in (7) satisfies

\[
 r^2(1-y)-(1-y^r)
 \ge r(r-1)(1-y)>0.
\]

Therefore

\[
\boxed{\text{the entire Lerch contribution is strictly positive.}}
\tag{8}
\]

It has a monotone positive truncation tail and requires no cancellation in a
directed producer.

## 6. Reusable prefix moments

Define

\[
 A(x)=\sum_{q\le x}{\Lambda(q)\over\sqrt q},
 \qquad
 B(x)=\sum_{q\le x}{\Lambda(q)\log q\over\sqrt q}.
\]

The complete prime part of (2) is

\[
\boxed{
 2\log n\,A(n^2)
 -2r\log n\,A(n^{2/r})
 +(r^2-1)B(n^{2/r})
 -B(n^2).}
\tag{9}
\]

One duplicate-free square-cutoff stream can therefore serve every fixed
dilation `r`: only two prefix indices and the same two cumulative moments are
needed.

## 7. Renormalized convex-polygon interpretation

With the decomposition `Psi=F-G` of PR #219,

\[
 \mathcal H_r(n)
 =r^2F(t)-F(rt)
 +G(rt)-r^2G(t).
\tag{10}
\]

The arithmetic term `G(rt)-r^2G(t)` is exactly the two-scale polygon transport
whose atom weights are described in Section 3. Thus the Haar/dilation route and
the prime-polygon route are not competing reductions: the former supplies a
fixed renormalized chord of the latter.

A positive proof may therefore target a block transport inequality which pays
the explicit archimedean deficit using the overwhelmingly positive band
`n^(2/(r+1))<=q<=n^2`, while treating the old prefix separately.

## 8. Proof boundary

- Formula (2), the sign split, the hyperbolic inequality, and the Lerch
  factorization are exact.
- The large positive prime band cancels an order-`n` polar term to RH-scale
  accuracy; entrywise positivity does not by itself prove the final sign.
- Known phase-blind PNT error estimates are not silently claimed sufficient.
- No cofinal lower bound for `H_r(n)` is proved here.