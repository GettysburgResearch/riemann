# T-26801 — Consolidated factor-five bottom-charge proposal for RH

Claim ID: `T-26801`  
Title: The complete dyadic source reduces RH to one bottom-charge sign, and a factor-five physical transition identity would prove that sign  
Status: **FULL CONDITIONAL RH PROPOSAL — ONE EXPLICIT PHYSICAL TRANSFERENCE IDENTITY OPEN**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Branch: `agent/gpt56-pro-source-specific/262-dyadic-parity-dipole`  
Scope: consolidated handoff for adversarial review; RH is not claimed proved

## 1. Frozen source graph

This consolidation uses the following live heads as mathematical inputs rather
than silently importing mutable branches:

```text
PR #241  3a227e7595e1fe9e38956048297aa97531c80e4e
          independent-frequency reflected physical block

PR #263  73e24368b62f32f31e10691ebbaf3764b544f2a3
          parity-paired Euler source frame and positive Bezout synthesis

PR #268  b67f3ee4e5c20fdd23ad0923641d452c4a89da83
          opposite-parity dipole, digital dual, transport, bottom charge

PR #269  51ce086be09be6849c89aa69e22fcff2665b0c03
          two-contact source, factor-five localization, carry Schur reserve

PR #271  9f5ac31cb975fd95a46eabf5af0b648e7c6bd126
          affine Green boundary lift and monotone-additive dual

PR #274  efec844e014dd716ef7822f1d368ea204e316faf
          zero-tax ordinary-prime transport and prime-tail charge
```

A later repair on one branch does not retroactively verify this frozen packet.

## 2. What is exact before the new hinge

### 2.1 The source

Define

\[
 \omega_2(n)
 =
 \mu(n)
 -\frac32\mathbf 1_{2\mid n}\mu(n/2)
 +\frac12\mathbf 1_{4\mid n}\mu(n/4).
 \tag{T-26801.1}
\]

Its Dirichlet series is

\[
 \boxed{
 \Omega_2(s)
 =
 \frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}.
 }
 \tag{T-26801.2}
\]

The two Euler factors have no zero at a zeta zero in the open critical strip.
The source therefore retains every hypothetical off-line pole of `1/zeta`.
Its four nonzero `2`-adic layers over one odd squarefree core are

\[
 1,-\frac52,2,-\frac12.
 \tag{T-26801.3}
\]

No same-sign Möbius family is deleted; all actual opposite-parity siblings are
retained.

### 2.2 Positive inverse, generalized primes, and digital boundary

The inverse

\[
 A_\omega(s)=\Omega_2(s)^{-1}
 =\frac{\zeta(s)}{(1-2^{-s})(1-2^{-s-1})}
 \tag{T-26801.4}
\]

has coefficients

\[
 \boxed{a_\omega(2^\nu m)=2\nu+2^{-\nu}>0}
 \qquad(m\text{ odd}).
 \tag{T-26801.5}
\]

The generalized von Mangoldt sequence is

\[
 \boxed{
 \Lambda_\omega(q)
 =
 \Lambda(q)+(\log2)(1+2^{-r})\mathbf1_{q=2^r}
 \ge0.
 }
 \tag{T-26801.6}
\]

The generalized Selberg coefficient identity is

\[
 \omega_2*(a_\omega\log^2)
 =\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega.
 \tag{T-26801.7}
\]

With `c_2(n)=1-v_2(n)`, whose partial sums are binary digit sums,

\[
 \boxed{c_2*\omega_2=\varepsilon-\frac52\delta_2+\delta_4.}
 \tag{T-26801.8}
\]

Thus the same infinite source has positive inverse data and a finite digital
boundary, but neither fact alone supplies the required sign.

### 2.3 Exact carry collapse

For

\[
 \beta_{nq}
 =\frac{\lfloor n/q\rfloor[q-1-(n\bmod q)]}{n+1},
 \tag{T-26801.9}
\]

one has

\[
 \boxed{
 \sum_{q=2}^{n}\omega_2(q)\beta_{nq}
 =
 \begin{cases}
 -5/6,&n=2,\\
 -1/2,&n=3,\\
 0,&n\ge4.
 \end{cases}}
 \tag{T-26801.10}
\]

