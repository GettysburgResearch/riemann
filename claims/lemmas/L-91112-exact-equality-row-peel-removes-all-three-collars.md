# L-91112 — Exact equality rows remove the target mismatch, terminal annulus, and quantization collar simultaneously

Claim ID: `L-91112` (provisional research range)  
Title: The continuously generated equality inverse has nonnegative exact rows throughout the certified factor-54 window; truncating those exact rows saturates every outer ordinary and radix-four detail column without approximation and leaves one source-complete inner residual  
Status: **PROPOSED COMPLETE EXACT FINITE/CONTINUOUS-ROW THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-12  
Depends on: PR #265 `L-26201/L-26204`; PR #352 `L-90029`; `L-91106/L-91107`  
Scope: exact outer peel and residual identity; no positivity theorem for the complete inner residual and no RH conclusion

## 1. Real endpoint rows

For real `s>=2`, retain the zero-extended parabolic seed

\[
 b_s(m)=2\sqrt m\left[
 \log\frac sm-2\left(1-\sqrt{m/s}\right)
 \right]\mathbf 1_{m\le s}.
\tag{L-91112.1}
\]

Put

\[
 A_s(m)=\frac{b_s(m)}{m-1},
 \qquad
 d_s(n)=(n+1)[A_s(n)-2A_s(n+1)+A_s(n+2)].
\tag{L-91112.2}
\]

The activation value and first endpoint derivative of `b_s(m)` both vanish at `s=m`. Thus `s -> d_s(n)` is continuously differentiable across every activation boundary.

For `s>=m`,

\[
 \dot A_s(m)
 =\frac{2}{m-1}\left(
 \frac{\sqrt m}{s}-\frac{m}{s^{3/2}}
 \right).
\tag{L-91112.3}
\]

## 2. Infinitesimal endpoint positivity

For every integer `n>=2`,

\[
\boxed{
 \dot d_s(n)\ge0
 \qquad(s\ge n).
}
\tag{L-91112.4}
\]

The inequality is strict away from the activation points.

### First activation strip

For `n<s<n+1`, only `A_s(n)` is active, and

\[
 \dot d_s(n)=(n+1)\dot A_s(n)>0.
\tag{L-91112.5}
\]

### Second activation strip

For `n+1<s<n+2`,

\[
 \dot d_s(n)=(n+1)[\dot A_s(n)-2\dot A_s(n+1)].
\tag{L-91112.6}
\]

Writing `m=n+1`, multiplication by the positive factor `s` reduces this to the boundary inequality for

\[
 C_s(x)=\frac{2(\sqrt x-x/\sqrt s)}{x-1}.
\]

On `m<=s<=m+1`, the expression `C_s(m-1)-2C_s(m)` is minimized at `s=m+1`. At that endpoint, with

\[
 a=\sqrt{\frac m{m+1}},
 \qquad
 b=\sqrt{\frac{m-1}{m+1}},
\]

positivity is equivalent to

\[
 (m-1)b(1+a)>(m-2)a(1+b).
\tag{L-91112.7}
\]

After using

\[
 a-b=\frac1{(m+1)(a+b)},
\]

the difference is

\[
 b(1+a)-(m-2)(a-b)>0.
\]

This is the pointwise boundary estimate underlying PR #265's positive endpoint increments.

### Deep strip

For `s>=n+2`, all three nodes are active. The exact derivative from PR #265 is

\[
 C_s''(x)=
 \frac{
 3\sqrt s\,x^2+6\sqrt s\,x-\sqrt s-8x^{3/2}
 }
 {2\sqrt s\,x^{3/2}(x-1)^3}.
\tag{L-91112.8}
\]

When `s>=x`, its numerator is at least

\[
 \sqrt x(3x^2+6x-1)-8x^{3/2}
 =\sqrt x(3x+1)(x-1)>0.
\]

Hence `C_s` is strictly convex on `[n,n+2]`, and its discrete second difference gives `dot d_s(n)>0`.

This proves (L-91112.4).

## 3. Exact equality-row representation

Let

\[
 L(x)=2\sqrt x\sum_{k\le x}\frac{\mu(k)}k
      -\sum_{k\le x}\frac{\mu(k)}{\sqrt k}
\tag{L-91112.9}
\]

be the endpoint equality density of `L-91107`. Let `b_X^star` be the exact zero-extended seed satisfying

\[
 v_q(b_X^\star)=w_X(q),
 \qquad
 w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}.
\tag{L-91112.10}
\]

The Volterra inversion of `L-91107` gives, for every node `m`,

\[
\boxed{
 b_X^\star(m)
 =\int_m^X L(X/s)\,\partial_s b_s(m)\,ds.
}
\tag{L-91112.11}
\]

Let `c_X(n)` be the unique average-carry row inverse of `w_X`. The row operator is finite and linear, and all activation boundary terms vanish. Therefore

\[
\boxed{
 c_X(n)
 =\int_n^X L(X/s)\,\dot d_s(n)\,ds.
}
\tag{L-91112.12}
\]

This is an exact real-endpoint representation of the finite equality row; it is not an asymptotic quadrature.

## 4. Exact factor-54 outer row positivity

Let `c_0` be the directed crossing from `L-91106`:

\[
 0.01844367547103<c_0<0.01844367547105,
\tag{L-91112.13}
\]

and put

\[
 K_X=\lceil c_0X\rceil.
\tag{L-91112.14}
\]

`L-91107` proves

\[
 L(x)>0.3186
 \qquad(1\le x\le c_0^{-1}).
\tag{L-91112.15}
\]

If `n>=K_X` and `s>=n`, then

\[
 1\le X/s\le X/K_X\le c_0^{-1}.
\]

