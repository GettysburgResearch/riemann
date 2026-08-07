# T-26201 — Dyadic parity-dipole and reflected Hall proposal for RH

Claim ID: `T-26201`  
Title: A source-specific reflected Hall inequality for the dyadic opposite-parity Möbius source yields a positive carry certificate and proves RH  
Status: **FULL PROPOSAL PENDING ADVERSARIAL REVIEW — THE REFLECTED DYADIC HALL IDENTITY IS OPEN**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Corrected: 2026-08-08 before PR handoff  
Source heads inspected: PR #257 `2f508a77a21593c7a8bc852a61e8b19c63367f8b`; PR #254 `be8405e06bc6c845267727b7347ea91f3593e16b`; PR #248 `45d327082422021955be81f1a49fde7b646ce1cb`; PR #244 `c81883549aa15ab16a77b19168647d0d39787f21`; PR #241 `3a227e7595e1fe9e38956048297aa97531c80e4e`; PR #236 `f1d51ae13da93a325349229a3701ae9f5f2f348d`  
New dependencies: `L-26201`--`L-26203`  
Scope: one source-specific arithmetic proposal replacing universal bounded-rank and automatic-line mechanisms

## 1. Corrected live boundary

The repository now rules out the following as general closing principles:

- absolute bounded rank of every balanced Möbius resonance;
- automatic cancellation of every positive-dimensional Brion cone;
- terminal-only endpoint counting;
- scalar reflected Selberg positivity substituted for a localized normal Gram;
- monotone deletion of the positive carry defect;
- a generic convolution inverse for the parity comb.

The durable exact inputs are instead:

1. the fixed-ratio Mertens shell and its RH-equivalent block energy;
2. the exact finite inverse-zeta/Heath--Brown packet;
3. high-order Euler closure of every complete macroscopic lattice variable;
4. the corrected two-frequency reflected local block of PR #241;
5. the parabolic carry seed and its exact objective;
6. exact signed carry correction and Green identities;
7. the binary-digit/parity source of PR #236.

The proposal below uses all seven but adds no universal geometric claim.

## 2. One source shared by the arithmetic routes

Define

\[
 \omega_2(n)
 =
 \mu(n)
 -\frac32{\bf1}_{2\mid n}\mu(n/2)
 +\frac12{\bf1}_{4\mid n}\mu(n/4).
\tag{T-26201.1}
\]

`L-26201` and `L-26202` prove three exact identities for the same source.

### Carry dipole

\[
 \sum_{k\le n/m}\omega_2(k)\beta_{n,mk}
 =
 \begin{cases}
  \dfrac{2m-n-1}{n+1},
       &m\le n<2m,\\[2mm]
  \dfrac{n+1-8m}{2(n+1)},
       &2m\le n<4m,\\[2mm]
  0,&\text{otherwise}.
 \end{cases}
\tag{T-26201.2}
\]

### Digital collapse

\[
 c_2*\omega_2
 =
 \varepsilon-\frac52\delta_2+\delta_4,
 \qquad
 c_2(n)=1-v_2(n),
\tag{T-26201.3}
\]

with nonnegative partial sums

\[
 \sum_{n\le N}c_2(n)=s_2(N).
\tag{T-26201.4}
\]

### Positive Selberg data

The inverse coefficients

\[
 a_2^\star(2^\nu m)=2\nu+2^{-\nu}
 \qquad(m\ {\rm odd})
\tag{T-26201.5}
\]

and generalized prime weights

\[
 \Lambda_2^\star(2^k)
 =(2+2^{-k})\log2,
 \qquad
 \Lambda_2^\star(p^k)=\log p\ (p\ {\rm odd})
\tag{T-26201.6}
\]

are positive.

This is the proposed replacement for generic geometry:

\[
 \boxed{
 \text{same-sign odd Möbius family}
 \;+\;
 \text{its three actual opposite-parity siblings}.}
\tag{T-26201.7}
\]

No family is set to zero merely because its tuple polytope contains a line.

## 3. Prime-only carry front door

Let `b_X^(0)` be the parabolic seed.  The exact carry reduction gives

\[
 b_X^{(0)}(m)\ge0
\tag{T-26201.8}
\]

and

\[
 J_{\mathbb P,X}(b_X^{(0)})
 \ge4\sqrt X-O(\log^2X).
\tag{T-26201.9}
\]

Higher prime powers contribute only `O(log^2 X)`, so it is enough to repair the
ordinary-prime constraints

\[
 v_p(b)
 \le p^{-1/2}\log(X/p).
\tag{T-26201.10}
\]

Put

\[
 d_X(p)=v_p(b_X^{(0)})-p^{-1/2}\log(X/p),
\]

and split the prime rows into positive defects `mathcal P_X^+` and negative
slack `mathcal P_X^-`.  Both von-Mangoldt weighted ledgers are of square-root
size, while their signed difference is the prime-ramp scalar.  Deleting the
positive part loses the sharp constant; signed transport is mandatory.

