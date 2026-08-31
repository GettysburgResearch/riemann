# Independent review: locally simple canonical cusp endpoint zeros

Verdict: PASS for the exact scientific source below. The source-specific
analytic theorem is accepted as a reviewed proof, not a machine-certified
theorem. All finite controls are subordinate to that distinction.

Review date: 2026-08-31.
Scientific source: 1653565cc80cde6fa882ae9e150626187d3071d0.
Authoring parent: 98b4058ac29ba88cf993d7a3ce67579fab0c7844.
Resident import: c95fb89ebf076ecd8ec4e0aae9ecb9234cc62ef7.
The five frozen scientific files and all AW/EP/UQ/CF parent files remain
unchanged. This separate audit supplies acceptance; the original proposed
status and its sealed fixture are deliberately not rewritten.

Root suggested the fixed-domain normal-family strategy before the authoring
freeze. Accordingly, root's post-freeze checks are additional verification,
not the sole claim of review independence. A designated non-author reviewer,
who did not contact the author or edit the source, independently reviewed
the analytic argument and reconstructed the finite controls. Both reviews
passed this exact source identity.

## 1. Accepted theorem and quantifiers

For every fixed real delta with 0<delta<12, all sufficiently large even k
have exactly one zero, counting multiplicity, in each disc

    |s-(1-12/k)|<delta/k,    |s-12/k|<delta/k.

These are the actual source-specified canonical cusp quotients Q_k,
not fitted scalar functions or generic positive matrices. Their restricted
denominators do not vanish in these discs. Each zero is therefore uncancelled,
real and simple, and the two zeros reflect across s=1/2. The full period
matrix has corank one, with [q] nonzero on its nullvector.

The sufficient threshold depends on the fixed delta and is not computed.
The earlier 65536 bound proves existence, not this simplicity threshold.
The older 6144 bound concerns the full parent at weights divisible by 12.
Neither number is imported as an effective local-uniqueness bound.

The real fine location remains the separately proved AW expansion:

    1-s_k=12/k+[288 log k+O(1)]/k^2.

Its more precise constant C_12 and error are inherited unchanged. No complex
fine error rate is derived here. The result is uniform over the six native
weight classes, including the r=14 representation of weights congruent to 2.

## 2. Load-bearing analytic review

The review checked the whole proof, not merely the presence of its lemmas.

1. For c=k(1-s), work on the CLOSED disc |c-12|<=R with fixed R<12.
   The exact gap is

       Re(1/(2c))-1/48
         =[144-|c-12|^2]/[48|c|^2]
         >=(12-R)/[48(12+R)]>0.

   In particular c=0 and the boundary of the full chamber are excluded.

2. The native Parseval first-moment estimate applies to every source form,
   with initial order N=2 for all W and N=1 for the full space. On its actual
   Petersson probability measure, Jensen with exponent
   Re(c)/k+1/log k proves E|y^(c/k)-1|=O_R(log k/k), uniformly over all forms.
   The region sqrt(3)/2<=y<1 is included. Multiplication by the polar
   coefficient leaves an O_R(log k) error; it is not an O(1/k) error.

3. The Fourier remainder bound genuinely extends to complex order:
   |cosh((x+it)u)|<=cosh(xu) gives |K_nu(t)|<=K_Re(nu)(t)<=K_(1/2)(t).
   The native half-lattice Fourier coefficient then gives
   |R_s|<=2 rho/(1-rho)^2<1. Normal convergence supplies the analytic
   identity; an inequality on real parameters was not simply continued.

4. The Taylor and Laurent expansions C=pi/6+O_R(1/k) and
   D=-k/(2c)+O_R(1) are uniform on the fixed disc. With the N=2 moment
   bound they make the Hermitian PART of the Gram-whitened W matrix
   at most -kappa_R k times the identity.

5. The complex W matrix need not be Hermitian or normal. Cauchy--Schwarz
   gives its minimum singular value at least kappa_R k and hence inverse
   norm at most 1/(kappa_R k). This establishes actual denominator
   nonvanishing, with no basis-coordinate or dimension loss.

6. For the full cusp space, the absolute |E*|-weighted form is bounded
   by C_R k times the Petersson form. Weighted Cauchy--Schwarz estimates
   the two off-diagonal Schur blocks separately. Thus

       |Q_k(1-c/k)| <= (C_R+C_R^2/kappa_R) k G(h_k).

   Replacing the analytic column by the adjoint of the row is invalid.
   No smallness or positive sign of the complex Schur correction is used.

7. For this fixed R, all sufficiently large weights give functions
   Phi_k=Q_k(1-c/k)/(kG(h_k)) holomorphic on the SAME open disc Omega_R.
   The preceding bound makes the family locally bounded. The real AW
   limit 1/24-1/(2c), on a real interval with an accumulation point,
   identifies every normal-family subsequential limit. The contradiction
   argument then proves convergence of the entire even-weight sequence
   locally uniformly. Eventual holomorphy on unrelated changing domains
   would not by itself justify this step.

