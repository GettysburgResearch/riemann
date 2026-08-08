# L-27606 — Diagonal energy and ratio-sign localization

Claim ID: `L-27606`  
Title: The diagonal prime-annulus energy is polylogarithmic, and every off-diagonal pair separated by a factor at least two has nonpositive kernel  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-27601`--`L-27605`; Chebyshev's elementary bound for `psi`  
Scope: exact energy decomposition and sign localization; no bound for the remaining signed correlation and no RH conclusion

## 1. Physical kernel

Let

\[
z(u)=e^{-u/2}W(e^{-u}).
\]

Using `L-27605.1`,

\[
\boxed{
z(u)=
\begin{cases}
2e^{-3u/2}-e^{-u/2},&0\le u<\log2,\\[1mm]
\frac12e^{-u/2}-4e^{-3u/2},&\log2\le u<2\log2,\\[1mm]
0,&\text{otherwise}.
\end{cases}}
\tag{L-27606.1}
\]

It is nonnegative on `[0,log2]` and nonpositive on `[log2,2log2]`.

The prime-annulus signal is

\[
\mathfrak P(e^t)
=\sum_q\frac{\Lambda(q)}{\sqrt q}z(t-\log q).
\tag{L-27606.2}
\]

For one unit block, define

\[
K_J(q,r)
=\int_J^{J+1}z(t-\log q)z(t-\log r)\,dt.
\tag{L-27606.3}
\]

Then

\[
\boxed{
\mathfrak E(J)
=\sum_{q,r}\frac{\Lambda(q)\Lambda(r)}{\sqrt{qr}}K_J(q,r).
}
\tag{L-27606.4}
\]

Only prime powers in

\[
\frac{e^J}{4}\le q,r\le e^{J+1}
\tag{L-27606.5}
\]

can occur.

## 2. Exact one-window norm

Direct integration of the two pieces in (L-27606.1) gives

\[
\int_0^{\log2}
(2e^{-3u/2}-e^{-u/2})^2du
=\frac16,
\]

and

\[
\int_{\log2}^{2\log2}
(\tfrac12e^{-u/2}-4e^{-3u/2})^2du
=\frac{13}{48}.
\]

Therefore

\[
\boxed{
\|z\|_2^2=\frac7{16}.
}
\tag{L-27606.6}
\]

In particular,

\[
0\le K_J(q,q)\le\frac7{16}.
\tag{L-27606.7}
\]

## 3. The diagonal is polylogarithmic

Let

\[
\mathfrak D(J)
=\sum_q\frac{\Lambda(q)^2}{q}K_J(q,q).
\tag{L-27606.8}
\]

Using (L-27606.5)--(L-27606.7),

\[
\mathfrak D(J)
\le\frac7{16}
\sum_{q\le e^{J+1}}
\frac{\Lambda(q)^2}{q}.
\]

For `q<=Y`,

\[
\Lambda(q)^2\le(\log Y)\Lambda(q).
\]

Chebyshev's elementary estimate `psi(Y)<<Y` and partial summation give

\[
\sum_{q\le Y}\frac{\Lambda(q)}q\ll\log(2Y).
\]

Hence

\[
\boxed{
\mathfrak D(J)\ll(1+J)^2.
}
\tag{L-27606.9}
\]

No RH input is used. Thus the diagonal already satisfies the required subexponential scale.

## 4. Exact sign beyond ratio two

Assume `q<r` and put

\[
h=\log(r/q).
\]

If both factors in (L-27606.3) are nonzero, set

\[
u=t-\log r.
\]

Then

\[
t-\log q=u+h,
\]

and both `u` and `u+h` lie in `[0,2log2]`.

If

\[
r/q\ge2,
\qquad\text{equivalently }h\ge\log2,
\]

then necessarily

\[
0\le u\le2\log2-h\le\log2,
\]

while

\[
\log2\le u+h\le2\log2.
\]

By the sign sectors of `z`,

\[
z(u)z(u+h)\le0
\]

pointwise. Therefore

\[
\boxed{
K_J(q,r)\le0
\qquad(q<r,\ r\ge2q).
}
\tag{L-27606.10}
\]

If `r>=4q`, the supports are disjoint and the kernel is zero.

This sign is preserved by the finite unit-block truncation; no full-line autocorrelation replacement is being made.

## 5. Exact signed-correlation frontier

Write

\[
\mathfrak O(J)
=2\sum_{q<r}
\frac{\Lambda(q)\Lambda(r)}{\sqrt{qr}}K_J(q,r).
\tag{L-27606.11}
\]

Then

\[
\boxed{
\mathfrak E(J)=\mathfrak D(J)+\mathfrak O(J).
}
\tag{L-27606.12}
\]

Since the diagonal is polylogarithmic,

\[
\boxed{
\mathfrak E(J)=e^{o(J)}
\iff
|\mathfrak O(J)|=e^{o(J)}.
}
\tag{L-27606.13}
\]

The implication from right to left uses (L-27606.9). The converse uses

\[
|\mathfrak O(J)|\le\mathfrak E(J)+\mathfrak D(J),
\]

because `mathfrak O=mathfrak E-mathfrak D`.

Equation (L-27606.10) further shows that every positive off-diagonal contribution comes from pairs with ratio strictly below two. However, the nonpositive ratio-two-to-four sector must remain in the complete signed sum: it may cancel the near-ratio sector and may not be discarded before estimation.

## 6. Correct remaining theorem

The prime-annulus energy problem is now equivalent to the source-specific signed correlation estimate

\[
\boxed{
\left|
2\sum_{q<r}
\frac{\Lambda(q)\Lambda(r)}{\sqrt{qr}}K_J(q,r)
\right|
=e^{o(J)}.
}
\tag{L-27606.14}
\]

The diagonal, far-ratio support, and ratio-at-least-two sign have all been closed. The unresolved cancellation is the joint balance between the near-ratio positive sector and the adjacent dyadic negative sector.

This is not an arbitrary prime-pair estimate: `K_J` is the exact opposite-parity annulus kernel and must be handled with both bands present.

## 7. Proof boundary

Closed exactly or elementarily:

1. the compact physical kernel and its sign sectors;
2. its exact `L2` norm `7/16`;
3. a polylogarithmic diagonal bound;
4. nonpositivity for every pair separated by a factor at least two;
5. equivalence of `PAE` to the complete signed off-diagonal correlation.

Open:

1. the signed near/adjacent-band correlation balance;
2. a source-specific reflected Selberg recurrence;
3. `PAE`;
4. RH.
