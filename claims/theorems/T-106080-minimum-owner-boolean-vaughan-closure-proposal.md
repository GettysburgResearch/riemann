# T-106080 — Minimum-owner Boolean Vaughan closure proposal

Claim ID: `T-106080`  
Programme aliases: `LFAM1.MINIMUM_OWNER_CLOSURE`, `STRESS.ALL_BLOCK_LONG_CORE`, `LFAM2.BOOLEAN_KUMMER_COMPLETION`  
Status: **FULL SOURCE-COMPLETE PROOF PROPOSAL; HOSTILE REVIEW REQUIRED**  
Created: 2026-08-25  
Depends on: `L-106080--L-106082`; parent PR #719 through `L-102880`, `L-102882--L-102883`, `L-102887--L-102888`; fixed Mellin consumer  
Programme issues: #743, #736, #737  
RH status: **CLAIMED BY THE COMPOSITION BELOW; NOT YET EXTERNALLY VALIDATED OR CANONICALLY ACCEPTED**

The corrected frontier `HQORO106071` arose in one particular scale-matched
auxiliary-character coordinate.  `L-106080--L-106082` propose to bypass its
high-owner-crowding cells by changing the source gauge before that quadratic
residue collapse occurs.

## 1. Literal squarefree Vaughan coordinate

The completed owner source is supported on

\[
N=P a^2,
\qquad \mu^2(a)=1.
\]

Boolean disjoint-support convolution gives the exact Vaughan identity

\[
\mu_{\rm sf}
=2\mu_U
-\mu_U\star\mu_U\star\mathbf1_{\rm sf}
+a_U\star a_U\star\mu_{\rm sf}.
\]

Its Type-I row remains power-saving under the zero-moment derivative kernel,
while every balanced atom has at least two distinct core-prime labels.

This removes the nonsquarefree representation artifacts which prevented a
source-level comparison between selected owner primes and the actual core.

## 2. Minimum-owner gauge

On each dyadic horizon choose:

```text
unique label >4 sqrt(Y), if present, plus the smallest other label;
otherwise the two smallest labels.
```

This is a valid horizon-safe owner rule.  Let `lambda` be its smaller owner.
Every balanced squarefree core `a` then satisfies

\[
\boxed{\lambda^2\le a.}
\]

After the linear dyadic projection

\[
B\le a<2B,
\qquad L\le\lambda<2L,
\]

one has

\[
\boxed{L^2<2B.}
\]

## 3. Complete coherent phase packing

For two clean source atoms, the two distinguished owner primes supply the
same-occurrence nonzero Ramanujan phases already used in the parent
owner-dispersion packet.  The same-family centered kernel identity of
`L-106082` extends the coherent theorem `L-102883` after deleting the inherited
shared-owner renewal.

The parent bound is

\[
\mathcal E_{B,L}
\ll
\frac{X^{o(1)}}Q
\left[
1+rac{L^2}{B\log^2(2L)}
\right].
\]

Since `L^2<2B`, every block is subpower.  Cauchy over only the linear
polylogarithmic block partition yields

\[
\boxed{
\int_X^{2X}|\mathcal B_{\rm sf}(t)|^2\frac{dt}{t}
=X^{o(1)}.
}
\tag{T-106080.1}
\]

Thus the balanced derivative row has subpower logarithmic negative mass.

## 4. Detector composition

The Boolean Type-I row is power-small by `L-106080`; the terminal, repeated
label, shared-owner, owner/core-overlap and equal-product rows are inherited
closed.  Therefore (T-106080.1) gives

\[
\int_1^Y(H_K(X))_-\frac{dX}{X}=Y^{o(1)}.
\tag{T-106080.2}
\]

Parent `L-102880` gives the positive Volterra transport

\[
H_R(X)=\int_1^XH_K(t)\frac{dt}{t},
\]

and the frozen Mellin--Landau consumer retains every hypothetical
reciprocal-zeta pole in the open right half-plane.  Hence the proposed chain is

\[
\boxed{
\begin{aligned}
&\text{Boolean squarefree Vaughan}
\ \wedge\ 
\text{minimum-owner gauge}
\ \wedge\ 
\text{coherent centered phase packing}\\
&\qquad\Longrightarrow
\int_1^Y(H_K)_-\frac{dX}{X}=Y^{o(1)}
\Longrightarrow
\mathrm{RH}.
\end{aligned}}
\tag{T-106080.3}
\]

## 5. Relation to the corrected residue frontier

This proposal does not claim to prove `HQORO106071` in its original arbitrary
owner gauge.  It claims that the high-crowding cells are avoidable source
artifacts:

```text
arbitrary horizon-safe pair:
  short-core/high-owner residue cells may survive;

minimum-owner Boolean gauge:
  every balanced source atom is automatically long-core;
  the already-proved coherent phase theorem applies before residue collapse.
```

If accepted, `T-106080` supersedes `HQORO106071` as the conclusion-facing
coordinate.  If rejected, the reviewer must identify the first failed source
or normalization interface in `L-106080--L-106082`.

## Exact claim boundary

```text
Boolean squarefree Vaughan identity                 PROVED EXACT
balanced support has two distinct core primes       PROVED EXACT
squarefree zero-moment lattice estimate             PROVED POWER-SAVING
minimum-owner horizon gauge                         PROVED EXACT
distinguished owner square <= core                  PROVED EXACT
same-family centered kernel identity                PROVED EXACT
all blocks satisfy long-core inequality             PROVED EXACT
transport of parent coherent phase allocation       PROPOSED COMPLETE / REVIEW REQUIRED
Boolean Type-I global source transport              PROPOSED COMPLETE / REVIEW REQUIRED
full detector composition                           CLAIMED PROOF PROPOSAL
external hostile review                             REQUIRED
canonical RH acceptance                             NOT GRANTED
```

The PR remains draft.  No canonical README, claim registry or `main` status is
changed by this proposal.