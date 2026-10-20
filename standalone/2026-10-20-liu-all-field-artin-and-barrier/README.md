# Liu's all-field boundary: Artin closure, arithmetic consequences, and an exact enlarged-system barrier

Date: 20 October 2026. Status: **proposed research packet with an imported preprint theorem**.

This packet imports Baiying Liu's newly posted *Zero-free half-planes for
Hecke L-functions over number fields*, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1),
and develops five consequences and component results. The new scalar theorem
closes the classwise mixing and unequal-length possibilities for the four
explicit numerator endpoints and the full supplied direct majorant. The
principal residue calculation isolates an angular Hecke factor and continues
the remaining unit to the half-plane Re(s)>1/2.

**No smaller zero-free boundary is proved in this packet. RH remains unproved.**
The imported all-field boundary is

\[
B_\flat=0.874886647039964\ldots,
\qquad
133488B_\flat^4-376596B_\flat^3+384534B_\flat^2
-167541B_\flat+26231=0.
\]

The theorem concerns the **open** half-plane Re(s)>B_flat for every
finite-order Hecke character over every number field, with the principal
simple pole at one permitted. It makes no claim on the boundary line.
The decimal 0.8749 in the circulating screenshot is a rounded version.

## What this adds

| Claim | Result | Evidence and scope |
|---|---|---|
| L26-IMPORT | Pinned all-field finite-order Hecke theorem at B_flat | [Focused source audit](liu_source_audit.md); Theorem 17.1, Theorem 18.2, Proposition 19.1. External analytic proof, not fully independently certified here. |
| L26-ARTIN | The same half-plane is a holomorphic unit domain after removing the exact principal pole for every finite-image Artin representation | [Complete Brauer proof](artin_chebotarev.md), including negative induction coefficients and ramified Euler factors. |
| L26-A5 | Explicit nonmonomial three-dimensional A5 examples | [Character identity and L-factorization](a5_artin_example.md); exact enumeration of all 60 group elements and all 25 character inner products. |
| L26-CHEB | Prescribed Frobenius types in every sufficiently large interval (x,x+x^alpha], for every fixed alpha>B_flat | [Fixed-extension theorem](artin_chebotarev.md); constants and onset depend on the extension and alpha. |
| L26-PRIMES | Small degree-one primes detect nontrivial characters and generate ray class groups and their subgroups | [Uniform explicit-formula proof](hecke_small_prime_consequence.md); exponent 1/(1-B_flat)=7.99275198323..., with field-uniform but uncomputed constant. |
| L26-MOBIUS | Actual signed ideal-Mobius sums obey a conductor-uniform X^(B_flat+epsilon) estimate over each fixed field | [Analytic proof](uniform_mobius_consequence.md); q^epsilon conductor loss, constants depend on the field. |
| L26-BARRIER | Classwise choice among four endpoints, free total length, and either sign of asymmetry cannot cross B_flat in the stated system | [Full proof](beyond_free_length_barrier.md), [four-class certificate](beyond_hybrid_barrier.md), exact rational checker. This is an obstruction for supplied estimates. |
| L26-PRINCIPAL | H_eta(s)=L_F^S(6s-3,(bar Lambda eta)^6) K_eta(s), with K_eta a holomorphic unit for Re(s)>1/2 | [Local factorization and analytic proof](principal_factorization.md); ordinary Euler products protect H_eta for Re(s)>2/3. The extracted character has infinite angular order. |

The Artin and arithmetic claims are explicit deductions using classical
methods. No literature-wide priority claim is made for them. The barrier is a
proposed extension of the optimality scope stated in Liu's Remark 14.13.
The principal calculation is compared with the distinct resonant calculation
already present in PR #975.

## 1. The family extension includes nonmonomial representations

Assume a common finite-order Hecke boundary B over every number field. For any
finite-image complex Artin representation rho, let m(rho) be the dimension of
its invariant subspace. Then

\[
(s-1)^{m(\rho)}L_K(s,\rho)
\]

is holomorphic and nowhere zero in Re(s)>B. Brauer induction expresses the
Artin function as an integer product of Hecke functions over intermediate
fields. The zero-free premise makes the factors holomorphic units after
normalizing their principal poles, so negative integers cause no new poles.
Frobenius reciprocity computes the total pole order exactly.

As a fully explicit nonmonomial example, for G=A5 and suitable linear
characters theta of C5 and lambda of A4,

\[
\chi_3=\operatorname{Ind}_{C_5}^{A_5}\theta
-\operatorname{Ind}_{A_4}^{A_5}\lambda
-\operatorname{Ind}_{A_4}^{A_5}1+1.
\]

