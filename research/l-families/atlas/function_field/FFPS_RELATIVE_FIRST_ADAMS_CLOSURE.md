# Relative-first closed-point Adams extraction

Status: **exact categorical composition theorem, exact four-profile theorem
for the clean ternary physical deck layer, and conditional trace gate; no
native complete-source adapter, uniform trace estimate, or proof of RH/GRH**

Architecture: **Architecture B only** — family/sheaf amplification.  This
packet does not invoke the beta primitive-pair criterion.

Bounded exact replay:
[`ffps_relative_first_adams_closure.py`](ffps_relative_first_adams_closure.py).
Canonical summary:
[`ffps_relative_first_adams_closure.json`](ffps_relative_first_adams_closure.json).

Frozen source: PR #757 head
`b870366141fe8d5f43d5b81f6e50a67d2a888070`, especially the cyclic torsor
relative projector, universal ternary norm torsor, closed-point Adams
compression, principal-anomaly dichotomy, and cyclic closure budget pinned by
the replay.

## 0. Outcome

The predecessor correctly asks whether the complete native ternary source is
a separable bivariate Weil class, or carries commuting partial Frobenii, so
that two independent closed-place degrees can be extracted by Adams--Möbius
inversion.  It also proves the exact torsor identity

\[
 \mathsf C-\mathsf S=\Pi_0.
\tag{0.1}
\]

The two facts should be composed in the opposite order from the naive family
route:

```text
common native source gluing
  -> apply the relative projector C-S=Pi_0
  -> simplify the resulting relative object
  -> prove partial Frobenius only for that object
  -> perform closed-point Adams extraction
  -> estimate the signed extracted principal trace.
```

In particular, **subtract before Adams extraction**.  The load-bearing
categorical interface is weaker than requiring the hard and selected
summands separately to admit partial Frobenius:

> **only the relative class needs partial Frobenius.**

This matters because every common resonant constituent and every faithful
cubic selected line has already cancelled from the relative projector before
an absolute value, Betti norm, or extension-field estimate is taken.

Let `X,Y/F_q` be the two fixed closed-point spaces.  Suppose the complete
common source cleanup produces a relative class

\[
 \mathfrak R\in\mathscr E(X,Y)
 =K_0^{\rm Weil}(X)_{\mathbf Q}
  \otimes K_0^{\rm Weil}(Y)_{\mathbf Q},
\tag{0.2}
\]

or, more generally, a bivariate Weil class with commuting partial Frobenii.
Assume its trace is exactly the native principal difference after every
owner, Boolean, Artin--Schreier, incidence, Wick, endpoint, and normalization
operation.  Then the existing two-place closed-point theorem applies directly:

\[
 \boxed{
 ab\,P_{a,b}(\mathfrak R)
 =\sum_{e\mid a}\sum_{f\mid b}
 \mu(e)\mu(f)
 A_{a/e,b/f}^{\partial}
 \!\left(\psi_1^e\psi_2^f\mathfrak R\right).}
\tag{0.3}
\]

If equal places must be excluded when `a=b`, retain the exact correction

\[
 \boxed{
 P_{a,a}^{\ne}(\mathfrak R)
 =P_{a,a}(\mathfrak R)-P_a(\delta\mathfrak R).}
\tag{0.4}
\]

No estimate for `C` or `S` appears in (0.3).  No `CYSEL` theorem is required
on this signed route.  No post-hoc family-to-principal amplifier is required
either: the principal object is already the image of `Pi_0` under the common
source functor.

For the clean ternary physical layer, the relative class has only **four
physical parity profiles** under every pair of partial Adams operations.  Put

\[
 R_2=\sum_{\alpha\in\widehat{C_2^2}}\alpha,
 \qquad
 \mathcal R_{\rm phys}=R_{2,X}\boxtimes R_{2,Y}.
\tag{0.5}
\]

Then

\[
 \boxed{
 \psi_1^e\psi_2^f\mathcal R_{\rm phys}
 =\begin{cases}
 R_{2,X}\boxtimes R_{2,Y},&e,f\text{ odd},\\
 4\mathbf1\boxtimes R_{2,Y},&e\text{ even},\ f\text{ odd},\\
 R_{2,X}\boxtimes4\mathbf1,&e\text{ odd},\ f\text{ even},\\
 16\mathbf1\boxtimes\mathbf1,&e,f\text{ even}.
 \end{cases}}
\tag{0.6}
\]

