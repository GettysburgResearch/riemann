# T-90301 — Inertia-tolerant Q4 recurrence as a full RH proposal

Claim ID: `T-90301`  
Title: The corrected two-state Q4 reflected programme does not need polarized PSD; the zero-bare relative source has an unconditionally subcritical bad eigenvalue, leaving only the complete block/delayed-state composition  
Status: **FULL CONDITIONAL PROPOSAL — ROW-LEVEL INERTIA DEFECT CLOSED COFINALLY; GLOBAL BLOCK RECURRENCE OPEN / RH-BEARING**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Updated: 2026-08-10 after `L-90304`  
Dependencies: `L-90301`–`L-90304`, `R-90301`; PRs #341, #342, #345, #346, #350; resident vector-valued pole-energy consumer  
Scope: corrected Q4/Jordan route only

## 1. Source-complete two-state principle

For a twice differentiable two-state path `V`, put

\[
K_V=V'V'^*-rac12(VV''^*+V''V^*),
\qquad
\delta(V)=\operatorname{tr}(K_V)_-.
\tag{T-90301.1}
\]

`L-90301` proves that every parameter-independent synthesis with `W^*W<=qI` obeys

\[
\boxed{
\mathcal C(WV)
\le q\,[\mathcal C(V)+\delta(V)].
}
\tag{T-90301.2}
\]

Thus full polarized PSD is sufficient but not necessary.

For a two-state matrix with positive trace,

\[
\boxed{
\delta(V)\le\frac{(-\det K_V)_+}{\operatorname{tr}K_V}.
}
\tag{T-90301.3}
\]

`L-90302/L-90303` reduce the determinant to one source/current Wronskian and then to one square-versus-reserve scalar for the relative Q4 path.

## 2. Zero-bare relative source closes the row-level inertia defect

The decisive extra source difference is

\[
b_\diamond
=(\varepsilon-\delta_4)
 *(\varepsilon-4\delta_4)*\mu.
\tag{T-90301.4}
\]

Its divisor prefix is

\[
\varepsilon-5\delta_4+4\delta_{16},
\]

so its bare field is exactly zero on every sufficiently deep balanced row.

`L-90304` couples this source leg to the compact-source relative Jordan coordinate.  Its jets are

\[
\boxed{
V(0)=(1,0),
\qquad
V'(0)=(E,I),
\qquad
V''(0)=(E^2-R,T),
}
\tag{T-90301.5}
\]

where

```text
R = compact-source radix-four reserve increment = Theta_eta(n log n);
E = O_eta(log n);
I = the genuine RH-sensitive compact current innovation;
T = O(n) by an exact filtered Selberg identity.
```

Therefore

\[
K=
\begin{pmatrix}
R&EI-T/2\\
EI-T/2&I^2
\end{pmatrix},
\qquad
\operatorname{tr}K=R+I^2>0.
\tag{T-90301.6}
\]

Completing the determinant defect in the unknown current gives the **current-independent** estimate

\[
\boxed{
\delta(K)
\le\frac{T^2}{4(R-E^2)}
=O_\eta\!\left(\frac n{\log n}\right).
}
\tag{T-90301.7}
\]

After critical physical normalization this is only `O_eta(1/log n)`.

Thus the former statement

```text
prove the complete polarized arithmetic 2x2 matrix PSD
```

is no longer the RH-bearing row theorem.  The matrix may be indefinite; its entire bad direction is already proved lower-order on the source which carries the hard compact innovation.

## 3. The remaining production theorem — Q4 Inertia-Defect Recurrence (QIDR)

What remains is a block/global composition theorem, not a new RH-scale current estimate.

> **QIDR.** Assemble the exact independent-frequency source-convolved block using the zero-bare relative source, the corrected Q2/Q4 finite state, and the resident terminal all-pass state.  Prove that for all sufficiently large logarithmic blocks `J`,
> \[
> \boxed{
> \mathcal E(J)
> \le
> \mathcal E(J-\delta_0)
> +C(1+J)^A,
> }
> \tag{T-90301.8}
> \]
> for fixed `delta0>0,A<infinity`, after charging the rowwise negative spectral mass from (T-90301.7), the fixed finite collars, and every strictly delayed gauge exactly once.

The source order is mandatory: the extra `(epsilon-delta_4)` difference must be formed before the reflected individual terms are separated.  On deep balanced blocks the bare field is then exactly zero, so those individual reflected terms vanish at that source scope.

The exact Q2/Q4 state identities on PR #350 supply the finite delayed-state dictionary.  `R-90301` prevents using the all-pass factor as a source-blind contraction: it is J-unitary on functional-equation off-line pairs.

## 4. QIDR implies RH

Iterating (T-90301.8) through `O(J)` fixed delays gives

\[
\mathcal E(J)=O((1+J)^{A+1})=e^{o(J)}.
\tag{T-90301.9}
\]

The resident vector-valued pole criterion for the compact/Q4 physical current then excludes every zeta zero with real part greater than one half. Functional-equation symmetry gives

\[
\boxed{\mathrm{QIDR}\Longrightarrow\mathrm{RH}.}
\tag{T-90301.10}
\]

## 5. Why the Claude import materially changes the frontier

Before this branch, the safe route required the full matrix sign `K>=0`; scalar curvature positivity was correctly known to be insufficient.

The Claude-style proof-order principle says to retain the indefinite direction and pay only the spectral quantity the consumer sees.  In the present two-state source this does more than rename the problem:

1. `L-90301` reduces synthesis to negative spectral mass;
2. `L-90302/L-90303` reduce that mass to one determinant/Wronskian scalar;
3. `L-90304` chooses the zero-bare source and proves the bad eigenvalue `O(n/log n)` **without any estimate of the unknown current**.

That removes a previously RH-strength-looking local matrix theorem.

## 6. Coefficient-charge firewall

PR #346 also contains a finite Bézout synthesis whose coefficient-energy charge is `<2/5` of a parity-frame reserve.  That number is **not** automatically the operator constant `q` in (T-90301.2): convolution/filter cross terms must be retained.  The exact jet-frame theorem on the same branch gives an operator-level `1/2` current/bare inequality, but the present proof does not multiply unrelated constants to manufacture a recurrence.

QIDR must use one declared Hilbert/block metric throughout.

## 7. Exact status

```text
Claude-style inertia synthesis inequality               PROPOSED COMPLETE EXACT
two-state Wronskian/determinant reduction               PROPOSED COMPLETE EXACT
relative Q4 square-vs-reserve identity                  PROPOSED COMPLETE EXACT
zero-bare source field                                  IMPORTED / PROPOSED COMPLETE EXACT
zero-bare second-current T=O(n)                         PROPOSED COMPLETE
row bad eigenvalue delta=O(n/log n)                     PROPOSED COMPLETE COFINAL
source-blind all-pass/inertia shortcut                  REFUTED EXACTLY
full polarized PSD as required local theorem            SUPERSEDED / TOO STRONG
independent-frequency block + delayed-state composition OPEN / RH-BEARING
QIDR -> polynomial energy -> RH                         COMPLETE CONDITIONAL
Riemann Hypothesis                                      UNPROVEN
```

No reviewer is asked to invent the row-level matrix estimate; it is supplied in `L-90304`.  The remaining review/production target is the complete block composition with one consistent operator metric.