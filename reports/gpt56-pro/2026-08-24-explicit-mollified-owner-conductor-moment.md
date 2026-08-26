# Explicit mollified owner-conductor moment

Date: 2026-08-24  
Programmes: #743, #736, #737  
Execution PR: #751  
Parent: PR #719 at `c2e82cfdd254a478731f005b3d83b49d3e1e33ea`  
RH status: **unproved**

## 1. From a descriptive gate to an explicit `L`-moment

The preceding checkpoint reduced the CV/XD physical restriction to coherent
assembly of short-core owner packets after a sharp local squareclass
contraction. This pass writes that assembly as an exact mollified
owner-conductor moment.

Fix an owner pair `P=pq`, an opposite owner conductor `rho`, and an even
character `eta (mod rho)`. Define

\[
Z_{P,\eta}(w)
=L(w,\eta)(1-\eta(p)p^{-w})(1-\eta(q)q^{-w})
\]

and the fixed-cutoff mollifier

\[
M_{U;P,\eta}(w)
=\sum_{\substack{n\le U\\(n,P)=1}}
{\mu(n)\eta(n)\over n^w}.
\]

The owner-excluded Vaughan defect is

\[
A_{U;P,\eta}=1-M_{U;P,\eta}Z_{P,\eta}.
\]

The balanced Type-II row has the exact Dirichlet series

\[
\boxed{
B_{U;P,\eta}(w)
={A_{U;P,\eta}(w)^2\over Z_{P,\eta}(w)}
={\bigl(1-M_{U;P,\eta}(w)Z_{P,\eta}(w)\bigr)^2
  \over Z_{P,\eta}(w)}.
}
\]

Equivalently,

\[
B=Z^{-1}-2M_U+M_U^2Z.
\]

This is exactly the generating-series version of the fixed-cutoff Vaughan
identity, not a heuristic mollifier analogy.

The physical shell projection must remain attached:

\[
B^{\mathcal S}_{U;P,\eta}
=\Pi_{\mathcal S}\left[(1-M_UZ)^2/Z\right].
\]

Removing that projection without a tail theorem would change the source.

## 2. Exact Mellin--Plancherel form

Let

\[
\kappa(u)=K_L(e^u),
\qquad
\widehat\kappa(0)=0.
\]

For one finite shell, the physical log-field has Fourier transform

\[
\widehat{\mathcal V}_{U;P,\eta}^{\mathcal S}(t)
=
\widehat\kappa(t)
P^{-1/2-it}
B_{U;P,\eta}^{\mathcal S}(1+2it).
\]

Hence every coherent finite owner assembly has energy

\[
{1\over2\pi}
\int_{\mathbb R}|\widehat\kappa(t)|^2
\left|
\sum_i\omega_iP_i^{-1/2-it}
B_i^{\mathcal S_i}(1+2it)
\right|^2dt.
\]

The principal balanced ratio has at most a simple pole at `w=1`. The derivative
kernel has a zero at `t=0`, so their product is bounded there. This is the
spectral form of the parent’s zero-square-lattice Type-I cancellation.

## 3. Owner quadratic classes are load-bearing

For fixed conductor `rho`, the owner products must be split by

\[
\sigma=\kappa_\rho(P)\in\{+1,-1\}.
\]

Inside one `sigma` sector, every physical residue `Pa^2` lies in one coset of
the square subgroup. The sharp local contraction remains valid coherently, and
the quadratic root field is exactly `sigma` times the principal root field.
Recombining the two sectors costs at most the absolute factor `2`.

If the two sectors are combined before the transform, the residues may occupy
all of `F_rho^*`; the strict contraction disappears and the physical
observation norm grows like `rho`. Thus the `sigma` index is part of the
source, not bookkeeping.

## 4. Exact positive moment

For each `(rho,sigma,eta)`, define

\[
\mathcal A_{\rho,\sigma,\eta}(t)
=
\sum_i\omega_i\chi_{\rho,\eta}(P_i)
P_i^{-1/2-it}
B_{U_i;P_i,\eta}^{\mathcal S_i}(1+2it),
\]

where `chi_(rho,eta)^2=eta` and the literal coefficient `omega_i` includes the
source-owned conductor weight.

The complete moment is

\[
\boxed{
\begin{aligned}
\mathfrak M_L
={1\over2\pi}\sum_{\rho,\sigma}
\int|\widehat\kappa(t)|^2
\Bigg[&{\rho+1\over\rho-1}
|\mathcal A_{\rho,\sigma,1}(t)|^2\\
&+{2\rho\over\rho-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
|\mathcal A_{\rho,\sigma,\eta}(t)|^2
\Bigg]dt.
\end{aligned}
}
\]

Every term is nonnegative and every source label is retained.

## 5. The two real analytic problems

The exact moment separates into:

```text
PCM106030:
  principal/quadratic-root mollified owner moment is subpower;

NEM106030:
  nonprincipal even-character mollified family moment is subpower.
```

`NEM106030` is the natural character-large-sieve, trace-formula or
arithmetic-geometric target. But ordinary large sieve does not automatically
close it: different owner pairs in the same quadratic class survive in the
same residue collision geometry.

`PCM106030` contains the coherent semiprime owner amplifier and the native
carrier cancellation. It is not implied by any estimate which discards the
principal/quadratic root fibre.

The exact conclusion is

```text
PCM106030 AND NEM106030
 -> explicit moment M_L is subpower
 -> SOCM106020
 -> HBCQDSP102888
 -> RH.
```

Neither estimate is proved.

## 6. Function-field handoff

Over `F_q[T]`, the local transform is the Kummer--Artin--Schreier Fourier
transform of the square map. The global target is now the exact analogue of
`M_L`, retaining degree-shell projections, owner irreducibles, quadratic owner
classes, root fibres and resonant strata.

A successful geometric proof should say whether the nonprincipal moment comes
from Deligne cancellation, monodromy averaging or a relative trace formula,
and identify the geometric replacement for the principal moment. Known
function-field RH alone does not provide that information.

## 7. Exact replay

```text
PASS_X_106030_MOLLIFIED_OWNER_CONDUCTOR_NORMAL_FORM
exact_checks=38780
proof_object_sha256=48c20069952efd0ec21e3b23a38c0b78af07e3b010e0dbb346e32014e898398b
```

The replay authenticates the owner-excluded inverse identity, Vaughan defect
algebra, owner quadratic-class partition, principal/quadratic root coherence
and finite Gaussian-integer Plancherel fixtures. It does not prove either
analytic moment or RH.

## Boundary

```text
balanced Vaughan = projected mollifier defect / L   PROVED EXACT
fixed-shell Mellin--Plancherel                       PROVED EXACT
owner quadratic-class split                         PROVED EXACT
local physical occupancy                            PROVED SHARP
PCM106030                                            OPEN / RH-BEARING
NEM106030                                            OPEN
SOCM106020                                           OPEN / RH-BEARING
HBCQDSP102888                                        OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
