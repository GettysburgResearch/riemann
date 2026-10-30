# A bounded continuation attack: the missing normal-family estimate

Status: **conditional analytic reduction and obstruction examples; its hypotheses are not established for the L-function family.**  
Scope: the corrected detector R_Q^* of `progression_profile.md`. The two earlier reports remain frozen. This note separates control of poles from control of the holomorphic part, and records the classical overlap of the shifted-prime lemma.

## 1. A sufficient package that really implies zero exclusion

Let Ω be a disk compactly contained in Re s>θ>0, meeting the half-plane Re s>1. Rescale Ω to the unit disk by s=c+Rz and put

$$f_Q(z)=R\,R_Q^*(c+Rz).$$

Residues are unchanged by this transformation. The known arithmetic estimate gives f_Q→0 locally uniformly on the nonempty open part corresponding to Re s>1.

Let P_Q be the finite set of distinct poles of f_Q in the unit disk. All these poles are simple: a logarithmic derivative has a simple pole even at a multiple zero, and coincident poles add their residues. Combine repeated locations and write their residues r_Q(a)>0. Set

$$h_Q(z)=f_Q(z)-\sum_{a\in P_Q}\frac{r_Q(a)}{z-a}.$$

This h_Q is holomorphic throughout the disk, including the removable points. It includes the analytic contribution of every pole outside the disk, the gamma/conductor terms, and the explicit arithmetic compensator; those terms cannot be discarded.

### Proposition: a pole-clearing continuation criterion

Suppose, along an unbounded sequence Q, all three conditions hold:

1. **Weighted pole mass:** Σ_{a∈P_Q} r_Q(a)≤M for a fixed M.
2. **Holomorphic regular part:** h_Q is locally uniformly bounded on the disk.
3. **Unweighted pole budget:** for one fixed basepoint z₀ in the right-hand open set,

   $$\sum_{a\in P_Q}-\log\left|\frac{z_0-a}{1-\bar a z_0}\right|\le B.$$

Then ζ has no zero in Ω. In fact, the same hypotheses exclude zeros in Ω of every fixed primitive Dirichlet L-function.

The third condition counts distinct pole locations without multiplying by their residues. A pole of residue 1/(Q−1) still contributes one zero to a pole-clearing Blaschke product.

**Proof.** Let B_Q be the finite Blaschke product with one factor for each distinct pole, normalized by a unimodular scalar so that B_Q(z₀)>0. Then |B_Q|≤1 and B_Q(z₀)≥e^(−B). Hence a subsequence converges locally uniformly to a holomorphic function B that is not identically zero.

The pole-cleared numerator A_Q=B_Qf_Q is holomorphic. For |z|≤r<1,

$$\left|\frac{B_Q(z)}{z-a}\right|\le\frac1{1-r},$$

because removing the corresponding Blaschke factor leaves another function bounded by 1. Conditions 1 and 2 give local uniform bounds for A_Q. Extract a further subsequence with A_Q→A holomorphically. On the right-hand open set f_Q→0 and |B_Q|≤1, so A=0 there. The identity theorem gives A≡0.

If a zeta zero lay in Ω, choose a small contour around it whose boundary avoids the discrete zero set of B. On that boundary A_Q/B_Q→0 uniformly. Its normalized contour integral (2πi)⁻¹∮f_Q(z)dz therefore tends to zero. But each normalized integral is the sum of positive residues inside, and the inherited zeta zero contributes at least its positive integer multiplicity for every Q. This is a contradiction. For a zero of multiplicity m from fixed primitive conductor d≥2, the inherited residue is at least m floor(Q/d)/(Q−1), which tends to m/d>0, giving the same contradiction. ∎

This argument deliberately does not claim that the original meromorphic functions form a normal family. Pole collisions can obstruct spherical normality. The bounded numerator/denominator extraction and the positive residue integral suffice for the stated conclusion.

**Scope cost.** This continuation-to-zero package is stronger than the original zeta-only contour threshold Z_Q(U)<1. The latter can tolerate a small positive contribution from a fixed nonprincipal conductor; convergence of the contour integral to zero cannot. Applied throughout a target half-plane, the package would establish that zero-free half-plane for all fixed-conductor Dirichlet L-functions, not only ζ. It must not be advertised as a weaker zeta-only obligation.

