# General cyclic resonance no-go and exact relative projector

Status: **exact all-\(k\) cyclic Fourier theorem, exact distinct-collision
no-go, and exact finite-fibre relative projector; no common
varying-conductor derived complex is constructed**.

## Start here

Let \(S\subset\mu_k\) be a nonempty retained set of size \(t\), with
\(t<k\), and put

\[
 c_r={1\over t}\sum_{s\in S}s^{-r},
 \qquad
 u=\sum_{r=1}^{k-1}|c_r|^2={k\over t}-1.
\tag{0.1}
\]

For two source atoms in one fixed physical fibre, write

\[
 g={\Phi(\omega_1)\over\Phi(\omega_2)}\in\mu_k.
\]

The averaged normalized hard-current kernel and its positive selected-energy
kernel are exactly

\[
 \boxed{
 K_C(g)={k\over t^2}|S\cap gS|,}
\tag{0.2}
\]

\[
 \boxed{
 K_S(g)=\sum_{r=1}^{k-1}|c_r|^2g^r
       ={k\over t^2}|S\cap gS|-1.}
\tag{0.3}
\]

Consequently

\[
 \boxed{K_C(g)-K_S(g)=1\qquad(g\in\mu_k).}
\tag{0.4}
\]

On every **orientation-preserving distinct-atom double physical collision**

\[
 \omega_1\ne\omega_2,\qquad
 X_1=X_2,\qquad Y_1=Y_2,
\tag{0.5}
\]

one has \(g=1\), and hence

\[
 \boxed{
 K_C(1)={k\over t}=1+u,\qquad
 K_S(1)=u>0,\qquad
 K_C(1)-K_S(1)=1.}
\tag{0.6}
\]

The result has three deliberately separate meanings.

1. **Geometric multiplicity.** If
   \[
   m(S)=\#\{1\le r<k:c_r\ne0\},
   \]
   then \(m(S)\) selected rank-one character systems restrict to
   geometrically constant systems on (0.5).
2. **Arithmetic coefficient.** Their weighted Frobenius trace on (0.5) is
   \(u=k/t-1\), because every arithmetic scalar is exactly \(1\).
3. **Wick scope.** Literal Wick subtraction removes only
   \(\omega_1=\omega_2\). It does not remove the distinct pairs in (0.5).

No proper mask can null (0.6). Rotation of \(S\) preserves every
\(|c_r|^2\), \(m(S)\), and the complete kernel. Changing the shape of \(S\)
at fixed \(t/k\) can redistribute or delete character labels, but Parseval
fixes their total collision coefficient at \(u\). Every
leverage-improving hard mask is proper, so every such mask carries this
resonance.

There is nevertheless an exact **relative** remedy. The hard current already
contains precisely the same selected Fourier channels, plus the principal
channel. In the normalized finite cyclic group algebra,

\[
 \boxed{
 \widetilde{\mathsf C}_S
 =\Pi_0+\sum_{r=1}^{k-1}|c_r|^2\Pi_r,\qquad
 \widetilde{\mathsf S}_S
 =\sum_{r=1}^{k-1}|c_r|^2\Pi_r,\qquad
 \widetilde{\mathsf C}_S-\widetilde{\mathsf S}_S=\Pi_0.}
\tag{0.7}
\]

Thus the nuisance coefficient \(u\) cancels in \(C-S\) on (0.5), leaving the
intended principal coefficient \(1\). This is the exact finite-fibre
projector behind \(P=C-S\).

There is an even earlier signed identity:

\[
 {1\over k}\sum_{j=0}^{k-1}O_j=P.
\tag{0.8}
\]

Rotation averaging removes every selected mode at the **amplitude** level.
It does not survive replacement by a positive squared assembly: Parseval
then retains the full selected energy \(u\). Thus (0.8) is a genuine signed
projector, not a way to obtain hard-mask leverage from positive moments.