This is literal source cancellation, not bounded rank or a polyhedral line
argument.

For every endpoint `X>=3`, let `c_X` be the unique triangular inverse

\[
 q^{-1/2}\log(X/q)
 =\sum_{n=q}^{X}c_X(n)\beta_{nq}.
 \tag{T-26801.11}
\]

Define

\[
 \mathcal R_\omega(X)
 =\sum_{q=2}^{X}
   \frac{\omega_2(q)}{\sqrt q}\log(X/q).
 \tag{T-26801.12}
\]

Pairing (T-26801.11) with the source gives

\[
 \boxed{
 B_X:=5c_X(2)+3c_X(3)=-6\mathcal R_\omega(X).
 }
 \tag{T-26801.13}
\]

Every carry coefficient above row three disappears from the RH-bearing
consumer.

## 3. The narrow sufficient arithmetic theorem

The preferred finite statement is

> **BCP — Bottom-Charge Positivity.** There is `X_0` such that
> \[
> \boxed{B_X=5c_X(2)+3c_X(3)\ge0}
> \qquad(X\ge X_0).
> \tag{T-26801.14}
> \]

BCP is weaker than full Carry Saturation, positivity of both bottom
coefficients, total Greedy Slack, full Green Energy, Reflected Dyadic Hall, or a
balanced Type-II theorem for all packets.

## 4. BCP implies RH

For `Re z>1/2`, termwise Mellin integration gives

\[
 \boxed{
 \int_1^\infty\mathcal R_\omega(X)X^{-z-1}\,dX
 =
 \frac{
 \dfrac{(1-2^{-z-1/2})(1-2^{-z-3/2})}
       {\zeta(z+1/2)}-1
 }{z^2}.
 }
 \tag{T-26801.15}
\]

Under BCP, `-mathcal R_omega(X)` is eventually nonnegative. After removing the
finite initial interval, Landau's one-sign theorem places the abscissa of
convergence at a singular point on the real axis. The explicit right side has
no singularity for positive real `z`; hence the abscissa is at most zero.

If `rho` were a zero of `zeta` with `Re rho>1/2`, then
`z=rho-1/2` would be a pole in the resulting holomorphic half-plane. Neither
Euler factor in (T-26801.15) can cancel such a zero. Therefore no zero lies to
the right of the critical line. The functional equation excludes zeros to the
left, and

\[
 \boxed{\mathrm{BCP}\Longrightarrow\mathrm{RH}.}
 \tag{T-26801.16}
\]

The review must check the exact version of Landau's theorem, the subtraction of
the finite initial interval, the half-shift, and possible multiple zeros.

## 5. What the factor-five programme now proves

For every scale `m`, PR #269 constructs the pointwise wavelet

\[
 Z_{n,m}(j)=g_m(n)-g_m(j)-g_m(n-j),
 \qquad
 g_m=\mathbf1_{[m,2m)}-\frac12\mathbf1_{[2m,4m)}.
 \tag{T-26801.17}
\]

With `F_n(j)=log binom(n,j)`, its reflected Kummer coupling can be negative only
in

\[
 \boxed{2m\le n<5m.}
 \tag{T-26801.18}
\]

The inner band and every row `n>=5m` have the correct sign by exact elementary
arguments.

On every sufficiently large row, the carry feature has the uniform reserve

\[
 \boxed{
 \min_a\|F_n-aZ_{n,m}\|_2^2
 \ge\frac1{60,000,000}\|F_n\|_2^2.
 }
 \tag{T-26801.19}
\]

The actual generalized-prime profile is the positive synthesis

\[
 \boxed{
 P_n=\sum_{m\le n}a_\omega(m)\log m\,Z_{n,m},
 }
 \tag{T-26801.20}
\]

and differs from ordinary Kummer by a digital correction of relative row energy
`O(log n/n)`. Hence an absolute carry-space Schur reserve survives for the
actual source.

PR #263 adds a parity-paired source frame with an exact positive Bezout
reconstruction of the identity. PR #241 supplies the correct independent-
frequency physical normal block. These are substantial source-side closures.

