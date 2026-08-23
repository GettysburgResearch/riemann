# L-105201 — Every sufficiently high Xi derivative is real-rooted on the natural Gaussian height scale

Claim ID: `L-105201`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105200`; PR #720 `L-104516`  
RH status: **not assumed**

## 1. Statement

Fix `C,H>0`. For a lower derivative cutoff `M`, put

\[
T_M=C\sqrt{M\over\log M}.
\tag{L-105201.1}
\]

Then, for all sufficiently large `M`, every zero of every derivative

\[
\Xi^{(m)}(z),
\qquad m\ge M,
\]

in the common rectangle

\[
\boxed{
|\Re z|\le T_M,
\qquad |\Im z|\le H
}
\tag{L-105201.2}
\]

is real and simple.

Moreover, if

\[
N_m(T)=\#\{x\in[-T,T]:\Xi^{(m)}(x)=0\},
\]

then, uniformly for `m>=M`,

\[
\boxed{
N_m(T_M)={2w_mT_M\over\pi}+O_C(1),
}
\tag{L-105201.3}
\]

where `w_m` is the saddle from `L-105200`.

This strengthens the `T_N sqrt(log N/N)->0` range of `L-104517` to every
fixed multiple of the natural reciprocal-width scale and simultaneously
covers the complete half-infinite derivative tail.

## 2. Gaussian trigonometric model

The exact reflected companion identity is

\[
\Xi^{(m)}(z)
=i^mM_m\left[A_m(z)+(-1)^mA_m(-z)\right].
\tag{L-105201.4}
\]

By `L-105200`, uniformly in (L-105201.2),

\[
{\Xi^{(m)}(z)\over i^mM_m}
=e^{-s_m^2z^2/2}
\left[e^{iw_mz}+(-1)^me^{-iw_mz}ight]
+o(1)e^{w_m|\Im z|+O_C(1)}.
\tag{L-105201.5}
\]

The model is a nowhere-zero Gaussian times

```text
2 cos(w_m z),  m even;
2i sin(w_m z), m odd.
```

Hence its zeros are simple and real, with spacing `pi/w_m`.

## 3. Cellwise Rouché argument

Fix `0<rho<pi/4`. Around every model zero in the slightly enlarged
rectangle, take the disk of radius `rho/w_m`. The disks are disjoint. On the
boundary of a cosine disk,

\[
|\cos(w_mz)|=|\sin(\rho e^{i\theta})|
\ge c_\rho e^{w_m|\Im z|},
\]

and the analogous lower bound holds for sine. The Gaussian multiplier in
(L-105201.5) has modulus between two positive constants depending only on
`C,H`, because

\[
|s_m\Re z|=O_C(1),
\qquad s_m|\Im z|=o(1).
\]

The error in (L-105201.5) is therefore smaller than the model on every disk
boundary once `M` is large. Rouché gives exactly one Xi-derivative zero per
model cell.

On the complement of the disks, use

\[
|\cos(x+iy)|^2=\cos^2x+\sinh^2y
\]

and its sine analogue. After division by `exp(w_m|Im z|)`, the model has a
uniform positive lower bound away from the disks. Equation (L-105201.5)
excludes every additional zero.

Each disk is invariant under conjugation and contains exactly one zero of the
real entire function `Xi^(m)`. A nonreal zero would bring its distinct
conjugate, so the zero is real. The Rouché multiplicity one also proves
simplicity.

## 4. Count and height-order corollary

Counting the cosine or sine cells in `[-T_M,T_M]` gives (L-105201.3).

Equivalently, for every fixed `K>0` and `H>0`, put

\[
M_T=\left\lceil K T^2\log(2+T)\right\rceil.
\]

Since

\[
T=O_K\!\left(\sqrt{M_T/\log M_T}\right),
\]

all zeros of every `Xi^(m)`, `m>=M_T`, in

\[
|\Re z|\le T,
\qquad |\Im z|\le H
\]

are real and simple for sufficiently large `T`.

Thus the derivative order needed to clear an original-height rectangle is
unconditionally of the natural order

\[
\boxed{T^2\log T,}
\tag{L-105201.6}
\]

without the additional diverging factor forced by the first-moment
approximation.

## 5. Scope

The theorem clears a growing rectangle for every derivative in a high-order
tail. It does not descend that zero-free rectangle through the remaining
`O(T^2 log T)` low derivative levels. The exact quantitative obstruction to
that descent is reorganized as a residue-coherence defect budget in
`L-105203`.