Lifting (0.7) through varying closed places and every FFPS cleanup would be
the strongest geometric route. The required common complex, compatible
cleanup functor, and Grothendieck-class identity are stated precisely below;
they are **not constructed here**.

The machine-readable companion exhausts all nonempty proper subsets of
\(C_k\) only for \(2\le k\le10\), with exact cyclotomic reduction. The all-\(k\)
proof is in Sections 2--5.

## 1. Frozen dependencies and scope

This packet uses:

- the all-\(k\) hard observation and centered identity in
  `FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md`, frozen at PR #756 head
  `6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`;
- the coefficient and invisible-direction ledger in
  `FFPS_CYCLIC_CLOSURE_BUDGET.md` at that same head;
- the leverage/selected-mass and Fourier-support results in
  `FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md` at commit
  `9e763fe5b`;
- the ternary geometric adapter in
  `FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md` at commit
  `8b4559a54`;
- the exact principal-anomaly fork in
  `FFPS_PRINCIPAL_ANOMALY_TRANSFER_DICHOTOMY.md` at commit
  `806f8c000`.

The present theorem is all-\(k\) finite cyclic Fourier algebra. Its geometric
claim concerns the character systems already source-realized on one fixed
clean physical fibre. It does not construct a mask simultaneously over
varying closed places, align their character groups globally, or prove a
family estimate.

The phrase **double physical collision** is typed carefully. Equation (0.6)
applies when the two corrected oriented physical coordinates agree, so that
\(\Phi(\omega_1)=\Phi(\omega_2)\). The even-character collision kernel also
contains components with

\[
 X_1=\pm X_2,\qquad Y_1=\pm Y_2.
\]

On a fixed sign component the quotient \(g=a\) is constant, so every selected
mode is still geometrically constant, but its arithmetic Frobenius scalar is
\(a^r\). Its total coefficient is \(K_S(a)\), not automatically \(u\).
Section 6 gives the exact firewall.

## 2. Fourier expansion of the rotated hard currents

Write \(G=\mu_k\), and let

\[
 O_j={k\over t}\sum_{\Phi(\omega)\in\zeta_k^jS}z_\omega,
 \qquad 0\le j<k.
\tag{2.1}
\]

For

\[
 H_r=\sum_\omega\Phi(\omega)^rz_\omega,
 \qquad 0\le r<k,
\]

one has \(H_0=P\) and the exact Fourier expansion

\[
 O_j=\sum_{r=0}^{k-1}
 c_r\zeta_k^{-jr}H_r,\qquad c_0=1.
\tag{2.2}
\]

Before squaring, averaging (2.2) over \(j\) gives

\[
 \boxed{{1\over k}\sum_{j=0}^{k-1}O_j=P.}
\tag{2.2a}
\]

Orthogonality across the rotations gives

\[
 {1\over k}\sum_{j=0}^{k-1}|O_j|^2
 =
 |P|^2+\sum_{r=1}^{k-1}|c_r|^2|H_r|^2.
\tag{2.3}
\]

This is an identity of complete quadratic kernels, before Wick subtraction.
The first term is the principal current and the remaining terms are the
positive selected energy.

Equations (2.2a) and (2.3) are an exact signed/positive boundary:

\[
 \begin{array}{ccl}
 \text{average amplitudes, then retain the result}
   &\Longrightarrow& \text{selected modes cancel},\\
 \text{square amplitudes, then average positively}
   &\Longrightarrow& \text{selected energies remain}.
 \end{array}
\tag{2.3a}
\]

The inverse-Gram hard gain belongs to the second construction. Importing the
first cancellation after the square would change the object being estimated.

For two atoms with quotient \(g=\Phi_1/\Phi_2\), the selected pair kernel is

\[
 K_S(g)=\sum_{r=1}^{k-1}|c_r|^2g^r,
\tag{2.4}
\]

