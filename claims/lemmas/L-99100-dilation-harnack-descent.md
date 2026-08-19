# L-99100 — A single factor-67 dilation inequality closes the primitive-prefix route

Claim ID: `L-99100`  
Status: **PROVED EXACT REDUCTION**  
Depends on: `L-99000`, `T-99001`  
RH status: **unproved**

Let

\[
 C(t)=\sum_{n\le t}\frac{a(n)}{\sqrt n},
 \qquad C(t)=0\quad(0<t<1),
\]

be the primitive prefix of T-99000.  For any real `P>1`, define

\[
 (T_Pf)(t)=f(t/P),
 \qquad
 \Delta_P C(t)=\bigl(I-P^{-1/2}T_P\bigr)C(t).
\]

Then the following descent statement is exact.

## Dilation-Harnack descent

Assume that `C(t)>=0` for `1<=t<T` and

\[
 \Delta_P C(t)\ge0\qquad(t\ge T).
\]

For any `t>=T`, choose the least `k>=1` for which `t/P^k<T`.  Iteration gives

\[
 C(t)\ge P^{-1/2}C(t/P)
      \ge\cdots\ge P^{-k/2}C(t/P^k)\ge0.
\]

Hence `C(t)>=0` for every real `t>=1`.  By T-99001 this implies C4MBI67 and
then RH.

For the annular scalar

\[
 \mathcal A_X=\int_{X/4}^{X}C(t)\,\frac{dt}{t},
\]

one also has the exact commuting identity

\[
 \boxed{
 \mathcal A_X-P^{-1/2}\mathcal A_{X/P}
 =\int_{X/4}^{X}\Delta_PC(t)\,\frac{dt}{t}.}
\]

Thus the pointwise dilation inequality supplies the same contraction directly
at the C4MBI67 window.

## The factor-67 specialization

Put

\[
 r=67^{-1/2}<\frac18,
 \qquad
 H_{67}(t)=C(t)-rC(t/67).
\]

Combining T-99000 with T-99100, the sole conclusion-producing tail statement
in this packet is now

\[
 \boxed{H_{67}(t)\ge0\quad(t\ge2{,}000{,}000{,}001).}
\]

If that tail inequality is proved, repeated division by `67` lands inside the
certified finite range and closes the entire primitive-prefix route.

This lemma does **not** prove the tail inequality.
