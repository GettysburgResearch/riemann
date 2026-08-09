# L-32314 — The shifted-zeta bottom tail has the critical SHARP scalar as its exact curvature

Claim ID: `L-32314`  
Title: The continuum bottom-tail Riesz mean is a positive-renewal `C^1` function whose scaled second derivative is exactly the RH-bearing all-depth SHARP scalar  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/FINITE-SUM THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: `L-32313`; parent PR #329 `T-32302` and `L-32312`  
Scope: exact bridge between the finite-band tail and the all-depth continuum margin; no sign theorem and no RH claim

## 1. The two continuum states

For real `x>=1`, put

\[
 M(x)=\sum_{n\le x}\mu(n),\qquad
 A(x)=\sum_{n\le x}{\mu(n)\over\sqrt n},\qquad
 B(x)=\sum_{n\le x}{\mu(n)\over n}.
\]

The bottom-tail state isolated in `L-32313` is

\[
\boxed{
 C(x)=B(x)-{2A(x)\over\sqrt x}+{M(x)\over x}.
}
\tag{L-32314.1}
\]

Equivalently,

\[
\boxed{
 C(x)=\sum_{n\le x}{\mu(n)\over n}
 \left(1-\sqrt{n/x}\right)^2
 =\sum_{n\le x}\mu(n)
 \left(n^{-1/2}-x^{-1/2}\right)^2.
}
\tag{L-32314.2}
\]

The critical fixed-ratio SHARP scalar of `T-32302` is

\[
\boxed{
 \Psi(x)=4\sqrt x\,B(x)-3A(x).
}
\tag{L-32314.3}
\]

Its eventual one-sidedness is already known to imply RH.  The point of this theorem is that `C` and `Psi` are not merely adjacent Möbius means: `Psi` is the exact curvature of `C`.

## 2. Exact positive renewal for the bottom tail

Define the harmonic multiplicative renewal operator

\[
 (\mathcal Hf)(x)=\sum_{d\le x}{1\over d}f(x/d).
\]

Using (L-32314.2), finite divisor switching gives

\[
\begin{aligned}
 \mathcal HC(x)
 &=\sum_{d\le x}{1\over d}
   \sum_{n\le x/d}{\mu(n)\over n}
   \left(1-\sqrt{dn/x}\right)^2\\
 &=\sum_{m\le x}{1\over m}
   \left(1-\sqrt{m/x}\right)^2
   \sum_{n\mid m}\mu(n).
\end{aligned}
\]

Only `m=1` survives. Therefore

\[
\boxed{
 \sum_{d\le x}{1\over d}C(x/d)
 =\left(1-x^{-1/2}\right)^2.
}
\tag{L-32314.4}
\]

This is a positive renewal identity with a positive square forcing. It is exact for every real `x>=1`; no asymptotic estimate is used.

If

\[
\boxed{H(x)=x^2C(x),}
\tag{L-32314.5}
\]

then (L-32314.4) is equivalently

\[
\boxed{
 \sum_{d\le x}d\,H(x/d)
 =(x-\sqrt x)^2.
}
\tag{L-32314.6}
\]

The forcing on the right is convex on `[1,infinity)`.

## 3. Regularity at the arithmetic breakpoints

For a fixed `n`, the newly activated summand

\[
 {\mu(n)\over n}\left(1-\sqrt{n/x}\right)^2
\]

vanishes to second order at `x=n`. Consequently both the summand and its first derivative vanish at activation.

It follows that

\[
\boxed{C\in C^1([1,\infty)),\qquad H=x^2C\in C^1([1,\infty)).}
\tag{L-32314.7}
\]

Both functions are smooth on every open interval `(N,N+1)`.  Their second derivatives have finite one-sided limits at every integer.

More precisely, the new `n=N` summand contributes

\[
 \Delta H''(N)={\mu(N)\over2N}.
\tag{L-32314.8}
\]

There is no delta mass in the second derivative because `H'` is continuous.

## 4. Exact curvature identity

On an interval `N<x<N+1`, the three prefixes `M,A,B` are constant. Equation (L-32314.1) gives

\[
 H(x)=x^2B(N)-2x^{3/2}A(N)+xM(N).
\tag{L-32314.9}
\]

Differentiating twice,

\[
 H''(x)=2B(N)-{3A(N)\over2\sqrt x}.
\tag{L-32314.10}
\]

Multiplication by `2sqrt(x)` yields

\[
 2\sqrt x\,H''(x)
 =4\sqrt x\,B(N)-3A(N)
 =\Psi(x).
\]

Thus

\[
\boxed{
 \Psi(x)=2\sqrt x\,{d^2\over dx^2}\bigl[x^2C(x)\bigr]
}
\tag{L-32314.11}
\]

on every open arithmetic interval.

The jump in the right side at `x=N` is, by (L-32314.8),

\[
 2\sqrt N\,{\mu(N)\over2N}
 ={\mu(N)\over\sqrt N},
\]

