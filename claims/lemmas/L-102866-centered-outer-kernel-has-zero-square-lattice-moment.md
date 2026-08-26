# L-102866 — Exact square-lattice moment of the centered outer kernel

Claim ID: `L-102866`  
Status: **CORRECTED EXACT ANALYTIC LEMMA; THE MOMENT IS NONZERO**  
Created: 2026-08-24  
Corrected: 2026-08-24  
Depends on: `L-102732`, `L-102737`, `T-102780`  
RH status: **not assumed**

Let

\[
R_L(y)=\frac{P_{-8}(y)-P_0(y)}{16}
\]

be the one-atom, carrier-centered outer/Lorentz kernel. Equivalently,

\[
R_L=J P_2\bigl[(S_--8)^2-S_-^2\bigr]/16
=JP_2\bigl[(4-S_-)\mathbf1_{[1,\infty)}\bigr].
\tag{L-102866.1}

It is supported in `[1,8]`.

## 1. Exact piecewise derivative

Writing `x=sqrt(y)`, the logarithmic derivative `K_L=D R_L` is

\[
\boxed{
K_L(y)=
\begin{cases}
8-4\sqrt y,&1\le y<2,\\
-8(1+\sqrt2)+4\sqrt2\sqrt y,&2\le y<4,\\
8\sqrt2-2\sqrt y,&4\le y<8,\\
0,&\text{otherwise}.
\end{cases}}
\tag{L-102866.2}

The endpoint values of `R_L` vanish at `1` and `8`.

## 2. Exact continuous square-lattice moment

Direct integration of the piecewise primitive gives

\[
\boxed{
M_0:=\int_1^8R_L(y)\frac{dy}{y}
=8(1-\sqrt2)(\log2)^2<0.
}
\tag{L-102866.3}

The historical zero-moment display in the first version of this file was
false. The factor `(1-2^{-s})^2` is exactly balanced by the two scale poles in
the underlying mother multiplier; after `J` and the outer differential
functional a nonzero value remains at `s=0`.

## 3. Uniform lattice asymptotic

Put

\[
\mathscr L_R(Z)
=\sum_{m\ge1}\frac1mR_L(Z/m^2).
\]

For

\[
g_Z(x)=x^{-1}R_L(Z/x^2),
\]

the change of variables `y=Z/x^2` gives

\[
\int_0^\infty g_Z(x)\,dx=\frac{M_0}{2}.
\]

Writing `x=sqrt(Z)t` shows that the variation of `g_Z` is `O_R(Z^(-1/2))`.
Therefore

\[
\boxed{
\mathscr L_R(Z)
=4(1-\sqrt2)(\log2)^2+O_R(Z^{-1/2}).
}
\tag{L-102866.4}

## 4. Favorable unrestricted Type-I main

In the unrestricted model of `L-102867`, the Type-I term is

\[
-\sum_{d,e\le U}\frac{\mu(d)\mu(e)}{de}
\mathscr L_R(Y/(de)^2).
\]

Using (L-102866.4), its main term is

\[
\boxed{
4(\sqrt2-1)(\log2)^2
\left(\sum_{d\le U}\frac{\mu(d)}d\right)^2\ge0,
}
\tag{L-102866.5}

and its remainder is `O_R(U^2/sqrt(Y))`.

Thus the unrestricted complete lattice has a favorable square main rather than
zero main. In the literal largest-two source the `q`-smooth cutoff changes this
lattice and must be retained as in `R-102866` and `L-102869`.

```text
exact moment                         VERIFIED / NONZERO
unrestricted Type-I main             NONNEGATIVE SQUARE
stopped largest-two Type-I sign       NOT ESTABLISHED HERE
Riemann Hypothesis                    UNPROVED
```
