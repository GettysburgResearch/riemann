# The relative branch ledger: Kummer ramification cancels, the source-open boundary does not

Status: **exact local inertia, virtual-character, and curve-extension theorem
for the clean split tame `C_2^r` Kummer model; no varying-place FFPS
pushforward, source-compatible boundary filling, signed family estimate, RH,
or GRH claim**

Scope: one fixed clean fibre, one smooth curve or transverse trait, and finite
hypercube/Fourier algebra.  All statements about the native FFPS family after
a geometric pushforward are explicitly conditional.

Exact bounded replay:
[`ffps_relative_branch_cancellation_ledger.py`](ffps_relative_branch_cancellation_ledger.py).

Frozen dependencies:

| source | commit | git blob | role |
|---|---|---|---|
| `FFPS_BLOCK_RESONANCE_TOMOGRAPHY.md` | `b500d04ff` | `f7ed072177ee706d66ee0ba8b4b7ba65b41e5d35` | sharp `C_2^r` Fourier normalization and `C-S=Pi_0` |
| `FUNCTION_FIELD_CLOSED_PLACE_SUPPLY_TAX.md` | `a096d71b0` | `09c00c4f3f35d0a622840574b642aa73bf2e13af` | growing-place order statistic and modewise firewall |
| `FUNCTION_FIELD_BLOCK_ENTROPY_CONDUCTOR_PHASE_DIAGRAM.md` | `2365255a2` | `79278711a57e337a3a2f3678c642e0f02bcb9d00` | exact `log d_(r)/r` law and `theta` threshold |
| `FFPS_MULTISCALE_SINGLE_SQUARE_GATE.md` | `c24df1d98` | `851d6ecdd943a793b497277ce796ce4a32c38217` | joint-spectrum and varying-degree conductor ledger |
| `FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md` | `464c3705f` | `ab16e6c0894e51303119692e67b2f2bf59ba73e4` | honest torsor endomorphism and common-functor rule |

## 0. Exact verdict

The hard-minus-selected projector has a real local cancellation, but that
cancellation is not by itself the hoped-for growing-place escape.

Let `X` be a smooth proper curve over `F_q`, let `D` be a reduced finite
closed divisor, put `U=X-D`, and let

\[
 \pi:T\longrightarrow U
\]

be a split tame torsor with deck group

\[
 K=C_2^r,\qquad h=|K|=2^r.
\]

Write `H=pi_*E_T` and decompose the regular local system as

\[
 \mathcal H=\bigoplus_{s\in\mathbf F_2^r}\mathcal L_s.
\tag{0.1}
\]

For the sharp block mask, the hard package and the **unnormalized** selected
package are

\[
 \mathcal C=\bigoplus_s\mathcal L_s,
 \qquad
 \mathcal S=\bigoplus_{s\ne0}\mathcal L_s.
\tag{0.2}
\]

Therefore, already as an honest direct summand on `U`,

\[
 \boxed{\mathcal C-\mathcal S=\mathcal L_0=E_U.}
\tag{0.3}
\]

At every genuine quadratic branch place, all ramified Kummer constituents in
`C` and `S` have identical multiplicity.  Their tame Artin conductors cancel
before any modewise estimate.  This is stronger than cancellation of a trace
or of a geometrically constant stratum.

There are then two different extension ledgers.

1. Termwise middle/maximal extension fills the surviving principal line:

   \[
    \boxed{\operatorname{ME}(\mathcal C)
      -\operatorname{ME}(\mathcal S)=E_X,}
    \qquad \operatorname{cond}(E_X)=0.
   \tag{0.4}
   \]

2. If the native source is supported only on the common clean open and hence
   uses extension by zero, then

   \[
    \boxed{
    [j_!\mathcal C]-[j_!\mathcal S]
      =[j_!E_U]=[E_X]-[i_*E_D].}
   \tag{0.5}
   \]

   The relative object has generic rank one, zero boundary stalk, and exact
   conductor divisor `D`.  In particular,

   \[
    \boxed{\deg\operatorname{cond}(j_!E_U)=\deg D.}
   \tag{0.6}
   \]

Thus the nonprincipal **ramification** cancels, but the clean-source
**support deletion** survives once per geometric boundary point.  If `D`
contains a selected closed place of degree `D_max`, the common-open relative
object still pays at least `D_max`.  Under the order statistic of the supply
packet this is

\[
 n^{\alpha/\delta-o(1)}.
\tag{0.7}
\]

The place-degree exponent is therefore **not avoided by representation-ring
algebra alone**.  It can disappear only after proving that the actual source
permits the common middle extension, or that the boundary skyscraper in
(0.5) is absorbed or cancelled by an independently constructed geometric
boundary term.  That is a pushforward/source theorem, not a Fourier theorem.

