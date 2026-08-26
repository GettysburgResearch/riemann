# L-102880 — The logarithmic derivative outer detector has zero square-lattice moment

Claim ID: `L-102880`  
Status: **PROVED EXACT DETECTOR AND TYPE-I THEOREM**  
Created: 2026-08-24  
Depends on: corrected `L-102866`; `T-102780--T-102790`; PR #715 fixed Mellin consumer  
RH status: **unproved**

Let `R_L` be the centered outer/Lorentz kernel of `L-102866` and put

\[
\boxed{K_L=DR_L,\qquad D=y{d\over dy}.}
\tag{L-102880.1}
\]

The kernel is supported in `[1,8]` and, writing `x=sqrt(y)`, is

\[
K_L(y)=
\begin{cases}
8-4\sqrt y,&1\le y<2,\\
-8(1+\sqrt2)+4\sqrt2\sqrt y,&2\le y<4,\\
8\sqrt2-2\sqrt y,&4\le y<8,\\
0,&\text{otherwise}.
\end{cases}
\tag{L-102880.2}
\]

## 1. Exact zero lattice moment

Because `R_L(1)=R_L(8)=0`,

\[
\boxed{
\int_1^8K_L(y){dy\over y}=0.
}
\tag{L-102880.3}
\]

For

\[
\mathscr L_K(Z)=\sum_{m\ge1}{1\over m}K_L(Z/m^2),
\]

put `g_Z(x)=x^{-1}K_L(Z/x^2)`.  The substitution `y=Z/x^2` gives

\[
\int_0^\infty g_Z(x)dx={1\over2}\int_1^8K_L(y){dy\over y}=0.
\]

Writing `x=sqrt(Z)t` shows that `Var(g_Z)=O_K(Z^(-1/2))`.  The one-dimensional Euler summation inequality therefore yields

\[
\boxed{
\mathscr L_K(Z)=O_K(Z^{-1/2}).
}
\tag{L-102880.4}
\]

This is an absolute estimate; unlike the original `R_L` lattice it has no nonzero square main.

## 2. Unrestricted Type-I is power-small in absolute value

With `U=floor(Y^(1/6))`, define

\[
\mathcal T_K^{\rm unres}(Y)
=-\sum_{d,e\le U}{\mu(d)\mu(e)\over de}
 \mathscr L_K\!\left({Y\over d^2e^2}\right).
\]

Equation (L-102880.4) gives

\[
\left|\mathcal T_K^{\rm unres}(Y)\right|
\ll_K
\sum_{d,e\le U}{1\over de}{de\over\sqrt Y}
\ll {U^2\over\sqrt Y}.
\]

Hence

\[
\boxed{
\mathcal T_K^{\rm unres}(Y)=O_K(Y^{-1/6}).
}
\tag{L-102880.5}
\]

This is the correct zero-moment Type-I statement.  It does not remove the stopped `P^+(m)<q` boundary; that source is retained in `L-102881`.

## 3. Fixed Mellin detector

For any finite source `sigma`, write

\[
H_R(X)=\sum_n{\sigma(n)\over\sqrt n}R_L(X/n),
\qquad
H_K(X)=\sum_n{\sigma(n)\over\sqrt n}K_L(X/n).
\]

Then, distributionally and coefficientwise,

\[
\boxed{H_K=DH_R.}
\tag{L-102880.6}
\]

The Mellin multipliers satisfy

\[
\boxed{\widehat K_L(s)=s\widehat R_L(s).}
\tag{L-102880.7}
\]

The additional zero is only `s=0`.  Thus every hypothetical reciprocal-zeta pole with `Re(s)>0` retained by the fixed outer detector is also retained by `K_L`.

Since `R_L(1)=0`,

\[
H_R(X)=\int_1^XH_K(t){dt\over t}.
\]

Consequently

\[
(H_R(X))_-
\le\int_1^X(H_K(t))_-{dt\over t},
\]

and Fubini gives

\[
\boxed{
\int_1^Y(H_R(X))_-{dX\over X}
\le
(\log Y)\int_1^Y(H_K(t))_-{dt\over t}.
}
\tag{L-102880.8}
\]

Therefore subpower logarithmic negative mass for the derivative detector implies `OER102780`, and hence RH through the already-fixed consumer.

```text
zero square-lattice moment                 PROVED EXACT
unrestricted Type-I absolute decay         PROVED
fixed zero-safe derivative detector        PROVED EXACT
stopped smooth boundary                    OPEN
balanced stopped Type-II                   OPEN
Riemann Hypothesis                         UNPROVED
```
