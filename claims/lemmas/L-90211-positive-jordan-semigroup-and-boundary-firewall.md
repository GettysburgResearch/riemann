# L-90211 — The low-row source has a positive all-order Jordan semigroup, but positive moments do not determine its boundary sign

Claim ID: `L-90211`  
Status: **PROPOSED COMPLETE EXACT POSITIVITY / NO-GO LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-26903/L-26904`; `L-90209/L-90210`; elementary Euler products  
Scope: closes the complete positive moment hierarchy and proves its exact limitation; no low-row sign theorem and no RH conclusion

## 1. Normalized source and positive inverse

Use the normalized source

\[
 \omega_2
 =\mu-\frac32\delta_2*\mu+\frac12\delta_4*\mu,
 \tag{L-90211.1}
\]

so that `omega=2 omega_2` in `L-90209`. Its positive Dirichlet inverse is

\[
 \boxed{
 a(n)=2v_2(n)+2^{-v_2(n)}>0,
 }
 \tag{L-90211.2}
\]

and

\[
 \omega_2*a=\varepsilon.
 \tag{L-90211.3}
\]

The Euler factors of `a` are

\[
 A_p(x)=\frac1{1-x}\qquad(p\ne2),
 \tag{L-90211.4}
\]

and

\[
 \boxed{
 A_2(x)=\frac1{(1-x)^2(1-x/2)}.
 }
 \tag{L-90211.5}
\]

## 2. Positive generalized Jordan semigroup

For real `tau>0`, define

\[
 \boxed{
 J_\tau=\omega_2*(a\,n^\tau).
 }
 \tag{L-90211.6}
\]

Its Dirichlet series is

\[
 \sum_n{J_\tau(n)\over n^s}
 =\frac{A(s-\tau)}{A(s)}.
 \tag{L-90211.7}
\]

### Odd primes

At an odd prime `p`, put `alpha=p^tau>1`. The local ratio is

\[
 \frac{1-x}{1-\alpha x}
 =1+\sum_{r\ge1}\alpha^{r-1}(\alpha-1)x^r.
 \tag{L-90211.8}
\]

Every nonconstant coefficient is strictly positive.

### Prime two

Put `alpha=2^tau>1`. From (L-90211.5),

\[
 \frac{A_2(\alpha x)}{A_2(x)}
 =\left(\frac{1-x}{1-\alpha x}\right)^2
  \left(\frac{1-x/2}{1-\alpha x/2}\right).
 \tag{L-90211.9}
\]

Each factor has constant coefficient one and strictly positive remaining coefficients by (L-90211.8), with the last factor scaled by `2^{-r}`. Their product therefore has strictly positive nonconstant coefficients.

Multiplicativity gives

\[
 \boxed{
 J_\tau(1)=1,
 \qquad J_\tau(n)>0\quad(n\ge2,\ \tau>0).
 }
 \tag{L-90211.10}
\]

The family is a semigroup under Dirichlet convolution:

\[
 \boxed{
 J_{\tau+\sigma}=J_\tau*(n^\tau J_\sigma),
 \qquad \tau,\sigma>0,
 }
 \tag{L-90211.11}
\]

which follows by multiplying the ratios `A(s-tau-sigma)/A(s-tau)` and `A(s-tau)/A(s)`.

## 3. Positive exponential moments of every carry source trace

Let `w(q)>=0` be any finite arithmetic target with `w(1)=0`. Define

\[
 U(m)=\sum_{k\ge1}\omega_2(k)w(mk).
 \tag{L-90211.12}
\]

Finite divisor switching gives, for every `tau>0`,

\[
\begin{aligned}
 \Phi_w(\tau)
 &:=\sum_{m\ge1}a(m)m^\tau U(m)\\
 &=\sum_q[\omega_2*(a n^\tau)](q)w(q)\\
 &=\boxed{\sum_{q\ge2}J_\tau(q)w(q)>0}
 \tag{L-90211.13}
\end{aligned}
\]

whenever the target is nonzero.

At `tau=0`, (L-90211.3) and `w(1)=0` give

\[
 \boxed{\Phi_w(0)=0.}
 \tag{L-90211.14}
\]

Differentiating at zero yields the complete logarithmic moment tower

\[
 \boxed{
 \Phi_w^{(r)}(0)
 =\sum_m a(m)(\log m)^rU(m)
 =\sum_q C_r(q)w(q)\ge0
 \qquad(r\ge1),
 }
 \tag{L-90211.15}
\]

where

\[
 C_r=\omega_2*(a\log^r).
 \tag{L-90211.16}
\]

The coefficient sequences are nonnegative for every order. Indeed

\[
 C_1=\Lambda_a\ge0
 \tag{L-90211.17}
\]

and the Dirichlet-series derivative identity gives the recurrence

\[
 \boxed{
 C_{r+1}=C_r\log+C_r*\Lambda_a.
 }
 \tag{L-90211.18}
\]

Thus `C_r>=0` implies `C_(r+1)>=0`. This extends the zero/first/second tower of `L-26904` to every logarithmic order and to the full positive exponential semigroup.

## 4. The bottom charge is the negative-time boundary

For a finite target, (L-90211.13) is an entire exponential polynomial in `tau`. As `tau->-infinity`, every `m>1` term vanishes and

\[
 \boxed{
 \lim_{\tau\to-\infty}\Phi_w(\tau)
 =a(1)U(1)=U(1).
 }
 \tag{L-90211.19]
\]

because `a(1)=1`.

For the critical target `w_X`,

\[
 U(1)=\sum_{q\ge2}\omega_2(q)w_X(q)
 =-\frac16[5c_X(2)+3c_X(3)].
 \tag{L-90211.20}
\]

Therefore the desired low-row sign is exactly a statement about the **negative-time endpoint** of a function known positive for every positive time and with every positive logarithmic derivative at zero.

## 5. Exact firewall: the positive semigroup and all moments do not determine the boundary sign

The information in Sections 2--3 is insufficient by itself. Consider the two finite exponential polynomials

\[
 \Phi_-(\tau)=e^\tau-1
 \tag{L-90211.21}
\]

and

\[
 \Phi_+(\tau)=e^{3\tau}-\frac32e^{2\tau}+\frac12.
 \tag{L-90211.22}
\]

Both satisfy

\[
 \Phi_\pm(0)=0.
 \tag{L-90211.23}
\]

For every `tau>0`,

\[
 \Phi_-(\tau)>0,
 \qquad
 \Phi_+(\tau)>0.
 \tag{L-90211.24}
\]

Moreover every positive-order derivative is nonnegative on `tau>=0`:

\[
 \Phi_-^{(r)}(\tau)=e^\tau>0,
 \tag{L-90211.25}
\]

and, for `r>=1`,

\[
 \Phi_+^{(r)}(\tau)
 =3^re^{3\tau}-\frac32\,2^re^{2\tau}
 \ge e^{2\tau}\left(3^r-\frac32\,2^r\right)\ge0,
 \tag{L-90211.26}
\]

with equality only at `(r,tau)=(1,0)`.

Yet their negative-time limits have opposite signs:

\[
 \boxed{
 \lim_{\tau\to-\infty}\Phi_-(\tau)=-1,
 \qquad
 \lim_{\tau\to-\infty}\Phi_+(\tau)=\frac12.
 }
 \tag{L-90211.27}
\]

Thus even the conjunction

```text
Phi(0)=0;
Phi(tau)>=0 for every tau>0;
Phi^(r)(tau)>=0 for every r>=1 and tau>=0
```

does not determine the sign of the unit boundary coefficient.

This countermodel is exact and finite. It is the mandatory reviewer mutation for any attempt to derive Bottom-Charge Positivity solely from the positive inverse, generalized-prime positivity, all Selberg moments, or the positive Jordan semigroup.

## 6. Consequence for the live route

The source-side hierarchy is now complete:

```text
positive inverse                         exact
positive generalized primes              exact
all logarithmic moments                  nonnegative
all positive Jordan deformations         coefficientwise positive
unit/bottom boundary sign                not determined by these data
```

A successful proof of the two-low-row sign must therefore consume **negative-time or source-specific coupling information** not contained in the positive moment cone. Candidate extra inputs include:

1. an ordered martingale coupling for the canonical reward of `L-90210`;
2. a boundary-preserving physical Schur complement;
3. a zero-safe annular inequality retaining the unit coordinate;
4. direct arithmetic information on the Möbius boundary source.

## 7. Proof boundary

Proved exactly:

- coefficientwise positivity of every generalized Jordan sequence `J_tau`, `tau>0`;
- its convolution semigroup law;
- positivity of every positive-time target pairing;
- nonnegativity of every logarithmic moment order;
- identification of the bottom charge as the negative-time boundary;
- an exact countermodel proving that all positive-time/moment data are insufficient.

Not proved:

- the bottom-charge or two-low-row sign;
- a boundary coupling;
- RH.