In the `d_(r)^theta` language of the entropy--conductor phase diagram, the
verdict is exact and three-part:

| realization of the relative class | local loss exponent | status |
|---|---:|---|
| abstract common middle extension | `theta=0` | **PROVED FOR THE FIXED CLEAN TORSOR** |
| common-open/extension-by-zero source | `theta=1` | **PROVED BY (0.5)--(0.6)** |
| native varying-place FFPS complex | undecided between these ledgers | **REQUIRES GEOMETRIC IDENTIFICATION** |

Thus the local `K_0` calculation makes `theta=0` genuinely plausible and
constructs it in the abstract fixed-fibre model; it simultaneously proves a
surviving linear boundary term for the common-open model.  It does not choose
the physical row.  Since the exact phase threshold is
`theta<delta log(5/4)`, the `theta=1` row loses decisively for either eligible
place density, while the `theta=0` row would cross the conductor threshold.

## 1. One block and one branch place

Start with `r=1`.  At a genuine tame quadratic branch place `v`, let `kappa`
be the nontrivial character of local inertia.  The complete ledger is

| package on `U` | inertia character | rank | inertia invariants | tame Artin conductor |
|---|---:|---:|---:|---:|
| hard `C` | `1+kappa` | `2` | `1` | `1` |
| unnormalized selected `S` | `kappa` | `1` | `0` | `1` |
| relative `C-S` | `1` | `1` | `1` | `0` |

For a closed point of degree `d`, the two first rows each contribute `d` to
the conductor degree and the open relative row contributes zero.  The
quadratic branch is gone coefficient by coefficient, not estimated.

This statement uses the unnormalized selected package.  In the sharp
`C_2` case it is the honest Kummer summand of the regular torsor sheaf.  The
atom-free object is different even at `r=1`: it is `Pi_0-Pi_1`, whose local
character is `1-kappa`, so it remains ramified.

## 2. Exact all-rank local inertia theorem

At a boundary point `v`, local tame inertia maps to an element

\[
 \lambda_v\in K.
\tag{2.1}
\]

The restriction of `L_s` to inertia is `kappa^(<s,lambda_v>)`.  When
`lambda_v` is nonzero, its kernel is a hyperplane of order `h/2`.  The zero
label lies in that hyperplane.  Consequently

\[
 \boxed{
 \begin{aligned}
 \mathcal C|_{I_v}
   &= {h\over2}\,1\oplus {h\over2}\,\kappa,\\
 \mathcal S|_{I_v}
   &= \left({h\over2}-1\right)1
      \oplus {h\over2}\,\kappa,\\
 (\mathcal C-\mathcal S)|_{I_v}&=1.
 \end{aligned}}
\tag{2.2}
\]

The rank/invariant/conductor ledger is therefore

| package | rank | inertia invariants | Swan | tame Artin conductor |
|---|---:|---:|---:|---:|
| `C` | `h` | `h/2` | `0` | `h/2` |
| unnormalized `S` | `h-1` | `h/2-1` | `0` | `h/2` |
| `C-S` | `1` | `1` | `0` | `0` |

Every one of the `h/2` characters ramified at `v` is nonprincipal and hence
occurs in both `C` and `S`.  The `h/2-1` unramified nonprincipal characters
also cancel.  The only survivor is the globally principal line.

If `lambda_v=0`, every line is unramified and (0.3) still holds.  The
nonzero hypothesis is used only for the half-hypercube census, not for the
relative identity.

Because tame inertia on a curve is procyclic, its image in an elementary
two-group has order at most two.  Thus (2.2) covers every local inertia type
in this clean quadratic model.  It does not assert that the native
varying-place FFPS source has already been put on one such torsor.

## 3. Normalization firewall

Put

\[
 \overline{\mathcal S}={1\over h-1}\mathcal S.
\tag{3.1}
\]

This is a rational endomorphism or a class in a rationalized representation
ring; it is not generally an honest direct-summand object.  Three expressions
that look similar have different local characters.

### 3.1 Hard minus unnormalized selected

\[
 \boxed{\mathcal C-\mathcal S=\Pi_0.}
\tag{3.2}
\]

Its Kummer coefficient is zero at every branch place.  This is the exact
relative cancellation theorem.

### 3.2 Hard minus normalized selected

\[
 \mathcal C-\overline{\mathcal S}
 =\Pi_0+{h-2\over h-1}\mathcal S.
\tag{3.3}
\]

For `h>2` it retains every nonprincipal line.  At a branch place its
`kappa` coefficient is

\[
 {h(h-2)\over2(h-1)}.
\tag{3.4}
\]

Only the accidental one-block equality `h=2` makes (3.3) principal.

