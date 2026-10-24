# A power saving in the full Möbius cubic Gauss moment

24 October 2026. Status: proposed source-dependent theorem, submitted for
independent review. This is a full all-row structured moment estimate in
the specified range, not only a bound for one Poisson component. It does
not imply a smaller global zero-free boundary without a further consumer
for the original sextic inverse moment.

## 1. Exact inputs and normalization

The primary analytic input is `openai/math` at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, in
`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/`:

* `sections/dispersion.tex`: the exact uncorrected Poisson identity
  `eq:poisson`, large-common-divisor removal, the frequency separation
  and all nonexceptional large-conductor estimates. Exact source SHA256:
  `9a04b892feb99a79ec4e825bcd5096d3adb994c53d539c41d2da35f0a77f317c`.
* `sections/dual.tex`: the full-sum functional-equation step,
  off-diagonal Gram estimate and exceptional
  large-value argument. Exact source SHA256:
  `1209fd17cee79f4a21b71d66d3d8b60b210216fa783ec555959d2ebff2fba483`.
* `sections/angular.tex`: the fixed-angular full-sum duality used in the
  exceptional argument. Exact source SHA256:
  `f14a7c1c4f0b19b70d6705c8a2adcb658bfbc77814edb61cd57edb2465f38510`.
* `sections/background-type1.tex`: Lemma `lem:cubic-extensions`,
  including its unrestricted-inner divisor-bounded form. Exact source SHA256:
  `1c7be908c862dc440772964cfdd59e095e7b0f079cec11d99f5c7a9644198dd1`.

The exact source bindings are collected in [SOURCES.json](SOURCES.json).
The adapter from prime convolutions to Möbius coefficients is proved in
[MOBIUS_EXCEPTIONAL_CUBIC_MEAN.md](MOBIUS_EXCEPTIONAL_CUBIC_MEAN.md).
The new step here is its use for this coefficient class; the subsequent
large-value ingredients are the pinned source.

The proposed all-unitary boundary input is PR1012, commit
`64cb43c038d1828a478cb97cbc32e435e111d2d2`,
`standalone/2026-10-20-boundary-iteration/global/ALL_UNITARY_REFINED_BOUNDARY.md`,
Git blob `b34d93c8b6d311ec7fb3a9ee9f5371a9b8fd3f2e`. To keep the
dependency explicit, the theorem below states the precise zero-free
orbit hypothesis it uses. It does not reprove that boundary packet.

Work in E=Q(omega) with the source's primary generators, cubic symbol
chi_b, and normalized cubic Gauss coefficient G(b). All omitted primes
belong to a fixed finite set S. Symbols are extended by zero on nonunits.
Let theta=Theta_ell nu, where ell is a fixed integer, Theta_ell is the
fixed angular Hecke character on primary generators, and nu is a fixed
finite ray character. Different fixed conventions for G or the angular
character can be absorbed in this fixed ray data.

Choose a nonnegative smooth radial plane weight W supported in a fixed
annulus and a smooth norm-annular weight V. Their seminorms are fixed.
Set X=AB and

\[
 \mathcal M_\theta(A,B)=
 \sum_{a\equiv1\ (3)}W(a/\sqrt A)
 \left|\sum_b\mu(b)\theta(b)G(b)
       \overline{\chi_b(a)}V(Nb/B)\right|^2,
 \quad H=B^2/A,\quad \mathcal Q=ABH^{1/3}.
\tag{1}
\]

The row a is not restricted to squarefree ideals. The columns are
squarefree by the actual Möbius coefficient, and their original zeros
are not replaced by phases on forbidden pairs.

**Hypothesis ZF_beta.** Fix 1/2<beta<1. Every primitive finite-character
twist of the fixed angular type ell is zero-free in Re s>beta, with a
possible principal pole permitted. The ordinary Hecke functional
equation, finite order and conductor-uniform polynomial growth are part
of the standard Hecke input. Only cubic finite twists and finitely many
fixed ray modifications are used in the argument.
The opposite angular orbit has the same zero-free half-plane by complex
conjugation; it is used in the conjugate column.

**Theorem.** Under ZF_beta there is eta>0, depending on beta, theta and
the fixed test class, such that for every epsilon>0,

