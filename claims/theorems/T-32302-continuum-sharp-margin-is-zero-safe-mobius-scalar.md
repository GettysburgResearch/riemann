# T-32302 — The continuum SHARP margin is one zero-safe Möbius scalar

Claim ID: `T-32302`  
Title: Fixed-ratio square-root-hinge coefficients converge to a single weighted Möbius scalar whose eventual one-sidedness implies RH  
Status: **PROPOSED COMPLETE EXACT LIMIT / CONDITIONAL RH THEOREM — SCALAR SIGN OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32303/L-32304`; elementary Riemann sums; Landau one-sign theorem  
Scope: asymptotic fixed-ratio SHARP margin and its Mellin firewall; no proof of the scalar sign or RH

## 1. Two weighted Möbius prefixes

For real `x>=1` define

\[
 A(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n},
 \qquad
 B(x)=\sum_{n\le x}\frac{\mu(n)}n.
\]

Put

\[
\boxed{
 \Psi(x)=4\sqrt x\,B(x)-3A(x).
}
\tag{T-32302.1}

This is a completely explicit step/square-root arithmetic function. No carry inverse occurs in its definition.

## 2. Exact fixed-ratio SHARP limit

Fix a noninteger real number

\[
 x>1,
 \qquad
 K=\lfloor x\rfloor,
 \qquad
 y=1/x.
\]

Let `T_r -> infinity` be any integer sequence and choose integers `j_r` such that

\[
 \frac{j_r}{T_r}\longrightarrow y.
\]

Because `x` lies strictly inside the quotient cell `(K,K+1)`, after modifying finitely many terms if necessary we may and do require

\[
\left\lfloor\frac{T_r}{j_r}\right\rfloor
=\left\lfloor\frac{T_r}{j_r+1}\right\rfloor
=K.
\tag{T-32302.2}

Retain

\[
 A_K=\sum_{k\le K}\frac{\mu(k)}{\sqrt k},
 \qquad
 M_K=\sum_{k\le K}\mu(k),
 \qquad
 B_K=\sum_{k\le K}\frac{\mu(k)}k.
\]

Then `L-32304` gives exactly on the same quotient cell

\[
 u_T(m)=\frac{A_K}{\sqrt m}-\frac{M_K}{\sqrt T}.
\tag{T-32302.3}

### Local term

Let

\[
 \mathcal L_T(j)
 =(j+2)u_T(j)-ju_T(j+1).
\]

Since

\[
 \sqrt j\left(
 \frac{j+2}{\sqrt j}-\frac{j}{\sqrt{j+1}}
 \right)\longrightarrow\frac52,
\]

(T-32302.3) gives

\[
\boxed{
 \sqrt T\,\mathcal L_T(j_r)
 \longrightarrow
 \frac52A_K\sqrt x-2M_K.
}
\tag{T-32302.4}

### Tail term

The exact tail may be rearranged as

\[
\begin{aligned}
 S_T(j)
 &=\sum_{m=j}^{T}\sum_{k\le T/m}\mu(k)
 \left((mk)^{-1/2}-T^{-1/2}\right)\\
 &=\sum_{k\le K}\mu(k)
 \sum_{m=j}^{\lfloor T/k\rfloor}
 \left((mk)^{-1/2}-T^{-1/2}\right)
\end{aligned}
\tag{T-32302.5}

for all sufficiently large `T=T_r`, because `T_r/j_r -> x in (K,K+1)`.

For each fixed `k<=K`, the elementary Riemann-sum limit is

\[
\frac1{\sqrt T}
\sum_{m=j}^{\lfloor T/k\rfloor}\frac1{\sqrt{mk}}
\longrightarrow
\frac1{\sqrt k}\int_y^{1/k}t^{-1/2}\,dt
=rac2k-rac{2\sqrt y}{\sqrt k},
\]

while

\[
\frac{\lfloor T/k\rfloor-j+1}{T}
\longrightarrow\frac1k-y.
\]

Hence

\[
\boxed{
 \frac{S_T(j_r)}{\sqrt{T_r}}
 \longrightarrow
 B_K-\frac{2A_K}{\sqrt x}+\frac{M_K}{x}.
}
\tag{T-32302.6}

Since `T_r/(j_r-1)->x`, the tail contribution in the exact SHARP identity obeys

\[
\boxed{
 \sqrt{T_r}\frac{2S_{T_r}(j_r)}{j_r-1}
 \longrightarrow
 2xB_K-4\sqrt x A_K+2M_K.
}
\tag{T-32302.7}

### Cancellation of the Mertens coordinate

The exact identity

\[
 j c_T(j)
 =\mathcal L_T(j)+\frac{2S_T(j)}{j-1}
\]

now combines (T-32302.4) and (T-32302.7). The `M_K` terms cancel completely:

\[
\begin{aligned}
\lim_{r\to\infty}
 \sqrt{T_r}\,j_r c_{T_r}(j_r)
 &=2xB_K-\frac32\sqrt x A_K\\
 &=\boxed{
 \frac{\sqrt x}{2}\Psi(x).}
\end{aligned}
\tag{T-32302.8}

This limit is independent of how the endpoint sequence approaches the fixed interior quotient ratio.

## 3. Consequence for full SHARP

If full SHARP holds, then

\[
 c_T(j)\ge0
\]

for every finite endpoint and coefficient index. Taking the limit (T-32302.8) gives

\[
\boxed{
 \Psi(x)\ge0
 \qquad\text{for every noninteger }x>1.
}
\tag{T-32302.9}

Thus the positive fixed-ratio continuum margin is a necessary consequence of SHARP.

Conversely, if `Psi(x_0)<0` at one noninteger `x_0`, then (T-32302.8) forces

\[
 c_T(j)<0
\]

along every sufficiently large same-cell sequence with `T/j -> x_0`. One negative value of `Psi` therefore refutes SHARP cofinally.

## 4. Mellin transform of the continuum margin

For `Re z>1/2`, absolute convergence permits finite Fubini:

\[
\int_1^\infty A(x)x^{-z-1}\,dx
=\frac1z\sum_{n\ge1}\frac{\mu(n)}{n^{z+1/2}}
=\frac1{z\zeta(z+1/2)}.
\tag{T-32302.10}

Likewise

\[
\int_1^\infty \sqrt x B(x)x^{-z-1}\,dx
=\frac1{z-1/2}
\sum_{n\ge1}\frac{\mu(n)}{n^{z+1/2}}
=\frac1{(z-1/2)\zeta(z+1/2)}.
\tag{T-32302.11}

Therefore

\[
\boxed{
 \int_1^\infty\Psi(x)x^{-z-1}\,dx
 =\frac{z+3/2}
 {z(z-1/2)\zeta(z+1/2)}.
}
\tag{T-32302.12}

The apparent singularity at `z=1/2` is removable because `zeta(z+1/2)` has its simple pole there.

There is no singularity on the positive real axis. At a nontrivial zeta zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad\delta>0,
\]

the point

\[
 z_\rho=\rho-\frac12
\]

is a genuine nonreal pole of (T-32302.12): the numerator is

\[
 z_\rho+\frac32=\rho+1\ne0.
\]

Thus every off-line zeta zero is retained.

## 5. Eventual one-sign of `Psi` implies RH

Assume `Psi(x)` has one sign for all sufficiently large real `x`.

After changing `Psi` on a compact interval, `f(t)=Psi(e^t)` is a nonnegative or nonpositive locally integrable function. Its Laplace transform differs from (T-32302.12) only by an entire function.

If an off-line zero existed, the transform would have a nonreal pole with positive real part, so its abscissa of convergence would be positive. Landau's one-sign theorem then forces a singularity at the corresponding positive **real** boundary point. But (T-32302.12) has no positive-real singularity. Contradiction.

Hence

\[
\boxed{
 \Psi(x)\text{ eventually one-signed}
 \Longrightarrow\mathrm{RH}.
}
\tag{T-32302.13}

In particular the all-depth same-cell positivity forced by full SHARP is itself already RH-bearing.

## 6. The deterministic zero-frequency baseline

Equation (T-32302.12) has a simple boundary pole at `z=0` with residue

\[
\boxed{
 -\frac3{\zeta(1/2)}>0.
}
\tag{T-32302.14}

This explains the persistent positive numerical baseline seen in finite quotient reconnaissance. Critical-line zeta zeros contribute boundary oscillations; a hypothetical off-line zero contributes a positive-horizontal-exponent mode.

The positive baseline is not a proof of one-sidedness.

## 7. Meaning for the quotient-band programme

The exact sequence of theorems

```text
T/8,
T/16,
T/32,
T/64,
...
```

can be extended through any **fixed** finite quotient range by verifying finitely many Mobius/radical gates and retaining enough global tail reserve. Equation (T-32302.8) identifies what happens when one tries to make that argument uniform as the quotient depth tends to infinity:

```text
finite quotient bookkeeping
    -> continuum margin Psi(x)
    -> zero-safe reciprocal-zeta scalar.
```

Therefore the shrinking margins are structural, not merely poor constants. An arbitrary-depth uniform tail theorem strong enough to make `Psi` eventually one-signed would itself prove RH by Section 5.

This does not make the finite-band theorems vacuous: they prove that any SHARP counterexample must move to progressively smaller relative index and isolate the exact scalar controlling that escape.

## 8. Proof boundary

Closed exactly, subject to review:

1. fixed-ratio limit of the local SHARP term;
2. fixed-ratio Riemann-sum limit of the complete Mobius tail;
3. exact cancellation of `M_K` and formula (T-32302.8);
4. necessity of `Psi>=0` for full SHARP;
5. Mellin transform (T-32302.12) and zero audit;
6. eventual one-sign `Psi -> RH` by Landau;
7. identification of the arbitrary-depth quotient-band frontier.

Open:

1. eventual one-sidedness of `Psi`;
2. a uniform all-depth SHARP theorem;
3. full SHARP;
4. RH.