### 3.3 Atom-free off-coset interferometer

The atom-free normalized object is

\[
 \mathcal I=\Pi_0-\overline{\mathcal S}.
\tag{3.5}
\]

At a nonzero local inertia vector, (2.2) gives

\[
 \boxed{
 \mathcal I|_{I_v}
 ={h\over2(h-1)}(1-\kappa).}
\tag{3.6}
\]

Its virtual rank is zero, but its ramified-character coefficient is nonzero.
The integral numerator

\[
 (h-1)\mathcal I=(h-1)\Pi_0-\mathcal S
\]

restricts to `(h/2)(1-kappa)`.  Hence atom deletion in the pair kernel does
not imply branch cancellation in local inertia.

The signed Artin conductor of a virtual class such as (3.6) can be negative.
It is additive bookkeeping, not a positive complexity norm.  The absolute
ramified coefficient of (3.6) is

\[
 {h\over2(h-1)}>{1\over2},
\tag{3.7}
\]

so a separate absolute estimate still sees a fixed fraction of every branch
degree.  This is why the atom-free normalization cannot be substituted for
the unnormalized `S` in (3.2).

## 4. Extension, support, and conductor

For a constructible sheaf `F` on `X`, use the local total-conductor
coefficient

\[
 c_v(\mathcal F)
 =\operatorname{rank}(\mathcal F_{\bar\eta})
  -\dim\mathcal F_{\bar v}
  +\operatorname{Swan}_v(\mathcal F).
\tag{4.1}
\]

This definition records both monodromy and a missing boundary stalk and is
additive in the Grothendieck group.  At a genuine branch point, the exact
extension ledger is

| package | generic rank | middle-extension stalk | middle `c_v` | zero-extension stalk | zero `c_v` |
|---|---:|---:|---:|---:|---:|
| `C` | `h` | `h/2` | `h/2` | `0` | `h` |
| unnormalized `S` | `h-1` | `h/2-1` | `h/2` | `0` | `h-1` |
| `C-S` | `1` | `1` | `0` | `0` | `1` |

Thus common middle extension cancels both the Kummer conductor and the
boundary drop.  Common extension by zero cancels all selected constituents
but leaves one principal drop.

The support ledger is equally explicit.

| relative object | generic rank | nonzero-stalk locus | support closure | singular locus | conductor degree from `D` |
|---|---:|---|---|---|---:|
| `E_U` | `1` | `U` | `U` | none on `U` | `0` on `U` |
| `j_!E_U` | `1` | `U` | `X` | `D` | `deg D` |
| `E_X` | `1` | `X` | `X` | empty | `0` |
| `i_*E_D` | `0` generically | `D` | `D` | boundary-supported | length `deg D` |

Here “support closure” means the closure of the generic support; the stalk
support of `j_!E_U` excludes `D`.  On a curve its singular support has the
zero section over `U` and the boundary cotangent directions over `D`.

The localization triangle for the constant sheaf is

\[
 j_!E_U\longrightarrow E_X\longrightarrow i_*E_D\longrightarrow,
\tag{4.2}
\]

which proves (0.5).  The difference between the two possible relative
extensions is not invisible.  At extension degree `m`, its trace is

\[
 \boxed{
 B_D(m)=\#D(\mathbf F_{q^m})
 =\sum_{\substack{v\in D\\ \deg v\mid m}}\deg v.}
\tag{4.3}
\]

A degree-`d` boundary place contributes zero when `d` does not divide `m`
and contributes exactly `d` whenever it does.  In particular, the boundary
cannot be declared uniformly bounded merely because it has no
`F_q`-rational point.

## 5. Consequence for the closed-place supply tax

In the bilateral block model, let the selected branch divisor contain the
closed places used by the two sides and write

\[
 \deg D=T=\sum_i(\deg\ell_i+\deg\rho_i).
\tag{5.1}
\]

The modewise maximal-extension average in the multiscale packet is of order
`T/2`.  The relative open representation improves the spectral ledger all
the way to one unramified line.  But if the source still deletes `D`, its
extension-by-zero realization has

\[
 \boxed{\deg\operatorname{cond}(\mathcal R_!)=T\ge D_{\max}.}
\tag{5.2}
\]

Therefore relative cancellation removes the exponential mode census and all
nonprincipal inertia, but it does not improve the exponent of the largest
place degree in a common-open estimate.  Combining (5.2) with the supply
order statistic, and more sharply with

\[
 {\log d_{(r)}\over r}\xrightarrow{\Pr}{1\over\delta}
 \qquad(r\to\infty,\ r=o(\log n)),
\tag{5.3}
\]

gives the relative zero-extension loss

\[
 d_{(r)}^1
 =\exp((1/\delta+o_{\Pr}(1))r).
\tag{5.4}
\]