\[
 \boxed{\quad
 \mathcal M_\theta(A,B)
 \ll (AB)^\epsilon\bigl[AB+\mathcal Q X^{-\eta}\bigr],
 \qquad A\ge B\ge2.
 \quad}
\tag{2}
\]

The exponent eta is an existence result from the source's compactness
argument; no numerical value is claimed. In normalized columns,

\[
 \sum_a W(a/\sqrt A)
 \left|\sum_b\frac{\mu(b)\theta(b)G(b)}{\sqrt{Nb}}
       \overline{\chi_b(a)}V(Nb/B)\right|^2
 \ll X^\epsilon\bigl[A+(AB)^{2/3}X^{-\eta}\bigr].
\tag{3}
\]

Equation (3) follows by absorbing the fixed scaled norm power in V and
dividing (2) by B. The A term retains the original pair diagonal.

## 2. Uniform Möbius cancellation in the required twists

ZF_beta implies, for every fixed delta,epsilon>0,

\[
 |L(\sigma+it,\psi)^{-1}|
 \ll_{\delta,\epsilon,\ell}
    [q_\psi(2+|t|)]^\epsilon,
 \qquad \sigma\ge\beta+\delta,
\tag{4}
\]

uniformly in finite twists psi of the fixed angular type. Here the
finite conductor norm is q_psi; fixed field and angular factors are
absorbed in the constant. A principal member is treated after removing
its pole; its reciprocal is holomorphic and vanishes at the pole.

For clarity, the needed uniformization is quantitative. Normalize the
analytic logarithm by its Euler series to the right of one. Uniform
polynomial Hecke bounds and Borel--Carathéodory on a fixed chain of
zero-free disks give |log L|=O_delta(log(q_psi(2+|t|))) on a line a fixed
distance to the right of beta. On a fixed line to the right of one,
the Euler series gives O(1). Apply the three-lines argument to log L,
with a Gaussian factor centered at the height in question. On any
intermediate fixed line this yields O((log(q_psi(2+|t|)))^c), with c<1.
Exponentiating its negative gives (4). For the principal member use
H(s)=((s-1)/(s+1)) zeta_E(s), after any pure norm shift. It is holomorphic
and nonzero on the stated half-plane and its logarithm is O(1) on the
Euler line, including large heights. The rational factor cancels the
principal pole without introducing a zero there. This explains why separate
zero-free statements with arbitrary conductor-dependent constants would
not suffice, and why the common orbit hypothesis does suffice.

Let Q be any puncture and let xi be a finite cubic twist, with all
imprimitive zeros retained. Mellin inversion, (4), and the deleted
Euler factors give

\[
 \sum_{(n,Q)=1}\mu(n)\theta(n)\xi(n)(Nn)^{it}U(Nn/Y)
 \ll [Y\,NQ\,q_\xi(2+|t|)]^\epsilon Y^\beta.
\tag{5}
\]

Here U belongs to a fixed smooth annular test class and Y>=1; bounded
subunit lengths are handled by the same bound with a changed constant.
Indeed the Dirichlet series is 1/L(s,theta xi) times the inverse deleted
Euler factors. On Re s>=beta+delta their product is O((NQ)^epsilon).
Move the Mellin line to beta+delta and choose delta smaller than the
requested exponent loss. Rapid Mellin decay absorbs the height growth.
This proof also gives finite seminorm dependence and common profile
families with a rapidly decaying parameter. Principal xi are included:
Möbius cancellation does not require a nonprincipal twist.

## 3. Literal Poisson identity and the common factors

Put beta_b=mu(b)theta(b)V(Nb/B). For an unequal pair b1,b2, write
f=(b1,b2), b_i=f p_i, F=Nf. Then f,p1,p2 are squarefree, p1,p2 are
coprime and both are prime to f. Remove the surviving row restriction
(a,f)=1 by the exact sum over m|f, with M=Nm. The cited Poisson formula,
with its squarefree-row-sieve variable d set to one, is

\[
 \frac{A\mu(m)}{9M}
 \frac{\beta_{fp_1}\overline{\beta_{fp_2}}}
      {\sqrt{Np_1Np_2}}
 \sum_{h\ne0}
 e(\operatorname{Tr}(h/(3\lambda)))
 \widehat W\!\left(\frac{h\sqrt A}
                 {3\lambda\sqrt M\,p_1p_2}\right)
 \chi_{p_1}(h/(fm))\overline{\chi_{p_2}(h/(fm))}.
\tag{6}
\]

