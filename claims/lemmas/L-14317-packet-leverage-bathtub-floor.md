# L-14317 — Packet-leverage bathtub floor

Claim ID: `L-14317`  
Status: `PROPOSED`  
Author: `gpt56-02-m`  
Created: 2026-07-31  
Dependencies: `L-14316`; orthogonal projection in `L2`; exact packet/radical provenance  
Related candidates: none

## Statement

Let `I` be a bounded interval of length `L`, and extend functions by zero to the
real line. Let `K` be a finite-dimensional subspace of `L2(I)`. For real
frequency `xi`, put

```text
e_xi(x)=exp(-i xi x) on I,
ell_K(xi)=||P_(K-perp) e_xi||^2,
c_K(xi)=ell_K(xi)/(2 pi).
```

For every nonzero `w in K-perp`, its normalized Fourier-energy density satisfies

```text
p_w(xi)=|hat(w)(xi)|^2/(2 pi ||w||^2) <= c_K(xi).       (1)
```

Consequently, for a real multiplier `s` and every `G` for which the integral is
finite,

```text
q_s(w)/||w||^2
>= G-integral c_K(xi)(G-s(xi))_+ dxi.                  (2)
```

Thus the compression of the multiplier to `K-perp` obeys

```text
inf_(0!=w in K-perp) q_s(w)/||w||^2
>= B_K(s),
B_K(s)=sup_G [G-integral c_K(G-s)_+].                  (3)
```

For `K={0}`, this is `L-14316`.

## Proof

Since `w` is orthogonal to `K`,

```text
hat(w)(xi)=<w,e_xi>=<w,P_(K-perp)e_xi>.
```

Cauchy--Schwarz gives

```text
|hat(w)(xi)|^2 <= ||w||^2 ell_K(xi),
```

which proves (1). Integrating `s>=G-(G-s)_+` against `p_w` gives (2), and taking
the supremum over `G` gives (3).

## Exact Gram formula

For any basis `k_1,...,k_r` of `K`, let

```text
M_ij=<k_i,k_j>,
b_i(xi)=<k_i,e_xi>.
```

Then

```text
ell_K(xi)=L-b(xi)^* M^(-1) b(xi).                      (4)
```

For an orthonormal basis this becomes

```text
ell_K(xi)=L-sum_j |hat(k_j)(xi)|^2.                    (5)
```

Therefore a directed packet certificate can bound the complement density
without constructing a complement basis.

## Constant-radical specialization

Take `I=[-1,1]` and `K=span{1}`. With the normalized constant
`phi_0=1/sqrt(2)`,

```text
|hat(phi_0)(xi)|^2=2 (sin(xi)/xi)^2,
```

so

```text
c_0(xi)=(1/pi) [1-(sin(xi)/xi)^2].                     (6)
```

In particular `c_0(0)=0`: the constant-radical complement cannot place Fourier
mass at the center frequency.

For `|xi|<=1`, the elementary bound

```text
sin(xi)/xi >= 1-xi^2/6
```

implies

```text
1-(sin(xi)/xi)^2 <= xi^2/3.
```

Using `333/106<pi`,

```text
c_0(xi) <= 106 xi^2/999.                               (7)
```

This quadratic zero is invisible to the uniform cap of `L-14316`.

## Strict synthetic separation

Suppose on `[-1,1]` that

```text
s(xi)>=-10 for |xi|<=1/2,
s(xi)>=+1 outside.
```

The uniform-cap certificate gives only

```text
1-(106/333)*11 = -833/333 < 0.
```

On the constant-radical complement, (7) gives on the low cell

```text
c_0(xi)<=53/1998.
```

Hence

```text
q_s(w)/||w||^2
>= 1-11*(53/1998)
 = 1415/1998 > 0
```

for every `w` orthogonal to constants. Thus a deep central well that defeats the
ordinary bathtub relaxation is harmless after exact radical removal.

## Finite directed certificate

Let disjoint rational cells `I_j` carry:

```text
s(xi)>=L_j,
c_K(xi)<=C_j,
```

and suppose `s>=G` outside their union. Then

```text
q_s(w)/||w||^2
>= G-sum_j C_j |I_j| (G-L_j)_+                       (8)
```

for every `w in K-perp`. The optimum over `G` occurs at the tail floor or one of
the distinct cell lower bounds. `X-14310` verifies this arithmetic exactly.

## Relationship to PR #152

This theorem converts an already-certified radical or finite low packet into a
frequency-dependent complement floor. It is strictly stronger than replacing
the packet by one global leakage number.

Suggested order:

1. run the ambient `L-14316` floor;
2. if it fails, remove the exact radical and rerun `L-14317`;
3. if needed, enlarge `K` to the finite weighted/prolate packet of `L-14311`;
4. reserve the block Schur theorem `L-14308` for the residual packet itself.

## Boundaries

- The abstract projection theorem is exact.
- Production requires a proof-grade subspace `K` and directed upper bounds on
  its leverage deficit.
- Approximate eigenvectors cannot be inserted without a subspace-error moat.
- A negative lower floor has no RH implication.
- No production Suzuki packet-leverage floor is currently available.