## 2. What density bounds do not supply

The exact conductor formula can sometimes turn a suitable primitive-family density bound into control of **weighted** mass. It does not imply condition 3: arbitrarily many distinct poles of residues of size 1/Q can have bounded total mass while their unweighted Blaschke budget diverges. Nor does a pole count control h_Q.

Two elementary examples isolate the missing hypotheses.

### One persistent pole and an unbounded regular part

For a fixed a with Re a<1,

$$f_N(s)=\frac{e^{-N(s-a)}}{s-a}$$

has exactly one pole, of positive residue 1, and tends to zero on compact subsets of Re s>1. Its regular part

$$\frac{e^{-N(s-a)}-1}{s-a}$$

is entire but is not locally bounded; its value at a is −N. Thus even one pole and strong right-half-plane convergence do not give continuation across that pole.

### Bounded pole mass is not a normality theorem

For fixed 0<r<1,

$$g_N(z)=\frac{z^{N-1}}{z^N-r^N}
=\frac1N\sum_{a^N=r^N}\frac1{z-a}$$

has zero regular part and total positive residue mass 1. Nevertheless it tends to 0 inside |z|<r and to 1/z outside |z|>r, so it is not a normal meromorphic family across the circle. At the basepoint 0 its pole-clearing denominator has modulus r^N→0. This is a counterexample to an abstract normality inference, not a model asserted to describe Dirichlet zero locations.

These examples explain why “the poles have small average density” is not the missing theorem.

### A quantitative version of the gap

On a fixed nested domain, suppose a pole-cleared numerator has bound M_Q globally and bound ε_Q on a right-hand subdomain. A two-constants estimate gives a bound of the form M_Q^(1−ω)ε_Q^ω on a target contour, where ω>0 depends on the domains. To recover the meromorphic detector, one must also divide by the lower bound β_Q for the pole-clearing denominator on that contour. The usable condition is

$$M_Q^{1-\omega}\varepsilon_Q^\omega/\beta_Q\longrightarrow0.$$

A count permitting Q^κ interior poles can allow β_Q as small as exp(−cQ^κ), even when κ<1. The available polynomial right-half-plane decay does not automatically overcome that cost. One needs substantially sharper pole-location control, cancellation in the analytic regular part together with a quantitative denominator estimate, or a different continuation method.

For this pass, none of the required conditions is asserted in the target strip. The profile correction removes a known deterministic source; it does not bound the remaining holomorphic regular part or the pole-clearing cost.

## 3. Classical overlap and a narrowed novelty statement

The weighted shifted-prime lemma used to construct P(u) should be classified as a **classical mechanism independently rederived here**. Its ingredients—expanding φ by Möbius inversion, summing primes in progressions, truncating the divisor variable, and obtaining an Artin-type Euler product—belong to the classical Titchmarsh/shifted-prime and mean-totient framework. The lemma is not presented as a newly discovered prime theorem.

Primary bibliographic checks located:

- R. C. Vaughan, *Some applications of Montgomery's sieve*, Journal of Number Theory 5(1), February 1973, 64–79, DOI [10.1016/0022-314X(73)90059-0](https://doi.org/10.1016/0022-314X(73)90059-0). The [author's publication list](https://personal.science.psu.edu/rcv4/publications.html) and [Penn State institutional record](https://pure.psu.edu/en/publications/some-applications-of-montgomerys-sieve/) confirm the bibliographic identity.
- Montgomery–Vaughan, *Multiplicative Number Theory I: Classical Theory*, Chapter 11, [publisher chapter record](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF). A secondary lead points to §11.4, Exercise 5; that exact exercise was not inspected and is not used as a verified theorem citation here.

The Vaughan publisher full-text endpoint returned 403 and the author's linked PDF returned 404. The accessible metadata/abstract does not expose the exact weighted-totient statement. Consequently no exact theorem number or verbatim match is asserted. The proof in `progression_profile.md` is supplied in full precisely so that the calculation does not rest on this incomplete attribution check.

The candidate contribution to this repository is the explicit finite-scale profile P, its pole-preserving Mellin compensator, and the precise continuation gate above. Even for that combination, no worldwide priority claim is made.