These are the four physical parity profiles.  Every row has absolute weighted character-line mass `16`.  The cubic
modulo-three profile has disappeared completely.  This is a genuine
simplification of the finite physical deck layer.

It is not a four-estimate proof of the full trace theorem.  In particular, the non-deck Frobenius eigenvalues still depend on the full exponents.  After source
pushforward, **the non-deck Frobenius eigenvalues still depend on the full
exponents** `e,f`, not only their parity.  Uniform Betti and signed-trace
control across the entire divisor-indexed Adams tower remains open.

## 1. Relative-first categorical theorem

Work in an idempotent-complete characteristic-zero linear category in which
the split cyclic torsor object `\mathcal H` carries the endomorphisms
`\mathsf C`, `\mathsf S`, and `\Pi_0` of the frozen relative-projector packet.
It proves

\[
 \mathsf C-\mathsf S=\Pi_0,
 \qquad
 \operatorname{im}\Pi_0\simeq E.
\tag{1.1}
\]

Let `F` be the one common additive cleanup functor implementing the native
source restrictions and pushforwards.  Additivity gives

\[
 F(\mathsf C)-F(\mathsf S)=F(\Pi_0).
\tag{1.2}
\]

Because the category is idempotent complete, the right side is represented by
an actual split relative object

\[
 \mathfrak R=F(\operatorname{im}\Pi_0).
\tag{1.3}
\]

The key point is logical.  Closed-point extraction is now applied to
`\mathfrak R` itself.  It is unnecessary to prove that the two larger objects
`F(\mathsf C)` and `F(\mathsf S)` separately belong to the partial-Frobenius
category.  It suffices to prove:

```text
NATREL:
  (1.2) is the exact complete native hard-selected-principal identity.

RELPARTFROB:
  R=F(im Pi_0) descends to the separable trace group or to a bivariate
  Weil category with commuting partial Frobenii.
```

This is strictly weaker as an interface: two coupled summands can have a
separable or partial-Frobenius difference after their common cubic and
resonant constituents cancel.

If all three objects already lie in the partial-Frobenius category, Adams
additivity also gives, for every `e,f>=1`,

\[
 \psi_1^e\psi_2^fF(\mathsf C)
 -\psi_1^e\psi_2^fF(\mathsf S)
 =\psi_1^e\psi_2^f\mathfrak R.
\tag{1.4}
\]

Equation (1.4) is useful for auditing an existing construction, but it is not
an additional assumption in the relative-first formulation.  One may build
`\mathfrak R` directly from the transported invariant projector.

Adams is applied **after** the source pushforward.  No commutation of Adams
operations with `F` is asserted or needed.

## 2. Exact closed-point extraction and its true cost

For one compatible class `V` on a fixed `F_q`-space, the frozen theorem is

\[
 dP_d(V)=\sum_{e\mid d}\mu(e)A_{d/e}(\psi^eV).
\tag{2.1}
\]

Tensoring the two one-place identities, or using commuting partial Frobenii,
proves (0.3).  Only squarefree divisors survive, so the number of nonzero
extension-field trace terms is exactly

\[
 2^{\omega(a)+\omega(b)}.
\tag{2.2}
\]

Consequently the following termwise estimate is sufficient.  If, uniformly
for every nonzero divisor pair in (0.3),

\[
 \left|
 A_{a/e,b/f}^{\partial}
 (\psi_1^e\psi_2^f\mathfrak R)
 \right|
 \le \mathcal B(a,b;Y),
\tag{2.3}
\]

then

\[
 \boxed{
 |P_{a,b}(\mathfrak R)|
 \le {2^{\omega(a)+\omega(b)}\over ab}\,
 \mathcal B(a,b;Y).}
\tag{2.4}
\]

For the distinct equal-degree row, (0.4) adds at most
`2^{\omega(a)}/a` one-place terms with its own diagonal trace budget.
The divisor factor is subpower.  Thus the exponential full-`S_d` cycle
selector has disappeared; the remaining difficulty is entirely in the
uniform trace budget `\mathcal B` and in the native source recombination.