## 4. Exact primal completion

`L-26203` proves the following finite theorem.

Suppose there are nonnegative blocks

\[
 (A_\ell,B_\ell,t_\ell),
 \qquad
 1\le A_\ell<B_\ell\le X,
\tag{T-26201.11}
\]

such that every prime factor of `A_ell` lies in `mathcal P_X^+`, every prime
factor of `B_ell` lies in `mathcal P_X^-`, and

\[
 \sum_{\ell:p\mid A_\ell}t_\ell
 \ge d_X^+(p)
 \qquad(p\in\mathcal P_X^+),
\tag{T-26201.12}
\]

\[
 \sum_{\ell:p\mid B_\ell}t_\ell
 \le d_X^-(p)
 \qquad(p\in\mathcal P_X^-).
\tag{T-26201.13}
\]

Then

\[
 b_X^\star(m)
 =
 b_X^{(0)}(m)
 +\sum_\ell t_\ell{\bf1}_{A_\ell<m\le B_\ell}
\tag{T-26201.14}
\]

is nonnegative and feasible, while

\[
 J_{\mathbb P,X}(b_X^\star)
 \ge J_{\mathbb P,X}(b_X^{(0)}).
\tag{T-26201.15}
\]

It follows that

\[
 \sum_{p\le X}\frac{\log p}{\sqrt p}\log(X/p)
 \ge4\sqrt X-O(\log^2X),
\tag{T-26201.16}
\]

and the square-screw/Landau theorem gives RH.

Thus the full problem is reduced to an exact finite bipartite transport
statement, not to pointwise Carry Saturation.

## 5. Reflected Dyadic Hall theorem

Fix the source-licensed block grammar generated from complete copies of
`omega_2`, including every opposite-parity sibling and every reflected cross
term.

Finite Farkas duality gives the exact alternative.  Failure of the bipartite
transport certificate produces nonnegative weights

\[
 \alpha_p\ge0
 \quad(p\in\mathcal P_X^+),
 \qquad
 \beta_p\ge0
 \quad(p\in\mathcal P_X^-)
\tag{T-26201.17}
\]

satisfying every licensed block inequality

\[
 \sum_{p\mid A}\alpha_p
 \le
 \sum_{p\mid B}\beta_p,
\tag{T-26201.18}
\]

but

\[
 \sum_{p\in\mathcal P_X^+}d_X^+(p)\alpha_p
 >
 \sum_{p\in\mathcal P_X^-}d_X^-(p)\beta_p.
\tag{T-26201.19}
\]

The load-bearing proposed theorem is:

> **RDH — Reflected Dyadic Hall.**  
> For the actual parabolic residual and the complete source-licensed block
> grammar, every nonnegative pair `(alpha,beta)` satisfying
> (T-26201.18) obeys
> \[
>  \boxed{
>  \sum_{p\in\mathcal P_X^+}d_X^+(p)\alpha_p
>  \le
>  \sum_{p\in\mathcal P_X^-}d_X^-(p)\beta_p.}
> \tag{T-26201.20}
> \]

RDH implies the exact transport certificate by Farkas and hence RH by
Section 4.

The proposal does **not** assert RDH as a generic Hall theorem.  It proposes
the source identity in Sections 6--8 as its proof.

## 6. Two-frequency reflected source map

Use the independent frequencies `t,s` and the physical block kernel

\[
 \Phi_{J,\alpha}(t-s)
\]

of PR #241 `L-9518`.  Insert `A_2^star`, `omega_2`, and
`Lambda_2^star` before decomposing any parity or carry band.

For a Hall witness `(alpha,beta)`, the licensed block inequalities define one
finite source vector

\[
 \mathcal V_{X,\alpha,\beta}
 =
 \mathcal V_{\rm in}
 -
 \mathcal V_{\rm out},
\tag{T-26201.21}
\]

where the inner component is supported on the positive carry band `[m,2m)`
and the outer component on `[2m,4m)`, with the exact weights in
(T-26201.2).

The corrected reflected identity yields the nonnegative normal Gram

\[
 \boxed{
 \mathfrak R_X(\alpha,\beta)
 =
 \int_J^{J+1}
 \left|
  Q_{\mathcal V_{\rm in}}(x)
  -
  Q_{\mathcal V_{\rm out}}(x)
 \right|^2dx
 \ge0.}
\tag{T-26201.22}
\]

Every cross term is retained.  This is where the old scalar reflected proposal
and the old line-cone proposal were insufficient.

Equation (T-26201.22) is an interface, not yet a derivation of the Hall
contraction.

## 7. Digital boundary closure

Convolve the same source with the binary-digit dual.  Equation
(T-26201.3) replaces the full parity family by the three boundary atoms

