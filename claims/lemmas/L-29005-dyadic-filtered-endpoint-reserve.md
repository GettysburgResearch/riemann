# L-29005 — Dyadic filtering removes the endpoint null direction

Claim ID: `L-29005`  
Title: The opposite-parity dyadic filter turns every zero-reserve endpoint split into a compact central-tree wavelet with an explicit strictly positive Selberg–Kummer reserve  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08  
Dependencies: `L-29002`, `L-29003`; the dyadic polynomial `epsilon-(3/2)delta_2+(1/2)delta_4`  
Scope: one source fiber; the complete reflected packet must still prove that these fibers enter with the required coupled coefficients

## 1. Endpoint and central commutators

Retain

\[
 D_n=T_n-T_{n-1}\equiv[n,1]\pmod{\ker\partial}
\tag{L-29005.1}
\]

from `L-29003`, and define

\[
\boxed{
 E_n=[2n,n]-[2n-1,n-1].
}
\tag{L-29005.2}

The central-tree recursions give

\[
 T_{2n}=[2n,n]+2T_n
\]

and

\[
 T_{2n-1}=[2n-1,n-1]+T_{n-1}+T_n.
\]

Therefore

\[
\boxed{
 D_{2n}=D_n+E_n.
}
\tag{L-29005.3}

Applying this once more gives

\[
 D_{4n}=D_n+E_n+E_{2n}.
\tag{L-29005.4}

## 2. Exact compact wavelet

Define the dyadically filtered endpoint chain

\[
\boxed{
 W_n=D_n-\frac32D_{2n}+\frac12D_{4n}.
}
\tag{L-29005.5}

Equations (L-29005.3)--(L-29005.4) give the exact cancellation

\[
\boxed{
 W_n=\frac12E_{2n}-E_n.
}
\tag{L-29005.6}

Thus every full tree `T_n` disappears.  The filtered endpoint is a compact
four-edge object:

\[
\boxed{
 W_n
 =\frac12[4n,2n]-\frac12[4n-1,2n-1]
  -[2n,n]+[2n-1,n-1].
}
\tag{L-29005.7}

Every split in (L-29005.7) is central or adjacent to central.

## 3. Carry and entropy coordinates

Since `D_m` is carry- and entropy-equivalent to `[m,1]`, for every carry column
`q>=2`,

\[
\boxed{
 L_q(W_n)
 =\mathbf1_{q\mid n}
  -\frac32\mathbf1_{q\mid2n}
  +\frac12\mathbf1_{q\mid4n}.
}
\tag{L-29005.8}

The logarithmic Kummer coordinate is

\[
\begin{aligned}
 F(W_n)
 &=\log n-\frac32\log(2n)+\frac12\log(4n)\\
 &=-\frac12\log2.
\end{aligned}
\]

Hence

\[
\boxed{F(W_n)=-\frac12\log2.}
\tag{L-29005.9}

The complete Selberg forcing coordinate is linear in the carry chain.  Because
an endpoint split `[m,1]` has forcing `log^2m`,

\[
\begin{aligned}
 S(W_n)
 &=\log^2n-\frac32\log^2(2n)+\frac12\log^2(4n)\\
 &=-\log2\log n+\frac12\log^22.
\end{aligned}
\]

Therefore

\[
\boxed{
 S(W_n)=-\log2\log n+\frac12\log^22.
}
\tag{L-29005.10}

## 4. Strict source-fiber reserve

Combining (L-29005.9)--(L-29005.10),

\[
\boxed{
 F(W_n)^2-S(W_n)
 =\log2\log n-\frac14\log^22.
}
\tag{L-29005.11}

For every integer `n>=2`,

\[
\boxed{
 F(W_n)^2-S(W_n)
 \ge\frac34\log^22>0.
}
\tag{L-29005.12
}

Thus the dyadic opposite-parity filter removes the exact endpoint nullity of
`L-29002`.  At the level of one complete fiber, the endpoint channel has a
strict logarithmically growing reserve.

## 5. Nonnegative superpositions

If `a_n>=0`, then the chain

\[
 W=\sum_na_nW_n
\]

has

\[
 F(W)=-\frac12\log2\sum_na_n
\]

and

\[
 S(W)=\sum_na_nS(W_n).
\]

Consequently

\[
\boxed{
\begin{aligned}
 F(W)^2-S(W)
 ={}&\frac14\log^22\left(\sum_na_n\right)^2\\
 &+\sum_na_n
   \left(\log2\log n-\frac12\log^22\right)
 \ge0.
\end{aligned}}
\tag{L-29005.13
}

For a nonzero superposition supported on `n>=2`, the reserve is strict.

This is the proof-facing positivity mechanism: if the complete reflected
endpoint packet can be grouped into nonnegative `W_n` fibers before a norm is
taken, no endpoint recurrence is needed.

## 6. Exact remaining source-binding question

The finite filter in `L-29001` is exactly

\[
 e=\varepsilon-\frac32\delta_2+\frac12\delta_4.
\]

Therefore `W_n` is the geometric endpoint image naturally associated with the
pole-preserving opposite-parity source.  What remains to be checked in the full
independent-frequency packet is not the sign of one fiber.  It is the exact
coefficient binding:

```text
does the recombined endpoint source enter as a nonnegative superposition of
complete W_n fibers, or are there signed cross-fiber coefficients that must be
retained in an ETSR recurrence?
```

A complete source manifest answering the first way would close the endpoint
channel outright.  If signed cross-fiber coefficients survive, equations
(L-29005.6)--(L-29005.13) are the correct local blocks for the recurrence.

## 7. Proof boundary

Closed exactly, subject to review:

- central-tree difference recursion;
- complete cancellation of the full dyadic trees;
- compact four-edge filtered endpoint wavelet;
- exact carry, Kummer, and Selberg coordinates;
- strict reserve of every individual fiber;
- positivity of every nonnegative fiber superposition.

Open:

- the sign and cross-term structure of the complete reflected endpoint source;
- whether the packet is a nonnegative fiber superposition;
- `ETSR` if signed cross-fiber terms remain;
- RH.