# R-102868 — The unrestricted Type-I term is not `O(Y^{-1/6})`

Claim ID: `R-102868`  
Status: **PROVED EXACT MAGNITUDE CORRECTION / FAVORABLE-SIGN FIREWALL**  
Created: 2026-08-24  
Depends on: corrected `L-102866`; `L-102867`; `L-102869`  
RH status: **unproved**

Let

\[
\mathscr L_\infty(Z)
=\sum_{m\ge1}{1\over m}R_L(Z/m^2).
\]

Corrected `L-102866` proves

\[
\mathscr L_\infty(Z)
=c_0+O_R(Z^{-1/2}),
\qquad
c_0=4(1-\sqrt2)(\log2)^2<0.
\tag{R-102868.1}
\]

For the stopped prefix

\[
M_{U,q}:=
\sum_{\substack{d\le U\\P^+(d)<q}}{\mu(d)\over d},
\]

the unrestricted Type-I coordinate is

\[
\mathcal T_{p,q}^{\rm full}(Y)
=-\sum_{\substack{d,e\le U\\P^+(de)<q}}
{\mu(d)\mu(e)\over de}
\mathscr L_\infty\!\left({Y\over d^2e^2}\right).
\]

Substitution of (R-102868.1) gives

\[
\boxed{
\mathcal T_{p,q}^{\rm full}(Y)
=c_+M_{U,q}^2
+O_R\!\left({U^2\over\sqrt Y}\right),
\qquad
c_+=4(\sqrt2-1)(\log2)^2>0.
}
\tag{R-102868.2}
\]

Indeed the error attached to one pair `(d,e)` is

\[
{1\over de}
O_R\!\left({de\over\sqrt Y}\right)
=O_R(Y^{-1/2}),
\]

and there are at most `U^2` pairs.

With the Vaughan choice

\[
U=\lfloor Y^{1/6}\rfloor,
\]

one therefore has

\[
\boxed{
(\mathcal T_{p,q}^{\rm full}(Y))_-
\ll_R Y^{-1/6}.
}
\tag{R-102868.3}
\]

The whole Type-I term need not be `O(Y^{-1/6})`; it contains the favorable
nonnegative square in (R-102868.2).  Accordingly:

```text
L-102867 display claiming T_unres=O(Y^-1/6)        FALSE AS A SIZE CLAIM;
L-102869 display claiming T_full=O(Y^-1/6)         FALSE AS A SIZE CLAIM;
negative part of T_full                             O(Y^-1/6), VERIFIED;
favorable square main                               RETAINED, NOT SPENT TWICE.
```

This correction strengthens the one-sided conclusion while preventing a false
absolute estimate from entering later source ledgers.