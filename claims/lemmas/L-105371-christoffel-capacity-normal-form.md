# L-105371 — Boundary positivity is a Christoffel capacity bound for the critical atoms

Claim ID: `L-105371`  
Status: **PROVED EXACT FINITE-DIMENSIONAL NORMAL FORM**  
Created: 2026-08-23  
Depends on: `L-105370`  
RH status: **not assumed**

## 1. Abstract domination lemma

Let `A` and `C` be real symmetric `k by k` matrices with `A\succeq0` and
`C\succeq0`. Let `A^\dagger` denote the Moore--Penrose inverse. Then

\[
\boxed{
C\preceq A
}
\tag{L-105371.1}
\]

if and only if

\[
\boxed{
\operatorname{Ran}C\subseteq\operatorname{Ran}A
}
\tag{L-105371.2}
\]

and

\[
\boxed{
\lambda_{\max}
\left(A^{\dagger/2}CA^{\dagger/2}ight)
\le1.
}
\tag{L-105371.3}
\]

Indeed, (L-105371.1) implies `ker A subseteq ker C`, hence the range condition.
Restricting to `Ran A`, where `A` is positive definite, and conjugating by
`A^(-1/2)` gives (L-105371.3). The converse reverses the same congruence and is
zero on `ker A`.

## 2. Source-normalized critical capacity

Use the matrices of `L-105370`. For `a in {0,1}`, suppose first that
`A_k^(a)(F)` is positive definite. Define

\[
\boxed{
\mathcal K_{k,a}(s)
=s^a v_k(s)^T
\left(\mathsf A_k^{(a)}(F)\right)^{-1}
v_k(s),
}
\tag{L-105371.4}
\]

where `v_k(s)=(1,s,...,s^(k-1))^T`. This is the source Christoffel leverage of
an atom at `s`.

Define the normalized critical operator

\[
\boxed{
\mathsf B_{k,\Omega}^{(a)}
=
\left(\mathsf A_k^{(a)}\right)^{-1/2}
\mathsf C_{k,\Omega}^{(a)}
\left(\mathsf A_k^{(a)}\right)^{-1/2}.
}
\tag{L-105371.5}
\]

Then

\[
\boxed{
\mathsf S_{k,\Omega}^{(a)}\succeq0
\iff
\lambda_{\max}
\left(\mathsf B_{k,\Omega}^{(a)}\right)
\le1.
}
\tag{L-105371.6}
\]

Thus one exact generalized eigenvalue measures how much of the source moment
space is consumed by all critical atoms together.

For singular source matrices, the same statement holds with the range
condition (L-105371.2) and the pseudoinverse normalization.

## 3. Atomic feature form

Let

\[
u_{c;k,a}
=
\sqrt{W_cs_c^a}
\left(\mathsf A_k^{(a)}\right)^{-1/2}v_k(s_c).
\]

Then

\[
\boxed{
\mathsf B_{k,\Omega}^{(a)}
=
\sum_cu_{c;k,a}u_{c;k,a}^T.
}
\tag{L-105371.7}
\]

The exact boundary condition is therefore the operator-frame bound

\[
\boxed{
\left\|\sum_cu_{c;k,a}u_{c;k,a}^T\right\|_{\rm op}
\le1.
}
\tag{L-105371.8}
\]

This is a capacity statement, not merely a sign test on individual residues.

## 4. A scalar sufficient lane

Since the operator in (L-105371.7) is positive semidefinite,

\[
\lambda_{\max}(\mathsf B)
\le\operatorname{tr}\mathsf B.
\]

Moreover

\[
\boxed{
\operatorname{tr}
\mathsf B_{k,\Omega}^{(a)}
=
\sum_cW_c\mathcal K_{k,a}(s_c).
}
\tag{L-105371.9}
\]

Consequently the scalar inequality

\[
\boxed{
\sum_cW_c\mathcal K_{k,a}(s_c)\le1
}
\tag{L-105371.10]
\]

is sufficient for the order-`k`, parity-`a` boundary matrix to be positive.
The closing bracket in this display is to be read as the tag delimiter;
explicitly, the intended formula is

\[
\boxed{
\sum_cW_c\mathcal K_{k,a}(s_c)\le1.
}
\tag{L-105371.10}
\]

This trace lane is generally stronger than the exact operator-capacity
condition. It is nevertheless source owned and scalar once the source
Christoffel function is controlled.

## 5. Necessary atomwise and aggregate tests

If the exact domination holds and `A_k^(a)` is positive definite, then every
individual atom satisfies

\[
\boxed{
W_c\mathcal K_{k,a}(s_c)\le1.
}
\tag{L-105371.11}
\]

because each rank-one summand in (L-105371.7) is bounded by the identity.
Also

\[
\boxed{
\sum_cW_c\mathcal K_{k,a}(s_c)
=\operatorname{tr}\mathsf B_{k,\Omega}^{(a)}
\le k.
}
\tag{L-105371.12}
\]

Thus trace at most one is sufficient, while trace at most `k` is necessary.
The gap records overlap between the normalized atomic feature directions.

## 6. Terminal reserve in capacity coordinates

For fixed `k,a`, the source matrix is independent of the window and the
critical matrix increases outward under `CRVH105330`. If `A_k^(a)` is positive
definite, `TAIR105360` is equivalently

\[
\boxed{
\limsup_{j\to\infty}
\lambda_{\max}
\left(\mathsf B_{k,\Omega_{N_j}}^{(a)}\right)
\le1
}
\tag{L-105371.13}
\]

for every fixed order along the terminal cofinal sequence. More generally, an
`o(1)` excess over one is enough, because `A_k^(a)` is a fixed finite matrix
before the limit is taken.

The terminal programme can therefore be read as **asymptotic non-overfilling
of every finite source moment space by the critical residue atoms**.

## 7. Scope

This theorem supplies no estimate for the source matrices, their inverses, the
critical weights, or the capacity. The trace lane (L-105371.10) is not
necessary and must not replace the exact operator norm in a sharp statement.
Ill-conditioned or singular source matrices require the range condition and
pseudoinverse formulation. RH remains unproved.
