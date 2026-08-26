# FFPS Wick-centering boundary for positive principal domination

Status: **exact all-cyclic-mask quadratic identity and sharp proper-mask
collision spectrum; no varying-conductor estimate**

Scope: finite source fibres and their exact cyclic Fourier operators

Exact replay:
[`ffps_wick_centered_domination_boundary.py`](ffps_wick_centered_domination_boundary.py)

## 0. Outcome

The cyclic hard covariance has an exact positive domination before Wick
centering.  After centering, domination fails for every proper mask on any
same-phase collision fibre containing at least two distinct atoms.

Let `S subset mu_k` be nonempty, put `t=|S|`, and set

\[
 u={k\over t}-1.
\tag{0.1}
\]

For a finite source atom set `Omega`, phase map
`Phi:Omega -> mu_k`, and amplitudes `z_omega`, define

\[
 \begin{aligned}
 Q_P(z)&=\left|\sum_\omega z_\omega\right|^2,\\
 Q_C(z)&={1\over k}\sum_{j=0}^{k-1}
 \left|{k\over t}\sum_{\Phi(\omega)\in\zeta_k^jS}z_\omega\right|^2,\\
 Q_S(z)&=\sum_{r=1}^{k-1}|c_r|^2
 \left|\sum_\omega\Phi(\omega)^rz_\omega\right|^2,
 \end{aligned}
\tag{0.2}
\]

where

\[
 c_r={1\over t}\sum_{s\in S}s^{-r}.
\]

Fourier orthogonality gives

\[
 \boxed{Q_C=Q_P+Q_S,\qquad Q_S\ge0.}
\tag{0.3}
\]

Thus the uncentered hard covariance dominates the principal energy with
sharp constant one:

\[
 \boxed{Q_P(z)\le Q_C(z).}
\tag{0.4}
\]

Let `D(z)=sum|z_omega|^2`.  The three atomic coefficients are `1`, `1+u`,
and `u`, so the Wick-centered forms are

\[
 Q_P^\circ=Q_P-D,
 \quad Q_C^\circ=Q_C-(1+u)D,
 \quad Q_S^\circ=Q_S-uD.
\tag{0.5}
\]

They satisfy

\[
 \boxed{Q_C^\circ=Q_P^\circ+Q_S^\circ}
\tag{0.6}
\]

but `Q_S^circ` is indefinite for every proper mask as soon as a phase fibre
contains two distinct source atoms.  If a phase fibre has size
`m>=2`, its selected centered block is

\[
 \boxed{u(J_m-I_m),}
\tag{0.7}
\]

with exact spectrum

\[
 \boxed{u(m-1)\quad\text{and}\quad -u
 \text{ with multiplicity }m-1.}
\tag{0.8}
\]

Consequently neither centered form dominates the other on such a collision
fibre.  The best universal diagonal repair is exact and sharp:

\[
 \boxed{
 Q_S^\circ(z)\ge-uD(z),
 \qquad
 Q_P^\circ(z)\le Q_C^\circ(z)+uD(z).}
\tag{0.9}
\]

No coefficient smaller than `u` can replace `u` in (0.9) on a double
physical collision.  Thus the local positive-domination route pays exactly
the same selected mass `u` that the leverage/mode Pareto theorem assigns to
the hard mask.

This pinpoints the architectural boundary:

- **uncentered:** principal domination is already exact;
- **centered proper mask with a collision:** positivity is lost on distinct
  same-phase atoms;
- **relative signed route:** `Q_C^circ-Q_S^circ=Q_P^circ` remains exact, but
  estimating that difference is the principal RH-bearing problem.

For the full mask, `u=0` and all selected forms vanish.  On an atom set with
no repeated phase, the collision witness is absent.  Neither degenerate case
is claimed to be indefinite.

## 1. Frozen dependencies

