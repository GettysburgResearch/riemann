# Native inverse moments as a signed affine prime–Möbius correlation

Status: exact finite identities and a conditional transfer target. No new
zero-free half-plane is proved. The analytic correlation bound is open.

Scope: the actual native Möbius coefficient, with its original character
orientation, masks, common smooth profiles and physical row measure. A
separate statement below retains the exact PR1019 projection complement.
This note does not replace Möbius by a Gauss-weighted column.

What was actually run: fresh GitHub reads of main and PRs 1013–1021, exact
source reads listed below, and reading the supplied arXiv:2610.20242v1 PDF.
The deductions below are algebraic; no finite numerical experiment is
claimed to establish the open analytic estimate.

Smallest remaining gap: a one-sided bound for the COMPLETE signed affine
correlation in (7), on the native physical range. The paper supplies neither
the affine/field/conductor scope nor the required fixed power saving.

## 1. Fresh repository state and exact dependencies

The following were read directly from the GitHub connector on 25 October
2026. Main is `f99d9e3908dde4865377c75d9ca051c1f545bf4f`; its integrated
scientific account says RH remains unproved. All PRs in this table were
open, draft, and unmerged when read.

| PR | Exact head read | Relevant scope |
| --- | --- | --- |
| 1013 | `ff620ffe983f086eaab070311ab304a994bbf0d4` | Gram conditioning; complementary native inverse still open |
| 1014 | `845225c2e7713b69766b95c5e6964d44bb62f6bb` | Complete conditional 437/500 consumer; missing native mean (H) |
| 1015 | `e87c5f669f81fe6371af926917d1c5b21023bce8` | Complete primitive scalar pairing, not total inverse norm |
| 1016 | `7ea66551190f291101b0dd44fb1fc9b3331c560d` | Quartic full-sieve tail; low-divisor centered mean open |
| 1017 | `450dd8abecf58dfe60b3bc39bda0f792ea82ce95` | Weil-resolvent packet; source identification/convergence open |
| 1018 | `591c880b68ba3de4850941ac7b6be002a6e6e025` | Proposed classical-form secondary region, not smaller fixed half-plane |
| 1019 | `3bcc1daaeb51c71cb2785b9744cde0d641f68f4c` | Actual Möbius projection; orthogonal complement open |
| 1020 | `c690f96fe6876f945398b3e2779810c563a64743` | Structured sextic μγ₂ theorem and cubic components; native coefficient mismatch retained |
| 1021 | `742e952be4ef7843de86ea12678c0bdd3d3579c3` | Marked-count criterion, coefficient continuation and coherent cutoff transport |

PR1021 was created on 25 October 2026 at 08:47 UTC. It is therefore newer
than the preceding conversation summaries. Its mathematical packet is
frozen at the head in the table, not on main.

Load-bearing source files read:

