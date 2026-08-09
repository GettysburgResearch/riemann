# L-34408 — The correctly typed odd relative second current is cofinally positive

Claim ID: `L-34408`  
Title: The odd relative second current is a sum of two ordinary Selberg-coefficient prefix defects; a two-term unconditional Selberg asymptotic makes that boundary positive on every fixed balanced cone  
Status: **PROPOSED COMPLETE EXACT IDENTITY + UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: `R-34402`; PR #349 `R-34401`; PR #346 `L-34404`; classical zero-free region / quantitative PNT  
Scope: aligned integer rows on fixed balanced cones; no upper recurrence and no RH conclusion

## 1. Correct boundary coordinate

Retain

\[
C_{\rm odd}
=\Lambda_{\rm odd}\log
 +\Lambda_{\rm odd}*\Lambda_{\rm odd}
\ge0
\]

and define its ordinary coefficient prefix

\[
\boxed{
H_C(x)=\sum_{m\le x}C_{\rm odd}(m).
}
\tag{L-34408.1}
\]

For a row `e=(n,j)`, with `k=n-j`, put

\[
\boxed{
\mathcal D_C(e)
=H_C(n)-H_C(j)-H_C(k).
}
\tag{L-34408.2}
\]

`R-34402` proves exactly that the source second current

\[
t_{\rm odd}=b_{\rm odd}*C_{\rm odd}
\]

satisfies

\[
\boxed{
T_{\rm odd}(4e)-T_{\rm odd}(e)
=\mathcal D_C(4e)+\mathcal D_C(2e).
}
\tag{L-34408.3}
\]

No sign has yet been used.  Equation (L-34408.3) is an exact finite identity.

## 2. Dirichlet series of the odd Selberg coefficient

Let

\[
A_{\rm odd}(s)
=\prod_{p\text{ odd}}(1-p^{-s})^{-1}
=(1-2^{-s})\zeta(s).
\]

Its logarithmic derivative has coefficients `Lambda_odd`.  Therefore

\[
\boxed{
\sum_{n\ge1}\frac{C_{\rm odd}(n)}{n^s}
=\frac{A_{\rm odd}''(s)}{A_{\rm odd}(s)}.
}
\tag{L-34408.4}
\]

Indeed, if `L_odd=-A_odd'/A_odd`, then

\[
\frac{A_{\rm odd}''}{A_{\rm odd}}
=L_{\rm odd}^2-L_{\rm odd}',
\]

whose coefficients are exactly

\[
\Lambda_{\rm odd}*\Lambda_{\rm odd}
+\Lambda_{\rm odd}\log.
\]

All coefficients are nonnegative.

## 3. Two-term unconditional asymptotic

Put `t=s-1`.  The Laurent expansions

\[
\zeta(s)=\frac1t+\gamma+O(t)
\]

and

\[
\frac{d}{ds}\log(1-2^{-s})\bigg|_{s=1}
=\log2
\]

give

\[
\boxed{
\frac{A_{\rm odd}''(s)}{A_{\rm odd}(s)}
=\frac2{(s-1)^2}
 -\frac{2(\gamma+\log2)}{s-1}
 +O(1)
}
\tag{L-34408.5}
\]

near `s=1`.

The classical de la Vallee Poussin zero-free region gives the usual effective prime number theorem and permits the standard two-term Perron/Ikehara--Delange extraction for (L-34408.4).  Since the coefficients in (L-34408.4) are nonnegative, one obtains

\[
\boxed{
H_C(x)
=2x\log x
 -2(1+\gamma+\log2)x
 +o(x).
}
\tag{L-34408.6}
\]

For completeness, the same formula can be recovered by starting from the ordinary Selberg coefficient

\[
C=\Lambda\log+\Lambda*\Lambda
\]

and writing

\[
\Lambda_{\rm odd}
=\Lambda-(\log2)\sum_{a\ge1}\delta_{2^a}.
\]

The pure dyadic terms have total prefix `o(x)`, while

\[
2(\log2)
\sum_{a\ge1}\psi(x/2^a)
=2(\log2)x+o(x)
\]

by the quantitative PNT and geometric tail control.  This changes only the linear coefficient of the ordinary two-term Selberg asymptotic and gives (L-34408.6).

No RH input occurs.