| source | commit | git blob | role |
|---|---|---|---|
| `FFPS_GENERAL_CYCLIC_RESONANCE_NO_GO.md` | `271ff4316` | `6c63def72b340f69be9caff41a619f23d2b66fd1` | all-`k` collision kernels |
| `FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md` | `90a6aad54` | `e8adbeb51053e62096ad1590774f13d01094f0b0` | selected mass and leverage frontier |
| `FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md` | `464c3705f` | `ab16e6c0894e51303119692e67b2f2bf59ba73e4` | endomorphism lift and principal projector |
| `FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md` | `6e4609dfe` | `9012f96b34a3ffe55b66282ba1e62bc02514b5c6` | Wick-normalized physical source identity |

The present note proves a finite quadratic-form statement.  Its application
to the physical FFPS source inherits the exact adapter scope of the last
dependency; no varying-place sum is silently introduced.

## 2. Uncentered Loewner order

The rotated hard observations have Fourier expansion

\[
 O_j=P+\sum_{r=1}^{k-1}\zeta_k^{-jr}c_rH_r,
\tag{2.1}
\]

where

\[
 P=\sum_\omega z_\omega,
 \qquad H_r=\sum_\omega\Phi(\omega)^rz_\omega.
\]

Averaging `|O_j|^2` over all rotations kills every cross-character term and
proves (0.3).  There is one normalization point.  Aggregate the atoms by
phase, writing \(z_g=\sum_{\Phi(\omega)=g}z_\omega\).  On that regular phase
space with its standard inner product,

\[
 Q_P=k\langle\Pi_0z,z\rangle,\qquad
 Q_S=k\left\langle
       \sum_{r\ne0}|c_r|^2\Pi_r z,z\right\rangle .
\tag{2.2}
\]

Thus, after the common harmless rescaling `Q_tilde=Q/k`, the corresponding
endomorphisms are

\[
 \mathsf C_S=\Pi_0+\mathsf S_S,
 \qquad
 \mathsf S_S=\sum_{r\ne0}|c_r|^2\Pi_r\succeq0
\tag{2.3}
\]

under any complex embedding with the regular deck action unitary.  Hence

\[
 \mathsf C_S\succeq\Pi_0.
\tag{2.4}
\]

The common factor `k` cancels from the Loewner comparison.  The constant is
sharp: equality holds on the principal line because every selected projector
vanishes there.  This is a genuine local positive principal amplifier, but
it is uncentered and therefore still contains the full atomic diagonal.

## 3. Exact effect of Wick centering

For one atom, exactly `t` of the `k` rotated masks retain its phase.  Its
average hard diagonal coefficient is

\[
 {1\over k}t\left({k\over t}\right)^2={k\over t}=1+u.
\tag{3.1}
\]

The principal coefficient is one.  Parseval gives the selected coefficient

\[
 \sum_{r\ne0}|c_r|^2=u.
\tag{3.2}
\]

Subtracting those three literal atomic diagonals from (0.3) proves (0.6).
Since `Q_S>=0`,

\[
 Q_S^\circ=Q_S-uD\ge-uD,
\]

which proves (0.9).  This lower bound is global on every finite atom set and
uses no collision assumption.

It is important that Wick centering is an affine diagonal subtraction, not a
positive functor on the cyclic representation.  It shifts the selected
Gram matrix by `-uI`; positive semidefiniteness need not survive.

## 4. Collision spectrum and sharpness

Take `m` distinct source atoms with one common phase `phi`.  On that fibre,

\[
 H_r=\phi^r\sum_{a=1}^m z_a
\]

for every selected mode, so

\[
 Q_S=u\left|\sum_{a=1}^m z_a\right|^2.
\tag{4.1}
\]

Its Gram matrix is `uJ_m`.  Removing the selected atomic diagonal `uI_m`
gives (0.7).  The all-ones vector has eigenvalue `u(m-1)` and the
sum-zero subspace has eigenvalue `-u`, proving (0.8).

For `m=2`, the two exact witnesses are

