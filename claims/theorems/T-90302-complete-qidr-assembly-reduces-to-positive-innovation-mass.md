# T-90302 — Complete QIDR assembly reduces to positive innovation mass

Claim ID: `T-90302`  
Title: After the fixed-filter source dictionary, block inertia lift, all-pass telescope and collar estimates are inserted, the coefficient-one Q4 recurrence has one remaining RH-bearing input: a polynomial bound for the balanced positive innovation energy  
Status: **PROPOSED COMPLETE CONDITIONAL ASSEMBLY / FAIL-CLOSED FRONTIER — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: PR #345 `L-34401`; `L-90305`--`L-90308`; `R-90302`; existing pole-energy consumer  
Scope: Q4 route only; does not prove the remaining innovation-energy gate or RH

## 1. Exact amplitude recurrence

Retain the corrected Q4 physical current `Q_4^phys` and the aligned compact innovation `I_circ` from PR #345.  Put

\[
U(n,j)=\frac{Q_4^{\rm phys}(n,j)}{\sqrt n}.
\]

Then exactly

\[
\boxed{
U(4n,4j)
=\frac12U(n,j)
 +\frac{I_\circ(n,j)}{2\sqrt n}.
}
\tag{T-90302.1}
\]

The sharp scalar adapter gives

\[
\boxed{
|U(4n,4j)|^2
\le |U(n,j)|^2
 +\frac{|I_\circ(n,j)|^2}{3n}.
}
\tag{T-90302.2}
\]

This is already coefficient one on the inherited energy.

## 2. Define one logarithmic block energy

Fix a balanced carry-position bank and one logarithmic parent block `J`.  Let `dnu_J` be the exact positive physical/carry measure supplied by the resident atomized block localization, normalized to total mass `O(1)`. Define

\[
\boxed{
\mathcal E(J)
=\int |U(n,j)|^2\,d\nu_J(n,j).
}
\tag{T-90302.3}
\]

and the normalized innovation forcing

\[
\boxed{
\mathcal I(J)
=\int \frac{|I_\circ(n,j)|^2}{n}\,d\nu_J(n,j).
}
\tag{T-90302.4}
\]

Positive integration of (T-90302.2) gives, on aligned interior pieces,

\[
\boxed{
\mathcal E(J+\log4)
\le\mathcal E(J)+\frac13\mathcal I(J).
}
\tag{T-90302.5}
\]

up to finite cut/collar terms.

## 3. Every non-innovation interface is now polynomial forcing

The following former gaps are disposed of before estimating `mathcal I`.

### 3.1 One physical block metric

`L-90307` freezes the dyadic filters and uses the common odd-Jordan carrier.  The Q2/Q4 source, output and state paths therefore live in one independent-frequency physical block metric and every transfer filter is parameter-independent.

### 3.2 All-pass/delayed-state sign

`L-90306` differentiates the exact two-frequency all-pass identity.  Current-state curvature occurs on the dissipative side, the predecessor state at the declared delay, and an indefinite state costs only its negative spectral mass.

### 3.3 Negative spectral mass cannot accumulate

`L-90305` proves convexity under positive carry integration, contraction monotonicity and the matrix-valued Toeplitz compression bound.  The row defect of `L-90304` therefore remains lower order in a complete finite block.

### 3.4 Finite collars

`L-90308` proves in the same fixed odd-Jordan metric that every fixed-child first current is `O(log n)` and every second current is `O(log^2 n)`.  Hence every fixed endpoint/cut collar contributes

\[
O((1+J)^A)
\]

for one fixed `A`.

### 3.5 Moving-filter derivative gauges

They are absent inside the odd-Jordan recurrence.  If the full `s`-current is used for an external consumer, PR #345/PR #346 already type the difference as a finite bare/delayed gauge.  This is not a current-scale source species inside the fixed-filter block identity.

Consequently the complete finite block version of (T-90302.5) has the form

