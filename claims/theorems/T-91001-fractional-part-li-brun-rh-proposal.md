# T-91001 — Fractional-Part Li–Brun full RH proposal

Claim ID: `T-91001`  
Title: A positive fractional-part amplifier and a moving-depth Möbius-free Brun projector give two exact, source-linked completion routes to RH; the first remaining theorem is a diagonal positive factorisation, not another global norm estimate  
Status: **FULL CONDITIONAL PROPOSAL — EXACT COMPONENTS SUPPLIED; ONE CONCLUSION-PRODUCING FACTORISATION OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-12  
Dependencies: `L-90423`–`L-90431`; `L-91001`–`L-91005`; `R-91001`  
Scope: phase-locked Möbius/PIG mean route and nonlinear Li-amplifier route; RH is not claimed

## 1. Why a new coordinate is needed

The live phase-locked route has compressed the RH obstruction to one scalar charge

\[
\mathcal C_*(X)=F_*(X)-\log X,
\tag{T-91001.1}
\]

where `F_*` is a coercive five-scale filter of the canonical Möbius Green state. The equivalent finite carry object has fourteen rows and depends on sixteen samples.

That compression is exact, but its positive divisor renewal is noncontractive. Trying to prove a generic norm contraction would simply rename RH.

The radical change is to use **moving order** rather than a fixed invariant cone.

## 2. Route A — Diagonal Brun Positivity

Put

\[
D(X)=-\mathcal C_*(X).
\tag{T-91001.2}
\]

The phase-locked divisor renewal has the exact form

\[
(I+K)D=G,
\tag{T-91001.3}
\]

where `K` is a positive strict divisor-delay operator and `G` has the finite Möbius-free source `1-ell`.

For every probability distribution on even depths, `L-91003` constructs polynomials

\[
R(z)=\sum_r\omega_rz^r,
\qquad
Q(z)=\frac{1-R(z)}{1+z},
\tag{T-91001.4}
\]

and proves

\[
\boxed{D=Q(K)G+R(K)D.}
\tag{T-91001.5}
\]

At a first point where `D<0`, the second term is nonnegative. Therefore the following theorem is sufficient:

> **DBP — Diagonal Brun Positivity.** For every sufficiently large `X`, choose an even-depth probability law supported where
> \[
> 2^r\le X<4\,2^r
> \]
> and prove
> \[
> \boxed{Q(K)G(X)\ge0.}
> \tag{T-91001.6}
> \]

Then no first negative point exists, so `D>=0` cofinally, equivalently

\[
\mathcal C_*(X)\le0
\tag{T-91001.7}
\]

cofinally. The zero-safe one-sign Mellin/Landau consumer of `T-90421` gives RH.

Thus

\[
\boxed{\mathrm{DBP}\Longrightarrow\mathrm{RH}.}
\tag{T-91001.8}
\]

## 3. Why DBP is finite rather than another Möbius estimate

The certificate source is

\[
Q(h)(\mathbf1-\ell),
\tag{T-91001.9}
\]

with no Möbius coefficient. The reciprocal-zeta state occurs only in the positive first-crossing remainder.

At the natural diagonal, `L-91004` proves:

```text
support starts at 2^r;
at most three factors differ from two when X<4*2^r;
ordered-factor complexity is polynomial in r;
all Möbius-bearing remainder Riesz mass is O(r^K 2^(-r/2)).
```

So DBP is a bounded-defect ordered-factorisation theorem. It is not a demand for a global Mertens estimate.

The probability law over even depths is a real design variable. Fejer, geometric, Poisson, or exact finite-linear-programming weights may be selected while preserving the first-crossing sign.

## 4. Route B — Fractional-Part Li spectral radius

Define

\[
A(s)=\frac{s}{s-1}-\zeta(s)
=s\int_0^\infty\{e^t\}e^{-st}\,dt.
\tag{T-91001.10}
\]

At every nontrivial zero,

\[
A(\rho)=\frac\rho{\rho-1}.
\tag{T-91001.11}
\]

Hence line zeros lie on `|A|=1`, while every right off-line zero lies strictly outside.

For `M>=2`, define the absolutely convergent moments

\[
\mathfrak M_{r,M}
=\sum_\rho m_\rho
\frac{A(\rho)^r}{[(\rho+4)(5-\rho)]^M}.
\tag{T-91001.12}
\]

