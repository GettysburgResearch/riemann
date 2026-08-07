# L-23013 — Positive p-adic digit combs and exact Euler-aligned inversions

Claim ID: `L-23013`  
Title: Every residue-digit comb is positive, carries one eta-type zeta factor, and annihilates its Euler-aligned Möbius source to a finite dilation polynomial  
Status: **PROPOSED COMPLETE EXACT ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-08  
Frozen parent: PR #236 at `1c9a749a1648c4772509eb3b056598c7044f4393`  
Dependencies: PR #236 `L-23010`--`L-23012`; elementary distributional differentiation and Euler products  
Scope: exact positive kernels and source identities; no coercive inverse or RH claim

## 1. Positive residue-digit kernel

Fix an integer `p>=2`, put

\[
h_p=\log p,
\qquad
r_p(n)=n-p\left\lfloor\frac np\right\rfloor\in\{0,\ldots,p-1\},
\]

and define the causal kernel

\[
\boxed{
P_p(t)=e^{-t/2}r_p(\lfloor e^t\rfloor)\mathbf 1_{t\ge0}.
}
\tag{L-23013.1}
\]

Then `P_p>=0` and

\[
P_p\in L^1(0,\infty)\cap L^2(0,\infty).
\tag{L-23013.2}
\]

The case `p=2` is exactly the parity comb `P_2` of `L-23012`.

## 2. Exact jump sequence

Extend `P_p` by zero to the negative half-line and differentiate in causal
distributions. The continuous exponential factor is removed by
`partial+1/2`, while the jump at `t=log n` is

\[
r_p(n)-r_p(n-1)=1-p\mathbf 1_{p\mid n}.
\]

Therefore

\[
\boxed{
\left(\partial+\frac12\right)P_p
=
\sum_{n\ge1}
\frac{1-p\mathbf 1_{p\mid n}}{\sqrt n}\,\delta_{\log n}.
}
\tag{L-23013.3}
\]

Taking Laplace transforms gives, initially for `Re z>1/2` and then by
continuation,

\[
\boxed{
\widehat P_p(z)
=
\frac{\left(1-p^{1/2}e^{-h_pz}\right)
      \zeta(z+1/2)}{z+1/2}.
}
\tag{L-23013.4}
\]

Thus `P_p` is a positive physical kernel whose only possible open-strip zeros
come from the Riemann zeta factor.

## 3. Full Möbius source

Let

\[
\alpha_\mu
=
\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}\,\delta_{\log n},
\qquad
w_\infty(t)=e^{-t/2}\mathbf1_{t\ge0}.
\]

Since `widehat alpha_mu(z)=1/zeta(z+1/2)`, equation (L-23013.4) gives

\[
\boxed{
P_p*\alpha_\mu
=
\left(I-p^{1/2}\tau_{h_p}\right)w_\infty.
}
\tag{L-23013.5}

This is a two-tap causal exponential, with no prime or zero remainder.

## 4. Euler-aligned source and compact output

Define

\[
\beta_p
=
\left(I-p^{-1/2}\tau_{h_p}\right)\alpha_\mu.
\tag{L-23013.6}
\]

Its coefficient is

\[
\boxed{
b_p(n)=\mu(n)-\mathbf1_{p\mid n}\mu(n/p),
}
\tag{L-23013.7}

and its Dirichlet series is

\[
\sum_n\frac{b_p(n)}{n^s}
=
\frac{1-p^{-s}}{\zeta(s)}.
\tag{L-23013.8}
\]

Combining (L-23013.5)--(L-23013.6),

\[
\boxed{
P_p*\beta_p
=
\left(I-p^{1/2}\tau_{h_p}\right)
\left(I-p^{-1/2}\tau_{h_p}\right)w_\infty.
}
\tag{L-23013.9}

For `t>=2h_p`, one has

\[
\tau_{h_p}^jw_\infty(t)=p^{j/2}w_\infty(t),
\]

and the polynomial in (L-23013.9) vanishes at `p^(1/2)`. Hence

\[
\boxed{
\operatorname{supp}(P_p*\beta_p)\subset[0,2\log p].
}
\tag{L-23013.10}

The exact source remains cofinal and RH-bearing, while its output under the
positive digit comb is compact.

## 5. p-free Möbius source

Let

\[
\alpha_{\mu,p\nmid}
=
\sum_{p\nmid n}\frac{\mu(n)}{\sqrt n}\,\delta_{\log n}.
\]

Then

\[
\alpha_{\mu,p\nmid}
=
\left(I-p^{-1/2}\tau_{h_p}\right)^{-1}\alpha_\mu,
\tag{L-23013.11}
\]

where the inverse is a causal `ell^1` filter. Consequently

\[
\boxed{
P_p*\alpha_{\mu,p\nmid}
=
\left(I-p^{1/2}\tau_{h_p}\right)
\left(I-p^{-1/2}\tau_{h_p}\right)^{-1}w_\infty.
}
\tag{L-23013.12}

This is an explicit p-adic layer ramp. It contains no odd-prime arithmetic.

## 6. Exact finite coefficient form

Put

\[
a_p(n)=1-p\mathbf1_{p\mid n}.
\]

Dirichlet convolution gives

\[
\boxed{
a_p*\mu=\delta_1-p\delta_p,
}
\tag{L-23013.13}

and

\[
\boxed{
a_p*b_p
=
\delta_1-(p+1)\delta_p+p\delta_{p^2}.
}
\tag{L-23013.14}

These are the coefficient versions of (L-23013.5) and (L-23013.9).

## 7. Proof boundary

Closed exactly:

- positivity and integrability of every `P_p`;
- its jump and transform formulas;
- the full-Möbius, aligned-Möbius, and p-free source contractions;
- compact support of the aligned output;
- the finite coefficient identities.

Not closed:

- any lower frame bound for inversion of `P_p`;
- source-specific coercivity;
- RH.