Combining (L-91112.4), (L-91112.12), and (L-91112.15),

\[
\boxed{
 c_X(n)\ge0
 \qquad(K_X\le n\le X).
}
\tag{L-91112.16}

Thus the exact equality inverse, not merely a continuum approximation to it, is coefficientwise nonnegative on the complete outer factor-54 window.

## 5. Exact ordinary saturation

Define the exact outer row peel

\[
\boxed{
 c_X^{\rm out}(n)=c_X(n)\mathbf1_{n\ge K_X}.
}
\tag{L-91112.17}

It is a nonnegative row vector by (L-91112.16). For every `q>=K_X`, the triangularity `beta_(nq)=0` for `n<q` gives

\[
\begin{aligned}
 \sum_n c_X^{\rm out}(n)\beta_{nq}
 &=\sum_{n\ge q}c_X(n)\beta_{nq}\\
 &=w_X(q).
\end{aligned}
\]

Hence

\[
\boxed{
 \sum_n c_X^{\rm out}(n)\beta_{nq}=w_X(q)
 \qquad(q\ge K_X).
}
\tag{L-91112.18}

No finite target-versus-continuum error occurs.

## 6. Exact radix-four saturation, including the terminal annulus

Put

\[
 \Omega_X(q)=w_X(q)-2w_X(4q).
\]

For `q>=K_X`, both ordinary columns in the detail are exact; when `4q>X`, the second column and its target are both identically zero. Therefore

\[
\boxed{
 \sum_n c_X^{\rm out}(n)
 [\beta_{nq}-2\beta_{n,4q}]
 =\Omega_X(q)
 \qquad(q\ge K_X).
}
\tag{L-91112.19}

In particular the tapering terminal annulus `q>X/4` is saturated exactly. No separate terminal-annulus correction is needed.

## 7. The three former errors are one exact inner residual

For `q<K_X`, define

\[
 \mathcal R_{X,K_X}(q)
 =w_X(q)-\sum_n c_X^{\rm out}(n)\beta_{nq}.
\tag{L-91112.20}
\]

Using the complete equality identity,

\[
\boxed{
 \mathcal R_{X,K_X}(q)
 =\sum_{q\le n<K_X}c_X(n)\beta_{nq}.
}
\tag{L-91112.21}

Its radix-four version is

\[
\boxed{
 \mathcal R^{(4)}_{X,K_X}(q)
 =\mathcal R_{X,K_X}(q)
  -2\mathcal R_{X,K_X}(4q),
}
\tag{L-91112.22}
\]

with causal zero extension above `K_X`.

Thus the previous bookkeeping objects

```text
finite target/continuum mismatch;
terminal quotient annulus;
width-three martingale-quantization collar
```

are not three independent debts. When the exact equality rows are used, all three disappear into the single source-complete inner residual (L-91112.21)--(L-91112.22).

The B-spline quantization theorem remains useful for constructing local packet bases, but no quantization is required for the exact outer peel.

## 8. Exact score split

The average-binomial entropy row satisfies

\[
 G_n=\sum_q\Lambda(q)\beta_{nq}.
\]

Therefore the complete equality row has exact score

\[
 \sum_nc_X(n)G_n
 =\sum_q\Lambda(q)w_X(q)
 =P_\Lambda(X).
\tag{L-91112.23}
\]

Splitting at `K_X` gives

\[
\boxed{
 P_\Lambda(X)
 =\sum_{n\ge K_X}c_X(n)G_n
  +\sum_{n<K_X}c_X(n)G_n.
}
\tag{L-91112.24}
\]

Hence the exact outer peel incurs no target, collar, or terminal score error. Every conclusion-producing loss is now concentrated in the transfer of the inner signed row state.

## 9. Positive component-row and parity interface

Define

\[
 h_Y(m)=m^{-1/2}\log(Y/m)\mathbf1_{m\le Y},
 \qquad
 S_Y(n)=\sum_{m\ge n}h_Y(m).
\]

Let

\[
 Q_Y(n)=(n+1)\Delta^2\left[\frac{S_Y(n)}{n-1}\right].
\]

Finite algebra gives the manifestly positive form

\[
\boxed{
\begin{aligned}
 Q_Y(n)={}&
 \frac{n+1}{n-1}[h_Y(n)-h_Y(n+1)]\\
 &+\frac{2(n+1)}{n(n-1)}h_Y(n+1)
 +\frac{2}{n(n-1)}S_Y(n+2)
 \ge0.
\end{aligned}}
\tag{L-91112.25}

The exact equality row decomposes as

\[
\boxed{
 c_X(n)=
 \sum_{k\le X/n}
 \mu(k)k^{-1/2}Q_{X/k}(n).
}
\tag{L-91112.26}

This is the row-level lift of the squarefree parity state in `L-91109`: every parity coordinate is a positive row packet, and all Möbius sign remains in the final even-minus-odd recombination.

The scaling law

\[
 k^{-1/2}Q_{X/k}(n)
\]

also shows that every prime `p>=59` sends the component endpoint from `X` to `X/p<c_0X`, exactly matching the contracted reset scale.

## 10. Proof boundary

Closed exactly, subject to review:

1. infinitesimal positivity of every real endpoint row;
2. exact integral representation of the equality inverse rows;
3. nonnegativity of all exact rows in the factor-54 outer window;
4. exact ordinary saturation above the reset;
5. exact radix-four saturation, including the terminal annulus;
6. replacement of three collar objects by one exact inner residual;
7. exact score splitting with no outer debt;
8. positive component-row decomposition and the parity interface.

Still open:

1. nonnegative realization of the complete inner residual;
2. a coefficient-one transfer of that residual to the contracted `(L,R)` state;
3. bounded score debt for the contracted transfer;
4. RH.
