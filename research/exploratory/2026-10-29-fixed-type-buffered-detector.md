# Fixed-type buffered zero detector: source-conditional derivation

**Status:** A derivation from the listed standard Hecke analytic and local-conductor inputs, modeled on [OpenAI Lemmas 4.9–4.10 and 8.1](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) and Hu [Proposition 6.3](https://hexagonmath.org/2610.00216v1). It is not a proof of Hu's full physical contour identity, a zero-free region, or all moment estimates. The source's finite-sector identification and the standard analytic inputs below are not independently reproved here.

## Data and explicit inputs

Fix a number field `K` containing `mu_12`, a finite set `S` of finite primes, and finitely many fixed unitary archimedean types, closed under conjugation. Fix the target and its finite local data after the real parameters are chosen. For each retained nonprincipal physical row `u` with `Nu~U=Z^d`, `0<dmin<=d<=dmax`, let `X_u` be the finite collection of actual numerator, denominator, conjugate and fixed finite-twist presentations required by the detector. Assume:

1. Each primitive character inducing a member of `X_u` is nonprincipal, has one of the fixed archimedean types, and has finite conductor norm `Q<=C_psi U^A0` for constants `A0,C_psi` independent of the moving row. The actual application expects `A0=1`. The collections are closed under conjugation. Rows with a principal primitive numerator or denominator are isolated and treated separately.
2. Original imprimitive presentations are obtained from their primitive functions by deleting Euler factors at a squarefree radical of norm at most `C_psi U^A0`, including the exact row and fixed-S masks. The nonunit value of every residue-character power is zero even if that power is a multiple of six.
3. For the fixed field and allowed archimedean types, primitive nonprincipal Hecke L-functions have the standard polynomial strip bound, uniformly over the finite conductors, on every fixed bounded real strip. In particular, on `1/2<=Re(s)<=4`,

       |L(s,xi)| <= C_(K,omega) [Q(3+|Im s|)^[K:Q]]^A,

   for a fixed exponent `A` and fixed-type constant. Euler products and logarithms converge absolutely on `Re(s)>1`. Each primitive L-function has entire continuation and discrete zeros. These are ordinary fixed-field Hecke analytic inputs; this note does not deduce them from Hu's §3.
4. The positive common upper boundary `B` dominates all relevant zero real parts and satisfies `B>=51/100`. The later norm twist is either removed from the target or explicitly included in the bounded height ledger; no unbounded row-dependent twist may be hidden in a fixed-type constant.

Hu's §2.2 family `F_omega` is closed under finite twists and conjugation. His Proposition 6.3 asserts the detector transfer and states that the conductor of a physical sextic row is controlled by its squarefree radical, with fixed local factors. The latter is consistent with tame Kummer theory: at primes outside S, ramification is supported on `rad(u)`, while the possible S-unit classes modulo sixth powers form a finite fixed set. This paragraph records source matching; the physical Kummer identification, local conductor exponents and sector calibration remain assumptions unless independently proved.

## Fixed-type logarithmic control

Let `xi` be primitive and nonprincipal, with allowed type and conductor `Q`. Fix `a in [51/100,1]`, `0<e<10^(-3)` and real `t`. Suppose `L(s,xi)` has no zero in the open disk about `2+it` of radius

```text
R2=2-a-2e.
```

Then for each `epsilon>0`, uniformly on the concentric closed disk of radius `R6=2-a-6e`,

```text
|L(s,xi)| + |L(s,xi)^(-1)|
   <<_(K,omega,e,epsilon) [Q(3+|t|)^[K:Q]]^epsilon.          (1)
```

The proof is the fixed-type version of OpenAI Lemma 4.9. Choose a holomorphic `g=log L` on the zero-free disk, with the Euler logarithm branch at `2+it`. At radius `49/100`, the Euler logarithm is uniformly bounded since the whole disk lies in `Re(s)>1.51`. The strip input bounds `Re g` by `O(log C)` on radius `R3=2-a-3e`, where `C` is a fixed constant times `Q(3+|t|)^[K:Q]`. Borel–Carathéodory bounds `|g|` by `O_e(log C)` on radius `R4=2-a-4e`. Hadamard three-circles between the fixed inner radius and `R4` yields `|g|<<_e (log C)^theta` on `R6`, with a `theta<1` uniform for `a in [51/100,1]`. Exponentiation gives (1). The logarithmic derivative is `O_e(log C)` on the smaller disk `R8=2-a-8e` by Cauchy's estimate.

For a deleted Euler product `D_R(s)=product_(p|R)(1-alpha_p Np^(-s))`, `|alpha_p|<=1`, OpenAI Lemma 4.10's elementary argument gives for each fixed `sigma0>0` and `epsilon>0`

```text
|D_R(s)|+|D_R(s)^(-1)| <<_(sigma0,epsilon) (N R)^epsilon,
Re(s)>=sigma0.                                               (2)
```

It has no zeros there. On the bounded left strip, its upper bound is `(N R)^((-Re s)_+ +epsilon)`. These estimates retain all natural zeros and do not replace a row-dependent mask with a different mask.

## Nested bins and the single buffer

Fix `0<tau<=dmin/100`, set `T1=Z^tau>2`, and let `I=ceil(1/e)+2`. For `j=1,...,I`, define

```text
M_j(u) = max( {51/100} union
  {Re rho : L(rho,xi)=0, xi induced by X_u,
              Re rho>=51/100, |Im rho|<=3j T1} ).
```

These maxima exist because `X_u` is finite, zeros are discrete in compact sets and Euler convergence excludes zeros with real part greater than 1. The sequence is nondecreasing in `[51/100,B]`. Some `i<I` satisfies `M_(i+1)-M_i<=e`; otherwise the total increase would exceed 1. Round `M_i` down to the grid anchored at `51/100` with step `e`, obtaining `a<=M_i<a+e` and `M_(i+1)<a+2e`. If `a>51/100`, a genuine zero has `Re rho>=a`, `|Im rho|<=3i T1`. There are only `O_e(1)` bins.

For any center height `|t|<=(3i+2)T1`, the disk of radius `2-a-2e` lies within the height interval `|Im s|<3(i+1)T1` for `T1>2`, and has real part `>a+2e`. It is therefore zero-free for every primitive member of `X_u`. Equations (1)–(2), `Q,NR <<_psi U^A0`, and `T1<=U^(1/100)` imply, after rechoosing the arbitrary epsilon,

```text
|L_orig(s,xi)| + |L_orig(s,xi)^(-1)| <<_(psi,e,epsilon) U^epsilon,
Re s>=a+6e,  |Im s|<=(3i+2)T1.                              (3)
```

For `Re s>2`, absolute Euler convergence supplies the same type of bound. This gives the buffered reciprocal for the **whole fixed finite collection**, not an all-height reciprocal on the shifted line. The field degree and fixed archimedean shifts enter the choice of the smaller epsilon and the constants, not a new uncontrolled row power.

Suppose a relevant buffered argument has imaginary part `gamma_j+sum_k a_jk v_k` and the finite coefficient matrix is fixed, with base `|gamma_j|<=(3i+1)T1`. Allocate once

```text
|v_k| <= T1/[2M(1+max_j |a_jk|)],     k=1,...,M.
```

Then the total added displacement is at most `T1/2`, leaving the argument within (3). Bounded fixed shifts are absorbed once `T1` is large. All detector, Mellin and approximate-functional-equation frequencies that actually enter any buffered argument must be listed **before** assigning these shares; the allowance is not renewed at successive contour shifts. Increasing external test decay orders later does not change this finite matrix or the fixed arithmetic height degree. An auxiliary coefficient measure with only weighted `L1` control is not thereby a trace-controlled external frequency.

## Reflected line and remaining gap

For a finite-order Kummer numerator (or a fixed-type numerator with its appropriate conjugate gamma factors), the ordinary functional equation on `Re(w)=1-a-6e`, together with (3) for the conjugate primitive function, gives the usual conductor factor `Q^(a-1/2+6e)` times a fixed polynomial in `T1`. Restoring deleted factors costs at most `U^(6e A0+epsilon)` because `Re(w)>=-6e` and the deleted radical is bounded by `U^A0`. Thus the source exponent `U^(a-1/2+12e+epsilon)` follows when `A0=1`; for general `A0`, using the same exponent for conductor and radical gives `U^[A0(a-1/2+12e)+epsilon]`, and this must not be silently replaced by the `A0=1` exponent.

The real outstanding verification is physical rather than an apparent failure of the nested-bin argument: identify **every** row-dependent presentation produced by Hu's compensated unit-sector construction, prove its primitive conductor and deleted radical are `O_psi(U)`, and show the source's fixed-infinity-type strip bound and gamma factors are uniform for that exact family. Separately verify the full quotient-free Euler correction and all trace-density hypotheses before moving the physical contours. The finite-family bin lemma and (3) do not by themselves establish the raised-line moment, the outer rows, a target-uniform saving, or descent to all unitary Hecke L-functions.