The inverse fm is residue notation on the actual coprime support. It
can be replaced in each cubic symbol by (fm)^2. The normalized Gauss
factors cancel exactly in (6), as proved in the source. The original
diagonal is bounded by X^epsilon AB using the elementary annular row
count. There is no zero Poisson frequency for the unequal primitive
pair. The exceptional pair p1=p2=1 belongs to that original diagonal
and remains excluded.

For formal separation of the coprime pair, first extend this displayed
expression and then insert sum_{l|(p1,p2)} mu(l), exactly as in the
source. Put L=Nl and p_i=l n_i. Squarefree support keeps (l,n_i)=1
and (f,l)=1. The common cubic factors give the zero-preserving mask
|chi_l(h/(fm))|², and the separate coefficient becomes

\[
 \beta_{fln}=
  \mu(fl)\theta(fl)\mu(n)\theta(n)
    1_{(n,fl)=1}\,V(FLNn/B).
\tag{7}
\]

If fl is not squarefree it is zero. Formula (7), not an arbitrary
coefficient replacement, is used at every subsequent stage. The full
two-norm kernel and both original column cutoffs are separated only
after (6)--(7), with the source's common rapidly decreasing Mellin
majorant. Every resulting shift and cutoff is independent of the
current frequency-character row.

The norm scales and prefactor on an h-dyad Nh asymptotic to J are

\[
 B'=B/(FL),\qquad H'=HM/F^2,\qquad k=J/H',
 \qquad \text{prefactor }\asymp AF/(MB).
\tag{8}
\]

The separated kernel costs (1+k)^(-R) times arbitrary rapid Mellin
decay, for any prescribed fixed R. The same bounds hold when H'<1:
every nonzero dyad is then in the decaying tail. No extra constant
frequency count is inserted.

## 4. The complete short-H range

