# R-105620 — Raw negative shell energy is not a real-rootedness certificate

Claim ID: `R-105620`  
Status: **PROVED EXACT COUNTERFAMILY**  
Created: 2026-08-25  
Depends on: `L-105602`; `L-105290`  
RH status: **not assumed**

The height-shell theorem `L-105602` gives the valid sufficient estimate

\[
M_{p_0}(h_1,h_2)
\le
\sum_k\mathcal E_-(\mathcal U_k)
\]

when the terminal rung is shell-free. This file proves that requiring the raw
right side to be below two is far stronger than shell emptiness and may fail by
an arbitrarily large factor even for a completely real-rooted derivative
ladder.

## 1. A real-rooted exact family

Let

\[
p_N(z)=z^N,
\qquad
0<h_1<h_2,
\]

and put

\[
r={h_2-h_1\over h_2+h_1}\in(0,1).
\]

Every zero of every derivative of `p_N` is real. Hence every open positive
height shell is empty on every rung.

Use the Cayley coordinate

\[
w={x-ih_1\over x+ih_1},
\qquad |w|=1.
\]

For the one-root polynomial `z`, its height-shell map is

\[
\boxed{
S_r(w)
={\Theta_{z,h_2}(x)\over\Theta_{z,h_1}(x)}
=w{1-rw\over w-r}.
}
\tag{R-105620.1}
\]

Since

\[
p_N^{(k)}(z)=c_{N,k}z^{N-k},
\]

the adjacent derivative shell quotient is the same map on every rung:

\[
\boxed{
\mathcal U_k=S_r
\qquad(0\le k<N).
}
\tag{R-105620.2}
\]

## 2. Exact Fourier energy

On the unit circle, expansion in negative powers gives

\[
\boxed{
S_r(w)
=-rw+(1-r^2)
+
\sum_{m\ge1}(1-r^2)r^m w^{-m}.
}
\tag{R-105620.3}
\]

Therefore

\[
\boxed{
\mathcal E_-(S_r)
=
\sum_{m\ge1}m(1-r^2)^2r^{2m}
=r^2.
}
\tag{R-105620.4}
\]

The positive energy is also

\[
\boxed{\mathcal E_+(S_r)=r^2,}
\tag{R-105620.5}
\]

so the signed degree is zero, exactly as required by the empty shell.

Across the complete derivative ladder,

\[
\boxed{
\sum_{k=0}^{N-1}\mathcal E_-(\mathcal U_k)
=Nr^2.
}
\tag{R-105620.6}
\]

This diverges with `N`, while every shell count remains identically zero.

For the explicit choice

\[
h_2=2h_1,
\qquad r={1\over3},
\qquad N=19,
\]

one has

\[
\boxed{
M_{p_N}(h_1,h_2)=0,
\qquad
\sum_{k<N}\mathcal E_-(\mathcal U_k)
={19\over9}>2.
}
\tag{R-105620.7}
\]

## 3. What the raw gate loses

The exact degree formula is

\[
-\deg\mathcal U_k
=\mathcal E_-(\mathcal U_k)
-
 \mathcal E_+(\mathcal U_k).
\]

Replacing it by

\[
-\deg\mathcal U_k\le\mathcal E_-(\mathcal U_k)
\]

discards the complete positive-frequency compensation. In the counterfamily,
that discarded compensation is exactly the whole negative energy on every
rung.

Thus the raw gate

```text
sum of negative shell energies < 2
```

is a valid sufficient condition but is not a natural consequence of
real-rootedness, even in the simplest real-rooted polynomial family. It should
not be treated as an independent theorem likely to follow merely from source
smallness.

## 4. Correct conclusion for the Xi programme

A viable shell proof must retain a source-owned lower bound for the positive
Hardy energy, or preserve cancellations before taking negative parts. The
phase-variance/one-sided-Hardy reserve is therefore not optional bookkeeping:
it is the missing compensation which the raw shell estimate throws away.

Accordingly `HSHE105602` is retained only as an overstrong sufficient route.
The conclusion-facing integrated target must be a **balanced** phase-energy
transfer, coupled to `MCTPHYS105610/L-105620--L-105621`, rather than a bound on
raw negative energy alone.

## 5. Scope

The counterfamily does not refute the possibility that the raw inequality may
happen to hold for a specially chosen Xi frame. It proves that no argument from
real-rootedness, shell emptiness, or topology alone can establish it, and that
an unbalanced rungwise energy estimate can pay arbitrarily large null energy.
