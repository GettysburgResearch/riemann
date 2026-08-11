# L-90427 — The phase-locked half-source is exactly the dyadic bottom-charge source

Claim ID: `L-90427`  
Title: The factor-four positive half-source of the phase-locked PIG filter is the opposite-parity dipole of PR #268; its RH-sensitive current, finite bottom carry image, and critical adjoint square are one source in three coordinates  
Status: **PROPOSED COMPLETE EXACT CROSS-ROUTE IDENTIFICATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90424`--`L-90426`; PR #268 `L-26201/L-26204/L-26805`  
Scope: exact source/current/carry identities; no bottom-charge sign, current upper bound, PIG, or RH conclusion

## 1. Exact source identity

The half-source of `L-90426` has Dirichlet series

\[
B_D(s)
 =\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}.
\tag{L-90427.1}
\]

Its coefficient sequence is therefore exactly

\[
\boxed{
\omega_2
 =\mu-\frac32\delta_2*\mu
  +\frac12\delta_4*\mu,
}
\tag{L-90427.2}
\]

the compact opposite-parity dipole of PR #268.

Writing every integer as `2^a m` with `m` odd, its four nonzero dyadic layers are

\[
\boxed{
\begin{aligned}
\omega_2(m)&=\mu(m),\\
\omega_2(2m)&=-\frac52\mu(m),\\
\omega_2(4m)&=2\mu(m),\\
\omega_2(8m)&=-\frac12\mu(m),
\end{aligned}}
\tag{L-90427.3}
\]

and all higher layers vanish.

Thus the factor-four PIG half-filter did not create a new arithmetic source. It rediscovered the exact source already singled out by the carry/digital programme.

## 2. The hard current is the PR #268 RH-sensitive current

Let

\[
A_D=B_D^{-1}
\]

and let `Lambda_D` be its nonnegative generalized-prime sequence. The own current is

\[
\boxed{
q_D=\omega_2*\Lambda_D=-\omega_2\log.
}
\tag{L-90427.4}
\]

This is exactly the RH-sensitive current denoted

\[
W=\omega_2*\Lambda_\omega
\]

in PR #268 `L-26805`. The primitive positive-inverse coordinate rejected in PR #268 `R-26802` is not being used here.

The ordinary complete-prime factor-four scalar of `L-90426` differs from the physical field of `q_D` only by the two-atom dyadic gauge of `L-90426.13`. Hence the direct endpoint criterion, the source-convolved reflected current, and the annular split current on PR #268 are the same RH-sensitive object up to a fixed finite boundary.

## 3. Finite bottom carry image

For the average carry matrix

\[
\beta_{nq}
 =\frac{\lfloor n/q\rfloor
        [q-1-(n\bmod q)]}{n+1},
\]

PR #268 `L-26204` proves

\[
\boxed{
\sum_{q=2}^{n}\omega_2(q)\beta_{nq}
 =
\begin{cases}
-5/6,&n=2,\\
-1/2,&n=3,\\
0,&n\ge4.
\end{cases}}
\tag{L-90427.5}
\]

Therefore, if `c_X(n)` is the exact triangular inverse of the critical target

\[
q^{-1/2}\log(X/q),
\]

then

\[
\boxed{
5c_X(2)+3c_X(3)
 =-6\sum_{q\le X}
 \frac{\omega_2(q)}{\sqrt q}\log(X/q).
}
\tag{L-90427.6}
\]

This is the bottom-charge coordinate. It is a source primitive, while the factor-four PIG scalar uses the own current `q_D`; the two may not be identified numerically. They are two exact consumers of the same source.

## 4. The phase-locked full source is the critical adjoint of omega2

Let

\[
D^\#(y)=(1-2y)(1-4y)
 =1-6y+8y^2.
\tag{L-90427.7}
\]

The factor-16 source of `L-90424` satisfies

\[
\boxed{
b_*=D^\#(\delta_2)*\omega_2.}
\tag{L-90427.8}
\]

On the critical circle, `D#` is the adjoint of the factor-four source polynomial `D`; consequently

\[
Q_*=DD^\#
\]

is the critically phase-locked normal operator of the same source.

For the source Riesz means

\[
\mathcal R_f(X)
 =\sum_{q\le X}\frac{f(q)}{\sqrt q}\log(X/q),
\]

finite scaling gives

\[
\boxed{
\mathcal R_{b_*}(X)
 =\mathcal R_{\omega_2}(X)
 -3\sqrt2\,\mathcal R_{\omega_2}(X/2)
 +4\mathcal R_{\omega_2}(X/4).
}
\tag{L-90427.9]

(The closing bracket in the tag is typographical only.)

Combining with (L-90427.6), if

\[
B(X)=5c_X(2)+3c_X(3),
\]

then

\[
\boxed{
-6\mathcal R_{b_*}(X)
 =B(X)-3\sqrt2\,B(X/2)+4B(X/4).
}
\tag{L-90427.10]

Thus the full phase-locked source is a three-scale critical adjoint of the single bottom charge. This does not prove the sign of either side.

## 5. Finite carry image of the full phase-locked source

The divisor-prefix coefficients of `b_*` are

\[
\delta_1-\frac{15}{2}\delta_2
 +\frac{35}{2}\delta_4-15\delta_8+4\delta_{16}.
\]

Both their total mass and first moment vanish. Hence the average carry image is exactly zero from row sixteen onward. Direct summation gives

\[
\boxed{
K_*(n):=\sum_{q=2}^{n}b_*(q)\beta_{nq}
 =
\begin{cases}
-17/6,&n=2,\\
-1/2,&n=3,\\
(101-11n)/(n+1),&4\le n\le7,\\
4(n-31)/(n+1),&8\le n\le15,\\
0,&n\ge16.
\end{cases}}
\tag{L-90427.11]

Therefore

\[
\boxed{
\mathcal R_{b_*}(X)
 =\sum_{n=2}^{15}K_*(n)c_X(n).
}
\tag{L-90427.12]

The critically phase-locked reciprocal-zeta source has a fourteen-row exact carry consumer.

## 6. Strategic consequence

Three routes now meet on one finite source:

```text
carry route:
    bottom charge 5c_X(2)+3c_X(3);

Q4/PIG endpoint route:
    factor-four own current q_D plus two-atom gauge;

phase-locked route:
    factor-16 critical adjoint square b_*.
```

The new phase-lock and coercivity theorems therefore attach directly to PR #268's already-developed annular split, digital, Selberg, and source-change infrastructure. They do not prove PR #268's complete source-weighted transition reserve, and they do not turn bottom-charge positivity into a current bound.

A valid continuation should exploit the common source before taking a norm; treating the three coordinates as independent would double-count the same arithmetic obstruction.

## 7. Proof boundary

Closed exactly here:

1. source identity with `omega_2`;
2. four dyadic layers;
3. current identity with PR #268's `W`;
4. finite bottom carry image;
5. critical-adjoint source relation;
6. three-scale bottom-charge relation;
7. fourteen-row full-source carry image;
8. exact cross-route map.

Open:

1. bottom-charge one-sign;
2. source-weighted reflected product-gram upper bound;
3. critical growth of the factor-four/factor-16 currents;
4. RH.