At the earlier logarithmic rank scale it gives the same lower scale

\[
 \deg\operatorname{cond}(\mathcal R_!)
 \ge n^{\alpha/\delta-o(1)}
\]

in the logarithmic high-probability sense of the supply packet, conditional
on transferring that random-core law to the relevant weighted source.

In particular, the common-open class has `theta=1`, not merely an unknown
positive power.  The exact gain criterion

\[
 \theta<\delta\log(5/4)
\tag{5.5}
\]

rejects it.  The middle-extended fixed-fibre class has `theta=0` and passes
this exponent test, but identifying it with the native source is still open.

There is one genuine escape left.  If the physical relative statistic is
shown to equal the trace of the common middle extension, then the local
relative conductor is zero and the place-degree tax disappears from that
object.  Equivalently, one must prove that the boundary term (4.3) is already
present with the correct sign in the source or cancels against another
geometric boundary complex.  No such identity follows from `C-S=Pi_0`.

## 6. Representation algebra versus geometric pushforward

The following claims are proved before any geometric pushforward:

- the hyperplane census (2.2) at every local inertia vector;
- equality of the ramified multiplicities in `C` and unnormalized `S`;
- the honest open summand identity `C-S=E_U`;
- the normalization formulas (3.3)--(3.7);
- the localization class (0.5) after choosing a fixed open immersion;
- the local ranks, stalk ranks, and conductor coefficients in Section 4;
- the fixed-divisor trace tower (4.3).

The following steps require geometry beyond representation-ring algebra:

1. construct one varying-closed-place torsor or correspondence carrying the
   actual hard and selected FFPS terms;
2. prove that owner, core, coprimality, incidence, diagonal, root, and Wick
   cleanups are common and equivariant;
3. identify the native source statistic with middle extension rather than
   extension by zero, or construct the missing boundary correction;
4. after a family map `f`, control or cancel

   \[
    R(f\circ i)_!E_D
   \]

   in the pushed-forward localization triangle;
5. prove uniform Betti/conductor control while `D` and its residue fields
   vary with the source.

An additive pushforward preserves the identity, but it does not annihilate
the boundary:

\[
 Rf_!j_!E_U
 =Rf_!E_X-R(f\circ i)_!E_D
 \quad\text{in }K_0.
\tag{6.1}
\]

Any assertion that the last term vanishes, cancels, or is harmless is a new
geometric theorem.  This packet makes no such assertion.

## 7. Proof ledger

| statement | grade |
|---|---|
| one-block inertia ledger | **PROVED EXACT** |
| all-`r` hyperplane census (2.2) | **PROVED EXACT FINITE FOURIER ALGEBRA** |
| open relative object `C-S=E_U` | **PROVED EXACT ON A GENUINE SPLIT TORSOR** |
| normalized and atom-free firewall | **PROVED EXACT IN `R(I_v) tensor Q`** |
| common middle-extension ledger | **PROVED TERMWISE ON THE FIXED CLEAN CURVE** |
| zero-extension boundary triangle and conductor `deg D` | **PROVED EXACT** |
| boundary Frobenius tower (4.3) | **PROVED EXACT FOR A FIXED REDUCED DIVISOR** |
| persistence of the supply exponent for `j_!` | **CONDITIONAL ONLY ON THE IMPORTED SOURCE ORDER STATISTIC** |
| native varying-place torsor and common cleanup | **NOT CONSTRUCTED** |
| source-compatible middle extension or boundary absorption | **OPEN / CENTRAL** |
| pushed-forward uniform trace estimate, RH, or GRH | **OPEN / UNPROVED** |

The elementary local character algebra is not claimed as externally novel.
The project contribution is the exact normalization/extension ledger: it
separates cancellation of Kummer inertia from cancellation of the
closed-place support tax.

## 8. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/ffps_relative_branch_cancellation_ledger.py --check
python -B -O research/l-families/atlas/function_field/ffps_relative_branch_cancellation_ledger.py --check
python -B -m unittest tests.test_ffps_relative_branch_cancellation_ledger
python -B -O -m unittest tests.test_ffps_relative_branch_cancellation_ledger
python -B -m ruff check research/l-families/atlas/function_field/ffps_relative_branch_cancellation_ledger.py tests/test_ffps_relative_branch_cancellation_ledger.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_relative_branch_cancellation_ledger.py tests/test_ffps_relative_branch_cancellation_ledger.py
```

The replay enumerates at most `2^10` binary character labels.  It verifies
the local hyperplane census, every normalization, the two extension ledgers,
and a small exact boundary trace tower.  It enumerates no finite-field point,
closed place, curve, source atom, pushforward, conductor family,
`L`-function, or zero.
