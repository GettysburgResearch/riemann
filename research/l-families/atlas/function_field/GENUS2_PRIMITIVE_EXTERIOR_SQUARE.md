# Primitive exterior square of genus-two `H^1`: an `SO(5)` family with a moving local eigenline

**Packet status.** Exact bounded algebra and histogram replay. The two
polynomial derivations, the all-odd-`q` low moments, and the compact `SO(5)`
baseline are exact. The `q=3,5,7` laws are complete pushforwards of a locked
joint coefficient histogram, not new finite-field scans. No numerical root,
random sample, field element, curve, or family member is constructed here.

The most unusual feature is a compatibility gap. The ambient decomposition
removes the canonical polarization line from `exterior^2 H^1`; its irreducible
five-dimensional `SO(5)` complement still has eigenvalue `q` at every
individual Frobenius element. On each finite-field fiber this is an actual
Frobenius-stable line. Ambient representation theory supplies no second line
common to all `SO(5)` elements, while the monodromy of the actual family is not
determined here and can specialize on endoscopic loci. Section 3 keeps these
three levels separate.

## 1. Representation and normalization

Start from the reciprocal genus-two polynomial

\[
 P_C(T)=1+aT+bT^2+qaT^3+q^2T^4
       =\prod_{i=1}^4(1-\alpha_iT).                                    \tag{1}
\]

The alternating pairing on `H^1(C)` supplies the canonical polarization Tate
line in its six-dimensional exterior square:

\[
 \bigwedge^2H^1(C)=\mathbf Q_\ell(-1)\oplus W,
 \qquad \dim W=5.                                                       \tag{2}
\]

After weight normalization, `W` is the standard representation under the
exceptional low-rank isogeny

\[
 USp(4)/\{\pm I\}\simeq SO(5).                                         \tag{3}
\]

This statement identifies the ambient algebraic representation. It does
**not** prove that the particular quintic family has Zariski-dense `SO(5)`
monodromy, nor that its actual local system has no further invariant
subsystem.

The central kernel already predicts a useful information-loss theorem. The
primitive exterior square is unchanged when the signed trace coefficient
`a` is replaced by `-a`. In fact its first two independent normalized
characters are

\[
 s={b\over q}-1=\chi_{(0,1)},\qquad
 k={a^2-b\over q}=\chi_{(2,0)}.                                        \tag{4}
\]

Character labels in this packet use the upstream `C2` convention. Under the
`C2`--`B2` correspondence, `C2 (0,1)` is `B2 (1,0)`, the five-dimensional
standard representation, while `C2 (2,0)` is `B2 (0,2)`, the
ten-dimensional adjoint representation.

Thus its polynomial recovers `b/q=1+s` and `a^2/q=1+s+k`, but cannot recover
the sign of `a`. This is an exact representation-theoretic quotient, not a
statistical correlation.

## 2. Two exact derivations of the exterior-square polynomial

For any four eigenvalues, the power sum of the six pair products is

\[
 p_n\!\left(\bigwedge^2H^1\right)
 ={p_n(H^1)^2-p_{2n}(H^1)\over2}.                                      \tag{5}
\]

The producer first applies the ordinary Newton recurrence to (1) through
order twelve, applies (5) through order six, and converts the resulting power
sums back to coefficients. Independently, an elementary-symmetric
calculation gives

\[
\boxed{\begin{aligned}
 L_{\wedge^2}(T)={}&1-bT+q(a^2-q)T^2-2q^2(a^2-b)T^3\\
                  &+q^3(a^2-q)T^4-q^4bT^5+q^6T^6.
\end{aligned}}                                                         \tag{6}
\]

Exact division by the canonical polarization factor `(1-qT)` gives the
primitive degree-five polynomial

\[
\boxed{\begin{aligned}
 R(T)={}&1+(q-b)T+q(a^2-b)T^2-q^2(a^2-b)T^3\\
        &+q^3(b-q)T^4-q^5T^5.
\end{aligned}}                                                         \tag{7}
\]

Both derivations are compared on every one of the 251 signed `(a,b)` atoms
in the complete locked histograms. In normalized variable `z=qT`, (7) is the
especially transparent character polynomial

\[
\boxed{R(z/q)=1-sz+kz^2-kz^3+sz^4-z^5.}                               \tag{8}
\]

The second coefficient is not an arbitrary function: `k` is the character
of `exterior^2 W`, the ten-dimensional adjoint representation. Equation (8)
therefore packages two distinct irreducible characters of `SO(5)` in one
local factor.

## 3. A memberwise `(1-qT)` factor versus a forced common line

