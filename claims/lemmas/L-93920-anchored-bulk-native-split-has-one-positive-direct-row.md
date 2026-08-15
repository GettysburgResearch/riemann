# L-93920 — The native row splits into an anchored finite realization and a direct positive Volterra bulk row

Claim ID: `L-93920`  
Status: **PROPOSED EXACT HYBRID PRODUCER ON FROZEN DIRECTED TARGET–LORENZ INPUTS — REVIEW REQUIRED**  
Created: 2026-08-16  
Primary inputs: `L-91760`, `L-91761`; retained-cell defect theorem `L-91733`; directed Target–Lorenz leaf compiler `L-93780--L-93783` at PR #508 head `4ae97dffd1f76ed3244b8f3028560ffa80663caf`  
Does not use: `L-91763`, `T-92910`, PR #509 as a theorem antecedent  
RH status: **unproved**

## 1. Moving anchored/bulk partition

Let `X>=10^12` be an integer and put

\[
K=\left\lfloor\frac X{67}\right\rfloor+1,
\qquad
W_X=6\left\lceil\sqrt K\right\rceil+4.
\]

Define the complete bulk cell set

\[
\mathcal I_X
=\{m\in\mathbb Z:K+2\le m\le X-W_X-3\}
\]

and let `\mathcal A_X` be its complement in the finite endpoint cells `1,...,X`.
For `X>=10^12`, the two sectors are disjoint and the bulk is nonempty.

Retain the exact finite divergence

\[
d_X^\star(t)=
\sum_{k\le X/t}
\frac{\mu(k)}{\sqrt{kt}}
\log\frac X{kt}.
\]

Write

\[
d_{X,I}^\star(m)=\mathbf1_{\mathcal I_X}(m)d_X^\star(m),
\qquad
d_{X,A}^\star=d_X^\star-d_{X,I}^\star.
\]

Let `b_(X,I)^star`, `b_(X,A)^star` be their exact discrete tails. On each retained complete cell define the continuum tail

\[
\overline b_{X,I}^\star(n)
=
\sum_{\substack{m\in\mathcal I_X\\m\ge n}}
\int_m^{m+1}d_X^\star(t)\,dt
\]

and the signed retained-cell defect

\[
E_X^I=b_{X,I}^\star-\overline b_{X,I}^\star.
\]

Then, before any positivity argument,

\[
\boxed{
 b_X^\star=b_{X,A}^\star+\overline b_{X,I}^\star+E_X^I.
}
\tag{L-93920.1}
\]

Applying the finite row map `\mathcal R` gives

\[
\boxed{
 c_X=c_{X,A}+\overline c_{X,I}+\mathcal R E_X^I.
}
\tag{L-93920.2}
\]

This identity is derived cell by cell. It does not import PR #509.

## 2. The bulk is already a finite nonnegative row

For `s` in a retained cell,

\[
1<\frac Xs<67.
\]

By `L-91760`,

\[
\overline c_{X,I}
=
\sum_{m\in\mathcal I_X}
\int_m^{m+1}
\frac{2L(X/s)}s\,p_s\,ds,
\]

where `p_s(j)>=0` for every row `j>=2`. The directed factor-67 density bound gives

\[
L(X/s)>\frac{159}{500}>0.
\]

Therefore

\[
\boxed{d_{X,I}:=\overline c_{X,I}\ge0}
\tag{L-93920.3}
\]

coefficientwise.

No endpoint quantizer is needed: `p_s` is itself a finite component row, and the positive integral is already a finite nonnegative row.

No causal difference of two Volterra fibres is formed. In particular, the exact witness in `R-93920` is accepted rather than challenged.

## 3. Exact anchored finite row

The anchored sector is kept in its literal finite native form. Each occurrence is labelled by

```text
(endpoint cell, small divisor, parity, rough history,
 least rough owner, causal path).
```

Apply the frozen directed Target–Lorenz theorem only to these finite canonical endpoint packets. At a terminal leaf let `E` and `O` be the positive even and odd finite source packets, let `U` be the literal Target–Lorenz cutoff submeasure, and define

\[
\nu=E-U\ge0,
\qquad
B=R(U)-R(O)\ge0.
\]

The exact typed leaf identity is

\[
R(\nu)+B=R(E)-R(O).
\]

Summing the actual stopping-line path weights over the anchored occurrences gives a finite row

\[
\boxed{
 d_{X,A}
 =\sum_{\omega\in\mathscr A_X}
 \omega_\omega\,[R(\nu_\omega)+B_\omega]
 \ge0
}
\tag{L-93920.4}
\]

with the exact physical marginal

\[
\boxed{d_{X,A}=c_{X,A}.}
\tag{L-93920.5}
\]

The family used here is the canonical finite endpoint family, not the derivative family `p_s`. The negative witness `(67,15,1005,14)` is therefore outside the operation list.

## 4. One actual direct row

Define

\[
\boxed{d_X^0=d_{X,A}+d_{X,I}.}
\tag{L-93920.6}
\]

It is coefficientwise nonnegative and, by (L-93920.2)--(L-93920.5),

\[
\boxed{d_X^0=c_X-\mathcal R E_X^I.}
\tag{L-93920.7}
\]

Thus every ordinary column and every radix-four detail column is an observation of this same row:

\[
\boxed{
C_{d_X^0}(q)=w_X(q)-v_q(E_X^I),
}
\tag{L-93920.8}
\]

\[
\boxed{
\Xi_{d_X^0}(q)=
\Omega_X(q)-\mathcal D_4v_q(E_X^I).
}
\tag{L-93920.9}
\]

There are no internal or exported Volterra children, no auxiliary port, no B-spline collar, and no terminal quantizer comparison. The only adverse term is the one signed retained-cell quadrature defect.

## 5. Lineage disposition

```text
PR #495 L-91760--L-91761               load-bearing and preserved
PR #495 L-91762                         preserved as a non-load-bearing audit
PR #495 L-91763 / T-92910               forbidden
PR #503 negative witness                accepted and regression-locked
PR #509                                 compared, not imported as confirmation
PR #508 finite Target–Lorenz leaves     frozen anchored-sector input
```
