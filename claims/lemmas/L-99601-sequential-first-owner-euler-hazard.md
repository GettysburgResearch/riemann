# L-99601 — A sequential first-owner hazard exactly preserves every native rough Euler coefficient

Claim ID: `L-99601`  
Status: **PROVED EXACT SOURCE IDENTITY; REMAINING SIGN GATE OPEN**  
Created: 2026-08-20  
Depends on: ordered rough-prime ownership and positive parity-labelled sources  
RH status: **not assumed**

## 1. Native positive parity source

Let

\[
67\le p_1<\cdots<p_k,\qquad r_i=p_i^{-1/2},
\]

and let \(U_i\) be the same-index endpoint shift. Let \(S\) swap the two parity
channels.

For a positive source packet \(P\), define the future-completed source

\[
\mathcal E_{i:k}P
=
\bigoplus_{A\subseteq\{i,\ldots,k\}}
r_A S^{|A|}U_A P,
\tag{L-99601.1}
\]

where \(r_A=\prod_{h\in A}r_h\). Its signed observation is

\[
\mathcal O(\mathcal E_{i:k}P)
=
\prod_{h=i}^k(I-r_hU_h)\,\mathcal O(P).
\tag{L-99601.2}
\]

This is the literal native Euler source: every rough subset occurs once with
its exact magnitude and cumulative parity.

## 2. One-step hazard

The elementary source identity is

\[
\boxed{
\mathcal E_{i:k}P
=
(1-r_i)\mathcal E_{i+1:k}P
\ \oplus\
r_i\bigl(
\mathcal E_{i+1:k}P
\oplus
SU_i\mathcal E_{i+1:k}P
\bigr).
}
\tag{L-99601.3}
\]

Both terms are positive sources. The second is one paired current containing
the **complete future-prime profile**. No raw child is exported with a
contracted coefficient.

Put

\[
s_0=1,\qquad
s_i=\prod_{h\le i}(1-r_h),\qquad
\lambda_i=r_is_{i-1}.
\tag{L-99601.4}
\]

Iterating only the first term of (L-99601.3) gives

\[
\boxed{
\mathcal E_{1:k}P
=
s_kP
\ \oplus\
\bigoplus_{i=1}^k
\lambda_i
\bigl(
\mathcal E_{i+1:k}P
\oplus
SU_i\mathcal E_{i+1:k}P
\bigr).
}
\tag{L-99601.5}
\]

As usual,

\[
s_k+\sum_i\lambda_i=1.
\tag{L-99601.6}
\]

Every source occurrence has the first distinguished prime \(p_i\) or belongs
to the survival source, so ownership is disjoint and exhaustive.

## 3. Signed observation

Applying the signed parity observation to (L-99601.5) gives

\[
\boxed{
\prod_{i=1}^k(I-r_iU_i)f
=
s_k f
+
\sum_{i=1}^k
\lambda_i
(I-U_i)
\prod_{h>i}(I-r_hU_h)f.
}
\tag{L-99601.7}
\]

This is an exact coefficient identity in the commuting shift algebra. The
replay checks all \(2^4\) monomials on a nontrivial exact rational fixture.

Unlike the contracted alpha-child identity, (L-99601.7) reproduces every native
coefficient

\[
(-1)^{|A|}\prod_{i\in A}r_i.
\]

## 4. The exact remaining gate

The paired first-owner current is

\[
\Delta_i^{\mathrm{fut}}f
=
(I-U_i)
\prod_{h>i}(I-r_hU_h)f.
\tag{L-99601.8}
\]

The future Euler completion is load-bearing. Replacing it by an unsieved
canonical packet, by an unrestricted reservoir, or by an independently
positive child loses the native source.

Define `FCHD67` to be a source-faithful realization, or a sufficient global
one-sided estimate, for the complete family (L-99601.8) in the actual SHARP
target/common-row source.

Then

```text
FCHD67
 -> exact positive first-owner source
 -> rows 2 and 3 nonnegative
 -> exact two-row Mellin--Landau consumer
 -> RH.
```

`FCHD67` is nonlocal and remains open. It is the honest replacement for the
invalid native promotion of the alpha-child recursion.

## 5. Relationship to the scalar Harnack route

PR #647 bypasses (L-99601.8) by asking directly for one scalar Harnack sign.
`L-99603` weakens that pointwise sign to a subpower logarithmic negative-mass
condition. The source route and scalar route are alternative conclusion-facing
mechanisms; neither may be declared proved by the algebra in this lemma.