8. Choose delta<R<12. The limiting function has a single simple zero at 12
   and no pole in |c-12|<=delta. Its boundary modulus is at least
   delta/[24(12+delta)]. Local uniform convergence supplies the strict
   Rouche inequality. Exactly one zero COUNTING MULTIPLICITY implies
   simplicity, not merely existence or an odd-order sign change.

9. Source conjugation gives I(bar s)=I(s)^*, hence
   Q(bar s)=conjugate(Q(s)); it does not make I(s) Hermitian at complex s.
   A nonreal zero would have a distinct conjugate in the same disc.
   Reflection preserves denominator nonvanishing and zero multiplicity.
   Block elimination gives the corank and flag conclusions. Only after
   reality is proved is the inherited real fine expansion applied.

The primary hypotheses were checked directly against
[DLMF 10.32.9](https://dlmf.nist.gov/10.32.E9),
[DLMF 10.39.2](https://dlmf.nist.gov/10.39.E2), and
[Tao, Math 246A Notes 4, Exercise 58(i) and Theorem 37](https://terrytao.wordpress.com/2016/10/11/math-246a-notes-4-singularities-of-holomorphic-functions/).
The normal-family argument is written out in the resident proof. The remote
pages are mathematical references, not bytes authenticated by offline Git
replay, and no novelty is claimed for these classical theorems.

## 3. Root replay and independent arithmetic

Root read all five new files completely and checked the unchanged AW/EP
source interfaces. The separate LS module passed all 32 tests normally
(5.253 seconds) and under -O (5.138 seconds). Both producer checks,
all four exact LF report/manifest emissions, Ruff, control-character checks
and the complete authoring-base-to-source whitespace check passed.

A separate transient script did not use the producer's arithmetic to
reconstruct the key controls:

- Finite products for Delta^j and binomial polynomials in E4-1 rebuilt
  all 12 native prefixes and 36 additional held-out prefixes: 432 exact
  coefficient entries, across all six residue classes.
- Symbolic rational algebra verified the chamber identity. Six additional
  rational radii and 48 rationally parametrized circle points checked both
  the closed-disc coercivity margin and the Rouche modulus reserve.
- Exact symbolic complex matrices checked the nonnormal inverse,
  its positive Gram reserve, both independent Schur cross directions,
  adjoint determinant conjugation and the inverse/quotient orientation.
- A separate nonnative rational analytic family checked why fixed-disc
  convergence cannot be promoted to an arbitrarily varying-radius claim.
  This control is not evidence about an actual cusp zero.
- Twenty-six independently resealed report alterations were rejected by
  ACTUAL fresh complete reconstruction in EACH normal and optimized mode.
  No cached or mocked build_report was substituted for these root attacks.
- Ten literal frozen source bindings, four artifact seals, all five
  frozen files, fixture identity and payload identity matched.

The designated non-author review also passed 64 LS+AW tests in each mode,
both packets' producer checks, and all four LS emissions. Its separate
coefficient route used Delta=(E4^3-E6^2)/1728 and binary polynomial powers:
12 complete native records/108 coefficients plus 24 held-out prefixes.
It independently used real matrix representations for the complex controls,
38 extra points and 81 vector inequalities. It rejected 128 hostile checks
per mode, including 49 resealed reports: seven against actual fresh
reconstruction and 42 against a cached complete reconstruction.
Those two categories are not conflated.

No finite prefix, rational circle control or test count proves Montel's
theorem, the analytic integral bounds or an eventual weight threshold.

## 4. Exact identities

Frozen Git blobs:

- Proof: 0fa98ad20e040ea9b2e81c9906042ed56782bfaf.
- Producer: 7ebf67ccbd2aba1059771c4a57d07f53de6ebe9b.
- Fixture: 9c5df6fafa484118cb16b6e46e4fb36b5e92c610.
- Sources: 496034972646f6c0ac1cb73bbf5ccf51afdcee54.
- Tests: be3719164ace6d90634efab5f07716b3421ba725.

Fixture LF SHA-256:
ab534135547ed8c82642b3d681988936a1e16b701d57f1736fa8c7294c27b1d7

Payload SHA-256:
88a6747ff97cd36312ab3097194d2d102dcde4aa6b9d9b51edf3b20fa691f9c4

## 5. Retained exclusions

This is not global uniqueness, a complete zero census, an effective
simplicity onset, a complex convergence rate, a varying-delta result or
a theorem uniform to the boundary of the full open chamber. Additional
zeros or poles on other scales are not excluded. Nothing concerns a
counterexample to classical zeta RH, a new automorphic representation,
unsigned global divisor asymptotics or external publication priority.

The independent frozen-SHA review obligation is satisfied. No repair to the
scientific source was required or applied.
