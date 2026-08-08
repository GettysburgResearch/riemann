# O-27601 — First-layer Mersenne compression is not an all-generation reciprocal-eta bound

Claim ID: `O-27601`  
Title: The logarithmic sparse seminorm of the recombined cutoff boundary solves atomization, not the reciprocal-eta resolvent  
Status: **EXACT SCOPE FIREWALL / REVISED RESEARCH INTERFACE**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: PR #309 `L-30502`; PR #302 `L-28004`; PR #280 `L-27701/L-27702`  
Scope: logical separation of a one-generation norm from the complete RH-bearing central cascade

## 1. The exact sparse boundary norm

PR #309 proves that the complete positive stopped-power boundary

\[
G_X=\mathscr C h_X,
\qquad
h_X(x)=x^{-1/2}\log(\min(x,X)),
\]

satisfies

\[
\boxed{
\|G_X\|_{\mathcal M}
:=|G_X(2)|
 +\sum_{P=2^r}P|G_X(2P-1)-G_X(2P)|
\le16(1+\log X).
}
\tag{O-27601.1}
\]

This is a genuine positive theorem. It explains why the same boundary can have linear ordinary divisor-source atomic norm and logarithmic coherent dyadic variation.

## 2. The reciprocal-eta scalar is an all-stage telescope

Let

\[
r_0=w_X,
\qquad
r_{j+1}=\mathscr C r_j.
\]

The finite central cascade terminates after `O(log X)` stages. PR #302 proves the exact source identity

\[
\boxed{
\mathcal R_\eta(X)
=\sum_j r_j(2)
 -\sum_j\sum_{P=2^r}
  P[r_j(2P-1)-r_j(2P)].
}
\tag{O-27601.2]

The closing bracket in the tag is typographical only.

Therefore

\[
|\mathcal R_\eta(X)|
\le\sum_j\|r_j\|_{\mathcal M}.
\tag{O-27601.3}
\]

Equation (O-27601.1) controls one recombined boundary state. It does not control

\[
\sum_{j\ge0}\|\mathscr C^jG_X\|_{\mathcal M}
\]

or establish invariance of the Mersenne seminorm under `mathscr C`.

## 3. Resolvent identity

Formally, on the terminating finite state,

\[
(I-\mathscr C)^{-1}
=I+\mathscr C+\mathscr C^2+\cdots.
\]

Since `G_X=mathscr C h_X`,

\[
\boxed{
(I-\mathscr C)^{-1}G_X
=\left[(I-\mathscr C)^{-1}-I\right]h_X.
}
\tag{O-27601.4]

Again the closing bracket in the tag is typographical only.

The operator `I-mathscr C` has reciprocal-eta symbol. Thus the all-generation estimate for `G_X` is not implied by its first-layer sparse norm; it retains the same inverse-eta pole family as the original critical source.

## 4. Correct use of the sparse theorem

The logarithmic Mersenne estimate may be used in either of two valid ways:

1. as an inhomogeneous input to a separately proved contractive recurrence in a source space invariant under the finite central operator;
2. as one boundary component of a coupled positive quadratic frame whose other component supplies the missing contraction.

It may not be iterated merely by repeating (O-27601.1), because later residuals are not shown to be profiles of the same form and the seminorm is not proved contractive.

## 5. Current strongest interface

The atomized carry-position frame of PR #297 retains the coherent boundary inside an exact positive normal Gram. Its scalar mean is PR #289's prime-annulus field. The ordinary-prime endpoint source has already been bound positively; the live theorem is the coupled interior source matrix.

Thus the corrected choice is:

```text
first-layer Mersenne compression       useful exact diagnostic;
all-generation eta/Mersenne recurrence open and RH-bearing;
atomized quadratic frame               exact pole-preserving positive state;
coupled interior matrix                preferred current producer.
```

## 6. Status

```text
initial complete-boundary Mersenne norm    PROPOSED COMPLETE / imported
all-generation Mersenne stability          OPEN / RH-BEARING
raw atomic terminal closure                REFUTED
atomized scalar-to-vector bridge           PROPOSED COMPLETE
Riemann Hypothesis                         UNPROVED
```
