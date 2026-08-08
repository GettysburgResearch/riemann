# T-32401 — A positive Jordan-totient Hardy-energy criterion for RH

Claim ID: `T-32401`  
Title: One explicit compact dyadic filter applied to the positive Jordan-totient source has weighted-energy abscissa equal to the rightmost zeta-zero displacement  
Status: **PROPOSED COMPLETE GLOBAL CRITERION — ENERGY BOUND NOT PROVED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32405`; standard half-plane Paley–Wiener/Hardy uniqueness and polynomial vertical bounds for zeta on fixed zero-free half-planes  
Scope: exact positive-source RH criterion; no unconditional proof of its subexponential energy estimate

## 1. Positive arithmetic source

Use the order-two Jordan totient

\[
\boxed{
 J_2(n)=n^2\prod_{p\mid n}(1-p^{-2})>0.
}
\tag{T-32401.1}
\]

By `L-32405`,

\[
\boxed{
 \sum_{n\ge1}{J_2(n)\over n^s}
 ={\zeta(s-2)\over\zeta(s)}
}
\tag{T-32401.2}
\]

initially for `Re s>3`, with meromorphic continuation thereafter.

The denominator contains every zeta zero. The only real pole to the right of the critical strip comes from the numerator at `s=3`.

## 2. Explicit compact pole-killing window

Let

\[
 L=\log2
\]

and let `B_K` be the `K`-fold convolution of the indicator of `[0,L]`, with any fixed integer

\[
 K\ge8.
\]

Then `B_K` is compactly supported and piecewise polynomial, and

\[
\boxed{
 \widehat B_K(z)
 =\left({1-2^{-z}\over z}\right)^K
}
\tag{T-32401.3}
\]

with the removable value at `z=0` understood.

The numerator pole `s=3` corresponds to

\[
 z=s-\frac12=\frac52.
\]

Define

\[
\boxed{
 H_J(u)=B_K(u)-2^{5/2}B_K(u-L).
}
\tag{T-32401.4}
\]

Its transform is

\[
\boxed{
 \widehat H_J(z)
 =\left({1-2^{-z}\over z}\right)^K
  \left(1-2^{5/2-z}\right).
}
\tag{T-32401.5}
\]

Hence:

1. `H_J` is real and compactly supported;
2. `widehat H_J(5/2)=0`, so the numerator pole is canceled;
3. the zeros of the first factor away from the removable origin lie on `Re z=0`;
4. the zeros of the last factor lie on `Re z=5/2`.

Therefore

\[
\boxed{
 \widehat H_J(z)\ne0
 \qquad(0<\Re z<1/2).
}
\tag{T-32401.6}

The window cancels the declared real pole but no possible RH counterexample pole.

## 3. Physical positive-source field

Define

\[
\boxed{
 Q_J(x)
 =\sum_{n\ge2}{J_2(n)\over\sqrt n}
 H_J(x-\log n).
}
\tag{T-32401.7}
\]

For every fixed real `x` the sum is finite because `H_J` is compactly supported.

For `Re z>5/2`, direct integration gives

\[
\boxed{
 \mathcal LQ_J(z)
 =\widehat H_J(z)
 \left[
 {\zeta(z-3/2)\over\zeta(z+1/2)}-1
 \right].
}
\tag{T-32401.8}
\]

The subtraction of one removes the `n=1` coefficient and is entire after multiplication by the compact-window transform.

## 4. Singularity audit

The numerator zeta pole is at `z=5/2` and is canceled by (T-32401.5).

Let `rho` be a nontrivial zeta zero with

\[
 \Re\rho>1/2
\]

and put

\[
 z_\rho=\rho-1/2.
\]

Then `0<Re z_rho<1/2`. Equation (T-32401.6) shows

\[
 \widehat H_J(z_\rho)\ne0.
\]

Moreover

\[
 \zeta(\rho-2)\ne0.
\]

Indeed `rho-2` is nonreal and has real part in `(-2,-1)`: it is neither a nontrivial zero nor a real negative-even trivial zero.

Thus every off-critical zero produces a genuine pole of (T-32401.8), with the same multiplicity as the denominator zero.

The pole of `zeta(s)` at `s=1` produces a zero of the quotient, not a singularity. No other real singularity remains in `Re z>0`.

## 5. Weighted-energy abscissa

Define

\[
 \Theta_\zeta
 =\sup_{\zeta(\rho)=0}\left(\Re\rho-\frac12\right).
\tag{T-32401.9}
\]

and

\[
 \sigma_{2,J}
 =\inf\left\{\sigma>0:
 \int_{\mathbb R}e^{-2\sigma x}|Q_J(x)|^2dx<\infty
 \right\}.
\tag{T-32401.10}
\]

Then

\[
\boxed{
 \sigma_{2,J}=\Theta_\zeta.
}
\tag{T-32401.11}
\]

### Lower bound

If the weighted `L^2` integral is finite at `sigma`, half-plane Paley–Wiener makes the Laplace transform holomorphic in `Re z>sigma`. Equation (T-32401.8), continued from its initial half-plane, would therefore be holomorphic there. Section 4 shows that every zeta zero with

\[
 \Re\rho-1/2>\sigma
\]

would create an uncancelled pole. Hence

\[
 \Theta_\zeta\le\sigma.
\]

### Upper bound

Fix `sigma>Theta_zeta`. The denominator is zero-free on every closed half-plane `Re z>=sigma`. After removal of the explicit `z=5/2` pole, the ratio in (T-32401.8) is holomorphic there.

The functional equation and standard fixed-strip estimates give polynomial vertical growth for `zeta(z-3/2)` and reciprocal-polynomial/logarithmic growth for `1/zeta(z+1/2)` on this fixed zero-free half-plane. The factor (T-32401.5), with `K>=8`, supplies more than enough inverse powers of `|Im z|` for an `L^2` boundary integral uniformly to the right of `sigma`.

Half-plane Paley–Wiener and uniqueness identify the Hardy inverse with the physical field (T-32401.7). Therefore the weighted energy is finite for every `sigma>Theta_zeta`.

This proves (T-32401.11).

## 6. Cumulative-energy criterion

Put

\[
 \mathcal E_J(X)=\int_{-\infty}^{X}|Q_J(x)|^2dx.
\tag{T-32401.12}
\]

The elementary abscissa/cumulative-mass lemma gives

\[
\boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
 {\log(1+\mathcal E_J(X))\over2X}.
}
\tag{T-32401.13}
\]

Consequently

\[
\boxed{
 \mathrm{RH}
 \iff
 \mathcal E_J(X)=\exp(o(X)).
}
\tag{T-32401.14}
\]

This criterion uses one fixed compact window and the **positive coefficients `J_2(n)` only**.

## 7. Exact relation to the all-order Hermitian square

`L-32405` proves

\[
 {\zeta(s-2+it)\zeta(s-2-iu)
  \over\zeta(s+it)\zeta(s-iu)}
 -{\zeta(s-2+it)\over\zeta(s+it)}
 -{\zeta(s-2-iu)\over\zeta(s-iu)}+1
\]

is, on the diagonal `u=t`, the literal square

\[
 \left|{\zeta(s-2+it)\over\zeta(s+it)}-1\right|^2.
\]

Thus the physical energy in this theorem is not an ad hoc positive form: it is the localized normal Gram of the fully resummed Selberg hierarchy.

Unlike the finite-order reflected identities, every nonconstant term already has two arithmetic Jordan legs.

## 8. Why this is a genuine change of coordinates

The source is neither Möbius nor prime-only:

```text
coefficient at n = positive Jordan totient J_2(n);
real numerator pole = canceled by one explicit dyadic window difference;
RH poles = denominator zeros, left untouched;
Hermitian square = exact all-order Selberg resummation.
```

The criterion therefore bypasses:

- terminal Möbius atomization;
- balanced Type-II packetization;
- Cycle-Debt source-flow capacity;
- endpoint-face enumeration;
- prime-only source-cone lifting.

Its remaining theorem is the direct positive-source energy estimate (T-32401.14).

## 9. Proof boundary

Closed here, subject to review:

- positive Jordan source;
- explicit compact pole-killing filter;
- complete singularity audit;
- weighted-energy abscissa equality;
- cumulative-energy RH criterion;
- exact connection to the all-order reflected Hermitian square.

Open:

- an unconditional proof that `mathcal E_J(X)=exp(o(X))`;
- RH.
