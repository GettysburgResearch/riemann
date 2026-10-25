# Independent review of the coherent short-product theorem

Reviewer: fractional/native agent.

Verdict: **Sections 2--5 pass at their stated source-dependent scope**.
The estimate concerns an actual coherent piece of the native inverse.
The complementary product range remains. This review does not certify a
full inverse saving or a new zero-free region.

## Exact reviewed bytes and source scope

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| `SIGNED_NATIVE.md` | 32953 | `d9426e96884b725f3db2467e62527eed204df931e72fe583d3681571e47e75f3` | `f10fc34928e22b77d9c681d46b8ec75bad40e7f5` |
| `check_signed_native.py` | 11048 | `f42962007a14c071390fffcf4d841e9b66aaf0ef474ca82d62053f6a3931de02` | `e1d5b2b90880a119c4fd782a2e828c3b73a1b495` |

These are local byte authentications, not remote publication claims.
The full-column sieve was independently fetched from
`GettysburgResearch/riemann@c690f96fe6876f945398b3e2779810c563a64743`,
`standalone/2026-10-23-structured-moment-gains/fifth-pass/SEXTIC_ROW_PHASE_CANCELLATION.md`,
Git blob `3a5d7adcc24ec8907be5c8fd6879d81736d44788`.
Its equation (6) is the precise squarefree-row, unrestricted-column,
divisor-bounded premise used here.

I also read the pinned source's `lem:sextic-large-sieve` in Git blob
`268c4e3206d460c617d3d2129742a72b831b3def`, and fetched the fixed-angular
ordinary Hecke equation from the same OpenAI commit's
`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex`,
Git blob `e93fbddf626ab532b7e8fbfac830f1b45370b0e3`.
Only the ordinary Hecke equation is used here, not that companion's
prime cancellation or metaplectic conclusions.

The imported global framework is not independently certified. Sections
6 onward of the new note contain further investigations outside this
review's affirmative analytic verdict.

## 1. Exact convolution and the object being estimated

The identity `mu=2m_y-m_y*m_y*1` through norm `y^2` follows by
multiplying `(delta_1-m_y*1)^2` by `mu`. Its support argument
works in the monoid of good ideals. With `y=sqrt(2D)` and
`D>=3`, the `2m_y` term vanishes on the stated annulus.

All factorizations `ab=r` are necessary in `a_y(r)`.
Adding `(a,b)=1` or discarding nonsquarefree `r` would change the
identity. The note and checker retain them. Complete multiplicativity
with natural zeros gives `psi_u(rc)=psi_u(r)psi_u(c)` even on
nonunits.

At the reviewer's request, the final file explicitly defines `I_R`
as the physical-row squared norm of `M_{u,R}` and `I_short` as the
norm of the coherent partial sum. Bounded nonnegative row weights
are retained. A norm of a sum is not silently replaced by a sum of
squared norms.

## 2. Primitive reflection and every normalization

The natural-factor expansion (9) has the correct coefficient
`mu(e)psi_u^*(e)/sqrt(Ne)`. Using the zero-extended value at a deleted
prime would incorrectly kill it. No extra coprimality condition is
imposed on the quotient and `e`. A prime in the primitive conductor
already gives its true zero coefficient.

The functional equation has the correct conjugate, root number and
central normalization:

\[
 T_u^*(C/Ne)=\varepsilon_u\sqrt{\frac{C}{q_uNe}}
     \sum_n\overline{\psi_u^*(n)}
          \Phi\!\left(\frac{NnC}{q_uNe}\right).
\]

Fixed field constants can be absorbed in the common transform.
Nonprincipality removes the pole residue. A full ordinary Hecke
function is reflected, so zeros are not crossed as poles. The
fixed-angular case uses its ordinary gamma quotient and opposite
dual angular order.

The transform and its Euler derivatives have the required bounded
behavior at zero and rapid decay at infinity. A fixed norm height
has a polynomial seminorm cost.

I independently recomputed the prefactor in (11):

\[
 (Nr)^{-1/2}(Ne)^{-1/2}
   \sqrt{\frac{D}{q_uNrNe}}
       =\sqrt{\frac D{q_u}}\frac1{Nr\,Ne}.
\]

Both denominators are necessary. The reflected coefficient is
`overline(psi_u^*(n))`; the coefficient of `e` is not conjugated.