## 6. The sole missing production theorem

The preceding results live in two different Hilbert spaces:

```text
physical space:
  compact log-prime signals and the independent-frequency normal Gram;

carry space:
  Kummer incidence vectors indexed by binomial positions j.
```

No current file proves that the physical block dominates, equals, or is
boundedly equivalent to the carry Gram. The rank-one dyadic translate matrix by
itself has a null direction and supplies no strict reserve.

The exact remaining theorem is the following fail-closed production statement.

> **F5PBT — Factor-Five Physical Bottom Transference.** For every sufficiently
> large endpoint, insert the complete source `omega_2` and its positive inverse
> into PR #241's independent-frequency physical block before any quotient-cell
> split. Emit the complete quotient cells `2,3,4`, every reflected cross term,
> and the three digital boundary atoms. Prove the exact identity
> \[
> \boxed{
> B_X
> =\mathfrak N_{2,X}+\mathfrak N_{3,X}+\mathfrak N_{4,X}
>  +\mathfrak D_X+\mathfrak O_X,
> }
> \tag{T-26801.21}
> \]
> where each `mathfrak N_(r,X)` is an explicitly emitted positive
> independent-frequency normal Gram, and the digital and outer ledgers satisfy
> \[
> \mathfrak D_X\ge0,
> \qquad
> \mathfrak O_X\ge0.
> \tag{T-26801.22}
> \]
> The construction must expose the finite operator carrying each physical
> source fiber to the carry vectors in (T-26801.17)--(T-26801.20), and prove
> that every remainder is one of the declared boundary terms.

Equation (T-26801.21) is not presently derived. It is the explicit source map
that the generic coefficient-first, Brion, reflected-Hall, and carry-reserve
arguments all lacked.

F5PBT immediately gives BCP and hence RH:

\[
 \boxed{
 \mathrm{F5PBT}\Longrightarrow
 \mathrm{BCP}\Longrightarrow\mathrm{RH}.
 }
 \tag{T-26801.23}
\]

## 7. Why the proposal is reviewable

The proposal has a binary outcome.

### Acceptance

A reviewer reconstructs (T-26801.21) from the complete source manifest and
checks:

1. the physical block is the two-frequency normal Gram, not a diagonal vertical
   integral;
2. all four `2`-adic siblings and all inner/outer cross terms are present;
3. only quotient cells `2,3,4` remain after the factor-five sign theorem;
4. the positive inverse synthesis is used before norms;
5. the carry-to-physical operator is written explicitly and has the asserted
   orientation;
6. every endpoint term maps to the three digital atoms or the certified outer
   reserve;
7. the resulting left side is exactly `5c_X(2)+3c_X(3)`.

### Rejection

Any one of the following rejects F5PBT:

- a missing source sibling or cross term;
- a carry Gram asserted equal to the physical Gram without an intertwiner;
- a negative transition remainder;
- a quotient row outside `2,3,4` whose sign is not covered by the factor-five
  theorem;
- an endpoint term absent from the digital ledger;
- a scalar multiple or half-shift mismatch in (T-26801.21);
- use of finite numerical positivity in place of the symbolic identity.

## 8. Exact status table

```text
opposite-parity source and Euler factors       PROPOSED EXACT / replayed
positive inverse and generalized primes         PROPOSED EXACT / replayed
digital three-atom boundary                     PROPOSED EXACT / replayed
compact carry image and bottom charge            PROPOSED EXACT / replayed
BCP -> RH by Mellin/Landau                       COMPLETE CONDITIONAL CHAIN
factor-five Kummer sign localization             PROPOSED COMPLETE
uniform carry Schur reserve                      PROPOSED COMPLETE
positive synthesis of actual prime profile       PROPOSED COMPLETE
parity-paired physical source frame              PROPOSED EXACT
physical-to-carry transition identity F5PBT       OPEN / RH-BEARING
Bottom-Charge Positivity                         OPEN
Riemann Hypothesis                               UNPROVED
```

This is a full, unmistakable proposal for review. It is not an unconditional
proof until (T-26801.21) is derived and independently verified.
