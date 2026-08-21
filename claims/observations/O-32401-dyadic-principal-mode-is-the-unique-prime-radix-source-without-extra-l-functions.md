# O-32401 — Dyadic principal-mode synthesis after the radix and contraction firewalls

Claim ID: `O-32401`  
Title: Radix two is the unique prime-radix renewal that introduces no nonprincipal Dirichlet-L modes, and the live dyadic source package reduces the remaining RH attack to one source-coupled lower-scale Schur descent  
Status: **EXACT CROSS-ROUTE SYNTHESIS + ONE NEW PRODUCTION TARGET; NO RH CLAIM**  
Author: `gpt56-sol`  
Date: 2026-08-08

## 1. Scope correction from prime-radix characters

PR #323 proves that a prime-radix residue decomposition at `p` diagonalizes into Dirichlet-character modes modulo `p`.  For `p=5` the four nonzero residue states contain the principal zeta channel plus three nonprincipal Dirichlet-L channels.  A source-free contraction of the complete residue state would therefore prove more than the zeta RH unless those modes are retained separately.

For `p=2`, the unit group `(Z/2Z)^*` is trivial.  There is no nonprincipal character mode.  Thus radix two is the unique prime radix for which a complete residue renewal does not enlarge the spectral problem beyond the principal zeta channel.

This does **not** prove a dyadic contraction.  It identifies the only prime-radix state space on which such a theorem has the correct spectral scope.

## 2. The exact RH-sensitive dyadic source

Retain the opposite-parity source

\[
\omega_2(n)
=\mu(n)-{3\over2}{\bf1}_{2\mid n}\mu(n/2)
 +{1\over2}{\bf1}_{4\mid n}\mu(n/4),
\]

with transform

\[
\Omega_2(s)
={(1-2^{-s})(1-2^{-s-1})\over\zeta(s)}.
\]

The finite Euler numerator has no zero in the counterexample half-strip, so every hypothetical off-line zeta zero remains an uncancelled pole.

The same source has three exact faces already present in the repository.

### Carry face

Its Möbius-adjoint carry image is the compact dipole

\[
\Gamma_2(n,m)=0\quad(n<m),
\]

\[
\Gamma_2(n,m)={2m-n-1\over n+1}\quad(m\le n<2m),
\]

\[
\Gamma_2(n,m)={n+1-8m\over2(n+1)}\quad(2m\le n<4m),
\]

and vanishes identically for `n>=4m`.

### Digital face

For `c_2(n)=1-v_2(n)`, whose partial sums are binary digit sums,

\[
c_2*\omega_2
=\varepsilon-{5\over2}\delta_2+\delta_4.
\]

Thus the complete infinite arithmetic source collapses to one three-tap boundary after convolution by a positive cumulative digital kernel.

### Selberg face

The inverse coefficients

\[
a_\omega(2^\nu m)=2\nu+2^{-\nu}\qquad(m\ {m odd})
\]

are strictly positive, and the generalized von Mangoldt sequence is nonnegative.  Hence the exact generalized Selberg forcing

\[
\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega
\]

is coefficientwise nonnegative.

## 3. The physical/carry source map is already exact

PR #268 `L-26802` gives an exact weighted isometry from an annular physical source to the additive carry split field.  It applies to arbitrary annular coefficients, including the RH-sensitive source

\[
W=\omega_2*\Lambda_\omega.
\]

Thus the old phrase

```text
construct a physical-to-carry map
```

is no longer the correct missing theorem.  The map exists exactly.

PR #241/PR #302 also give the independent-frequency source-convolved reflected Selberg identity for the corresponding inverse-source current.  The remaining issue is quantitative source comparison, not source typing.

## 4. Current source plus strict lower-scale family

The positive inverse gives exactly

\[
a_\omega*W=\Lambda_\omega.
\]

Since `a_omega(1)=1`,

\[
\boxed{
W(n)=\Lambda_\omega(n)
 -\sum_{\substack{d\mid n\\d\ge2}}
  a_\omega(d)W(n/d).
}
\tag{O-32401.1}
\]

Every noncurrent destination obeys `n/d<=n/2`.  On annuli, the RH-sensitive source is therefore