A termwise triangle inequality is only a sufficient gate.  The potentially
weaker and more faithful target is the assembled signed estimate

\[
 \boxed{
 \sum_{e\mid a}\sum_{f\mid b}
 \mu(e)\mu(f)
 A_{a/e,b/f}^{\partial}
 (\psi_1^e\psi_2^f\mathfrak R)
 = (ab)\,Y^{o(1)},}
\tag{2.5}
\]

with the exact source weights and all conductor/degree summations retained
before the outer absolute value.  Call this gate `RELTRACE`.  It may exploit
cancellation between Adams rows that (2.3) discards.

## 3. Four physical parity profiles

The clean ternary universal norm torsor has physical deck group

\[
 G_{\rm phys}=C_2^4\times C_3.
\]

The hard and selected classes can be written as

\[
\begin{aligned}
 \mathcal S_\varepsilon
 &=\frac14\sum_{\alpha,\beta}
   \sum_{r=1}^2
   (\alpha\otimes\kappa_X^r)
   \boxtimes
   (\beta\otimes\kappa_Y^{\varepsilon r}),\\
 \mathcal C_\varepsilon
 &=R_{2,X}\boxtimes R_{2,Y}+\mathcal S_\varepsilon.
\end{aligned}
\tag{3.1}
\]

Subtracting gives (0.5), independently of the relative alignment
`\varepsilon`.  For a character `\alpha` of `C_2^2`, Adams sends
`\alpha` to `\alpha^e`.  Therefore

\[
 \psi^eR_2=
 \begin{cases}
 R_2,&e\text{ odd},\\
 4\mathbf1,&e\text{ even}.
 \end{cases}
\tag{3.2}
\]

Taking the external product proves (0.6).  Its four rows have respectively
`16,4,4,1` distinct characters with multiplicities `1,4,4,16`; every row has
absolute weighted line mass `16`.

This proves three exact simplifications.

1. The selected cubic lines and their mod-three Adams cases cancel before
   estimation.
2. The relative physical rank/mass is `16`, not the hard rank `48` or the
   hard absolute weighted mass `24`.
3. Every physical Adams transform is one of four tame finite-deck types.

It does **not** bound the compactly supported cohomology created by the
owner/Boolean/Artin--Schreier/source pushforward.  If that pushforward has
Frobenius eigenvalues `\lambda_j`, partial Adams replaces them by
`\lambda_j^e` and `\lambda_j^f`; those powers retain the full divisor data.

## 4. Exact conditional closure architecture

The signed family/sheaf route can now be stated without a vague
family-to-principal step.

```text
NATREL
  complete native source gluing carries C-S=Pi_0 through every common cleanup

RELPARTFROB
  the transported relative object F(im Pi_0), by itself, has commuting
  partial Frobenii or a finite external-product presentation

CLOSED-POINT ADAMS
  exact formula (0.3), including the equal-place correction

RELTRACE
  conductor-uniform subpower bound for the signed Adams-Mobius recombination

PRINCIPAL BINDING
  the resulting trace is the frozen native principal moment at the exact
  horizon, endpoint, diagonal, and normalization

FROZEN PRINCIPAL CONSUMER
  the native principal subpower estimate implies BCI and RH.
```

Under those hypotheses,

\[
 \boxed{
 \mathrm{NATREL}+\mathrm{RELPARTFROB}+\mathrm{RELTRACE}
 +\mathrm{PRINCIPAL\ BINDING}
 \Longrightarrow\mathrm{RH}.}
\tag{4.1}
\]

The implication is formal after the named hypotheses.  None of the four
load-bearing hypotheses is proved here for the complete native source.

The phrase “principal individualization” needs a firewall.

- On this **signed relative route**, individualization is equation (1.2): the
  principal member is already `F(im Pi_0)`.  No later amplifier is needed.
- For a **positive hard-family estimate** that has discarded `C-S`, the old
  principal-individualization gap remains.  This packet does not convert a
  positive family average into a principal estimate.

## 5. What remains genuinely geometric

