# L-23709 — Cumulative Green profile and fifth-aligned forcing

Claim ID: `L-23709`  
Title: The cumulative carry inverse has a simpler reciprocal-zeta profile, and its Euler-aligned base-five shell has two explicit positive forcing primitives  
Status: **PROPOSED EXACT ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23701`, `L-23704`, `L-23707`, `L-23708`  
Scope: continuum scaling and exact Dirichlet-convolution identities; no pointwise shell sign is claimed

## 1. Finite cumulative Green state

Let `c_X(n)` be the unique triangular carry inverse of

\[
w_X(q)=q^{-1/2}\log(X/q),
\qquad 2\le q\le X,
\]

and define

\[
s_{X,m}=\sum_{n=m}^{X}\frac{c_X(n)}{n+1}.
\tag{L-23709.1}
\]

By `L-23701`, if

\[
u_X(m)=\frac1{\sqrt m}
\sum_{k\le X/m}\frac{\mu(k)}{\sqrt k}
\log\frac{X/m}{k},
\]

then exactly

\[
s_{X,m}=
\frac{m u_X(m)+\sum_{\ell=m+1}^{X}u_X(\ell)}{m(m-1)}.
\tag{L-23709.2}
\]

This is the scalar Green state whose monotonicity is full Carry Saturation and whose nonnegativity is the weaker cumulative certificate of `L-23702`.

## 2. Scaling profile

Put

\[
p(y)=4\sqrt y-4-\log y
\qquad(y\ge1),
\tag{L-23709.3}
\]

and set `p(y)=0` for `0<y<1`. Define

\[
\boxed{
\mathfrak S(y)=
\sum_{n\le y}\frac{\mu(n)}{\sqrt n}
\,p(y/n).
}
\tag{L-23709.4}
\]

Let `X_j,m_j -> infinity` with `X_j/m_j -> y>1`, away from an integer quotient boundary. Then

\[
\boxed{
 m_j^{3/2}s_{X_j,m_j}\longrightarrow\mathfrak S(y).
}
\tag{L-23709.5}
\]

### Derivation

For one fixed Möbius coordinate `k`, the contribution to `u_X(m)` is

\[
m^{-1/2}k^{-1/2}\log(X/(mk)).
\]

In the tail term of (L-23709.2), put `\ell=mt`. The Riemann sum contributes

\[
\frac{\mu(k)}{\sqrt k}
\int_1^{y/k}t^{-1/2}\log\frac{y}{kt}\,dt.
\]

The elementary substitution `t=r^2` gives the exact integral

\[
\boxed{
\int_1^{y/k}t^{-1/2}\log\frac{y}{kt}\,dt
=4\sqrt{\frac yk}-2\log\frac yk-4.
}
\tag{L-23709.5a}
\]

Adding the leading `m u_X(m)` contribution `log(y/k)` gives

\[
4\sqrt{y/k}-4-\log(y/k)=p(y/k),
\]

which proves (L-23709.5). Since only finitely many `k<=y` occur on a compact quotient interval, the convergence is locally uniform away from its integer boundaries. One-sided limits follow by retaining the entering Möbius atom.

## 3. Mellin transform and zero firewall

For `Re z>1/2`,

\[
\int_1^\infty p(y)y^{-z-1}\,dy
=\frac4{z-1/2}-\frac4z-\frac1{z^2}
=\frac{z+1/2}{z^2(z-1/2)}.
\tag{L-23709.6}
\]

Therefore

\[
\boxed{
\int_1^\infty\mathfrak S(y)y^{-z-1}\,dy
=\frac{z+1/2}
 {z^2(z-1/2)\zeta(z+1/2)}.
}
\tag{L-23709.7}
\]

Every zero `rho` of zeta with `Re rho>1/2` remains an uncancelled pole at `z=rho-1/2`. Positivity of `mathfrak S` is therefore an RH-bearing statement, not a soft consequence of the Green representation.

## 4. Euler-aligned fifth shell

Define

\[
b_5(n)=\mu(n)-\mathbf1_{5\mid n}\mu(n/5)
\tag{L-23709.8}
\]

and

\[
\boxed{
\mathfrak S_5(y)
=\mathfrak S(y)-5^{-1/2}\mathfrak S(y/5)
=\sum_{n\le y}\frac{b_5(n)}{\sqrt n}p(y/n).
}
\tag{L-23709.9}
\]

Its transform acquires the exact Euler factor

\[
\boxed{
\widehat{\mathfrak S_5}(z)
=\frac{(1-5^{-(z+1/2)})(z+1/2)}
 {z^2(z-1/2)\zeta(z+1/2)}.
}
\tag{L-23709.10}
\]

The factor has no zero at a hypothetical off-line zeta zero.

## 5. First positive forcing primitive

Let `1(n)=1`. Since

\[
1*b_5=\delta_1-\delta_5,
\]

finite Dirichlet convolution gives

\[
\boxed{
\sum_{m\le y}\frac1{\sqrt m}
\mathfrak S_5(y/m)
=p(y)-5^{-1/2}p(y/5)
=:H_5(y).
}
\tag{L-23709.11}
\]

The forcing is nonnegative for every `y>=1`, and strictly positive for `y>1`. For `1<=y<5`, it equals `p(y)`, with `p(1)=0` and

\[
p'(y)=\frac{2\sqrt y-1}{y}>0.
\]

For `y>=5`,

\[
H_5(y)=
\frac{16}{5}\sqrt y-4+\frac4{\sqrt5}
-\left(1-\frac1{\sqrt5}\right)\log y
-\frac{\log5}{\sqrt5}.
\tag{L-23709.12}
\]

Its derivative is positive for `y>=5`, and its value at five is positive.

## 6. Digital positive forcing primitive

Put

\[
c_5(n)=1-4v_5(n).
\tag{L-23709.13}
\]

The exact base-five digit identity of `L-23708` gives

\[
c_5*b_5=\delta_1-5\delta_5,
\qquad
\sum_{n\le N}c_5(n)=s_5(N)\ge0.
\]

Consequently

\[
\boxed{
\sum_{m\le y}\frac{c_5(m)}{\sqrt m}
\mathfrak S_5(y/m)
=p(y)-\sqrt5\,p(y/5)
=:R_5(y).
}
\tag{L-23709.14}
\]

Again `R_5(y)>=0`, strictly for `y>1`. For `y>=5`,

\[
R_5(y)=
4(\sqrt5-1)+(\sqrt5-1)\log y-\sqrt5\log5,
\tag{L-23709.15}
\]

which is increasing and has value

\[
R_5(5)=4(\sqrt5-1)-\log5>0.
\]

## 7. Exact lower-scale transport of a negative excursion

Equation (L-23709.11) implies the pointwise fail-closed estimate

\[
\boxed{
(\mathfrak S_5(y))_-
\le
\sum_{2\le m\le y}\frac{(\mathfrak S_5(y/m))_+}{\sqrt m}.
}
\tag{L-23709.16}
\]

Thus a negative aligned-shell value cannot be an independent same-scale mode: it must be paid by positive values at arguments at most `y/2`. This is a genuine source-specific descent, although the harmonic coefficient sum is not contractive at the critical exponent.

## 8. What this proves and what remains

The new identities prove that the fifth-aligned cumulative shell has:

1. the exact Euler-aligned inverse-zeta source;
2. one ordinary positive forcing primitive;
3. one base-five digital positive forcing primitive;
4. an explicit lower-scale transport law for every negative excursion.

They do **not** prove `mathfrak S_5>=0`, the finite fifth-scale Green inequality, Greedy Slack, DCRS, or RH. The remaining theorem is inversion of these positive forcing identities without losing the negative-order endpoint trace. That is the same local boundary represented finitely by `DGB(5)`.