\[
 z_+=(1,1),\qquad z_-=(1,-1).
\]

They give

\[
 Q_S^\circ(z_+)=2u,
 \qquad
 Q_S^\circ(z_-)=-2u.
\tag{4.2}
\]

Therefore `Q_C^circ-Q_P^circ` has both signs.  Adding `lambda D` makes the
collision block positive semidefinite only if

\[
 -u+\lambda\ge0.
\]

Thus `lambda>=u`, proving sharpness of (0.9).

The witness uses distinct atoms.  Literal Wick subtraction removes
`omega_1=omega_2`; it does not remove the off-diagonal pair between these
atoms.  The all-`k` resonance theorem proves that every proper hard mask has
`u>0` on an orientation-preserving double physical collision.

## 5. Consequence for hard-mask amplification

The selected mass is also the exact density coordinate in the leverage
frontier:

\[
 L(u)={(1+u)^2\over A+Bu}.
\tag{5.1}
\]

On panels with `B/A` large, the continuous leverage optimum has `u_*` close
to one.  Equation (0.9) then demands an order-one atomic payment.  Changing
the shape or rotation of the mask cannot lower it, because Parseval fixes
`u` at a given retained density.

This does not say the hard mask is useless.  It says exactly what an
arithmetic theorem must contribute beyond positive Hilbert-space algebra:

1. cancellation of the centered selected off-diagonal trace before absolute
   values;
2. geometric removal of every same-phase collision by a common cleanup; or
3. a relative trace estimate for `C-S` that never pays `uD` separately.

The Kummer-torsor packet constructs the local relative endomorphism needed
for option 3.  It does not bound its principal trace.

## 6. Proof ledger

| statement | grade |
|---|---|
| uncentered identity and domination (0.3)--(0.4) | **PROVED EXACT ALL-`k`** |
| atomic coefficients and centered identity (0.5)--(0.6) | **PROVED EXACT ALL-`k`** |
| universal repaired inequality (0.9) | **PROVED EXACT ALL-`k`** |
| collision block and spectrum (0.7)--(0.8) | **PROVED EXACT FOR EVERY `m>=2` SAME-PHASE FIBRE** |
| sharpness of diagonal payment `u` | **PROVED EXACT ON A TWO-ATOM COLLISION** |
| full mask `u=0` | **SELECTED FORM IDENTICALLY ZERO** |
| occurrence in the fixed physical adapter | **INHERITED AT DECLARED COLLISION STRATA** |
| removal of every collision in full FFPS cleanup | **OPEN** |
| varying-conductor centered trace estimate | **OPEN / RH-BEARING** |
| RH or GRH | **UNPROVED** |

No external novelty or priority claim is made.  The Fourier/Gram facts are
elementary; the project contribution is the exact Wick-centered spectral
boundary and its alignment with the physical hard-mask route.

## 7. Reproduction

The replay checks every density pair `1<=t<k<=12` and collision multiplicity
`2<=m<=10` using rational matrices.  It accounts for 152,064 entries across
six named conceptual matrices; this is not an allocation counter for Python
temporaries.  Independently, it constructs every nonempty proper translated
mask for `2<=k<=7` and checks its exact rational covariance,
autocorrelation kernel, centered covariance factorization, selected mass,
and row sums.  It performs no arithmetic-family enumeration.

~~~powershell
python research/l-families/atlas/function_field/ffps_wick_centered_domination_boundary.py --check
python -O research/l-families/atlas/function_field/ffps_wick_centered_domination_boundary.py --check
python -m unittest tests.test_ffps_wick_centered_domination_boundary
python -O -m unittest tests.test_ffps_wick_centered_domination_boundary
python -m ruff check research/l-families/atlas/function_field/ffps_wick_centered_domination_boundary.py tests/test_ffps_wick_centered_domination_boundary.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_wick_centered_domination_boundary.py tests/test_ffps_wick_centered_domination_boundary.py
~~~