The relative-first order removes work that is not logically necessary, but it
does not solve the geometric gates.

### 5.1 Native source gluing

One must construct a single object carrying, before subtraction:

- both complete Boolean source sums;
- owner/core factorization and the actual `Pc^2,Qd^2` maps;
- both source-selected Artin--Schreier phases;
- shared incidence and root cleanups;
- Wick subtraction and equal-product removal;
- the signed varying-conductor recombination;
- the exact horizon and endpoint conventions.

Every cleanup must be common and equivariant so that (1.2) remains the native
identity rather than a clean local surrogate.

### 5.2 Relative partial Frobenius

The full hard or selected object may remain coupled.  The sharper question is
whether the invariant-projector image simplifies enough to admit:

\[
 \mathfrak R=\sum_j c_jV_j\boxtimes W_j,
\tag{5.1}
\]

or an equivalent bivariate Weil structure.  A source-selected phase that
couples the two residues can still obstruct this after cubic cancellation.
That obstruction must be checked on `\mathfrak R`, not inferred from the
larger summands.

### 5.3 Uniform trace/Betti control

Rank `16` and four physical deck profiles are not total Betti bounds.  The
source pushforward, discriminant/resultant boundary, Artin--Schreier phases,
and Adams powers may create growing cohomology.  One must prove either the
assembled estimate (2.5) or a termwise theorem strong enough for (2.4), with
all constants uniform in the growing place degrees and conductor horizon.

### 5.4 Principal binding

The closed-point object must be identified coefficientwise with the exact
native principal moment consumed by the frozen RH implication.  A trace
identity for the clean ternary mask, a different horizon, or a degree-shell
average is not enough.

## 6. Scope firewall

This packet proves a composition and a smaller interface, not the missing
estimate.

- It does not construct NATREL.
- It does not prove RELPARTFROB for the native source.
- It does not prove RELTRACE or a uniform Betti theorem.
- It does not prove the new principal binding.
- The four parity profiles concern only the finite physical deck quotient.
- The non-deck Adams eigenvalues are not reduced to four cases.
- It does not prove `CYSEL`, `WCADD106140`, or `WCKUM106140`.
- It does not make any positive family moment individual.
- It makes no number-field transfer from function-field geometry.

**No native source adapter, uniform trace estimate, RH, or GRH is proved.**

## 7. Proof ledger

| statement | grade |
|---|---|
| common-functor relative identity (1.2)--(1.3) | **IMPORTED EXACTLY AND COMPOSED** |
| only the relative class needs partial Frobenius | **PROVED AS A SUFFICIENT CATEGORICAL INTERFACE** |
| direct relative closed-point formula (0.3) | **PROVED FROM THE FROZEN ADAMS THEOREM** |
| equal-place correction (0.4) | **IMPORTED EXACT** |
| four clean physical parity profiles (0.6) | **PROVED EXACT FINITE-CHARACTER ALGEBRA** |
| constant relative physical mass `16` | **PROVED EXACT** |
| termwise cost (2.4) | **PROVED BY TRIANGLE INEQUALITY** |
| conditional route (4.1) | **PROVED AS AN IMPLICATION OF THE NAMED GATES** |
| NATREL / RELPARTFROB / RELTRACE / principal binding | **OPEN** |
| RH or GRH | **NOT PROVED** |

No external novelty or priority claim is made for Adams operations, closed
point inversion, or cyclic projectors separately.

## 8. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_relative_first_adams_closure.py --check
python -B -O research/l-families/atlas/function_field/ffps_relative_first_adams_closure.py --check
python -B -m unittest tests.test_ffps_relative_first_adams_closure
python -B -O -m unittest tests.test_ffps_relative_first_adams_closure
```

The replay checks both ternary alignments, verifies subtraction before every
partial Adams pair through exponent `12`, exhausts the four physical parity
profiles, checks constant line mass `16`, verifies one- and two-place
Adams--Möbius extraction on exact synthetic closed-point eigenvalue packets,
checks the nonzero divisor-term counts, and checks the equal-degree diagonal
correction.  It enumerates no finite field, polynomial, place, curve,
conductor family, `L`-function, or zero.
