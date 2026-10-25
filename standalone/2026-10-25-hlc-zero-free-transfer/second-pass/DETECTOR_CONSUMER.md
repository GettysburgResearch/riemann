# Does the improved long inverse moment move the zero-free boundary?

Status: exact scalar consumer calculation. It explains the consequence and
the limit of the new native estimate; it does not assume that a smaller
half-plane has been obtained.

Dependency: the proposed source-dependent native moment in
`CAPPED_NATIVE_MOMENT.md`, with all of its finite-order family, height,
profile, mask and imported-source qualifications. The old selected-prime
count is the one retained in PR1014, commit
`845225c2e7713b69766b95c5e6964d44bb62f6bb`,
`standalone/2026-10-22-inverse-length-consumer/PROOF.md`.

## 1. The actual improvement and the remaining target

For `D=U^r`, `1<=r<=3/2`, the old inverse exponent is

\[
 e_0(r)=\frac{1+5r}{6}.
\]

The new estimate can be expressed on this interval as

\[
 e_1(r)=\min\left\{\frac{1+5r}{6},\frac27+\frac34r\right\}
 =\begin{cases}
 (1+5r)/6,&1\le r\le10/7,\\
 2/7+3r/4,&10/7\le r\le3/2.
 \end{cases}                                               \tag{1}
\]

At the long endpoint,

\[
 e_0(3/2)=\frac{17}{12},\qquad
 e_1(3/2)=\frac{79}{56},\qquad
 e_0(3/2)-e_1(3/2)=\frac1{168}.                            \tag{2}
\]

This is an improvement for the actual Möbius coefficient, after all
physical rows have been summed. It is different from the moving-twist
Gauss estimate elsewhere in this packet.

The particular sufficient hypothesis of PR1014 would require the
exponent `max(1,1/6+4r/5)`. At `r=3/2` this is `41/30`; the new result
still exceeds it by

\[
                  \frac{79}{56}-\frac{41}{30}=\frac{37}{840}.
                                                               \tag{3}
\]

More fundamentally, the new saving starts after the length used by
the old optimized detector balance, as the next section proves.

## 2. The complete old balance stays in the unchanged interval

Use the old foundation `a<=7/8`, put `delta=2a-1`, and take
`0<delta<=3/4`, `0<=x<=1/2`. Define

\[
 P_x=(2-8x/9)(1-x),\qquad D_x=3-17x/9,\qquad
 C=\delta P_x/D_x.
\]

The selected-prime short-witness bound has exponent

\[
 R_{\rm short}(t)=1-\delta+C(3/2-t),\qquad1\le t\le3/2.
                                                               \tag{4}
\]

With the old inverse moment the long-witness exponent is

\[
 R_{\rm long,0}(t)=\frac16+(5/6-\delta)t.                    \tag{5}
\]

This includes the maximal inverse length `r=t`: the function is
nondecreasing for the entire allowed delta range, and at `r=1` it is
`1-delta`. The crossing of (4) and (5) occurs at

\[
 t_* =1+\frac{C}{2(5/6-\delta+C)}.                           \tag{6}
\]

The denominator is positive. The following exact polynomial identity
provides the required bound without a sampled optimization:

\[
 2D_x-3P_x=\frac49x(11-6x)\ge0.
\]

Consequently `C<=2delta/3`. Since `delta<=3/4`,

\[
 C\le\frac23\delta\le5-6\delta,
 \qquad\boxed{t_*\le10/7.}                                 \tag{7}
\]

The last equivalence follows by multiplying (6) by its positive
denominator. Equality requires `delta=3/4` and `x=0`.

Replace the long moment by (1). Its resulting long-witness count is

\[
 R_{\rm long,1}(t)=e_1(t)-\delta t.
\]

Both slopes, `5/6-delta` before `10/7` and `3/4-delta` afterwards,
are nonnegative. Thus this count is nondecreasing on the entire
interval and equals the old count at `t_*`. For `t<=t_*`, the short
count in (4) is at least its crossing value. For `t>=t_*`, the new
long count is at least that same value. Hence

\[
 \min_{1\le t\le3/2}\max\{R_{\rm short}(t),R_{\rm long,1}(t)\}
 =R_{\rm short}(t_*)
 =\min_{1\le t\le3/2}\max\{R_{\rm short}(t),R_{\rm long,0}(t)\}.
                                                               \tag{8}
\]

The floor bin retains its original row count and is unchanged. The
same holds for the other plain-polynomial witness and all physical
frequency endpoints, since (8) supplies exactly the old optimized
count. Thus simply inserting (1) into this consumer cannot certify a
smaller zero-free boundary.

## 3. Why lowering a source ceiling alone has the same contact

The preceding calculation is not a numerical accident. Let
`delta_b=2b-1`, with `0<delta_b<5/6`, and use the source's unamplified
row-density exponent at that ceiling:

\[
 R_b=\frac{15-16\delta_b}{15-6\delta_b}.
\]

The endpoint-bin line `R_b+delta_b r` intersects the old inverse line
exactly at

\[
 r_b=\frac{R_b-1/6}{5/6-\delta_b}
                    =\frac5{5-2\delta_b}.                 \tag{9}
\]

For every `delta<=delta_b`, (6) and `C<=2delta/3` give
`t_*<=5/(5-2delta)<=r_b`. Therefore this endpoint-line improvement
again begins at or beyond the old detector crossing. This is a
statement about reusing this particular density estimate in this
particular detector. It is not an impossibility theorem for a new
signed estimate, different detector, or a genuinely stronger density
input.

## 4. Exact next target

The new native theorem has closed a component that was previously
left open at these longer lengths. To change the current global
consumer, the saving has to reach the inverse lengths at its crossing,
or the short-witness bound itself has to improve. A proof for only the
centered affine remainder or a better bound for a separate Gauss norm
does not provide that statement.

No new numerical boundary follows from this note. The imported
source-qualified benchmark `B_flat=0.874886647039964...` is unchanged.