which is exactly the jump law for `Psi` proved in parent `L-32312`. Therefore (L-32314.11) holds globally with the right-second-derivative convention, and equivalently as an equality of locally integrable distributions.

Writing `D=x d/dx` and `F(x)=sqrt(x)C(x)`, the same identity is

\[
\boxed{
 \Psi=2(D+\tfrac12)(D+\tfrac32)F.
}
\tag{L-32314.12}
\]

## 5. Mellin compatibility

`L-32313` gives

\[
 \int_1^\infty C(x)x^{-s-1}\,dx
 ={1\over s(s+1)(2s+1)\zeta(s+1)}.
\tag{L-32314.13}
\]

Hence

\[
 \int_1^\infty F(x)x^{-z-1}\,dx
 ={1\over (z-\frac12)(z+\frac12)(2z)\zeta(z+\frac12)}.
\tag{L-32314.14}
\]

Multiplication by the symbol `2(z+1/2)(z+3/2)` of the operator in (L-32314.12) gives

\[
 {z+\frac32\over z(z-\frac12)\zeta(z+\frac12)},
\]

exactly the Mellin transform of `Psi` in `T-32302`.

This explains spectrally what (L-32314.11) does: two Euler derivatives move the harmless-looking shifted denominator `zeta(s+1)` back to the critical denominator `zeta(z+1/2)`.

## 6. Convexity is precisely the missing all-depth sign

Because `H=x^2C` is `C^1`, it is convex on an interval if and only if its one-sided second derivative is nonnegative there. Equation (L-32314.11) therefore gives

\[
\boxed{
 H=x^2C\text{ is eventually convex}
 \iff
 \Psi(x)\ge0\text{ eventually}.
}
\tag{L-32314.15}
\]

Likewise eventual concavity of `H` is equivalent to eventual nonpositivity of `Psi`.

Since parent `T-32302` proves that either eventual one-sign of `Psi` excludes every off-line zeta zero,

\[
\boxed{
 x^2C(x)\text{ eventually convex or eventually concave}
 \Longrightarrow \mathrm{RH}.
}
\tag{L-32314.16}
\]

No convexity or concavity is asserted here.

## 7. Exact connection to the fixed-ratio SHARP margin

For a noninteger fixed ratio `x=T/j`, parent `T-32302` proves

\[
 \lim \sqrt T\,j c_T(j)
 ={\sqrt x\over2}\Psi(x).
\tag{L-32314.17}
\]

Using (L-32314.11), this becomes

\[
\boxed{
 \lim \sqrt T\,j c_T(j)
 =x\,{d^2\over dx^2}\bigl[x^2C(x)\bigr].
}
\tag{L-32314.18}
\]

Thus the finite quotient-band programme is literally a directed finite approximation to the convexity of `x^2C`:

```text
bottom tail at depth R
+
local quotient-cell term
=
curvature of x^2 C at the limiting ratio.
```

The one-tail criterion `L-32312` is therefore not an unrelated sufficient estimate. It is a finite-endpoint lower certificate for the exact curvature in (L-32314.18).

In particular, the outer `255/256` theorem proves the corresponding finite-endpoint curvature inequalities throughout every ratio cell below depth 256. Passing to fixed-ratio limits gives nonnegative curvature on that finite continuum range.

## 8. New proof-facing formulation

The all-depth elementary route may now be stated without a triangular inverse:

> **Shifted-tail convexity problem.**  For
+> \[
+> C(x)=\sum_{n\le x}{\mu(n)\over n}
+>       (1-\sqrt{n/x})^2,
+> \]
+> prove eventual convexity or eventual concavity of `x^2C(x)`.
+
The function being differentiated has:

1. the positive-square renewal (L-32314.4);
2. a shifted-zeta Mellin transform whose nontrivial poles all lie strictly left of `Re(s)=0`;
3. `C^1` matching across every arithmetic breakpoint;
4. explicit second-derivative impulses (L-32314.8).

The RH-bearing obstruction appears only after taking the exact curvature (L-32314.11). This separates the subcritical renewal state from the critical sign-producing differential observable.

A proof must control curvature, not merely positivity of `C`; positivity alone does not imply (L-32314.15).

## 9. Proof boundary

Closed exactly here, subject to review:

1. the positive harmonic renewal for `C`;
2. the equivalent renewal for `H=x^2C`;
3. `C^1` regularity and the exact second-derivative jump;
4. the global curvature identity `Psi=2sqrt(x)(x^2C)''`;
5. Mellin compatibility with both prior transforms;
6. equivalence between the all-depth SHARP sign and convexity/concavity of `x^2C`;
7. the fixed-ratio SHARP margin as `x(x^2C)''`.

Still open:

1. eventual convexity or concavity of `x^2C`;
2. eventual one-sidedness of `Psi`;
3. full SHARP;
4. RH.
