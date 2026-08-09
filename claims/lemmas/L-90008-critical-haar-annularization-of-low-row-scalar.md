# L-90008 — Critical-Haar annularization of the two-low-row RH scalar

Claim ID: `L-90008` (provisional range 90001+; allocate at registry before integration)  
Status: **PROPOSED COMPLETE EXACT STRUCTURAL LEMMA — independent review required**  
Authoring agent: `gpt56-sol`  
Date: 2026-08-09  
Depends on: the low-row source identity of `T-32403`; elementary Dirichlet convolution.  
Scope: exact localization/renewal of the low-row reciprocal-zeta scalar; no sign theorem and no RH claim.

## 1. The low-row source

Let
\[
\boxed{
\omega=(\varepsilon-\delta_2)*(2\varepsilon-\delta_2)*\mu.
}
\tag{L-90008.1}
\]
Its Dirichlet series is
\[
\Omega(s)
=\frac{(1-2^{-s})(2-2^{-s})}{\zeta(s)}.
\tag{L-90008.2}
\]
For real `T>=1`, define the **complete hinge**
\[
\boxed{
W(T)=\sum_{n\le T}\omega(n)
\left(n^{-1/2}-T^{-1/2}\right),
}
\tag{L-90008.3}
\]
with `W(T)=0` for `0<T<1`.

Since `omega(1)=2`, the deleted-unit scalar of `T-32403` is
\[
D(T)=W(T)-2(1-T^{-1/2}).
\tag{L-90008.4}
\]
The exact row formulas of `T-32403` therefore give
\[
\boxed{
5c_T(2)+3c_T(3)=-3D(T).
}
\tag{L-90008.5}
\]
Thus the cofinal sign `D(T)<=0` is already RH-bearing.  The present lemma does
not prove that sign.

## 2. Insert the critical Haar factor

Put
\[
\boxed{
\eta=(\varepsilon-\sqrt2\,\delta_2)*\omega
}
\tag{L-90008.6}
\]
and define
\[
U(T)=\sum_{n\le T}\eta(n)
\left(n^{-1/2}-T^{-1/2}\right).
\tag{L-90008.7}
\]
Then exactly
\[
\boxed{U(T)=W(T)-W(T/2).}
\tag{L-90008.8}
\]

### Proof

The delayed term in (L-90008.6) contributes
\[
\begin{aligned}
&\sqrt2\sum_{2m\le T}\omega(m)
\left((2m)^{-1/2}-T^{-1/2}\right)\\
&\qquad=
\sum_{m\le T/2}\omega(m)
\left(m^{-1/2}-(T/2)^{-1/2}\right)
=W(T/2).
\end{aligned}
\]
Subtracting from `W(T)` proves (L-90008.8).  The amplitude `sqrt(2)` is forced
by the critical `n^(-1/2)` normalization.

## 3. Complete 2-adic fibers cancel exactly

At the prime two, the local polynomial of `omega` is
\[
(1-x)^2(2-x)=2-5x+4x^2-x^3.
\]
After the critical Haar factor,
\[
\boxed{
C(x)
=(1-x)^2(2-x)(1-\sqrt2 x).
}
\tag{L-90008.9}
\]
Write
\[
C(x)=\sum_{a=0}^4 c_ax^a.
\]
Explicitly,
\[
\boxed{
(c_0,c_1,c_2,c_3,c_4)
=
(2,
-5-2\sqrt2,
4+5\sqrt2,
-1-4\sqrt2,
\sqrt2).
}
\tag{L-90008.10}
\]
For every odd integer `m`,
\[
\eta(2^am)=\mu(m)c_a
\qquad(0\le a\le4),
\tag{L-90008.11}
\]
and the value is zero for `a>=5`; when `mu(m)=0`, the whole fiber vanishes.

The polynomial has the two exact critical zeros
\[
\boxed{C(1)=0,
\qquad C(2^{-1/2})=0.}
\tag{L-90008.12}
\]
Consequently, if `16m<=T`, the complete fiber contribution to (L-90008.7) is
\[
\begin{aligned}
&\mu(m)\sum_{a=0}^4c_a
\left((2^am)^{-1/2}-T^{-1/2}\right)\\
&\quad=
\mu(m)m^{-1/2}C(2^{-1/2})
-\mu(m)T^{-1/2}C(1)
=0.
\end{aligned}
\tag{L-90008.13}
\]
Thus **every complete two-adic fiber below `T/16` disappears identically**.

## 4. Exact factor-16 annular formula

