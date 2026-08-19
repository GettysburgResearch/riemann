# L-98920 — Reciprocal-Julia prefix satisfies an exact positive renewal identity

Claim ID: `L-98920`  
Status: **PROVED EXACT FINITE CONVOLUTION IDENTITY**  
Created: 2026-08-19  
Depends on: `L-97100/L-97101/L-97103`  
RH status: **not assumed**

Let

\[
B_\diamond(s)=\sum_{n\ge1} b_\diamond(n)n^{-s},\qquad
G_\diamond(s)=\sum_{n\ge1} g_\diamond(n)n^{-s},
\]

with `B_diamond G_diamond=1` and `g_diamond(n)>0`. Define

\[
\mathcal B(x)=\sum_{n\le x}\frac{b_\diamond(n)}{\sqrt n},
\qquad
\mathcal G(d)=\frac{g_\diamond(d)}{\sqrt d}>0.
\]

Because square-root normalization is completely multiplicative,

\[
\left(\frac{b_\diamond}{\sqrt{\cdot}}\right)
*
\left(\frac{g_\diamond}{\sqrt{\cdot}}\right)=\delta_1.
\]

Hence finite divisor switching gives, for every real `x>=1`,

\[
\boxed{
\sum_{d\le x}\mathcal G(d)\mathcal B(x/d)=1.
}
\tag{L-98920.1}
\]

Equivalently,

\[
\boxed{
1-\mathcal B(x)
=
\sum_{2\le d\le x}\mathcal G(d)\mathcal B(x/d).
}
\tag{L-98920.2}
\]

The scalar derivative prefix satisfies `M_*(x)=6[1-mathcal B(x)]`, so the desired upper barrier `mathcal B<=1` is already an exact positive renewal of smaller quotient values.

Writing `mathcal B_- = max(-mathcal B,0)`, one obtains the one-sided exceedance bound

\[
\boxed{
(\mathcal B(x)-1)_+
\le
\sum_{2\le d\le x}\mathcal G(d)\,\mathcal B_-(x/d).
}
\tag{L-98920.3}
\]

No absolute value has been placed on the good-sign descendants. This identity is exact and source-faithful.
