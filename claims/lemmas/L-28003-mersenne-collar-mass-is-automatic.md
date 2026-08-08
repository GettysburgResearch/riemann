# L-28003 — Mersenne collar mass is automatic under exact nonnegative saturation

Claim ID: `L-28003`  
Title: Every exact nonnegative carry saturation flow automatically has logarithmic total mass on the Mersenne extreme edges  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Depends on: `T-28001` definitions only  
Scope: removes the separate collar-mass hypothesis from `MCF`; it does not construct the restricted-support saturation flow

## 1. Exact diagonal carry load

Let

\[
n=2^r-1\ge3.
\]

For either extreme split

\[
j=1
\qquad\text{or}\qquad
j=n-1,
\]

the carry in the diagonal column `q=n` is

\[
\chi_{n,n}(j)
=\left\lfloor{n\over n}\right\rfloor
-\left\lfloor{j\over n}\right\rfloor
-\left\lfloor{n-j\over n}\right\rfloor
=1.
\tag{L-28003.1}

Assume only exact saturation and nonnegativity:

\[
\sum_{m=n}^{X}\sum_{k=1}^{m-1}
 d_X(m,k)\chi_{m,n}(k)
=w_X(n),
\qquad d_X(m,k)\ge0.
\tag{L-28003.2}

Every term on the left is nonnegative. Therefore the two declared Mersenne extreme edges satisfy

\[
\boxed{
 d_X(n,1)+d_X(n,n-1)
 \le w_X(n).
}
\tag{L-28003.3}

No support information on any other row is needed.

## 2. Logarithmic total collar bound

For

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

put

\[
\mathfrak M_X
=\sum_{2^r-1\le X}
[d_X(2^r-1,1)+d_X(2^r-1,2^r-2)].
\]

Equation (L-28003.3) gives

\[
\mathfrak M_X
\le
\sum_{2^r-1\le X}
{\log(X/(2^r-1))\over\sqrt{2^r-1}}.
\tag{L-28003.4}

For `r>=2`,

\[
2^r-1\ge2^{r-1},
\]

so

\[
{1\over\sqrt{2^r-1}}
\le2^{-(r-1)/2}.
\]

Also `log(X/(2^r-1))<=log X`. Extending the geometric sum to infinity,

\[
\begin{aligned}
\mathfrak M_X
&\le
\log X\sum_{r=2}^{\infty}2^{-(r-1)/2}\\
&=(1+\sqrt2)\log X.
\end{aligned}
\]

Thus

\[
\boxed{
\mathfrak M_X
\le(1+\sqrt2)\log X.
}
\tag{L-28003.5}

In particular, for every `epsilon>0`,

\[
\mathfrak M_X=O_\epsilon(X^\epsilon).
\]

## 3. Corrected sole hinge

The subpower collar condition `(T-28001.7)` is therefore redundant. The Mersenne-collar route needs only the following finite theorem:

> **Restricted Mersenne Saturation (`RMS`).** Construct an exact nonnegative carry saturation flow satisfying the support rules:
>
> - binary central-window splits on non-Mersenne rows;
> - extreme splits on Mersenne rows.

Any such flow automatically satisfies the required collar bound by (L-28003.5). Hence the existing eta-source pairing and Landau consumer give

\[
\boxed{
\mathrm{RMS}\Longrightarrow\mathrm{RH}.
}
\tag{L-28003.6}

The proof of `RMS` remains open.

## 4. Review consequence

A proposed construction must no longer spend effort estimating Mersenne mass after exact saturation. Review should focus exclusively on:

1. nonnegativity of every emitted flow coefficient;
2. exact equality in every carry column;
3. compliance with the binary-window/extreme-edge support grammar.

The diagonal capacity automatically controls the entire exceptional collar.

## 5. Proof boundary

Closed exactly:

- diagonal load of each extreme Mersenne edge;
- pointwise capacity bound (L-28003.3);
- global logarithmic collar estimate (L-28003.5);
- reduction from `MCF` to restricted exact saturation.

Open:

- construction of the restricted nonnegative saturation flow;
- RH.