\[
 1,\quad 2,\quad4.
\tag{T-26201.23}
\]

The proposed source calculation uses Abel summation against the nonnegative
binary digit sums to convert all non-Hermitian endpoint terms in the Hall
contraction into a finite boundary ledger

\[
 \mathfrak D_X(\alpha,\beta)\ge0.
\tag{T-26201.24}
\]

All quotient-layer interiors have already been consumed by the compact carry
dipole; no universal line cancellation is invoked.

The sign in (T-26201.24) is part of the open symbolic identity and must be
checked atom by atom.

## 8. Proposed exact reserve identity

The source-specific closing identity to be reconstructed is

\[
 \boxed{
 \sum_{p\in\mathcal P_X^-}d_X^-(p)\beta_p
 -
 \sum_{p\in\mathcal P_X^+}d_X^+(p)\alpha_p
 =
 \mathfrak R_X(\alpha,\beta)
 +\mathfrak D_X(\alpha,\beta)
 +\mathfrak O_X(\alpha,\beta).}
\tag{T-26201.25}
\]

Here

- `mathfrak R_X` is the two-frequency reflected normal Gram;
- `mathfrak D_X` is the finite digital boundary ledger;
- `mathfrak O_X` is only the explicitly signed outer parabolic reserve on the
  ordinary-prime rows.

The higher-prime-power `O(log^2 X)` comparison is handled before this identity
and is not hidden inside `mathfrak O_X`.

The proposal requires an explicit formula and proof of

\[
 \mathfrak O_X(\alpha,\beta)\ge0.
\tag{T-26201.26}
\]

Equations (T-26201.22), (T-26201.24), and (T-26201.26) would imply RDH.

This is the sole new source-specific hinge.  It is deliberately stronger than
an inequality inferred from a generic operator norm and narrower than BTP for
all packets.

## 9. Why this mechanism can evade the exact obstructions

### Same-sign Möbius hypercubes

They survive in `mathcal V_in`.  Their actual `2`-adic siblings occur in
`mathcal V_out` with coefficients `-5/2,2,-1/2`.  Cancellation is checked in
the reflected Gram, not inferred from tuple rank.

### Nonvertex line-cone obstruction

No line is declared zero.  The affine bulk disappears only through the exact
identity (T-26201.2).

### Scalar Selberg versus local block

The consumer is the two-frequency block (T-26201.22), not the global diagonal
integral.

### Carry positivity

The primal correction consists only of positive blocks, so coefficient
nonnegativity is automatic.  Slack capacities are enforced separately from
defect coverage.

### Mertens firewall

`omega_2` differs from the dyadic shell by a stable invertible filter.  Any
subexponential conclusion still carries the full fixed-ratio Mertens exponent.

## 10. Full proposed proof chain

\[
\begin{aligned}
&\text{parabolic carry seed}\\
&\to\text{prime-only defect/slack bipartition}\\
&\to\text{exact dyadic opposite-parity source}\\
&\to\text{compact inner/outer carry contraction}\\
&\to\text{two-frequency reflected normal Gram}\\
&\to\text{binary-digit finite boundary ledger}\\
&\to\text{Reflected Dyadic Hall identity}\\
&\to\text{positive multiplicative defect-to-slack blocks}\\
&\to\text{feasible nonnegative carry certificate}\\
&\to 4\sqrt X-O(\log^2X)\text{ prime ramp}\\
&\to\text{square-screw/Landau}\\
&\to\boxed{\mathrm{RH}}.
\end{aligned}
\tag{T-26201.27}
\]

## 11. Binary review outcome

Reject the proposal upon finding any one of:

1. a missing `2`-adic sibling of `omega_2`;
2. failure of the compact dipole formula;
3. a Hall block not represented in the reflected source map;
4. a reflected cross term estimated separately or omitted;
5. a digital endpoint term with negative undeclared residue;
6. a same-sign Möbius cube appearing without its opposite-parity family;
7. a prime assigned to the wrong side of the defect/slack bipartition;
8. an endpoint or outer-prime term hidden in `mathfrak O_X`;
9. a failure of the exact transport implication.

Acceptance requires an emitted symbolic identity (T-26201.25), not merely
successful finite LPs.

## 12. Status boundary

```text
dyadic source and compact carry dipole       PROPOSED EXACT
positive inverse and digital dual            PROPOSED EXACT
bipartite multiplicative transport theorem   PROPOSED EXACT
transport certificate -> RH                  PROPOSED COMPLETE COMPOSITION
two-frequency source map                     PROPOSED INTERFACE
reflected dyadic Hall identity                OPEN / RH-BEARING HINGE
Riemann Hypothesis                            UNPROVED
```

This proposal treats coefficient-first and Brion localization as lessons:
recombine before estimating, but demand an actual source identity rather than
a universal rank or automatic line theorem.