1. [PR1014 native consumer](https://github.com/GettysburgResearch/riemann/blob/845225c2e7713b69766b95c5e6964d44bb62f6bb/standalone/2026-10-22-inverse-length-consumer/PROOF.md),
   Git blob `50f611b563446d32838721d05d4c693e7b9b310b`.
2. [PR1020 coefficient transfer audit](https://github.com/GettysburgResearch/riemann/blob/de3403df774ae0eaddfaeb9bae045ea7c9250b69/standalone/2026-10-23-structured-moment-gains/fifth-pass/PR1019_COEFFICIENT_TRANSFER_AUDIT.md),
   Git blob `945847ee7d1bc1ba0836f916dfabb01b9ae56a9b`.
3. [PR1020 sextic normalization and proof](https://github.com/GettysburgResearch/riemann/blob/de3403df774ae0eaddfaeb9bae045ea7c9250b69/standalone/2026-10-23-structured-moment-gains/fifth-pass/SEXTIC_ROW_PHASE_CANCELLATION.md),
   Git blob `3a5d7adcc24ec8907be5c8fd6879d81736d44788`.
4. [PR1020 cubic raw inverse](https://github.com/GettysburgResearch/riemann/blob/de3403df774ae0eaddfaeb9bae045ea7c9250b69/standalone/2026-10-23-structured-moment-gains/fourth-pass/CUBIC_RAW_CONSUMER.md),
   Git blob `4402fd254e92503029e4f6c23480bc4d2dda9d61`.
5. [PR1021 coherent transport](https://github.com/GettysburgResearch/riemann/blob/742e952be4ef7843de86ea12678c0bdd3d3579c3/standalone/2026-10-24-fresh-zero-free-routes/family/COHERENT_LOG_TRANSPORT.md),
   Git blob `b477bca07958d51db11c686a42308accddeaf343`.
6. [PR1021 direct marked-count target](https://github.com/GettysburgResearch/riemann/blob/742e952be4ef7843de86ea12678c0bdd3d3579c3/standalone/2026-10-24-fresh-zero-free-routes/POSITIVE_MARKED_COUNT_TARGET.md).

The current source-qualified benchmark in these branches is
`B_flat=0.874886647039964...`; these reads do not independently certify
Liu's preprint or the full OpenAI framework.

The general logarithmic Möbius identity is already in PR1021. The present
addition is the exact prime-only coprime representation of the full
off-diagonal native moment and of the exact projected complement. Its
purpose is to expose the precise affine prime correlation to which a
Hardy–Littlewood–Chowla mechanism would actually have to apply.

## 2. Conventions: no coefficient or zero-mask substitution

Work over `E=Q(omega)` and `O=Z[omega]`. Every nonzero ideal prime to the
prime above 3 has the unique primary generator congruent to 1 modulo 3.
We use that generator to write additions, while products and prime
factorization refer to ideals. This is the convention explicitly used
in the pinned sextic source, Section 1. Let `S` contain all originally
omitted primes, including those above 6. All ideal variables and prime
ideals below are outside `S`.

For each permitted physical row `u`, let

\[
 \psi_u(n)=\nu(n)\chi_n(u)^{\mathrm{sign}}(Nn)^{it}
             1_{(n,Q)=1},
 \tag{1}
\]

where the fixed ray/angular factors may be incorporated in `nu`, and
`Q`, when present, is held fixed throughout the common column sum.
The inverse orientation must be interpreted on units with its original
zero extension, not as a negative power of zero. Thus `psi_u` is
completely multiplicative with `|psi_u(n)|<=1`, including every natural
nonunit zero. A unitary angular factor `(n/|n|)^ell` and a common height
factor are completely multiplicative and fit (1). No divisor weight,
Gauss coefficient, or row-dependent smooth test is inserted into (1).

Take `D>=2`, `V in C_c^infinity((1,2))`, and the nonnegative physical
row weight `w(u)`. Write

\[
 M_u(D;V)=D^{-1/2}\sum_n\mu_E(n)\psi_u(n)V(Nn/D),
 \qquad I(D)=\sum_u w(u)|M_u(D;V)|^2.
 \tag{2}
\]

The permitted native row family in PR1014 is sixth-power-free, `Nu`
comparable to `U`; the finite identities also hold for the squarefree
rows in PR1019. A normalization `1/sqrt(Nn)` in a source is converted to
(2) by replacing its profile with `y^(-1/2)V(y)`.

Define

\[
 V_D(y)=\frac{\log D}{\log(Dy)}V(y).
 \tag{3}
\]

The denominator is positive on the support, and for each fixed smooth
seminorm order the `V_D` seminorm is bounded uniformly in `D>=2` by a
fixed finite seminorm of `V`. This retains the common-profile scope.

## 3. A prime-only coprime logarithmic identity

For every ideal `n` outside `S`,

\[
 \boxed{\quad
 \mu_E(n)\log Nn
 =-\sum_{\substack{ap=n\\p\text{ prime}\\(a,p)=1}}
                   \mu_E(a)\log Np.\quad}
 \tag{4}
\]

For squarefree `n`, each allowed `a=n/p` has `mu_E(a)=-mu_E(n)`, and
the sum of `log Np` over its prime divisors is `log Nn`. For
nonsquarefree `n`, every prospective summand is zero: either `p`
repeats in `n`, contradicting `(a,p)=1`, or some squared prime remains
in `a`, forcing `mu_E(a)=0`. The unit case has both sides zero.

The coprimality restriction is load-bearing. At `n=p^2`, deleting it
makes the right side `+log Np` instead of zero. The familiar unrestricted
formula is instead

\[
 \mu_E(n)\log Nn
 =-\sum_{ap^j=n,\ j\ge1}\mu_E(a)\log Np,
 \tag{5}
\]

whose prime powers cancel the repeated-prime terms. Formula (4) carries
out precisely that cancellation through squarefree support, and is
closer to the supplied paper's prime–Möbius correlation. It does not
assume that prime powers are small or neglect their contribution.

## 4. Exact affine correlation for the entire native mean

The genuine pair diagonal is

\[
 \Delta(D)=D^{-1}\sum_n\mu_E(n)^2|V(Nn/D)|^2
                        \sum_u w(u)|\psi_u(n)|^2.
 \tag{6}
\]

For the annular physical rows, `sum_u w(u) << U` and there are `O(D)`
column ideals. Thus `Delta(D)<<_V U`, with the original masks retained.
This is the row-volume term in PR1014's target, not a power-saving
estimate for the off-diagonal.

Define the finite affine prime correlation

\[
\begin{split}
 \mathcal T(D)={}&
 \sum_u w(u)\sum_a\mu_E(a)\psi_u(a)
 \sum_{\substack{h\in3O\\h\ne0}}
 \sum_{\substack{p\text{ prime}\\(a,p)=1\\m=ap+h\ \mathrm{admissible}}}
    \log Np\,\psi_u(p)\mu_E(ap+h)\overline{\psi_u(ap+h)}\\
 &\hspace{20mm}\times
 V_D(Na\,Np/D)\overline{V(N(ap+h)/D)}.
\end{split}
 \tag{7}
\]

Here `m` is required to be a primary generator of an ideal outside the
same `S`. All sums are finite by the two profile supports: `Na Np`
and `N(ap+h)` lie in the fixed norm annulus about `D`. In particular
`|h|<<sqrt(D)` in the complex embedding, so the relevant lattice shift
set has `O(D)` elements. Every fixed puncture in (1) is retained in
both `psi_u` factors. Shifts for which the second column violates a
mask give zero, rather than being replaced by a primitive inducing
character with different Euler factors.

Then the exact identity is

\[
 \boxed{\qquad I(D)=\Delta(D)-\frac{\mathcal T(D)}{D\log D}.
 \qquad}
 \tag{8}
\]

**Proof.** Expand the square in (2), separate `n=m`, and in each
off-diagonal summand use (3)–(4) on
`mu_E(n)V(Nn/D)`. Write `n=ap`, retain `(a,p)=1`, use the exact
multiplicativity `psi_u(ap)=psi_u(a)psi_u(p)`, and write `h=m-n`.
Both primary generators are 1 modulo 3, hence `h in 3O`. This gives
(7) with factor `-1/(D log D)` and no remainder. All rearrangements
are of finite sums. This proves (8).

Although (7) is not visibly real term by term, (8) proves that its
complete sum is real. For the one-sided upper estimate on `I`, it
would suffice to prove a lower bound on this signed real sum. Taking
absolute values in `u,a,h`, or splitting it into independently bounded
shift families, is an additional estimate and may lose the cancellation.

### An exact conditional input to PR1014

Throughout PR1014's native range

\[
 1\le\log D/\log U\le3/2
 \tag{9}
\]

and its fixed small endpoint neighborhoods, suppose the complete sum
(7) obeys

\[
 \mathcal T(D)\ge
 -C_\epsilon D\log D\,(UD)^\epsilon(1+T)^A p_J(V)^2
       \left(U+U^{1/6}D^{4/5}\right).
 \tag{10}
\]

The height order `A`, profile order `J`, masks, and all constants must
have precisely the uniformity required in the pinned native consumer.
Then (6), (8), and (10) imply its missing hypothesis (H). Subject to
the other pinned analytic interfaces, PR1014 would give the
half-plane `Re(s)>437/500`. A two-sided bound for (7) implies (10)
but is stronger than necessary.

This is a proved implication, not proof of (10). The displayed affine
target is intentionally source-complete. It is mathematically equivalent
to the off-diagonal part of the native task up to the explicit diagonal;
its value is to state the actual prime–Möbius object, not to claim the
reformulation has reduced its analytic difficulty.

## 5. The exact PR1019 complement can also be retained

Let `A(n)` be the finite row vector with components
`sqrt(w(u))psi_u(n)`. Let `Pi=I-P_K`, where `P_K` is PR1019's actual
orthogonal projection onto its Gauss-label frame; equivalently
`P_K=V_frame G^{-1}V_frame^*` with the exact Gram matrix, on the source's
licensed label range where `G` is invertible. Define the
Hermitian kernel, linear in its first argument,

\[
 K_\Pi(n,m)=\sum_u[\Pi A(n)]_u\overline{[\Pi A(m)]_u}.
 \tag{11}
\]

The conjugation in the source is explicit. PR1019 uses
`x=A_U overline(b)`, with
`b_n=mu_E(n)nu_0(n)W(Nn/D)1_(n,Q)=1/sqrt(Nn)` and
`(A_U)_(u,n)=sqrt(w(u))chi_n(u)`. To recover precisely this `x` from
(2), choose the positive character orientation,
`nu=overline(nu_0)`, and `V(y)=y^(-1/2)overline(W(y))`.
Any common height phase in `b` is conjugated as well. Then
`x=D^(-1/2)sum_n mu_E(n)V(Nn/D)A(n)` exactly. The projection
`Pi=I-V_frame G^(-1)V_frame^*` remains the original common projection
in these weighted row coordinates; it is not recomputed from a
different coefficient, and the row weight is not applied twice.

This definition keeps the whole coupled Gram inverse. It does not turn
the projected coefficient into a different multiplicative column.
Set

\[
 I_\Pi(D)=D^{-1}\left\|\sum_n\mu_E(n)V(Nn/D)\Pi A(n)\right\|^2,
\]
\[
 \Delta_\Pi(D)=D^{-1}\sum_n\mu_E(n)^2|V(Nn/D)|^2K_\Pi(n,n).
 \tag{12}
\]

Projection contraction gives `0<=K_Pi(n,n)<=sum_u w(u)|psi_u(n)|^2`,
hence `Delta_Pi(D)<<_V U`. The identical finite argument gives

\[
 I_\Pi(D)=\Delta_\Pi(D)-\frac{\mathcal T_\Pi(D)}{D\log D},
 \tag{13}
\]

where

\[
\begin{split}
 \mathcal T_\Pi(D)=
 \sum_a\sum_{\substack{h\in3O\\h\ne0}}
 \sum_{\substack{p\text{ prime}\\(a,p)=1\\ap+h\ \mathrm{admissible}}}
 &\mu_E(a)\mu_E(ap+h)\log Np\,
 K_\Pi(ap,ap+h)\\
 &\times V_D(Na\,Np/D)\overline{V(N(ap+h)/D)}.
\end{split}
 \tag{14}
\]

Formula (14) offers a direct, centered correlation target if the known
projection is to be used. It retains the exact arithmetic kernel rather
than subtracting an upper bound on a projection from an upper bound on
the total. The original paper's scalar theorem does not control this
kernel; even its arbitrary endpoint coefficients do not license arbitrary
coefficients depending jointly on `a,p,h` through `K_Pi(ap,ap+h)`.

## 6. What the new paper supplies, and the unmatched parts

The paper [Lü–Wang–Wu, arXiv:2610.20242v1](https://arxiv.org/abs/2610.20242)
claims `sum_{n<=x}Lambda(n)mu(n+2)=o(x)`. Its displayed proof mechanism
contains:

- Proposition 2.2, p. 5: rough Möbius–Dirichlet character sums with
  `q<=(log x)^B`, arbitrary fixed polynomial Mellin height, and
  `D(log x)^(-A)` savings.
- Proposition 4.2, p. 17: the logarithmic-error replacement of a
  determinant square by major arcs for bounded coefficients supported
  on rough integers.
- Proposition 4.5, p. 32: the growing prime-list moment estimate.
- Proposition 5.3, p. 42: major-arc cancellation with the specific
  coefficient `mu(m)R_Z(m)` and log-bounded rough second coefficient.
- Section 5.3, pp. 45–46: weighted estimates are unweighted by first
  fixing the number of independent mark groups, sending `x` to infinity,
  and then sending that number to infinity. The final stated conclusion
  is qualitative `o(x)`.

In the rational analogue of (7), the subcase `a=1`, `h=2`, trivial row
character and a corresponding scalar profile has the supplied paper's
prime–Möbius shape. This is not literally a subcase in the chosen
Eisenstein primary coset: there `h` must lie in `3O`, while `2` does not.
A field and residue-class extension would need to be proved.

The determinant relation in the paper is

\[
 (mn+2)/a=(rs+2)/b
 \quad\Longleftrightarrow\quad bmn-ars=2(a-b),
 \tag{15}
\]

on its stated coprime support. The nonzero additive shift remains in
the root geometry and parity conjugacy. The full native inverse has
no original fixed shift: its exact matching objects are (7) or (14),
with the entire variable shift family. A determinant identity at
one fixed nonzero shift is therefore not automatically an estimate
for the homogeneous native norm or its complement.

To use the new mechanism in (10), one would need all of the following
in a single retained signed sum: the Eisenstein lattice, varying affine
coefficient `a`, growing shifts `h`, the complete row characters of
polynomial conductor, the exact coprime restriction `(a,p)=1`, the
common profiles, and a fixed power improvement. No separate absolute
sum over these parameters is asserted to suffice.

The distinction in rates is quantitative: PR1014 asks to replace
`D^(5/6)` by `D^(4/5)`, a saving of `D^(1/30)`. For every fixed `A`,
`D^(1/30)/(log D)^A` tends to infinity. Thus the paper's arbitrary
fixed logarithmic savings cannot be entered as the missing exponent
in that consumer.

## 7. Two attempted transfers that do not close

### Apply the new determinant operator directly after first Poisson

The complete cubic first-Poisson formula in PR1020 contains the signed
frequency phase, the common-divisor variables `f,m,l`, natural row
zeros, and the column `mu(n)G(n)` at a moving cubic twist. Its
unit-divisor block for the example target `131/150` requires
`J(D^(22/25),D)<<D^(1+epsilon)`. The paper does not estimate that
character/Gauss column, and its fixed-shift determinant has no equality
to that column. Replacing the whole native coefficient with `mu gamma_2`
would instead use a different theorem from PR1020.

The exact sextic mismatch is already documented: native first Poisson
produces `mu gamma_1=alpha G conjugate(gamma_2)`, whereas the new
structured theorem requires an additional `mu` multiplying `gamma_2`.
A second Poisson step returns the inverse coefficient, not an ordinary
full-character coefficient. The supplied HLC theorem does not insert
that missing Möbius factor.

### Extract a prime through logarithmic transport, then use scalar HLC

The prime-only identity (4) does produce the desired prime–Möbius
affine correlation (7), and it does so without the unnecessary
prime-power tail. But extracting one scalar case discards nearly all
the physical sum: the remaining variables include a whole lattice of
shifts and the character correlation. Bounds whose constants depend
on a fixed `a,h,u` do not sum uniformly over that growing set. This
transfer therefore reaches the explicit new analytic target (10),
not its proof.

## 8. Research recommendation

The closest coefficient-faithful use of the paper in the existing
inverse route is to attack (14) with its exact complement kernel, or
(7) before introducing projection. The paper suggests that a high
moment of prime-replacement operators might retain more cancellation
than a marginal large sieve. The first concrete feasibility test is
whether its root-averaging step survives the complete affine
parameters and the native polynomial conductor budget while producing
a fixed power, not whether another scalar special case is small.

If that test fails, the alternative averaged additive-shift route
being investigated separately is genuinely different from the current
sextic Gauss consumer. Neither route should be labeled a new zero-free
region until its all-scale analytic input is established.