## 3. Conductor and zero masks

For a good prime of row valuation `j=1,...,5`, the local order is
`6/gcd(6,j)>1` and its tame conductor exponent is one. The fixed
bad-set twist cannot cancel it. After a finite bad-place split,

\[
 q_u=c_s\,N\operatorname{rad}(v)\,Nw
\]

for `u=vw` with squarefree `w`, powerful `v` and `(v,w)=1`.
The inequality `P=Nrad(v)<=sqrt(Nv)` follows. The common puncture
does not enter this primitive conductor; its redundant zeros have
already been expanded exactly.

Primes of `v` remain natural zeros in the common column coefficient.
Primes of `w` remain the sieve kernel's natural zeros. The primitive
dual variable may meet the fixed bad set: it is counted as an ideal
and used as a bounded row multiplier, not placed into a good-column
sieve.

## 4. The fixed-product norm and puncture cancellation

For fixed `v,e` the nominal dual scale is `L_0=q_vRE/D`.
Separation of the one smooth profile in the three normalized annular
variables gives a common Fourier/Mellin density. It does not select
a new coefficient vector independently on each row.

After fixing a dual ideal and a separation mode, the primitive root
number, puncture character and dual character are bounded row
scalars. The remaining column sequence is common and divisor-bounded,
so the pinned full-column sieve applies.

The actual dual ideals cost `O(L)` on a dyad. For every `L_0>0`,

\[
 \sum_{L\ge1}^{\rm dyadic}L(1+L/L_0)^{-J_0}\ll L_0
 \quad(J_0>1).
\]

If `L_0<1`, the left side is `O(L_0^{J_0})`. No artificial
constant column count is inserted below unit scale.

The remaining prefactor is

\[
 \frac{\sqrt{D/q_v}}{RE}L_0\sqrt R
                  =\sqrt{\frac{q_vR}{D}}.
\]

This confirms exact cancellation of `E` in (17). The finite divisor
sum costs only `tau(Q_s)` and fits in the reserved small power.

The full-column sieve deduction is also consistent: for a powerful
column part of norm `T`, the squarefree coefficient energy is
`O(R/T)`. Its square root cancels the `T^(1/2)` powerful count
in Minkowski. This is the stated divisor-bounded consequence, not
an unlicensed operator-norm strengthening.

## 5. All physical rows and the coherent cutoff

Powerful counting and `P<=sqrt(V_0)` give
`sum_(Nv~V_0)P<<V_0^(1+epsilon)`. Substitution of `A~U/V_0`
gives precisely

\[
 \frac{U^2R}{DV_0},\qquad
 \frac{UR^2}{D},\qquad
 \frac{U^{5/3}R^{5/3}}{DV_0^{2/3}}.
\]

The first and third dyadic sums converge; the second is logarithmic.
The physical rows in these pieces are disjoint, so adding their
squared norms is legitimate.

For `R<=sqrt U`, the bracket in (1) is `O(U)`. The row norms
grow as `sqrt R`, so their dyadic Minkowski sum is controlled by
its last scale. This proves `I_{<=R_0}<<U^2R_0/D`.

The native exponents in the table check exactly. I also pointed out
the `R_0=U^(1/4)` specialization now included in the final file:
its exponent `9/4-r` is below `(1+5r)/6` by
`(22r-25)/12` whenever `r>25/22`.
At the stated critical length this gives exponent
`1.0860464234909890437...` and saving
`0.0505815569331867532...`. Its complement is explicitly
`R>U^(1/4)`; the estimate does not control it.

## 6. Checker replay and limitation

The final checker ran independently under `python -O` with its
explicit exceptions active. It returned PASS for 1352 Heath--Brown
identities, 108 masked rows, 10000 gcd inversions, six Eisenstein
additive class sums, 16 interpolation identities, 286 exponent
predicates, and 1500 weighted-prime-mark identities.

All six reported negative-control categories detected their intended
mutations. The rational root-of-unity row model tests multiplicativity
and masks, not the full native Hecke family. The additional finite
prime-mark tests concern later sections outside this analytic review.
No finite check certifies the large sieve, functional equation, or
asymptotic moment.

No remaining mathematical blocker was found in Sections 2--5 at
the precise scope above.
