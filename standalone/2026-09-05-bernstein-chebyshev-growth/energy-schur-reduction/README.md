# Full-source Schur reduction with an explicit residual certificate

**PROPOSED COMPLETE COMPONENT PROOFS. Independent review required. RH and
positivity of the resulting actual effective matrices remain unproved.**

This is an add-only continuation of PR #792 at
`ddeca90f7aa6facd77841d38207aabe38d7a8f53`. All earlier layers, including the
other agent's separated-window gluing and the published coercivity packet,
remain unchanged.

## What is completed

The preceding coercivity packet left TWO tasks: justify eliminating the
infinite positive sector despite its unbounded L2 inverse, then prove the
remaining sign. This packet completes the analytic elimination, not the sign.

For each finite L, use the parent's exact positive subspace V and its finite
complement E. The full arithmetic kernel has W in W^(1,1)(-L,L). The primitive
identity gives, for every v in V and z in L2,

```
q(v,z)=b <phi_v', F_z>,
F_z=-(W*z)' + (1/4) integral_0^t (W*z),
|q(v,z)| <= sqrt(3)||Pi F_z||_2 sqrt(q(v,v)).
```

Pi is an explicitly defined elementary orthogonal projection. It removes
unnecessary constant/low-mode contributions to the residual. No second
kernel derivative, omitted prime cusp, or assumed inverse is used.

The energy-completed Riesz vectors g_i define

```
S_L,ij=q(e_i,e_j)-q(g_i,g_j),
T_L>=0 iff S_L>=0,
n_-(T_L)=n_-(S_L).
```

For L=1 the prior conservative parameters make this a 104-by-104 EFFECTIVE
matrix. It is not the leading 104-by-104 compression: its entries include
all infinite-sector coupling. Nullity need not be preserved.

For arbitrary trial corrections v_i in V, set z_i=e_i-v_i and

```
U_ij=q(z_i,z_j),
R_ij=<Pi F_(z_i),Pi F_(z_j)>.
```

The full signed certificate is

```
U-3R <= S_L <= U.
At L=1, a stronger proved coercivity constant improves 3 to 15/8.
```

Galerkin upper matrices decrease to S_L. Their positivity alone cannot
certify its sign. A verified nonnegative LOWER matrix U-3R would certify a
complete finite window; such an actual certificate was not obtained here.

## Exact controls and exploratory outcome

The standard-library checker reconstructs 581 exact rational controls. These
include shifted-cusp weak integration, general signed Schur identities,
Galerkin order, residual error direction, and infinite compact models with
finite-energy minimizers outside L2. Finite formulas do not machine-prove the
analytic results. No actual Schur sign is accepted by the checker.

A separate non-certifying experiment tested the L=1 source on three sampled
grids and, at the largest grid, several positive-sector Galerkin ranks. The
sampled upper matrices were positive. The constant-three residual lower
matrices were not, but the improved 15/8 bound gave positive sampled lower
matrices for three of the tested trial ranks. There is no continuum-error
certificate: these values prove neither positivity nor negativity of T_1.
They motivate a finite-window validation task, not an RH conclusion.

## Replay

With the three unchanged parent proof siblings present:

```sh
python verify_schur.py --check result.json
python -O verify_schur.py --check result.json
sha256sum -c SHA256SUMS
```

The optional `reconnaissance.py` uses NumPy, SciPy and mpmath and is NOT a proof
input. It has no interval acceptance or validated discretization remainder.
Read PROOF.md, SOURCES.md and VALIDATION.md before extending any conclusion.

No new general RH criterion, external priority, independent review, Lean
build, broad prime/zero scan or remote CI success is claimed.
