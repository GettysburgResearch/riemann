# R-25601 — The aggregate reflected identity has zero packet Schur reserve

Claim ID: `R-25601`  
Title: The exact two-frequency reflected block controls only the synthesized sum and has zero Schur reserve on every nontrivial packet splitting  
Status: **PROPOSED EXACT REFUTATION / SCOPE THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #256  
Dependencies: PR #241 `L-9518`; PR #250 `L-24904`  
Scope: reflected-reserve constructions using only the aggregate identity

## 1. Physical block Hilbert space

Fix one physical block and let

\[
\mathcal H_J=L^2([J,J+1])
\]

with its usual inner product.  By the exact two-frequency identity of
`L-9518`, the reflected Selberg construction computes the norm of the
**synthesized physical source**.  If a signed packet is split into components

\[
q=(q_1,\ldots,q_m)\in\mathcal H_J^m,
\]

then the aggregate block is

\[
\boxed{
E_J(q)=\left\|\sum_{r=1}^m q_r\right\|_{\mathcal H_J}^2.}
\tag{R-25601.1}
\]

The two-frequency kernel is essential for the equality with the physical
block, but it does not change the following finite Hilbert-space fact.

## 2. Synthesis Gram and its kernel

Let

\[
S:\mathcal H_J^m\longrightarrow\mathcal H_J,
\qquad
S(q_1,\ldots,q_m)=\sum_rq_r.
\]

Then

\[
E_J(q)=\langle q,S^*Sq\rangle,
\]

and the block matrix of `S^*S` is

\[
\boxed{
S^*S=
\begin{pmatrix}
I&I&\cdots&I\\
I&I&\cdots&I\\
\vdots&\vdots&\ddots&\vdots\\
I&I&\cdots&I
\end{pmatrix}.}
\tag{R-25601.2}
\]

For every `m>=2`,

\[
\ker S=\{(q_r):\sum_rq_r=0\}
\]

is nonzero.  In particular,

\[
(v,-v,0,\ldots,0)\in\ker S
\qquad(v\ne0).
\tag{R-25601.3}
\]

Therefore there is no `kappa>0` such that

\[
S^*S\succeq\kappa I_{\mathcal H_J^m}
\tag{R-25601.4}
\]

on the complete packet space.

## 3. Exact Schur calculation

For a two-block splitting `q=(h,z)`, the aggregate quadratic form is

\[
\|h+z\|^2
=
\left\langle
\binom hz,
\begin{pmatrix}I&I\\I&I\end{pmatrix}
\binom hz
\right\rangle.
\tag{R-25601.5}
\]

The lower-right block is `I`, and its Schur complement is exactly

\[
\boxed{
I-I I^{-1}I=0.}
\tag{R-25601.6}
\]

Thus the reserve operator of `L-24904` is zero when its three blocks are taken
only from the aggregate reflected identity.  Moving the complete Hermitian
square from one side of the identity to the other gives the tautology

\[
E_J=E_J,
\]

not a strict source estimate.

## 4. The geometric-recurrence restriction does not repair the abstract gap

One may try to restrict the packet coordinates to a geometric depth orbit

\[
q_j=r^jv,
\qquad 0\le j<K,
\tag{R-25601.7}
\]

and hope that synthesis becomes coercive there.  Algebra alone still supplies
no uniform reserve.  If `r` is a nontrivial `K`-th root of unity, then

\[
\sum_{j=0}^{K-1}r^jv=0
\]

while

\[
\sum_{j=0}^{K-1}\|r^jv\|^2=K\|v\|^2>0.
\tag{R-25601.8}
\]

This is a scope counterexample, not an assertion that the arithmetic residual
is a constant root of unity.  It proves that the geometric-resolvent algebra,
without an additional source-specific inequality, cannot yield the required
reserve.

## 5. Correct reserve interface

A useful reflected completion must add an independently proved frame estimate
on the **actual arithmetic source manifold**, for example

\[
\boxed{
\left\|\sum_r q_r\right\|^2
\ge
\kappa_K\sum_r\|q_r\|^2
-
\operatorname{Low}_K(q)
-
\operatorname{Boundary}_K(q),}
\tag{R-25601.9}
\]

with `kappa_K>0` independent of `J` and with the two error terms already routed
strictly lower scale or charged at exponent `o_K(1)`.  A polynomial loss in `K`
is harmless for the fixed-`K`, `J->infinity` exponent, but `kappa_K=0` is not.

For the fixed-logarithm Möbius slice, an estimate of the form
(R-25601.9) contains the fixed-ratio shell energy of PRs #229/#234.  It is the
source-specific arithmetic theorem, not a consequence of reflection.

## 6. Disposition

The following implication is rejected:

```text
exact reflected Hermitian identity
+ packet/face enumeration
=> strict reflected Schur reserve.
```

What survives is:

```text
exact reflected identity
+ independently proved source frame/coercivity
+ charged lower-scale boundary ledger
=> a valid reserve.
```

## 7. Proof boundary

Closed exactly here:

- the physical synthesis Gram;
- its kernel;
- the zero Schur complement;
- the failure of a reserve based only on geometric depth algebra.

Not decided here:

- whether the actual Möbius packet satisfies an additional arithmetic frame
  inequality;
- `BTP(K)`;
- RH.
