# L-32408 — The critical target is a positive alpha-hinge mixture for every alpha at most one half

Claim ID: `L-32408`  
Title: For every fixed `0<alpha<=1/2`, the critical carry target is an exact nonnegative finite combination of endpoint-vanishing fractional-power hinges `q^-alpha-T^-alpha`  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: elementary convexity; same finite divided-difference argument as PR #295 `L-29203`  
Scope: exact target decomposition only; no fractional-hinge flow theorem or RH conclusion

## 1. Fractional hinge family

Fix an integer endpoint `X>=3` and a real exponent

\[
 0<\alpha\le {1\over2}.
\]

For every integer `3<=T<=X`, define

\[
\boxed{
 h_{T,\alpha}(q)
 =\begin{cases}
 q^{-\alpha}-T^{-\alpha},&2\le q\le T,\\
 0,&q>T.
 \end{cases}}
\tag{L-32408.1}
\]

Every hinge is nonnegative, decreasing in the carry coordinate, and vanishes exactly at its endpoint.

It also has exact factor-two self-similarity:

\[
\boxed{
 h_{2T,\alpha}(2q)=2^{-\alpha}h_{T,\alpha}(q).
}
\tag{L-32408.2}
\]

## 2. The correct convex coordinate

Put

\[
 x_q=q^{-\alpha},
 \qquad
 p={1\over2\alpha}\ge1.
\tag{L-32408.3}
\]

Then

\[
 q^{-1/2}=x_q^p
\]

and

\[
 \log{X\over q}
 ={1\over\alpha}\log{x_q\over x_X}.
\]

Therefore the critical target

\[
 w_X(q)=q^{-1/2}\log(X/q)
\]

is

\[
\boxed{
 w_X(q)=F_{X,\alpha}(x_q),
 \qquad
 F_{X,\alpha}(x)
 ={1\over\alpha}x^p\log{x\over x_X}.
}
\tag{L-32408.4}

The endpoint value is `F_(X,alpha)(x_X)=0`.

Differentiate twice:

\[
 F_{X,\alpha}''(x)
 ={1\over\alpha}x^{p-2}
 \left[
 p(p-1)\log{x\over x_X}+2p-1
 \right].
\tag{L-32408.5}
\]

Since `p>=1` and `x>=x_X`, every term in the bracket is nonnegative and `2p-1>=1`. Hence

\[
\boxed{
 F_{X,\alpha}''(x)>0
 \qquad(x_X\le x\le x_2).
}
\tag{L-32408.6}

Thus the critical target is strictly convex in **every** fractional coordinate `q^-alpha` with `alpha<=1/2`.

## 3. Exact positive divided-difference coefficients

For `2<=q<=X-1`, define the secant slopes

\[
 \sigma_q^{(\alpha)}
 ={w_X(q)-w_X(q+1)
   \over
   q^{-\alpha}-(q+1)^{-\alpha}}.
\tag{L-32408.7}
\]

Because the points `x_q` decrease with `q` and `F_(X,alpha)` is strictly convex,

\[
 \sigma_2^{(\alpha)}
 \ge\sigma_3^{(\alpha)}
 \ge\cdots
 \ge\sigma_{X-1}^{(\alpha)}>0.
\tag{L-32408.8}

Define

\[
\boxed{
 \lambda_{X,X}^{(\alpha)}=\sigma_{X-1}^{(\alpha)},
 \qquad
 \lambda_{X,T}^{(\alpha)}
 =\sigma_{T-1}^{(\alpha)}-\sigma_T^{(\alpha)}
 \quad(3\le T<X).
}
\tag{L-32408.9}

Then

\[
\boxed{
 \lambda_{X,T}^{(\alpha)}\ge0.
}
\tag{L-32408.10}

## 4. Positive alpha-hinge identity

For every carry coordinate `2<=q<=X`,

\[
\boxed{
 w_X(q)
 =\sum_{T=3}^{X}
 \lambda_{X,T}^{(\alpha)}h_{T,\alpha}(q).
}
\tag{L-32408.11}

Indeed both sides vanish at `q=X`. Their first differences agree because

\[
 h_{T,\alpha}(q)-h_{T,\alpha}(q+1)
 =\begin{cases}
 q^{-\alpha}-(q+1)^{-\alpha},&T\ge q+1,\\
 0,&T\le q,
 \end{cases}
\]

and

\[
 \sum_{T=q+1}^X\lambda_{X,T}^{(\alpha)}
 =\sigma_q^{(\alpha)}.
\]

This proves the finite identity exactly.

For `alpha=1/2`, (L-32408.11) is PR #295 `L-29203`.

## 5. Consequence for the carry route

Suppose that for one fixed exponent

\[
 0<\alpha\le1/2
\]

and every endpoint `T` there exists a nonnegative balanced split flow whose carry load is exactly `h_(T,alpha)`.

Extend each finite flow by zero to endpoint `X` and combine them using the nonnegative coefficients in (L-32408.11). The result is a nonnegative exact carry saturation of the complete critical target `w_X`.

Therefore

\[
\boxed{
 \text{positive carry flows for all }h_{T,\alpha}
 \Longrightarrow
 \text{critical carry saturation}
 \Longrightarrow
 \text{the existing prime-ramp/RH consumer}.
}
\tag{L-32408.12}

The logarithmic RH target does **not** single out `alpha=1/2`. Any one fractional exponent in `(0,1/2]` is sufficient.

## 6. Strategic consequence

This changes the elementary theorem search from

```text
prove square-root SHARP at alpha=1/2
```

to

```text
choose any alpha in (0,1/2]
for which the finite hinge inverse has the strongest arithmetic structure,
and prove positivity there.
```

The exact factor-two scaling becomes `2^-alpha`; endpoint vanishing and positive superposition are retained for the entire family.

In particular rational exponents such as `alpha=1/3`, `1/4`, and `1/2` may now be compared on structural rather than merely numerical grounds.

## 7. Proof boundary

Closed exactly:

- strict convexity of the critical target in every coordinate `q^-alpha`, `0<alpha<=1/2`;
- explicit nonnegative finite divided-difference coefficients;
- exact positive alpha-hinge decomposition;
- factor-two self-similarity;
- positive-flow superposition to the full critical target.

Open:

- a nonnegative carry realization of all `h_(T,alpha)` for any one fixed `alpha<=1/2`;
- fractional SHARP;
- RH.
