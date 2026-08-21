# L-93240 — Prime-block coherence principle

Claim ID: `L-93240`  
Status: **PROPOSED COMPLETE EXACT FINITE HILBERT-SPACE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: none  
Scope: finite families in a real or complex Hilbert space; no zeta estimate and no RH conclusion

## 1. Statement

Let \(\mathcal H\) be a real or complex Hilbert space and let

\[
(v_p)_{p\in\mathcal P}\subset\mathcal H
\]

be a finite family. Put

\[
V=\sum_{p\in\mathcal P}v_p,
\qquad
E=\|V\|^2,
\qquad
D=\sum_{p\in\mathcal P}\|v_p\|^2.
\tag{L-93240.1}
\]

Then the complete square has the exact prime-diagonal / distinct-prime split

\[
\boxed{
E
=D+2\sum_{p<r}\operatorname{Re}\langle v_p,v_r\rangle.
}
\tag{L-93240.2}
\]

Assume \(E>0\), set

\[
u=\frac{V}{\|V\|},
\qquad
a_p=\bigl[\operatorname{Re}\langle v_p,u\rangle\bigr]_+,
\tag{L-93240.3}
\]

and write

\[
\mathcal P_+=\{p:a_p>0\}.
\]

Then

\[
\boxed{
\sum_pa_p\ge\sqrt E,
\qquad
\sum_pa_p^2\le D.
}
\tag{L-93240.4}
\]

Consequently,

\[
\boxed{
|\mathcal P_+|\ge\frac ED.
}
\tag{L-93240.5}
\]

If \(J\subseteq\mathcal P_+\) has minimum cardinality among sets satisfying

\[
\sum_{p\in J}a_p\ge\frac12\sqrt E,
\tag{L-93240.6}
\]

then

\[
\boxed{
|J|\ge\frac{E}{4D}.
}
\tag{L-93240.7}
\]

Thus no fewer than \(E/(4D)\) blocks can carry half of the positive projection of the obstruction onto its own direction.

Finally the positive projections themselves give a nonnegative rank-one distinct-block certificate:

\[
\boxed{
2\sum_{p<r}a_pa_r
=\left(\sum_pa_p\right)^2-\sum_pa_p^2
\ge E-D.
}
\tag{L-93240.8}
\]

When \(E>D\), the obstruction therefore contains at least \(E-D\) units of positive distinct-block correlation after projection onto one explicit direction.

## 2. Proof

Equation (L-93240.2) is the expansion of \(\|\sum_pv_p\|^2\).

Since \(u=V/\|V\|\),

\[
\sum_p\operatorname{Re}\langle v_p,u\rangle
=\operatorname{Re}\langle V,u\rangle
=\|V\|=\sqrt E.
\]

Discarding the negative summands can only increase the sum, proving the first inequality in (L-93240.4). For every \(p\),

\[
a_p
\le |\langle v_p,u\rangle|
\le\|v_p\|,
\]

so summing squares proves the second inequality.

Cauchy--Schwarz now gives

\[
\sqrt E
\le\sum_{p\in\mathcal P_+}a_p
\le |\mathcal P_+|^{1/2}
   \left(\sum_pa_p^2\right)^{1/2}
\le |\mathcal P_+|^{1/2}D^{1/2},
\]

which proves (L-93240.5). Applying the same argument to (L-93240.6) gives

\[
\frac12\sqrt E
\le |J|^{1/2}D^{1/2},
\]

and hence (L-93240.7). Equation (L-93240.8) follows from (L-93240.4). \(\square\)

## 3. Exact rational form used by the checker

The normalisation by \(\sqrt E\) is not needed for exact arithmetic. Put

\[
b_p=\bigl[\operatorname{Re}\langle v_p,V\rangle\bigr]_+.
\tag{L-93240.9}
\]

Then

\[
\sum_pb_p\ge E,
\qquad
\sum_pb_p^2\le ED.
\tag{L-93240.10}
\]

All cardinality conclusions follow by Cauchy--Schwarz, and

\[
2\sum_{p<r}b_pb_r\ge E(E-D).
\tag{L-93240.11}
\]

For rational vectors, every quantity in (L-93240.9)--(L-93240.11) is rational. The retained checker uses this square-root-free form.

## 4. Why this is the useful normal form

The lemma does not estimate \(E\). It converts any independently obtained large obstruction into three exact objects:

1. the complete same-block budget \(D\);
2. one canonical dual direction \(u\);
3. a large set of blocks lying in the same open half-space, together with a nonnegative rank-one cross certificate.

The label \(p\) may denote a prime base while \(v_p\) contains every power of that prime. The diagonal \(D\) then pays the complete same-prime tower before any deterministic distinct-prime estimate is attempted.

## 5. Proof boundary

Established exactly:

- the complete diagonal / cross identity;
- the canonical half-space direction;
- the \(E/D\) positive-block lower bound;
- the \(E/(4D)\) half-carrier lower bound;
- the rank-one projected cross certificate.

Not established:

- an upper bound for an arithmetic obstruction \(E\);
- deterministic exclusion of the resulting prime alignment;
- RH.
