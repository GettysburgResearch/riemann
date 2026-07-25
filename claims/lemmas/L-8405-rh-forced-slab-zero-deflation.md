# L-8405 — Total critical-strip zero counts suffice for RH-conditional deflation

Claim ID: L-8405  
Title: A certified horizontal-slab zero count becomes line-zero mass under the RH assumption  
Status: PROPOSED  
Authoring agent: `gpt56-06-e`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: L-8401–L-8403; definition of RH; certified nontrivial-zero counts  
Scope: argument-principle, Turing, and global zero-count inputs for deflation  
Related counterexample candidates: none

## Statement

Let

\[
 I_r=[a_r,b_r],\qquad r=1,\ldots,R,
\]

be pairwise disjoint positive-ordinate intervals whose horizontal boundary lines
contain no nontrivial zero of `xi`. Suppose a rigorous argument-principle,
Turing, or other zero-count certificate proves that at least `m_r>=1`
nontrivial zeros

\[
 \rho=\beta+i\gamma,
 \qquad 0<\beta<1,
\]

counted with multiplicity, have ordinates `gamma in I_r`. The certificate need
not prove that any of these zeros lies on the critical line.

Then every scalar, fixed-vector, and matrix deflation conclusion of
L-8401–L-8403 remains valid with these `m_r`.

Explicitly, if

\[
 s=\frac12+x+iT,
 \qquad x>0,
\]

and `D_r=max(|T-a_r|,|T-b_r|)`, then RH implies

\[
 \boxed{
 \operatorname{Re}\frac{\xi'}{\xi}(s)
 -\sum_r m_r\frac{x}{x^2+D_r^2}\ge0.
 }
 \tag{1}
\]

Likewise, for the Pick transfer function `Phi_v` of L-8402 and any checked
`L_r<=inf_{gamma in I_r}|Phi_v(gamma)|^2`, RH implies

\[
 \boxed{
 v^*Kv-\sum_rm_rL_r\ge0.
 }
 \tag{2}
\]

The whole-matrix lower blocks of L-8403 also apply with multiplicities `m_r`.

## Proof

Assume RH. Every nontrivial zero counted by the unconditional slab certificate
then has real part exactly `1/2`. Its ordinate remains in the same certified
interval `I_r`. Therefore the slab certificate becomes, under the RH assumption,
a lower count of at least `m_r` critical-line zeros in `I_r`.

All hypotheses needed by L-8401, L-8402, and L-8403 are now satisfied, so their
conclusions follow. A negative deflated residual contradicts the RH assumption.
∎

## Important logical direction

The zero-count certificate is unconditional; only the conversion

```text
nontrivial zero in the slab
        + RH assumption
        -> critical-line zero in the same ordinate bin
```

is conditional. This is exactly the direction required for a proof by
contradiction.

No circular verification of RH is used. If the counted slab already contains an
off-line zero, RH is false; if RH is assumed, the same count supplies the
positive line mass that may be deflated.

## Consequence for production

Line-root isolation is optional. Suitable count inputs include:

1. an exact difference `N(b)-N(a)` with zero-free endpoints;
2. a Turing-method certificate for all nontrivial zeros in an ordinate window;
3. an argument-principle count in a rectangle covering the full critical strip
   between heights `a` and `b`;
4. a lower count from several disjoint smaller rectangles whose union lies in the
   same ordinate bin.

Exact total counts are especially valuable because even-multiplicity line zeros
and zeros missed by Hardy-Z sign changes still contribute to the subtraction.

## Analytic domain audit

- Counts refer only to nontrivial zeros in `0<Re(s)<1`.
- Positive ordinate bins exclude the real trivial zeros and the pole of zeta.
- Horizontal endpoint lines must be proved zero-free or assigned by an explicit
  half-open convention.
- Symmetric conjugate zeros at negative ordinates are not double counted in a
  positive-ordinate bin.
- No statement is made about the real parts of counted zeros without assuming
  RH.

## Dependency audit

- The definition of RH moves every counted nontrivial zero to the critical line.
- L-8401–L-8403 convert the resulting line-zero lower counts into scalar, vector,
  and matrix subtraction bounds.
- The chosen argument-principle or Turing certificate retains its own contour,
  branch, endpoint, and completeness audit.

## Gap audit

- Counting zeros only in a narrow real-part rectangle that does not cover the
  full critical strip may miss RH-compatible line zeros unless the rectangle
  contains the line; a lower count remains sound, but a claimed exact slab count
  requires full coverage.
- A numerical value of the Riemann-von Mangoldt main term is not an exact count.
- Endpoint zeros can cause off-by-one errors and must be excluded or allocated.
- Trivial zeros, poles, and zeros of an auxiliary completed function must be
  reconciled exactly.
- The theorem does not make a finite negative search into a proof of RH when no
  violation is found.

## Adversarial tests

1. Use a synthetic slab containing one off-line reflected pair and verify that,
   under the RH branch of the implication, the count is treated as line mass.
2. Put a zero on a horizontal endpoint and require the count certificate to fail
   or adopt a declared half-open convention.
3. Count a trivial zero and require rejection by the nontrivial-strip gate.
4. Compare a Hardy-Z one-zero bin with an argument-principle one-zero slab and
   require identical deflation arithmetic.
5. Deliberately omit one side of the critical strip from an alleged exact count
   and require the completeness audit to reject it.

## Remaining uncertainty

The mathematical reduction is immediate but strategically important. The
practical question is which certified local count primitive is cheapest at the
active heights: short Turing blocks, argument-principle rectangles, or direct
Hardy-Z sign changes.

## Suggested next attack

Extend the Issue #39 Riemann-Siegel backend to emit exact local zero-count
certificates `N(T+h)-N(T-h)` around every passivity nominee. Feed those counts
straight into X-8401. Use Hardy-Z brackets only when a narrower ordinate bin is
needed to improve the lower Poisson/Gram contribution.
