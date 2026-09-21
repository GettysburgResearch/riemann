# L-family connection: a known central order and an exact rank-one subtraction

**Relevance to issue #738; separate from the Möbius covariance implication.**
This is a concrete reference adapter and regression suite, not a claim to
have constructed or certified numerical elliptic L-functions.

## 1. The imported result, at its actual strength

Burungale--Tian, arXiv:2609.14893v2, Theorem 1.1, states that for every
prime p=8 mod 9, both curves

$$E_p:y^2=x^3+p^2/4,\qquad E_{p^2}:y^2=x^3+p^4/4$$

have analytic rank exactly one, with arithmetic center s=1. These are
CM **cubic twists**, not the original quadratic-twist family of #738.
The extension is explicit. This theorem controls the central order,
not all zeros; it does not imply GRH for these curves.

The relevant proof mechanism is at Proposition 7.10, Theorem 8.7, Theorem
8.11 and Theorem 10.5: a nonzero first-division boundary, an integral
norm/projector identity, exclusion of torsion, then Gross--Zagier and
nonvanishing of the complementary Rankin--Selberg factor.

The current packet checks only bounded algebraic fixtures from this
mechanism. It does not independently certify the modular-parametrization,
CM-field, descent, local torsion, or Gross--Zagier inputs.

## 2. Explicit normalization and deflation

Let Lambda_E(s) denote the completed elliptic L-function in arithmetic
normalization, with functional equation

$$\Lambda_E(s)=-\Lambda_E(2-s).$$

The exact conductor is a required input of any numerical adapter. None
is guessed in these fixtures. Define the real-entire critical coordinate

$$X_E(z)=-i\Lambda_E(1+iz).$$

Reality follows from real coefficients and the negative functional-
equation sign: conjugation and reflection give
`overline(X_E(overline(z)))=X_E(z)`. Also X_E is odd. The imported
analytic-rank theorem says that its zero at z=0 is exactly simple.
Thus

$$\widehat X_E(z)=X_E(z)/z$$

extends to a nonzero value at zero and is even. Deflation removes exactly
the central zero and no hypothetical off-line zero. This is an algebraic
consequence of knowing the exact central multiplicity, not GRH.

## 3. BCP26-L1: exact central-rank correction of a Pick matrix

More generally let X(z)=z^r F(z), with r a nonnegative integer and
F(0)!=0. At points away from zeros and z=0 put

$$m_X(z)=-X'(z)/X(z),\qquad m_F(z)=-F'(z)/F(z).$$

Logarithmic differentiation gives

$$m_F(z)=m_X(z)+r/z.$$

For upper-half-plane sample points z_i at which these functions are
finite, use the conventional Pick matrix

$$K_X(i,j)={m_X(z_i)-\overline{m_X(z_j)}\over z_i-\overline{z_j}}.$$

Then the exact correction is

$$\boxed{\quad K_F=K_X-rvv^*,\qquad v_i=1/z_i.\quad}$$

Proof: the kernel of -r/z is r/(z_i overline(z_j)). This is a positive
rank-one term, irrespective of the other zeros. QED.

**The operation is subtraction, not addition.** A legitimate central
zero can make a finite raw matrix more positive and mask a negative
direction contributed by off-line zeros. This is why a theorem-backed
rank-one family is useful even without computing any new zeros.

The identity is elementary and is not claimed new in the literature or
absent from all earlier #738 branches. Its role here is a fully specified
adapter and regression test attached to the new reference family.

## 4. Exact synthetic masking control

Take X(z)=z(z^2+1), whose noncentral zeros are at +i and -i, and sample
at z=i/2. Direct rational calculation gives

$$K_X=4/3>0,\qquad K_{X/z}=-8/3<0.$$

Thus one raw positive scalar Pick test can miss the off-real pair, while
the correct central deflation exposes it. This polynomial is a synthetic
control, not an elliptic L-function or a counterexample to GRH.

The all-real-zero control X(z)=z(z^2-1) has deflated value 8/5>0 at the
same point. With X(z)=z^3(z^2+1), incorrectly deflating only one central
zero leaves value 16/3>0. Root-number parity alone does not determine the
required rank correction. The paper's exact rank-one theorem does.

The code also verifies the full three-point identity for ranks 1 and 3,
both signs in z^2 +/- 1, at i/2, i/3 and 2i/3.

## 5. Exact reference computations actually performed

`lfamily.py` uses Fraction arithmetic in Q(omega), omega^2+omega+1=0.
It checks the integral norm/projector identities of Lemma 8.6 for both
cubic characters and group orders 3,6,9,18,27,81. It checks the Fermat
identities for q=13 and q=31 (Appendix A), including the q=31 nontrivial
cube factor, and the resulting affine curve equations.

For all fourteen primes p=8 mod 9 below 500, it selects the least eligible
auxiliary q by exact modular arithmetic, computes the cubic residue
exponent, both descent matrices modulo 3, class-group order, and the
three-primary quotient. It reproduces the boundary sign **relative to
eta_q**. In particular eta_67 is left undetermined, as in the paper.

The finite code does not prove that a point is the analytic CM evaluation,
that a rational point is non-torsion, that a central derivative is nonzero,
or that a detector is positive at all sample sizes. Those are distinct
statements with different proof obligations.

## 6. Bounded next use in #738

Use these fixtures as a compulsory rank-deflation regression when a
normalization-certified cubic-twist adapter is built. Its missing inputs
include conductor/bad Euler-factor certificates, rigorous L-evaluation,
and validated matrix enclosures. Keep the original quadratic family,
the new cubic reference family, synthetic controls, and their statuses
separate. No numerical elliptic L-value or zero data is supplied here.
