# L-19874 — Exact Jordan-to-scattering Radon–Nikodym wave operator

Claim ID: `L-19874`  
Status: **PROVED EXACT SOURCE-SPACE UNITARY AND COVARIANCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91037`; `L-91307`; elementary metric-connection calculus  
RH status: **no RH input**

## 1. The two prime first-chaos measures

Fix

\[
 a>0,
 \qquad c>1.
\]

For a prime power `n=p^k`, write

\[
 u_n=\log n.
\]

The normalized Jordan-curvature measure of `L-91037` is

\[
 \boxed{
 d\omega^{\rm J}_{a,c}(u)
 =\sum_{n=p^k}
 {1-(1+2au_n)e^{-2au_n}\over k a^2}
 e^{-cu_n}\,\delta_{u_n}(du).
 }
\tag{L-19874.1}
\]

The ordinary-prime scattering-score measure of `L-91307`, on the same safe
vertical line, is

\[
 \boxed{
 d\beta_{a,c}(u)
 =a\sum_{n=p^k}\Lambda(n)e^{-cu_n}\,
 \delta_{u_n}(du)
 =a\sum_{n=p^k}{u_n\over k}e^{-cu_n}\,
 \delta_{u_n}(du).
 }
\tag{L-19874.2}
\]

Both are positive and have exactly the same support.  The source mismatch in
`R-91301` is therefore not a support mismatch and not a scalar-normalization
problem.  It is an explicit nonconstant Radon–Nikodym transport.

## 2. Exact Radon–Nikodym multiplier

Put

\[
 \phi(x)=1-(1+x)e^{-x}
 =\int_0^x t e^{-t}\,dt,
 \qquad x>0,
\tag{L-19874.3}
\]

and define

\[
 \boxed{
 m_a(u)
 =\left({d\omega^{\rm J}_{a,c}\over d\beta_{a,c}}(u)\right)^{1/2}
 ={\sqrt2\over a}
 \left({\phi(2au)\over2au}\right)^{1/2}.
 }
\tag{L-19874.4}
\]

The formula is independent of `c`.  Indeed, at `u=u_n`,

\[
 m_a(u_n)^2
 ={1-(1+2au_n)e^{-2au_n}\over a^3u_n}.
\tag{L-19874.5}
\]

Define

\[
 \boxed{
 \mathcal U_{a,c}:L^2(\omega^{\rm J}_{a,c})
 \longrightarrow L^2(\beta_{a,c}),
 \qquad
 (\mathcal U_{a,c}f)(u)=m_a(u)f(u).
 }
\tag{L-19874.6}
\]

Then

\[
 \begin{aligned}
 \|\mathcal U_{a,c}f\|_{L^2(\beta)}^2
 &=\int |f(u)|^2m_a(u)^2d\beta_{a,c}(u)\\
 &=\int |f(u)|^2d\omega^{\rm J}_{a,c}(u).
 \end{aligned}
\]

Since the measures have the same atoms and every coefficient is strictly
positive,

\[
 \boxed{\mathcal U_{a,c}\text{ is unitary}.}
\tag{L-19874.7}
\]

This is the explicit source wave operator missing from the scalar-multiple
comparison.  No unidentified square root of a target kernel occurs.

## 3. Carrier and delay covariance

Let

\[
 (Af)(u)=u f(u)
\tag{L-19874.8}
\]

be the logarithmic carrier generator and

\[
 (S_\tau f)(u)=e^{-i\tau u}f(u),
 \qquad \tau\in\mathbb R,
\tag{L-19874.9}
\]

be the delay group.  Because `m_a` is a scalar function of `u`,

\[
 \boxed{
 A\mathcal U_{a,c}=\mathcal U_{a,c}A,
 \qquad
 S_\tau\mathcal U_{a,c}=\mathcal U_{a,c}S_\tau.
 }
\tag{L-19874.10}
\]

Thus the transport retains every prime carrier, every carrier cross term and
every delay phase exactly.  It may be inserted before the tail-Hankel Julia
synthesis of `L-91307`, before reflection, or before any common compressed-delay
map.

## 4. Metric-compatible radial connections

Let a positive measure family have density `w_a` relative to one fixed atomic
reference measure.  Its metric-compatible logarithmic derivative is

\[
 \nabla^{(w)}_a
 =a\partial_a+{1\over2}a\partial_a\log w_a.
\tag{L-19874.11}
\]

Write `w_a^J` and `w_a^S` for the coefficients in
(L-19874.1)--(L-19874.2).  Since

\[
 m_a^2={w_a^J\over w_a^S},
\]

one has identically

\[
 a\partial_a\log m_a
 ={1\over2}
 \left(a\partial_a\log w_a^J
      -a\partial_a\log w_a^S\right).
\tag{L-19874.12}
\]

Consequently, on the common finite-cylinder core,

\[
 \boxed{
 \nabla^{(w^S)}_a\mathcal U_{a,c}
 =\mathcal U_{a,c}\nabla^{(w^J)}_a.
 }
\tag{L-19874.13}
\]

The nonconstant source renormalization is therefore exactly covariant for the
correct Hilbert-bundle connections.  The apparent second-fundamental-form term
arises only if ordinary differentiation is used while the source metric moves.

## 5. Uniform ordinary-derivative bound

Put `x=2au`.  From (L-19874.4),

\[
 \boxed{
 a\partial_a\log m_a(u)
 =-{3\over2}
 +{x^2e^{-x}\over2\phi(x)}.
 }
\tag{L-19874.14}
\]

Since

\[
 \phi(x)=\int_0^xte^{-t}dt
 >e^{-x}\int_0^xtdt
 ={x^2e^{-x}\over2},
\tag{L-19874.15}
\]

one gets

\[
 -{3\over2}
 <a\partial_a\log m_a(u)
 <-{1\over2}.
\tag{L-19874.16}
\]

In particular,

\[
 \boxed{
 \|a\partial_a\mathcal U_{a,c}\,
       \mathcal U_{a,c}^{-1}\|\le{3\over2}.
 }
\tag{L-19874.17}
\]

Thus even in a fixed trivialization the source connection is bounded.  There is
no uncontrolled radial derivative mismatch between the Jordan curvature and
ordinary-prime scattering first chaoses.

## 6. Tail-Hankel functoriality

For a positive atomic measure `mu`, let

\[
 (\mathsf H_\mu g)(t)
 =\int_{u>t}g(u-t)d\mu(u)
\tag{L-19874.18}
\]

and let `V_mu` be the triangular first-chaos synthesis of `L-91307`.  The
unitary (L-19874.6) lifts fibrewise to

\[
 \widetilde{\mathcal U}_{a,c}:
 L^2(\Omega,dt\,d\omega^J)
 \longrightarrow
 L^2(\Omega,dt\,d\beta),
\quad
 (\widetilde{\mathcal U}F)(t,u)=m_a(u)F(t,u).
\tag{L-19874.19}
\]

It commutes with the triangular support indicator `1_(t<u)`, the carrier
generator and every common delay.  Hence

\[
 \boxed{
 \widetilde{\mathcal U}_{a,c}V_{\omega^J}
 =V_\beta M_{m_a},
 }
\tag{L-19874.20}
\]

where `M_(m_a)` is multiplication in the incoming carrier variable.  This is
the precise source-level adapter between the positive Jordan first chaos and
the ordinary-prime tail-Hankel source.

It does not assert that the completed Fisher law is Poisson.  `R-91402` remains
in force: the map here is a nonconstant Hilbert-space wave operator, not an
identity of probability laws.

## 7. Consequences and boundary

Closed exactly:

```text
Jordan and scattering measures have common support       YES
explicit Radon--Nikodym unitary                           YES
carrier covariance                                       EXACT
delay covariance                                         EXACT
metric-compatible radial covariance                      EXACT
ordinary radial connection uniformly bounded             YES
tail-Hankel triangular-source lift                        EXACT
```

Still separate:

```text
gamma/pole completion;
theta/Brownian boundary reserve;
bridge and compressed model-space leakage;
identification of the completed source defect with the delayed Weil form.
```

The theorem removes the prime-source normalization mismatch as an independent
obstruction.  It does not prove the completed positive-energy or RH statement.
