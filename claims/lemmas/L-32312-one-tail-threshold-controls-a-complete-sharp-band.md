# L-32312 — One tail threshold controls a complete SHARP quotient band

Claim ID: `L-32312`  
Title: After local negativity is fixed, every same-cell row and every quotient transition in an entire finite SHARP band are controlled by one scalar bottom-tail threshold  
Status: **PROPOSED COMPLETE EXACT REDUCTION — NO ALL-DEPTH SIGN CLAIM**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32303`; transition identity of `L-32307`; fixed-cell notation of `L-32309/L-32310`  
Scope: finite-band reduction; the required tail inequality remains arithmetic and becomes RH-bearing at unbounded depth

## 1. Setup

Retain the square-root hinge multiples-Möbius state

\[
u_T(m)=\frac{A_K}{\sqrt m}-\frac{M_K}{\sqrt T},
\qquad
K=\left\lfloor\frac Tm\right\rfloor,
\]

with

\[
A_K=\sum_{k\le K}\frac{\mu(k)}{\sqrt k},
\qquad
M_K=\sum_{k\le K}\mu(k),
\]

and the tail

\[
S_T(j)=\sum_{m=j}^{T}u_T(m).
\]

The exact inverse identity is

\[
\boxed{
 j c_T(j)
 =(j+2)u_T(j)-j u_T(j+1)
 +\frac{2S_T(j)}{j-1}.
}
\tag{L-32312.1}
\]

Fix an even integer depth `R>=4` and consider the band

\[
\frac TR<j\le\frac{2T}{R}.
\tag{L-32312.2}
\]

Its quotient indices are exactly

\[
\frac R2\le K<R.
\]

## 2. Fixed local quantities

For every quotient index put

\[
\boxed{
 L_K=\frac52A_K\sqrt{K+1}-2M_K.
}
\tag{L-32312.3}
\]

Assume throughout the band that

\[
\boxed{
A_K<0,
\qquad
A_K\sqrt K-M_K<0.
}
\tag{L-32312.4}
\]

The second inequality implies that the complete local state is negative on the whole quotient cell:

\[
 u_T(m)<0.
\tag{L-32312.5}
\]

Indeed `sqrt(T/m)>=sqrt(K)` and multiplication by `A_K<0` reverses the inequality.

For a same-cell pair, the standard bound

\[
\frac{j+2}{\sqrt j}-\frac{j}{\sqrt{j+1}}
<\frac5{2\sqrt j}
\]

gives

\[
\boxed{
\sqrt T[(j+2)u_T(j)-j u_T(j+1)]>L_K.
}
\tag{L-32312.6}
\]

At a transition from cell `K` to `K-1`, `L-32307` gives the exact additional correction

\[
\mu(K)\left[
\frac1{\sqrt T}-\frac1{\sqrt{K(j+1)}}
\right].
\tag{L-32312.7}
\]

The bracket is positive and its contribution to the scaled local term is strictly less than `1/2` in absolute value. Thus only `mu(K)=+1` is adverse.

## 3. The canonical threshold

Define

\[
\boxed{
\vartheta_R
=
\max_{R/2\le K<R}
\frac{-L_K+\frac12\mathbf1_{\{\mu(K)=1\}}}{2K}.
}
\tag{L-32312.8}
\]

This is a completely finite arithmetic number depending only on the quotient cells in the new band.

Let

\[
J_R=\left\lfloor\frac TR\right\rfloor+1.
\]

Suppose that at the endpoint under consideration

\[
\boxed{
S_T(J_R)>\vartheta_R\sqrt T.
}
\tag{L-32312.9}
\]

Because every local state in the new band is negative, for every `j` satisfying (L-32312.2),

\[
S_T(j)\ge S_T(J_R)>artheta_R\sqrt T.
\tag{L-32312.10}
\]

Also `j-1<T/K`, so

\[
\boxed{
\sqrt T\frac{2S_T(j)}{j-1}>2\vartheta_RK.
}
\tag{L-32312.11}
\]

## 4. Same-cell rows

If `j,j+1` lie in the same quotient cell `K`, (L-32312.1), (L-32312.6), and (L-32312.11) give

\[
\sqrt T\,j c_T(j)
>L_K+2\vartheta_RK.
\]

By definition of `vartheta_R`,

\[
2\vartheta_RK\ge-L_K,
\]

with strictness supplied by the strict tail gate. Hence

\[
\boxed{c_T(j)>0}
\tag{L-32312.12}
\]

for every same-cell row in the band.

## 5. Quotient transitions

If `j,j+1` cross from cell `K` to `K-1`, then:

- `mu(K)<=0` makes (L-32312.7) favorable, so the same-cell argument already proves positivity;
- if `mu(K)=1`, the adverse scaled loss is `<1/2`.

Therefore

\[
\sqrt T\,j c_T(j)
>L_K+2\vartheta_RK-\frac12.
\]

Definition (L-32312.8) gives

\[
2\vartheta_RK\ge-L_K+\frac12,
\]

again with strictness from (L-32312.9). Thus

\[
\boxed{c_T(j)>0}
\tag{L-32312.13}
\]

at every quotient transition as well.

## 6. Band theorem

Combining Sections 4--5:

> **One-tail band criterion.**  If the fixed cells `R/2,...,R-1` satisfy (L-32312.4) and the single bottom-tail inequality (L-32312.9), then
> \[
> \boxed{
> c_T(j)>0
> \qquad(T/R<j\le2T/R).
> }
> \tag{L-32312.14}
> \]

Thus a band containing `R/2` quotient cells requires only:

```text
fixed local negativity;
one finite number vartheta_R;
one scalar endpoint tail gate.
```

No coefficient-by-coefficient endpoint replay is mathematically necessary.

The outer `127/128` and `255/256` theorems are concrete instances of this criterion. In the latter case `R=256` and the directed proof establishes the stronger convenient tail threshold `1/16`.

## 7. Continuum meaning of the bottom tail

The continuum limit of the bottom tail is explicit. With

\[
B_K=\sum_{k\le K}\frac{\mu(k)}k,
\]

one has

\[
\boxed{
\lim_{T\to\infty}
\frac{S_T(\lfloor T/R\rfloor+1)}{\sqrt T}
=
B_{R-1}-\frac{2A_{R-1}}{\sqrt R}+\frac{M_{R-1}}R.
}
\tag{L-32312.15}
\]

This is the quotient-cell sum in `T-32302` evaluated at the lower edge of the band.

Likewise, the complete same-cell scaled margin at a fixed ratio `x=T/j` is

\[
\frac{\sqrt x}{2}\Psi(x),
\qquad
\Psi(x)=4\sqrt x\sum_{n\le x}\frac{\mu(n)}n
-3\sum_{n\le x}\frac{\mu(n)}{\sqrt n}.
\tag{L-32312.16}
\]

Therefore the sequence of finite criteria (L-32312.9) approaches the zero-safe reciprocal-zeta scalar of `T-32302` as the depth grows. The reduction does not turn arbitrary-depth positivity into a soft estimate.

## 8. Proof boundary

Closed exactly:

1. reduction of a complete finite quotient band to one bottom-tail threshold;
2. automatic treatment of every same-cell row;
3. automatic treatment of every quotient transition, including positive-Möbius transitions;
4. explicit canonical threshold `vartheta_R`;
5. identification of the limiting tail and its relation to the continuum `Psi` scalar.

Open:

1. a uniform all-depth lower bound `S_T(J_R)>vartheta_R sqrt(T)`;
2. eventual one-sidedness of `Psi`;
3. full SHARP;
4. RH.