## 4. Balanced additive defects

Fix

\[
0<\eta<\frac12,
\qquad
\eta n\le j\le(1-\eta)n,
\]

and write

\[
\alpha=\frac jn,
\qquad
\beta=1-\alpha,
\]

\[
\mathcal H(\alpha)
=-\alpha\log\alpha-\beta\log\beta,
\qquad
h_\eta=\min_{\eta\le\alpha\le1-\eta}\mathcal H(\alpha)>0.
\]

Insert (L-34408.6) into (L-34408.2).  The linear term cancels because `n=j+k`, and the `x log x` terms give

\[
\boxed{
\mathcal D_C(n,j)
=2n\mathcal H(\alpha)+o_\eta(n).
}
\tag{L-34408.7}
\]

The error is uniform on the fixed balanced cone: `j,k>=eta n`, so the three individual `o(x)` errors are all `o_eta(n)`.

Consequently, outside one finite base depending only on `eta`,

\[
\boxed{
\mathcal D_C(n,j)\ge h_\eta n>0.
}
\tag{L-34408.8}
\]

Applying (L-34408.7) at scales two and four gives the sharper combined asymptotic

\[
\boxed{
\mathcal D_C(4e)+\mathcal D_C(2e)
=12n\mathcal H(\alpha)+o_\eta(n).
}
\tag{L-34408.9}
\]

Hence cofinally

\[
\boxed{
T_{\rm odd}(4e)-T_{\rm odd}(e)
\ge6h_\eta n>0.
}
\tag{L-34408.10}
\]

The factor six is only a safe half of the main coefficient twelve.

## 5. Correct repaired relative curvature

PR #349 correctly proves the relative bare charge

\[
Y_{\rm odd}(4e)-Y_{\rm odd}(e)=-2.
\tag{L-34408.11}
\]

Let

\[
I_{\rm odd}(e)
=Q_{\rm odd}(4e)-Q_{\rm odd}(e).
\]

The source-complete relative vector curvature is therefore

\[
\boxed{
\begin{aligned}
\mathfrak C(W_e^{\rm odd})
={}&\Delta_4R_{\rm odd}(e)
 +|I_{\rm odd}(e)|^2\\
&+2\mathcal D_C(4e)
 +2\mathcal D_C(2e).
\end{aligned}}
\tag{L-34408.12}
\]

This replaces the false exact formula containing

\[
2S_{\rm odd}(4e)+2S_{\rm odd}(2e).
\]

PR #346 `L-34404` proves on the same fixed balanced cone, cofinally,

\[
\Delta_4R_{\rm odd}(e)
\ge12h_\eta n\log n.
\]

Combining with (L-34408.10),

\[
\boxed{
\mathfrak C(W_e^{\rm odd})
\ge |I_{\rm odd}(e)|^2
 +12h_\eta n\log n
 +12h_\eta n
>0
}
\tag{L-34408.13}
\]

outside one finite base.

Thus the odd-relative route remains locally positive after the second source-order correction, but the extra positive term is a **cofinal ordinary-prefix boundary**, not an exact all-row Selberg carry.

## 6. What has and has not survived

Survives exactly:

```text
odd Jordan deformation;
relative bare charge = -2;
relative current innovation I_odd;
critical reserve increment Delta_4 R_odd;
exact source-complete vector curvature pattern.
```

Repaired:

```text
relative second current
 = D_C(4e)+D_C(2e),
not S_odd(4e)+S_odd(2e).
```

Survives cofinally and unconditionally:

```text
relative second current >0 on every fixed balanced cone;
corrected relative curvature contains I_odd^2 with coefficient one;
corrected relative curvature has an n log n deterministic moat.
```

Still absent:

```text
an upper/dissipative law for the corrected curvature;
a coefficient-one global recurrence;
RH.
```

## 7. Proof boundary

Closed here, subject to review:

1. the exact corrected relative second-current identity;
2. the Dirichlet series `A_odd''/A_odd`;
3. its two-term unconditional summatory asymptotic;
4. uniform cofinal positivity of the ordinary-prefix defect;
5. the correctly typed positive relative curvature.

Open:

1. all-row positivity of `D_C`;
2. reflected dissipative placement of (L-34408.12);
3. an upper recurrence for `I_odd`;
4. RH.