Every element of an odd-dimensional special orthogonal group has eigenvalue
one. Its non-real eigenvalues occur in reciprocal pairs; one eigenvalue is
left unpaired, and determinant one forces that eigenvalue to be one.
Consequently, (7) has the memberwise factorization

\[
 R(T)=(1-qT)Q_{\rm local}(T),                                          \tag{9}
\]

where exact division gives

\[
\boxed{\begin{aligned}
 Q_{\rm local}(T)={}&1+(2q-b)T+q(a^2-2b+2q)T^2\\
                    &+q^2(2q-b)T^3+q^4T^4.
\end{aligned}}                                                         \tag{10}
\]

Equivalently,

\[
 Q_{\rm local}(z/q)
 =1+(1-s)z+(1-s+k)z^2+(1-s)z^3+z^4.                                  \tag{11}
\]

At a torus element with normalized `H^1` eigenvalues
`x,x^-1,y,y^-1`, the six exterior-square eigenvalues are

\[
 1,1,xy,x/y,y/x,(xy)^{-1}.                                             \tag{12}
\]

One of the two displayed `1` eigenvalues is the canonical symplectic line.
After its removal, the other remains at this individual element. For a fiber
over `F_q`, whose Galois group is procyclic, its `q`-eigenspace is an actual
Frobenius-stable `Q_l(-1)` line (canonical when the eigenvalue has multiplicity
one). Its axis varies with the `SO(5)` element, however, and the ambient
five-dimensional representation is irreducible with no common fixed vector.
Therefore:

- `(1-qT)` in (6) is the canonical polarization subrepresentation;
- `(1-qT)` in (9) is a genuine line on each finite-field fiber but is not a
  second line forced uniformly by the ambient `SO(5)` representation; and
- the quartics (10) are not thereby proved to form a family-wide or
  cross-prime compatible representation or motive.

The actual family monodromy group is unproved and may be smaller than `SO(5)`,
so this packet cannot rule out an extra sub-local-system. On an endoscopic
specialization `H^1=V_1 direct_sum V_2`, the decomposition
`exterior^2 H^1=exterior^2 V_1 direct_sum (V_1 tensor V_2) direct_sum
exterior^2 V_2` visibly has two Tate lines; after removing the diagonal
polarization line, the anti-diagonal one remains in the primitive factor.