\[
\boxed{
\mathcal E(J+\log4)
\le
\mathcal E(J)
+\frac13\mathcal I(J)
+O((1+J)^A).
}
\tag{T-90302.6}
\]

No hidden matrix-sign, state-dimension, collar, or metric term remains in this statement.

## 4. The positive-innovation gate

Define

> **PIG — Positive Innovation Gate.** There exists a fixed `B<infinity` such that
> \[
> \boxed{
> \mathcal I(J)\ll (1+J)^B
> }
> \tag{T-90302.7}
> \]
> for every sufficiently large logarithmic block.

Then (T-90302.6) gives

\[
\boxed{
\mathcal E(J+\log4)
\le\mathcal E(J)+O((1+J)^{\max(A,B)}).
}
\tag{T-90302.8}
\]

Iteration through `O(J)` fixed delays yields

\[
\boxed{
\mathcal E(J)=O((1+J)^{\max(A,B)+1})=e^{o(J)}.
}
\tag{T-90302.9}
\]

The resident pole-energy consumer therefore gives

\[
\boxed{\mathrm{PIG}\Longrightarrow\mathrm{RH}.}
\tag{T-90302.10}
\]

The same conclusion holds with the zero-safe compact odd-Jordan current of `L-90307` as the pole consumer.

## 5. Why the inertia breakthrough does not prove PIG

`R-90302` is load bearing.  For the zero-bare relative curvature matrix

\[
K(I)=
\begin{pmatrix}
R&EI-T/2\\
EI-T/2&I^2
\end{pmatrix},
\qquad R-E^2>0,
\]

one has

\[
\det K(I)
=(R-E^2)I^2+ETI-T^2/4.
\]

Thus `K(I)` is positive semidefinite for all sufficiently large `|I|`.  Its negative spectral mass can be zero while the innovation is arbitrarily large.

Therefore

```text
small row/block inertia defect
    DOES close the former PSD/synthesis objection;

small row/block inertia defect
    DOES NOT imply PIG.
```

Any proof of PIG must control or transport the **positive** current mass.

## 6. Exact reflected formulation of PIG

For the extra zero-bare source

\[
b_\diamond
=(\varepsilon-\delta_4)
 *(\varepsilon-4\delta_4)*\mu,
\]

PR #345 proves that the two source-convolved individual reflected terms vanish identically on every sufficiently deep balanced block.  The complete reflected identity there reduces to

```text
product-source block
    = 2 * current normal Gram.
```

Thus PIG is equivalently an upper bound for this **positive source-convolved product block** in the common independent-frequency metric.

This is the correct remaining place to attack.  Generalized-prime positivity or the sign of the individual terms cannot finish it, because those individual terms are already zero.

## 7. Firewalls inherited from the Anthropic transcript

A proposed proof of PIG must reject the following shortcuts:

1. pointwise symbol negativity/positivity in place of the true Gram;
2. an ill-conditioned change of metric or mass-matrix orthonormalization;
3. an inertia-only current bound (`R-90302`);
4. source-blind Q4 all-pass contraction (`R-90301`);
5. a third/fourth moment computation without a zero-side polynomial count inequality first;
6. separate absolute-value estimates of product and individual reflected terms before their exact subtraction.

## 8. Honest frontier

Closed, subject to review:

```text
coefficient-one amplitude recurrence                 exact;
common independent-frequency metric                  exact;
all-pass current/predecessor orientation              exact;
negative-mass block lift                              exact;
zero-bare local matrix defect                         lower order;
finite endpoint/cut collars                           polynomial;
source-blind inertia/current shortcut                 refuted;
complete QIDR assembly outside positive innovation    closed.
```

Open / RH-bearing:

```text
PIG: balanced positive innovation energy polynomial;
Riemann Hypothesis.
```

This theorem deliberately does not rename PIG as bookkeeping.  It is the surviving positive-mass theorem.