```text
current principal-mode block
= reserved generalized-prime block
  - complete proper-divisor half-scale family.
```

The generalized Selberg defect has the same structural form.  Writing

\[
\mathcal F
=\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega,
\]

one has

\[
\boxed{
a_\omega(n)\log^2n-\mathcal F(n)
 =\sum_{\substack{d\mid n\\d\ge2}}
   a_\omega(d)\mathcal F(n/d)\ge0,
}
\tag{O-32401.2}
\]

and every term on the right lies at half scale or lower.

The source-change family and the positive Selberg defect must therefore be eliminated **together**.  Estimating either by absolute convolution recreates the reciprocal-zeta obstruction.

## 5. Existing current-scale reserve

The generalized-prime carry profile is a positive synthesis of the same opposite-parity wavelets and has an absolute source-specific Schur reserve on every sufficiently large balanced row.  The balanced physical field is pointwise controlled by a polylogarithmic multiple of the same Selberg reserve; endpoint neighbors are retained separately.

The endpoint two-contact energy is itself absorbed, rowwise and quadratically, by the nearest interior generalized-prime reserves except for finitely many bottom rows.

Thus the current-scale positive geometry is substantially complete.  The unproved theorem is the source-coupled elimination of the proper-divisor family without double-counting the reserve.

## 6. Why source-blind contraction is forbidden

PR #323 proves that the critical eta-comb multiplier equals one at every critical zeta zero.  Hence no translation-invariant physical norm containing those wave packets can strictly contract the complete eta source.

This does not affect the dyadic source package above, because the intended contraction is a **Schur descent after the principal source has been retained explicitly**, not a source-blind operator norm.

Any valid proof must preserve the principal current `W` until it is paired with the generalized-prime reserve and lower-scale source-change family.

## 7. New production theorem: Principal-Mode Schur Descent (`PMSD`)

A proof-producing `PMSD` certificate at one annular scale `M` must emit:

1. the exact RH-sensitive annular physical/carry block for `W`;
2. the positive generalized-prime block `P` corresponding to `Lambda_omega`;
3. every proper-divisor source-change term in (O-32401.1), with its exact delay and annular destination;
4. every proper-divisor Selberg-defect term in (O-32401.2);
5. the complete source-convolved two-frequency reflected identity;
6. the current generalized-prime Schur reserve;
7. the endpoint-neighbor/bottom-charge ledger;
8. one congruence or Schur elimination proving
   \[
   E_W(M)
   \le C(1+\log M)^A
     +\sum_\beta\theta_\beta E_W(M_\beta),
   \qquad M_\beta\le M/2,
   \quad\sum_\beta\theta_\beta\le1;
   \]
9. no absolute convolution by `a_omega` before the current square and the proper-divisor defect are combined.

A strict coefficient sum `<1` is welcome but unnecessary: half-scale descent with total charge at most one already gives a polylogarithmic/subpower recurrence.

`PMSD` is rejected if the current `d=1` term is routed to lower scale, if a source sibling is omitted, if the same reserve pays both source-change and Selberg-defect terms, or if a one-frequency square replaces the reviewed physical block.

## 8. Why this is the preferred shake-up target

The live graph has repeatedly shown that the following generic ideas are too strong or ill-typed:

```text
source-free prime-radix contraction;
source-blind eta contraction;
absolute terminal atomization;
bounded endpoint rank;
monotone positive-part cover.
```

The dyadic principal-mode package avoids all five failure modes.  It uses a zero-safe source, exact physical/carry typing, a positive current reserve, and strict proper-divisor scale descent.  It does not assert a theorem stronger than RH for unrelated Dirichlet characters.

## 9. Status boundary

Exact/imported at their stated scopes:

- unique dyadic character scope;
- opposite-parity source/filter identities;
- compact carry dipole;
- positive inverse/generalized-prime data;
- binary digital finite forcing;
- annular physical-to-carry isometry;
- source-change half-scale identity;
- positive Selberg-defect half-scale identity;
- balanced current reserve and endpoint absorption.

Open:

- the source-coupled Schur elimination `PMSD`;
- the resulting cofinal RH-sensitive energy recurrence;
- RH.