At one finite-field fiber the quotient is genuine. What remains formal is the
assembly of the varying quartics across a family or across primes into a
compatible system. This packet makes no claim about bad local factors,
analytic continuation, poles, compensating zeros, automorphy, or motivic
decomposition. This “unisingular” compatibility gap is the strongest
follow-up target in the packet; the degree-five `GSp(4)` local factor itself is
classical context. A primary reference is Daniel File,
[“On the degree five L-function for GSp(4)”](https://arxiv.org/abs/1201.2783).
The project-specific contribution here is instead the exact locked-family
pushforward, all-`q` character Gram defects, and reproducible finite-field
orientation anomaly.

## 4. Exact all-odd-`q` character moments

The upstream squarefree-Moebius certificate proves exact formulas for
`E[a^2]`, `E[a^4]`, `E[a^2b]`, `E[b]`, and `E[b^2]` for uniform monic
squarefree quintics over every odd prime power. Substituting (4), without any
fit to the three frozen fields, gives

\[
\boxed{\begin{aligned}
 \mathbb E[s]
   &=-q^{-1}+q^{-2}-q^{-4},\\
 \mathbb E[s^2]
   &=1-q^{-1}+q^{-3}-q^{-4}-q^{-5},\\
 \mathbb E[k]
   &=q^{-3}-q^{-4},\\
 \mathbb E[k^2]
   &=1-2q^{-1}+q^{-2}+3q^{-3}-3q^{-4}-6q^{-5},\\
 \mathbb E[sk]
   &=-q^{-1}+q^{-2}+3q^{-3}-3q^{-4}-2q^{-5}.
\end{aligned}}                                                         \tag{13}
\]

At compact `SO(5)` Haar measure, `s` and `k` are distinct nontrivial
irreducible characters. Character orthogonality gives the limiting Gram
target

\[
 (\mathbb E[s],\mathbb E[s^2],\mathbb E[k],
   \mathbb E[k^2],\mathbb E[sk])=(0,1,0,1,0).                           \tag{14}
\]

Equation (13) is therefore an exact finite-family character-orthogonality
defect matrix. The relatively large `-q^-1` term in `E[sk]`, compared with
the `q^-3` first bias of `k`, shows that mixed character channels can detect
finite-family boundary structure much earlier than a single coefficient
mean.

## 5. Compact `SO(5)` trace moments and the orientation fingerprint

The producer verifies the compact baseline directly from the `B2` Weyl
constant-term formula. It uses the standard character

\[
 \chi=1+x+x^{-1}+y+y^{-1},                                             \tag{15}
\]

multiplies by `(1-e^alpha)(1-e^-alpha)` for the four positive `B2` roots,
takes the constant term, and divides by the Weyl-group order eight. Through
degree six this gives

| trace moment order | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `SO(5)` Haar | 1 | 0 | 1 | 0 | 3 | **1** | 15 |

The fifth moment is the first orientation-sensitive surprise. Pair
contractions account for the even moments, while the volume tensor in
`exterior^5 W` contributes one invariant at order five. Passing from
`SO(5)` to the disconnected group `O(5)` adds a reflection and kills every
odd trace moment, so

\[
 \mathbb E_{SO(5)}[(\operatorname{tr}g)^5]=1,
 \qquad
 \mathbb E_{O(5)}[(\operatorname{tr}g)^5]=0.                            \tag{16}
\]

This nominates the finite-family fifth moment of `s=b/q-1` as an orientation
detector. Strikingly, every frozen value has the **opposite sign** from the
compact target:

| `q` | exact family `E[s^5]` | `SO(5)` Haar target |
|---:|:---:|---:|
| 3 | `-8059/6561` | 1 |
| 5 | `-541001/390625` | 1 |
| 7 | `-5982775/5764801` | 1 |

This is a clean high-weight anomaly to explain, not evidence against an
eventual `SO(5)` limit. Three small fields establish no all-`q` fifth-moment
formula, monotonicity, asymptotic sign, or convergence rate.

## 6. Complete frozen pushforwards, with no new enumeration

For each of `q=3,5,7`, the producer reads every atom of the complete joint
`(a,b)` member histogram in `balanced_control_family_scan.json`. It checks
the two polynomial derivations, performs the two exact divisions, and then
compresses by `(a^2,b)`. The JSON retains:

- every compressed primitive polynomial and its exact member weight;
- every normalized trace atom `s=(b-q)/q`;
- trace moments through order eight, compared with `SO(5)` through order six;
- all five character quantities in (13), independently recovered from the
  histogram;
- three Newton/division witnesses per field; and
- the exact size of the `a=0` fixed locus.

The signed source histogram is checked to be invariant under `a -> -a`.
That finite symmetry is consistent with the central kernel in (3), but the
packet does not silently replace the marked-equation/model-stack measure by
a uniform law on coarse twist orbits.

The resource ledger charges declared high-level histogram atom visits, Newton
comparisons, character terms, frozen moment terms, and Laurent-polynomial
products. It stays strictly below an exclusive 10,000-accounted-work-unit
cap. These units are not literal arithmetic instructions or a wall-clock
complexity claim. All computations use the Python standard library and exact
integers or `Fraction` values.

## 7. Concrete next theorem targets

1. **Unisingular Euler-product target.** Determine whether the good-prime
   quartics (10) admit an independent compatible, automorphic, or motivic
   realization. If not, identify the mechanism by which the formally
   extracted zeta factor is globally compensated.
2. **Orientation moment target.** Evaluate or power-save
   `E[(b/q-1)^5]` across the all-`q` family and isolate the contribution
   corresponding to the `SO(5)` volume tensor.
3. **Character Gram tower.** Extend (13) to larger irreducible-character
   blocks and separate boundary, endoscopic, and automorphic corrections.
4. **Measure comparison.** Construct the actual twist-orbit and coarse-curve
   pushforwards before comparing them with the model/stack law recorded here.
5. **Cross-family test.** Apply the same exterior-square transform to
   genus-two families with constrained endomorphisms or different base
   parameter spaces. The local `(1-qT)` identity is universal; deviations in
   the character Gram matrix are where family-specific arithmetic can enter.

## 8. Epistemic firewall

- The polynomial identities are pointwise algebra. They do not establish
  full `SO(5)` monodromy for the quintic family.
- Ambient `SO(5)` theory forces no second common Tate line, but every
  finite-field fiber has a genuine Frobenius-stable `q`-eigenline and special
  family loci may have additional invariant subsystems.
- A formal local Euler-factor extraction is not a four-dimensional motive.
- The `q=3,5,7` histograms are exhaustive finite facts only and are not an
  asymptotic theorem, interpolation basis, or convergence-rate estimate.
- Uniform marked quintics/model-stack weights are not uniform coarse moduli
  weights.
- Nothing in the packet proves analytic continuation, a zero-free region,
  RH, or GRH for any global `L`-function.

Replay with:

```text
python research/l-families/atlas/function_field/genus2_primitive_exterior_square.py --check research/l-families/atlas/function_field/genus2_primitive_exterior_square.json
python -m unittest tests.test_genus2_primitive_exterior_square
python -O -m unittest tests.test_genus2_primitive_exterior_square
```