`L-91001` proves

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\limsup_{r\to\infty}|\mathfrak M_{r,M}|^{1/r}\le1.
}
\tag{T-91001.13}
\]

`L-91002` supplies two unusually strong prime-side facts:

\[
A(s)^r
=s^r\mathcal L(\theta^{*r})(s),
\qquad
\theta(t)=\{e^t\}\ge0,
\tag{T-91001.14}
\]

and

\[
\sup_t|A(3+it)|<3/4.
\tag{T-91001.15}
\]

Thus a proof of

\[
\boxed{|\mathfrak M_{r,M}|\le e^{o(r)}}
\tag{T-91001.16}
\]

from the positive fractional-part convolutions would prove RH.

`R-91001` explains why one-sided safe-line decay alone does not prove (T-91001.16): the reflected completed boundary is load bearing.

## 5. The two routes are one symbol calculus

Put

\[
h(s)=\zeta(s)-1,
\qquad
u(s)=\frac1{s-1}.
\]

Then

\[
\boxed{A(s)=\nu(s)-h(s),}
\tag{T-91001.17]

while

\[
\frac1{1+h(s)}=\frac1{\zeta(s)}.
\tag{T-91001.18}
\]

So:

```text
Brun route:
    polynomially precondition the singular inverse of 1+h;

Li route:
    take positive-kernel powers of the continuum-discrete error nu-h.
```

At a zeta zero, `h=-1`, and both calculi detect the same obstruction.

The proposed fusion theorem is:

> **FPBF — Fractional-Part Brun Factorisation.** Choose an even-depth probability polynomial `Q` at the scale diagonal and factor its finite source certificate in the declared half-power physical cone as
> \[
> \boxed{
> Q(h)(\mathbf1-\ell)
> =\sum_\nu \mathcal T_\nu(A)^*\mathcal T_\nu(A)
> +\mathcal E_r,
> }
> \tag{T-91001.19}
> \]
> where each `T_nu(A)` uses positive fractional-part convolution powers and the diagonal error obeys
> \[
> \mathcal E_r(X)\ge-O(r^K2^{-r/2}).
> \tag{T-91001.20}
> \]

A version with a strict positive margin dominating (T-91001.20) proves DBP, hence RH.

FPBF is not proved here. It is the exact new proof obligation.

## 6. Why this is a radical rather than cosmetic change

The prior finite-state cone route attempted to control the same sixteen Möbius samples at every scale. The present route instead lets the certificate order grow with the scale:

\[
r\sim\log_2X.
\]

At that moving order:

- the reciprocal-zeta remainder is positive at a first crossing;
- its absolute size is exponentially small;
- only `O(1)` nonminimal multiplicative defects survive;
- the certificate itself is Möbius-free;
- the continuum-discrete discrepancy has a positive convolution kernel;
- an off-line zero is exponentially amplified rather than merely retained.

This is the multiplicative analogue of increasing heat/Hermite order to isolate a terminal spectral defect, but it remains entirely in exact finite arithmetic.

## 7. Adversarial review tests

Reject the proposal if any of the following fails:

1. the phase-locked renewal is not exactly `(I+K)D=G` in the declared normalization;
2. the delays in `K` are not strict and positive;
3. the depth law uses an odd depth or negative weight;
4. the first-crossing remainder is estimated before its sign is used;
5. the certificate source still contains hidden Möbius coefficients;
6. the near-diagonal ordered-factor bound omits a cofactor or dyadic source shift;
7. a proposed FPBF factorisation drops the reflected completed boundary;
8. a numerical diagonal scan is promoted to DBP;
9. the `3/4` right-line contraction is used as though it controlled `A(1-s)^r`.

## 8. Exact proof boundary

Supplied here:

```text
fractional-part Li amplifier                    exact;
zero map and spectral-radius RH criterion       exact;
positive convolution powers                     exact;
strict safe-line contraction                    exact;
even-depth probability projectors               exact;
first-crossing orientation                       exact;
Möbius-free projector source                     exact;
near-diagonal polynomial complexity              exact;
exponentially small depth remainder              exact;
reflection shortcut                              refuted;
DBP -> RH                                        complete conditional;
subexponential Li moments -> RH                  complete conditional.
```

Still open:

```text
FPBF or another proof of DBP;
subexponential weighted Li-amplifier moments;
Riemann Hypothesis.
```

**RH remains unproved.** Reviewers are asked to verify the supplied theorems and the sharp new factorisation target, not to invent the missing factorisation.