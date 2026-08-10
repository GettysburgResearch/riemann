# L-90301 — Two-state curvature synthesis needs only the negative spectral mass

Claim ID: `L-90301`  
Title: A parameter-independent synthesis of a two-state Jordan curvature is controlled by its scalar curvature plus one explicit inertia defect; full polarized positivity is stronger than necessary  
Status: **PROPOSED COMPLETE EXACT LINEAR-ALGEBRA LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: PR #350 `L-34412`; finite-dimensional spectral theorem  
Scope: exact Hermitian linear algebra; no arithmetic estimate and no RH conclusion

## 1. Setup

Let `V(tau)` be a twice differentiable path in `C^2` and put

\[
K_V
=V'V'^*-rac12(VV''^*+V''V^*).
\tag{L-90301.1}
\]

Its scalar Jordan curvature is

\[
\mathcal C(V)=\operatorname{tr}K_V
=\|V'\|^2-\operatorname{Re}\langle V,V''\rangle.
\tag{L-90301.2}
\]

PR #350 `L-34412` proves that for every parameter-independent linear synthesis `W`,

\[
K_{WV}=WK_VW^*.
\tag{L-90301.3}
\]

That file then uses the sufficient hypothesis `K_V >= 0`.  The point of this lemma is that the synthesis estimate itself does **not** require that hypothesis.

For a Hermitian matrix `K`, write

\[
K=K_+-K_-,\qquad K_\pm\ge0,\qquad K_+K_-=0,
\]

and define its negative spectral mass

\[
\boxed{\delta(K)=\operatorname{tr}K_- .}
\tag{L-90301.4}
\]

## 2. Inertia-tolerant synthesis inequality

Suppose

\[
W^*W\le qI,\qquad q\ge0.
\tag{L-90301.5}
\]

Then

\[
\boxed{
\mathcal C(WV)
\le q\,[\mathcal C(V)+\delta(K_V)].
}
\tag{L-90301.6}
\]

More precisely,

\[
-q\,\delta(K_V)
\le \operatorname{tr}(WK_VW^*)
\le q\,\operatorname{tr}(K_V)_+.
\tag{L-90301.7}
\]

### Proof

Put `A=W^*W`.  By cyclicity of trace,

\[
\operatorname{tr}(WK_VW^*)=\operatorname{tr}(AK_V).
\]

Since `0<=A<=qI`,

\[
0\le\operatorname{tr}(AK_+)\le q\operatorname{tr}K_+,
\qquad
0\le\operatorname{tr}(AK_-)\le q\operatorname{tr}K_-.
\]

Therefore

\[
-q\operatorname{tr}K_-
\le\operatorname{tr}(AK_+)-\operatorname{tr}(AK_-)
\le q\operatorname{tr}K_+.
\]

Finally

\[
\operatorname{tr}K_+
=\operatorname{tr}K+\operatorname{tr}K_-
=\mathcal C(V)+\delta(K_V),
\]

which proves the claim.

This is the exact analogue, at the current Q4 proof interface, of the methodological step in Claude's 2026 finite-compression argument: retain the indefinite block and pay only for the spectral information actually needed rather than promote the whole form to positive semidefinite.

## 3. In dimension two the defect is one scalar

Let

\[
t=\operatorname{tr}K,\qquad f^2=\|K\|_F^2=\operatorname{tr}(K^2).
\]

For a `2 x 2` Hermitian matrix the eigenvalues are

\[
\lambda_\pm
=\frac{t\pm\sqrt{2f^2-t^2}}2.
\]

Hence

\[
\boxed{
\delta(K)
=\max\!\left(0,
\frac{\sqrt{2f^2-t^2}-t}{2}
\right).
}
\tag{L-90301.8}
\]

If `t>=0`, put

\[
e=(f^2-t^2)_+=(-2\det K)_+.
\tag{L-90301.9}
\]

Then exactly

\[
\boxed{
\delta(K)
=\frac{e}{\sqrt{t^2+2e}+t}
}
\tag{L-90301.10}
\]

with the right side interpreted as zero when `e=0`.  If `t>0`,

\[
\boxed{
\delta(K)\le \frac{e}{2t}
=\frac{(-\det K)_+}{t}.
}
\tag{L-90301.11}
\]

Thus, once the scalar curvature is positive, the full polarized PSD condition

```text
det K >= 0
```

can be replaced by a quantitative bound on the **negative determinant defect**.

## 4. Consequence for the live Q4 route

The corrected Q4/critical-Haar reflected ledger on PRs #341 and #350 has dynamic source dimension exactly two.  Its current proof frontier has been stated as positivity of the complete polarized jet matrix.

For that two-state matrix, `L-90301.6` shows that a synthesis estimate only needs

```text
scalar curvature t
+
negative spectral mass delta(K).
```

The scalar curvature is already source-complete and cofinally positive on the corrected Q4 branches.  Therefore the genuinely new quantity is only

\[
\boxed{
\delta_J
=\operatorname{tr}(K_J)_-
}
\tag{L-90301.12}
\]

or, equivalently when `t_J>0`, the scalar determinant excess

\[
\boxed{e_J=(-2\det K_J)_+.}
\tag{L-90301.13}
\]

A polylogarithmic or fixed-delay bound on `delta_J` is strictly weaker than proving `K_J>=0`.

In particular, if the existing critical moat gives

\[
t_J\gg n\log n
\]

and one can prove source-specifically

\[
(-\det K_J)_+\ll n\log^B n,
\]

then (L-90301.11) gives

\[
\delta_J\ll\log^{B-1}n.
\]

This is exactly the scale separation wanted by the coefficient-one delayed recurrence.

## 5. Proof boundary

Closed exactly here:

1. synthesis control by positive spectral mass rather than PSD;
2. the exact two-state negative-mass formula;
3. determinant-defect reduction when scalar curvature is positive;
4. the quantitative `(-det K)_+/tr K` bound.

Not proved here:

1. any arithmetic bound for the Q4 determinant defect;
2. the complete dissipative recurrence;
3. RH.