Put
\[
r=T/m.
\]
For `1<=r<16`, let
\[
K=\lfloor\log_2r\rfloor
\]
and define
\[
w(r)=\sum_{a=0}^{K}c_a
\left(2^{-a/2}-r^{-1/2}\right).
\tag{L-90008.14}
\]
Then (L-90008.13) gives the exact finite localization
\[
\boxed{
U(T)
=\sum_{\substack{T/16<m\le T\\m\ {m odd}}}
\frac{\mu(m)}{\sqrt m}\,w(T/m).
}
\tag{L-90008.15}
\]
Only odd squarefree cores contribute automatically through `mu(m)`.

The weight is completely explicit:
\[
\boxed{
w(r)=
\begin{cases}
2-2r^{-1/2},&1\le r<2,\\[3pt]
-\dfrac{5\sqrt2}{2}+(3+2\sqrt2)r^{-1/2},&2\le r<4,\\[6pt]
2-(1+3\sqrt2)r^{-1/2},&4\le r<8,\\[6pt]
-\dfrac{\sqrt2}{4}+\sqrt2\,r^{-1/2},&8\le r<16,\\[6pt]
0,&r\ge16.
\end{cases}}
\tag{L-90008.16}
\]
At `r=2,4,8,16`, the adjacent formulas agree because the newly entering tap
has hinge value zero.  Thus `w` is continuous on `[1,infinity)`.

This is not a one-sign kernel: the middle two bands have internal sign changes.
The theorem is a localization result, not a disguised positivity claim.

## 5. Exact finite dyadic renewal

Equation (L-90008.8) rearranges to
\[
W(T)=U(T)+W(T/2).
\]
Iterating until the endpoint drops below one gives the finite identity
\[
\boxed{
W(T)=\sum_{j=0}^{\lfloor\log_2T\rfloor}U(T/2^j).
}
\tag{L-90008.17}
\]
Every summand is a factor-16 annulus by (L-90008.15).  Hence the global low-row
scalar is reconstructed from a fixed-width critical-Haar annular bank; no
unbounded two-adic fiber remains inside an individual innovation.

For a fixed odd core `m`, only `O(1)` neighboring dyadic scales in
(L-90008.17) can see it, because each annulus has multiplicative width sixteen.
This is an exact finite-overlap property, not an asymptotic truncation.

## 6. Mellin audit: no off-line zero is lost

For `Re z` initially large, one hinge has transform
\[
\int_n^\infty
\left(n^{-1/2}-T^{-1/2}\right)T^{-z-1}dT
=
\frac{n^{-z-1/2}}{2z(z+1/2)}.
\]
Therefore
\[
\boxed{
\int_1^\infty W(T)T^{-z-1}dT
=
\frac{(1-2^{-s})(2-2^{-s})}
{2z(z+1/2)\zeta(s)},
\qquad s=z+1/2.
}
\tag{L-90008.18}
\]
Using (L-90008.8),
\[
\boxed{
\int_1^\infty U(T)T^{-z-1}dT
=
(1-2^{-z})
\frac{(1-2^{-s})(2-2^{-s})}
{2z(z+1/2)\zeta(s)}.
}
\tag{L-90008.19}
\]
The new factor is
\[
1-2^{-z}=1-\sqrt2\,2^{-s}.
\]
Its zeros lie on `Re z=0`, equivalently `Re s=1/2`.  The other two finite
factors vanish only on `Re s=0` and `Re s=-1`, respectively.  Hence a
hypothetical nontrivial zero with
\[
\Re\rho>1/2
\]
produces an uncancelled pole of (L-90008.19) at
\[
z=\rho-1/2.
\]
Thus the annularization is **zero-safe off the critical line**.

## 7. Significance and boundary

The low-row route previously presented a global reciprocal-zeta hinge.  This
lemma converts its exact dyadic innovation into a compact multiplicative
annulus while retaining every off-line pole.  That makes local block,
martingale, or finite-overlap energy attacks possible without reintroducing an
infinite two-adic tail.

Closed exactly, subject to independent review:

1. `U(T)=W(T)-W(T/2)`;
2. the five-tap critical-Haar source polynomial;
3. simultaneous cancellation of the constant and half-power moments on every
   complete two-adic fiber;
4. exact localization to `T/16<m<=T`;
5. the explicit four-band annular kernel;
6. finite dyadic reconstruction of `W`;
7. survival of every off-critical zeta pole in the annular Mellin transform.

Still open:

1. a useful one-sided or coercive estimate for the annular bank;
2. cofinal sign of `D(T)` / `5c_T(2)+3c_T(3)`;
3. SHARP;
4. RH.