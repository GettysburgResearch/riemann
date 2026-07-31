# L-15117 — Directed intervals for the actual smooth-window Hermite-radical coefficients

Claim ID: `L-15117`  
Status: **PROVED ANALYTIC ENCLOSURE LEMMA; INTERVAL PRODUCER NOT YET RUN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: corrected `L-15101`; the centered/CCM sign adapter of `L-14304`  
Scope: the first arrow in the smooth-window → Loewner → arithmetic-line proof program  
Related counterexample candidates: none

## 1. Setup

Let

\[
 K(t)=k(e^t),
 \qquad
 \widehat K(z)=\frac14\Xi(z),
\]

where `k=E(h)` is the exact Hermite radical from corrected `L-15101`.  Let

\[
 \ell=\log\lambda,
 \qquad
 \omega_n=\frac{\pi n}{\ell}.
\]

Choose an even smooth cutoff `chi_ell` satisfying

```text
0 <= chi_ell <= 1,
chi_ell(t)=1 for |t|<=ell-1,
chi_ell(t)=0 for |t|>=ell.
```

In the centered orthonormal Fourier basis on `[-ell,ell]`, followed by the exact
CCM centering sign, define

\[
 \boxed{
 p_n^{\rm sm}
 =\frac{(-1)^n}{\sqrt{2\ell}}
   \int_{\mathbb R}\chi_\ell(t)K(t)e^{-i\omega_nt}\,dt.}
 \tag{L-15117.1}
\]

The corresponding full-transform surrogate is

\[
 \boxed{
 p_n^{\rm full}
 =\frac{(-1)^n}{4\sqrt{2\ell}}\Xi(\omega_n).}
 \tag{L-15117.2}
\]

For the Xi-normalized target `4K`, multiply both quantities by `4`.

## 2. Uniform super-Gaussian coefficient radius

Let

\[
 \Lambda_\ell=e^{\ell-1}=\lambda/e.
\]

For `Lambda_ell>=2`, the tail estimate of `L-15101` gives, for `t>=0`,

\[
 |K(t)|\le C_H e^{9t/2}e^{-\pi e^{2t}}.
\]

Consequently

\[
 \begin{aligned}
 \int_{|t|>\ell-1}|K(t)|\,dt
 &\le 2C_H\int_{\Lambda_\ell}^{\infty}
        u^{7/2}e^{-\pi u^2}\,du\\
 &\le \frac{2C_H}{\pi}
        \Lambda_\ell^{5/2}e^{-\pi\Lambda_\ell^2}.
 \end{aligned}
 \tag{L-15117.3}
\]

The last inequality follows by writing

\[
 u^{7/2}e^{-\pi u^2}
 =(u^{5/2}e^{-\pi u^2/2})(u e^{-\pi u^2/2})
\]

and using that the first factor decreases for `u>=2`.

Since `1-chi_ell` is supported in `|t|>=ell-1`, one obtains the **uniform in
`n`** enclosure

\[
 \boxed{
 |p_n^{\rm sm}-p_n^{\rm full}|
 \le
 \tau_\ell
 :=\frac{\sqrt2 C_H}{\pi\sqrt\ell}
   \Lambda_\ell^{5/2}e^{-\pi\Lambda_\ell^2}.}
 \tag{L-15117.4}
\]

For the target normalized to transform exactly to `Xi`, the radius is
`4 tau_ell`.

No hard-window quadrature or algebraic taper approximation enters this bound.
It applies directly to the smooth form-core target used by the positive route.

## 3. Directed interval producer

Suppose an independent ball backend emits

\[
 \Xi(\omega_n)\in[X_{n,-},X_{n,+}].
\]

Then the actual coefficient is enclosed by

\[
 \boxed{
 p_n^{\rm sm}\in
 \frac{(-1)^n}{4\sqrt{2\ell}}[X_{n,-},X_{n,+}]
 +[-\tau_\ell,\tau_\ell].}
 \tag{L-15117.5}
\]

A proof object must bind:

1. the exact rational or ball value of `ell` and `omega_n`;
2. the completed-`Xi` normalization and precision;
3. a directed upper bound for `C_H`;
4. the cutoff profile and the facts `0<=chi<=1`, `chi=1` on the inner interval,
   and `chi=0` outside the outer interval;
5. the common radius `tau_ell`;
6. the CCM centering sign `(-1)^n`.

Because the radius is common, no adaptive quadrature of the transition strip is
needed merely to certify an enclosure.  Direct smooth-cutoff quadrature can be
intersected with (L-15117.5) to make the intervals narrower.

## 4. Growing-band consequence

The logarithm of the radius is

\[
 \log\tau_\ell=-\pi e^{2(\ell-1)}+O(\ell).
\]

By contrast, the gamma factor makes `Xi(omega_n)` decay only exponentially in
`|omega_n|`.  Therefore any polynomial band

\[
 N_\ell=O(\ell^A)
\]

has coefficient-tail uncertainty smaller than every exponential in `ell`.
In particular the quadratic-log schedule `N_ell=O(ell^2)` used by the latest
prolate/radical work is safely inside the coefficient-certification regime.

This statement concerns absolute coefficient enclosures.  A later Loewner
inertia transfer must still audit the small denominators `P(lambda_i)`; a tiny
coefficient radius can be amplified by a nearly vanishing node value.

## 5. Gap audit

1. The lemma encloses the actual smooth target, not the hard-window model of PR
   #173.
2. The common bound is deliberately conservative; it does not exploit
   oscillation or derivatives of the cutoff.
3. `Xi/4` is the corrected normalization.  Omitting the factor four corrupts
   absolute interval radii even though it does not change zero sets.
4. Coefficient closeness alone does not prove canonical inertia; `L-15113` is
   the required kernel-pinned transfer.
5. No finite or cofinal sign is asserted here.