up to replacing \(g\) by \(g^{-1}\) under the opposite harmless Fourier
convention.

There is also a direct hard-support count. A rotation contributes to the
pair exactly when both quotient values lie in that rotated copy of \(S\).
The number of such rotations is \(|S\cap gS|\). The normalized coefficient
\((k/t)^2\), followed by the average over \(k\) rotations, gives (0.2).
Comparing (2.3) with this count proves (0.3)--(0.4).

At \(g=1\), \(|S\cap S|=t\), so (0.6) follows. Parseval gives the same result:

\[
 1+\sum_{r=1}^{k-1}|c_r|^2={k\over t}.
\tag{2.5}
\]

## 3. The general distinct-collision no-go

On the source-realized physical fibre, each nonzero coefficient \(c_r\)
indexes the rank-one local system

\[
 \mathcal M_r
 =
 \operatorname{pr}_1^*\mathcal F_r
 \otimes
 \operatorname{pr}_2^*\mathcal F_r^\vee.
\tag{3.1}
\]

On (0.5), the defining quotient is \(1\). Therefore

\[
 \mathcal M_r|_{\Delta_{XY}^{\ne}}\simeq\mathbf1
\tag{3.2}
\]

geometrically and arithmetically for every \(r\) with \(c_r\ne0\). Here
\(\Delta_{XY}^{\ne}\) denotes the double physical collision with the literal
source diagonal removed.

The underlying geometric invariant multiplicity is