For fixed f,l,m,h, apply (5) to each column in (7), retaining the
puncture and the finite cubic twist h/(fm). After common separation
the product is bounded by X^epsilon (B')^(2beta). The character
conductor and all punctures have polynomial norm on every retained
frequency range; the remaining tails converge by the kernel decay.

There are O(J) ideal frequencies in a dyad. Summing the Schwartz
frequency weights gives O(H') rather than O(H'+1), also for H'<1.
Consequently (8) gives the absolute majorant

\[
 X^\epsilon\frac{AF}{MB}\frac{HM}{F^2}
          \left(\frac B{FL}\right)^{2\beta}
 =X^\epsilon B^{2\beta+1}
           F^{-1-2\beta}L^{-2\beta}.
\tag{9}
\]

The sums over f and l converge because beta>1/2; m|f costs only a
divisor power. The excluded p1=p2=1 term, if added during the formal
extension, has f asymptotic to B. Its nominal nonzero-frequency scale
is H'=M/A=O(1), and its prefactor is A/M. Schwartz decay bounds its
frequency sum by O_R((M/A)^R) for any fixed sufficiently large R,
with constants also covering bounded M/A near one. Thus each f,m
contributes O(1); the whole artificial-diagonal subtraction is
O(B X^epsilon), which is at most O(AB X^epsilon) and also at most
O(B^(2beta+1) X^epsilon). It is not silently included as a primitive
Poisson identity. Thus the full nonzero part satisfies

\[
                  |\mathcal M-\mathcal D|
                  \ll X^\epsilon B^{2\beta+1}.
\tag{10}
\]

In particular (2) follows in H<=B^(2-2beta), because AB=B³/H.
This branch includes all cubic frequencies, all common divisors and
all small primes; it is not a large-conductor truncation.

## 5. Reduction in the remaining range

Assume H>B^(2-2beta). Equivalently B<=A<B^(2beta), so
B>X^(1/(1+2beta))>X^(1/3)>X^(8/25). Thus the entire remaining range
lies inside the pinned source's scale range; the final theorem needs
no lower power restriction on B. Also H has a fixed positive power
of X. In particular the original diagonal AB=Q H^(-1/3)
is itself smaller than Q by a fixed power, although it remains visible
in (2).

Choose small fixed delta,delta'>0 in the order described below. The
source's inversion of 1_{N(b1,b2)>=X^delta}, followed by its positive
unrestricted-outer cubic sieve, bounds an f-dyad F>=X^delta by

\[
                  X^\epsilon[AB+\mathcal Q F^{-2/3}].
\tag{11}
\]

It applies to the present coefficients because it uses only their
divisor bounds and original common support. Both terms in (11) save
a fixed power relative to Q in the present H range. Dyadic sums cost
only logarithms. The remaining f satisfy F<X^delta.

Next remove L>=X^delta after (7), using the source's unchanged
large-l calculation. Its ratios, including its L weights, are bounded
by small-power multiples of

\[
        (B/F)^{-1/3},\qquad L^{-2/3},\qquad L^{-1}.
\tag{12}
\]

Choose delta' small relative to delta, and delta small relative to the
fixed lower exponent 8/25. Each gives a fixed power saving. The f,m
weights are exactly those in the source's benchmark computation and
remain summable. No Möbius structure is needed in (11)--(12), so no
new coefficient hypothesis is hidden there.

For the retained f,l, truncate k and the common Mellin shifts at
X^delta' with a negligible tail, retaining the rapidly decaying
majorants inside the truncation. Then B'>=X^(8/25-2delta), and
J<=X^(2delta') B/F because H<=B. All these are the same retained
support inequalities used by the source.

## 6. All small-conductor frequencies, including the principal ones

Factor h=epsilon lambda^i p q² j³ with i in {0,1,2}, p,q coprime and
squarefree. Write P=Np, Q0=Nq. The available cube factors have total
count comparable, with Schwartz tails, to
(J/(P Q0²))^(1/3). For each such fixed j, the source uses the benchmark

\[
                         (B')^2(PQ_0^2)^{1/3}.
\tag{13}
\]

The inner polynomial has exactly the coefficient (7), with additional
puncture j and the cubic twist (fm)^2 p q². Thus (5) bounds each row
by X^epsilon (B')^beta, including when the induced character is
principal. There are O(P Q0) rows, so its ratio to (13) is

\[
 X^\epsilon(B')^{-2(1-\beta)}P^{2/3}Q_0^{1/3}
 \le X^\epsilon(B')^{-2(1-\beta)}(P Q_0²)^{2/3}.
\tag{14}
\]

Choose a sufficiently small fixed kappa>0. For P Q0²<=X^kappa,
(14) saves a fixed power because B'>=X^(8/25-2delta). For example,
one may first choose kappa much smaller than (1-beta)/10, and then
delta sufficiently small. The conductor and puncture factors in (5)
are absorbed by taking its arbitrary exponent loss smaller than this
gap. The common transform shifts are treated in exactly the same way.

This replaces both the source's low-conductor Siegel--Walfisz step
and its principal cube extraction. No roughness is required. The
principal cube frequencies are controlled because Möbius has the same
bound (5) for a principal character. Their exact local restrictions
remain in (7).

## 7. Large conductors and the exceptional Möbius adapter

For P Q0²>=X^kappa, use the source's large-conductor argument with its
small positive threshold replaced by kappa. The limiting inequalities
are unchanged. If P has the larger exponent, the ratios supplied by
the cubic sieve are

\[
 \frac{P^{2/3}Q_0^{1/3}}{B'},\qquad
 (Q_0/P)^{1/3},\qquad (P Q_0/B')^{1/3}.
\tag{15}
\]

If Q0 has the larger exponent, they are

\[
 \frac{P^{2/3}Q_0^{1/3}}{B'},\qquad
 (P/Q_0)^{2/3},\qquad (P^2/B')^{1/3}.
\tag{16}
\]

In the equal-exponent region the ordinary character sieve is used as
in the source. Under P Q0²<=(B')^(1+o(1)), these estimates have a
strict limiting power gap except at

\[
 (P,Q_0)=((B')^{1+o(1)},(B')^{o(1)})
 \quad\hbox{or}\quad
 (P,Q_0)=((B')^{1/3+o(1)},(B')^{1/3+o(1)}).
\tag{17}
\]

The lower bound X^kappa excludes the zero-exponent endpoint. The
usual compactness argument now reduces the uniform remaining bound
to fixed neighborhoods of (17).

In either neighborhood, the frequency and column scale inequalities
force J=(B')^(1+o(1)), B=X^(1/2+o(1)), and the cube factor j and
the retained f,l,m twists have subpower norm in the limiting test.
Thus (7) meets the *Möbius* exceptional-mean adapter, with

\[
       v=(fm)^2,\qquad e=flj\times\text{fixed puncture}.
\tag{18}
\]

The conductor handoff can be made quantitative before taking limits.
Write Y=B', c=8/25-2delta, and let rho be a sufficiently small fixed
radius for the exponent neighborhoods in (17). Then Y>=X^c,
J<=X^(2delta') L Y, and P Q0²>=Y^(1-3rho). Consequently

\[
 Nv\le Y^{4\delta/c},\qquad
 Ne\ll Y^{\rho+(7\delta+2\delta')/(3c)}.
\]

The latter follows by bounding Nj by (J/(P Q0²))^(1/3) and retaining
both f and l in e. First choose rho smaller than the adapter's permitted
exponent, then choose delta and delta' sufficiently small. Both extra
norms therefore lie in its required fixed neighborhood; the original
fixed puncture is absorbed by a further small margin.

Its independent smooth column profile is the rescaled original V;
no new character-row-dependent norm cutoff is introduced. The norm
shifts are at most X^delta', hence below (B')^.36 after delta' is
chosen sufficiently small. The adapter gives

\[
                         (B')^{7/3-\eta_0}
\tag{19}
\]

for a fixed eta0>0 in fixed neighborhoods. Shrink those neighborhoods
so that (19) still saves a fixed power relative to (13), exactly as
in the source's normalization check.

This is the only place where the source needs a prime-convolution
coefficient class. Formula (7) and the exact short Möbius identity
supply a legitimate replacement. Neither primality nor roughness
is inferred for the actual coefficients.

## 8. Parameter order, conclusion and scope

Fix beta, the angular/ray data and the smooth test class first. Fix a
small kappa for (14). Apply the exceptional adapter and compactness
to choose uniform neighborhoods and a positive high-conductor gap.
Choose delta and then delta' sufficiently small for those neighborhoods,
(11)--(12), the extra twists and exclusions in (18), and the retained
scale inequalities. Finally choose every large-sieve and reciprocal
epsilon loss smaller than the fixed gaps; choose transform decay orders
large enough to make all discarded tails smaller than them. The
original seminorms are fixed and only a finite number is used.

For a fixed f,m,l, multiplication by the Poisson prefactor and the
cube-factor count restores the source's benchmark identity

\[
 \frac{AF}{MB}\frac{J^{1/3}(B')^2}{\mathcal Q}
       = k^{1/3}M^{-2/3}F^{-5/3}L^{-2}.
\tag{20}
\]

The f,m,l sums converge with these weights and the divisor bounds.
The rapidly decaying k and Mellin weights remain integrable, also
after the fixed polynomial losses. Hence Sections 5--7 bound the
complete off-diagonal by Q X^(-eta) for some fixed eta>0, plus terms
already bounded by AB. Section 4 proves the complementary H range.
Restoring the diagonal proves (2) and then (3).

This theorem retains the full all-row norm and the complete Möbius
coefficient, all common-divisor and cube-factor zeros, and every
Poisson frequency. It proves an actual power improvement over the
generic cubic large-sieve term for this one structured coefficient
vector. It is not an arbitrary-coefficient operator norm.

The initial puncture set S and theta's conductor are fixed. Arbitrary
moving initial punctures are not asserted: although (5) permits them,
the exceptional adapter requires its extra exclusion to be small near
the limiting configurations. The generated f,l,j exclusions meet that
requirement by (17)--(18).

The angular order may be any fixed integer, including -2. The proposed
all-unitary boundary source supplies ZF_beta for any beta strictly
above its stated source-qualified boundary, if that input is adopted.
The value of eta is not numerically optimized. The range is all A>=B>=2;
the physical first cubic Poisson of a short-row inverse moment can
instead have B>A. The original sextic nonsquare complement also has
additional characters and completion factors. No transposition,
conductor reduction, or smaller global boundary is inferred from (2).