The certificate constructs this identity over Z[z]/Phi_15, rather than
accepting a supplied character table. The analytic inference still depends
on the imported universal Hecke theorem.

## 2. An arithmetic exponent just below eight

Write n=[K:Q], D=|disc(K)|, and let m_0 be the finite part of a ray modulus.
For a subgroup H of the ray class group G, put i=[G:H]. The degree-one prime
ideals whose classes lie in H and whose norms satisfy

\[
N\mathfrak p\le C_B
\left(i\{\log(DN\mathfrak m_0)+n\}\right)^{1/(1-B)}
\]

generate H. For the entire group, i=1. The proof uses a fixed nonnegative
annular weight, the Hecke logarithmic derivative at two, a smoothed explicit
formula, and finite character orthogonality. It keeps the finite-conductor
exclusions and the cost of removing higher rational prime powers.

The exponent is 32 for the input 31/32, 8 for 7/8, and
7.992751983230945... for Liu's B_flat. The constant is uniform in the field,
modulus, character, and order, but its numerical value is not computed here.
This is a generator/detection bound; it does not promise a prime in every
prescribed residue class at the same scale.

## 3. What the exact barrier rules out

Liu's refined optimality statement excludes classwise mixing and unequal
lengths. The enlarged system here grants both freedoms. Each formal class
can independently choose its best pointwise contour endpoint or averaged
endpoint, with full available prime capacity and all positive technical
losses omitted.

Four exact witness classes cover every nonnegative asymmetry. Paying the full
direct cost proves that changing the total length cannot improve any of the
four exponents at the witnesses. Negative asymmetry has an additional direct
cost; its four paid slopes have the wrong sign for an improvement. The
result applies throughout the explicitly stated relaxed length domain.

This does not establish that the formal worst classes occur arithmetically,
or that separate moments are simultaneously sharp. A new mixed estimate,
an exclusion of those classes, or a different direct average changes an
input and lies outside this obstruction. The earlier intermediate-contour
closure of #1005 is used only within its licensed balanced range; arbitrary
new unequal-length contour constructions are not silently included.

## 4. The principal residue exposes an angular problem

At the actual principal residues (w,z)=(1,1/6), the source correction factors as

\[
H_\eta(s)=L_F^S(6s-3,\nu)K_\eta(s),
\qquad \nu=(\overline\Lambda\eta)^6.
\]

The remaining Euler product K_eta is a holomorphic unit for Re(s)>1/2.
Therefore the possible zeros of H_eta in that half-plane are exactly the
affine images s=(rho+3)/6 of zeros of the extracted angular Hecke function.
In particular H_eta is nonzero for Re(s)>2/3.

The angular infinity type is nonzero. Liu's finite-order theorem does not
apply to nu. An exact Mobius convolution can strip this factor, but taking
absolute values costs the 2/3 exponent. The note proves that cost by splitting
the complete ideal sum at N(a)=Z^(1/6), including the small-argument tail.
It does not assert a new bound for the transformed theta average.

## Relationship to the latest repository work

The observed integrated base is
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
The latest inspected research inventory ended at PR #1008; those later
research packets were open drafts rather than integrated mathematics.
[repo_audit.md](repo_audit.md) records exact source commits and comparisons.

The most relevant previous numerical packet, #1005, gives the source-qualified
0.87488666 deduction for Eisenstein-field Hecke and Dirichlet functions.
Liu's number is only about 1.296e-8 smaller, but the number-field quantifier is
much broader. The #1006 target 437/500=0.874 still requires a complete mixed
mean of size U^(6/5+epsilon); its recorded corner bound U^(11/8) leaves a
7/40 power saving unproved. The present scalar theorem explains why using
the same endpoint estimates with different lengths will not fill that gap.

## Reading and replay

Start with [CLAIMS.md](CLAIMS.md) for quantifiers and status, then the source
audit, the full barrier proof and its four-class certificate. The Artin,
small-prime, Mobius, and principal-factor notes can be read independently.
[REVIEW.md](REVIEW.md) records the separate checks and their limits.
[VALIDATION.md](VALIDATION.md) gives exact replay commands and arithmetic
contracts. [NEXT_STEPS.md](NEXT_STEPS.md) identifies the smallest missing
analytic statements.

The core checkers require Python's standard library only. A separate optional
SymPy checker independently expands 22 displayed identities. Ordinary and
optimized runs of each core checker are compared byte for byte. The finite
checks certify algebra, group enumeration, and a rational witness cover;
they do not certify the source's 136-page analytic proof.

This packet adds original notes, source locators, and a pinned source hash.
It does not redistribute the source PDF. It is submitted for review on its
own branch and does not alter the integrated scientific status.