\[
 \boxed{m(S)=\#\{1\le r<k:c_r\ne0\}.}
\tag{3.3}
\]

The positive energy is not an unweighted direct sum: its channel \(r\) has
the scalar coefficient \(|c_r|^2\). The total arithmetic coefficient is

\[
 \boxed{\sum_{r=1}^{k-1}|c_r|^2=u={k\over t}-1.}
\tag{3.4}
\]

Thus \(m(S)\) and \(u\) must not be called the same multiplicity.

Nor should either be confused with the source contribution. An ordered
distinct pair contributes

\[
 u\,z_{\omega_1}\overline{z_{\omega_2}}.
\]

The kernel coefficient \(u\) is positive, but the off-atomic source sum is a
signed real quadratic ledger after conjugate pairs are combined. The theorem
does not assert that every collision stratum contributes a positive scalar
main term.

### Wick firewall

The three literal atomic coefficients in (2.3) are

\[
 {k\over t},\qquad
 {k\over t}-1,\qquad
 1
\tag{3.5}
\]

for hard, selected, and principal energy respectively. Wick normal ordering
subtracts those coefficients only on
\(\omega_1=\omega_2\). Since

\[
 {k\over t}-\left({k\over t}-1\right)=1,
\]

the centered identity remains exact. But a distinct pair in
\(\Delta_{XY}^{\ne}\) is untouched, and its coefficients remain (0.6).

This is different from the positive Wick **atomic** residual already proved
in PR #756. That residual compares a hard inequality with the full additive
phase cardinality. The present no-go identifies a non-atomic geometrically
constant selected channel.

## 4. No mask or rotation can null the exact collision

If \(S\) is rotated to \(bS\), then

\[
 c_r(bS)=b^{-r}c_r(S).
\tag{4.1}
\]

Therefore every \(|c_r|^2\), the mode count \(m(S)\), the total \(u\), and
the autocorrelation \(|S\cap gS|\) are invariant.

Changing the shape of \(S\) can change which \(c_r\) vanish. It cannot change

\[
 K_S(1)={k\over t}-1
\tag{4.2}
\]

at fixed \(t\). The only way (4.2) can vanish is \(t=k\), the complete mask.
That mask performs no hard deletion and has complete-frame leverage.
Consequently:

\[
 \boxed{
 \text{every proper cyclic hard mask, hence every leverage-improving one,
 has a nonzero exact-collision selected coefficient.}}
\tag{4.3}
\]

This is stronger than a ternary accident and weaker than a universal
arithmetic obstruction: it says that separate selected-mode cancellation
cannot follow merely by deleting the literal diagonal or rotating the mask.
The signed global source coefficients could still cancel after recombination.

## 5. How many geometrically constant modes?

Let \(R(S)\) be the Fourier support size including the constant coefficient.
Then \(m(S)=R(S)-1\). The elementary uncertainty argument gives

\[
 \boxed{
 m(S)\ge\left\lceil{k\over t}\right\rceil-1.}
\tag{5.1}
\]

Indeed, for \(f=\mathbf1_S\),

\[
 \|\widehat f\|_\infty\le\|f\|_1
 \le\sqrt t\,\|f\|_2,
\]

while Parseval gives

\[
 \|\widehat f\|_2^2=k\|f\|_2^2.
\]

If \(\widehat f\) has support \(R\), then
\(k\|f\|_2^2\le Rt\|f\|_2^2\), proving \(Rt\ge k\).

The bound is sharp. If \(t\mid k\) and \(S\) is a coset of the unique subgroup
of order \(t\), its Fourier support is the annihilator of size \(k/t\), so

\[
 m(S)={k\over t}-1.
\tag{5.2}
\]

If \(k\) is prime, every nonempty proper \(S\) instead has

\[
 \boxed{m(S)=k-1.}
\tag{5.3}
\]

For if a nonconstant coefficient vanished, the zero-one polynomial of \(S\)
would vanish at a primitive \(k\)-th root. It would be divisible by
\(1+X+\cdots+X^{k-1}\), forcing \(S\) to be empty or full.

Equations (5.1)--(5.3) quantify geometric complexity, not Betti complexity
after pushforward. Several character systems can become isomorphic on a
smaller source stratum, while boundary extensions can create additional
cohomology.

## 6. Sign-pair components: constant geometrically, different arithmetically

The exact \(g=1\) component is unavoidable. A broader even-character double
collision can have a fixed oriented quotient

\[
 g=a\in\mu_k.
\tag{6.1}
\]

Every \(\mathcal M_r\) is still geometrically constant there, because its
defining quotient is constant. Its arithmetic Frobenius scalar is \(a^r\),
and the weighted trace is

\[
 \boxed{
 K_S(a)
 =\sum_{r=1}^{k-1}|c_r|^2a^r
 ={k\over t^2}|S\cap aS|-1.}
\tag{6.2}
\]

This coefficient may be positive, negative, or zero. For example, with

\[
 k=8,\qquad S=\{1,\zeta_8,\zeta_8^2,-1\},
\]

the orientation-preserving component has \(K_S(1)=1\), but the sign-flipped
component \(a=-1\) has

\[
 |S\cap(-S)|=2,\qquad K_S(-1)=0.
\tag{6.3}
\]

Rotation cannot change (6.2), but mask shape can. Thus the correct theorem is:

- every fixed collision component has geometrically constant selected modes;
- the total coefficient \(u\) is forced specifically on \(g=1\);
- other sign components retain their arithmetic scalar ledger.

This is why geometric invariant multiplicity alone does not determine a
main term.

## 7. The exact finite-fibre signed projector

Let \(E\) contain the \(k\)-th roots of unity, and let
\(\Pi_r\) be the orthogonal Fourier idempotent on \(E[\mu_k]\) for character
\(g\mapsto g^r\). Normalize the hard covariance operator by the harmless
factor making each \(\Pi_r\) an actual projector. Equation (2.3) gives

\[
 \widetilde{\mathsf C}_S
 =\sum_{r=0}^{k-1}|c_r|^2\Pi_r
 =\Pi_0+\sum_{r=1}^{k-1}|c_r|^2\Pi_r.
\tag{7.1}
\]

Define

\[
 \widetilde{\mathsf S}_S
 =\sum_{r=1}^{k-1}|c_r|^2\Pi_r.
\tag{7.2}
\]

Then (0.7) follows as an equality of endomorphisms, not merely traces.
It holds at every quotient value, not just on the collision locus.

This is the strongest exact relative remedy currently available:

\[
 \boxed{\text{subtract the selected Fourier projector before estimating.}}
\tag{7.3}
\]

On the exact distinct collision, the hard coefficient \(1+u\) and selected
coefficient \(u\) leave the principal coefficient \(1\). The common
geometrically constant nuisance cancels; the intended principal channel does
not.

The identity does not prove a small trace. Its right side is precisely the
principal object whose global control is RH-bearing.

### Collision-local signed renormalization

At pure kernel level, define the exact distinct double-collision quadratic
ledger

\[
 \mathfrak D_{\Delta}^{\ne}(z)
 =
 \sum_{\substack{\omega_1\ne\omega_2\\
                  X_1=X_2,\ Y_1=Y_2}}
 z_{\omega_1}\overline{z_{\omega_2}}.
\tag{7.4}
\]

One may define

\[
 C^\flat=C-u\,\mathfrak D_{\Delta}^{\ne},
 \qquad
 S^\flat=S-u\,\mathfrak D_{\Delta}^{\ne}.
\tag{7.5}
\]

Then

\[
 C^\flat-S^\flat=C-S=P,
\tag{7.6}
\]

while the selected kernel on that stratum becomes zero and the hard kernel
becomes one. This is an exact signed bookkeeping operation. It destroys the
standalone positivity of the two pieces, estimates no collision sum, and
does not remove the other resonances classified by the cube criterion in the
ternary audit.

## 8. Precise conditional Grothendieck-class lift

The finite projector suggests a geometric construction, but trace-function
algebra is not automatically a derived-category identity.

Let \(U\) be one proposed common source stack and suppose the following data
are actually constructed:

1. a physical quotient map or torsor carrying all \(\mu_k\)-rotations;
2. hard-current correspondences \(\mathcal C_j\) on \(U\times U\);
3. selected character kernels
   \[
   \mathcal M_r
   =\operatorname{pr}_1^*\mathcal F_r
    \otimes\operatorname{pr}_2^*\mathcal F_r^\vee;
   \]
4. one exact/additive cleanup and pushforward functor \(\mathcal G\) applied
   identically to hard and selected objects;
5. all source weights, Tate shifts, arithmetic Frobenius structures, and
   boundary extensions matched.

Let \(E\) contain the Fourier coefficients. In the scalar-extended formal
trace class

\[
 K_0(D_c^b(U\times U,E))\otimes_{\mathbf Z}E,
\]

the desired lift is

\[
 \boxed{
 {1\over k}\sum_{j=0}^{k-1}[\mathcal C_j]
 -
 \sum_{r=1}^{k-1}|c_r|^2[\mathcal M_r]
 =
 [\mathcal P_0].}
\tag{8.1}
\]

If (8.1) holds **before** cleanup, additivity gives

\[
 \boxed{
 {1\over k}\sum_j[\mathcal G(\mathcal C_j)]
 -
 \sum_{r=1}^{k-1}|c_r|^2[\mathcal G(\mathcal M_r)]
 =
 [\mathcal G(\mathcal P_0)].}
\tag{8.2}
\]

Then matching constant constituents cancel in the relative class, including
the coefficient \(u\) on \(\Delta_{XY}^{\ne}\).

Five firewalls are load-bearing.

- The scalar coefficients \(|c_r|^2\) need not be integers or rational
  numbers. Thus (8.1) is a scalar-extended formal class, not automatically
  the class of one honest sheaf.
- Matching geometric multiplicity alone is insufficient. Tate shifts,
  arithmetic Frobenius scalars, source coefficients, and extension data must
  agree.
- Removing a stratum from only one side destroys (8.1).
- Numerical trace cancellation on finitely many fields does not construct a
  morphism, cone, or Grothendieck identity.
- Even a proved (8.2) identifies the remainder with the principal complex; it
  does not bound that complex.

No \(U\), \(\mathcal C_j\), \(\mathcal G\), or common complex satisfying these
requirements is constructed in this packet. Equation (8.1) is an exact
acceptance criterion for the proposed relative sheafification.

## 9. Relation to `CYSEL` and the principal anomaly

The no-go applies to a separate selected-mode estimate: one cannot argue that
nonprincipal character labels alone remove every constant constituent.
However,

\[
 P=C-S
\]

is already exact. The invisible displacement

\[
 (C,S,R)\mapsto(C+T,S+T,R-T)
\]

changes the common background and leaves \(P\) fixed. The collision
coefficient \(u\) is exactly such a matching local background in (0.7).

There are therefore two valid targets.

1. **Separate target:** classify and estimate all selected resonances,
   including \(\Delta_{XY}^{\ne}\), and prove `CYSEL`.
2. **Relative target:** construct (8.1)--(8.2), cancel matching constituents
   before absolute values, and estimate the remaining principal relative
   trace.

The relative route can avoid an unnecessarily strong separate bound. It
does not evade the principal theorem: after exact cancellation the remaining
object is \(\mathcal P_0\).

## 10. Exact proof grades

| statement | grade |
|---|---|
| hard and selected kernels (0.2)--(0.4) | **PROVED EXACT ALL-\(k\)** |
| exact-collision coefficient \(u=k/t-1\) | **PROVED EXACT ALL-\(k\)** |
| geometric multiplicity \(m(S)\) versus arithmetic coefficient \(u\) | **PROVED EXACT AT FIXED SOURCE FIBRE** |
| literal Wick-diagonal firewall | **PROVED EXACT FROM LOCKED SOURCE** |
| mask/rotation no-go (4.3) | **PROVED EXACT ALL-\(k\)** |
| uncertainty, prime-order, and subgroup formulas | **PROVED EXACT ALL-\(k\)** |
| sign-component coefficient (6.2) | **PROVED EXACT ALL-\(k\)** |
| finite group-algebra projector (0.7) | **PROVED EXACT ALL-\(k\)** |
| signed amplitude projector (0.8) and positive-energy boundary (2.3a) | **PROVED EXACT ALL-\(k\)** |
| collision-local renormalization (7.4)--(7.6) | **PROVED EXACT FORMAL KERNEL** |
| criterion (8.1)--(8.2) | **EXACT CONDITIONAL ACCEPTANCE CRITERION** |
| common varying-place derived complex | **NOT CONSTRUCTED** |
| relative invariant cancellation after FFPS cleanup | **OPEN** |
| `CYSEL`, `WCADD106140`, or `WCKUM106140` | **OPEN / RH-BEARING** |
| RH or GRH | **UNPROVED** |

No external novelty or priority claim is made.

## 11. Reproduction

The producer constructs cyclotomic polynomials only through order ten and
exhausts 2,026 nonempty proper cyclic subsets. It uses at most two million
small integer/rational operations and five seconds. This finite audit is not
the proof of the all-\(k\) theorem.

~~~powershell
python research/l-families/atlas/function_field/ffps_general_cyclic_resonance_no_go.py --check
python -O research/l-families/atlas/function_field/ffps_general_cyclic_resonance_no_go.py --check
python -m pytest -q tests/test_ffps_general_cyclic_resonance_no_go.py
python -O -m pytest -q tests/test_ffps_general_cyclic_resonance_no_go.py
python -m ruff check research/l-families/atlas/function_field/ffps_general_cyclic_resonance_no_go.py tests/test_ffps_general_cyclic_resonance_no_go.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_general_cyclic_resonance_no_go.py tests/test_ffps_general_cyclic_resonance_no_go.py
~~~

Regenerate the canonical JSON only by omitting `--check` from the first
command.
