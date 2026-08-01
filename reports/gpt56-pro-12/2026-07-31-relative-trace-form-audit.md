# Relative trace-form audit and continuation

Agent: `gpt56-pro-12`  
Date: 2026-07-31  
Issue: #162  
PR: #164

## Executive verdict

The originally requested statement

```text
A_lambda = sigma_lambda G_lambda
           +a_lambda(I-K_lambda)+R_lambda,

lambda^(2tau_lambda)||R_lambda||_(G_lambda)
 /(a_lambda d_8(lambda))->0
```

cannot be proved under its most natural **ambient bounded-operator** reading:
the localized Weil operator is unbounded above, whereas the prolate defect and
a bounded Gram-relative remainder are bounded.

This is a scope refutation, not a failure of the positive route. The proof uses
only a finite constrained source block. On that block the program can be made
both exact and stronger:

1. a `0/4/8` prolate repair satisfies both source-radical constraints exactly;
2. the repaired target still has Rayleigh scale `(8/11)d_4`;
3. the next exact-radical direction still has scale `(176/211)d_8`;
4. the arithmetic source is an exact weak Weil-radical vector;
5. the localized source Weil matrix equals the omitted-tail Weil matrix term by
   term in an absolutely convergent zero sum;
6. the ordinary omitted-tail Gram equals the prolate leakage Gram plus one
   explicit arithmetic alias remainder;
7. the normalized tail Weil form scalarizes universally by the
   Riemann--von Mangoldt local Weyl law once the rescaled tail profiles have a
   uniform envelope;
8. the ambient Hardy inflation `lambda^(2tau)` is unnecessary on the fixed
   low-source packet.

No RH proof is claimed. Two prolate boundary-profile estimates and the global
background/floor gates remain.

## 1. Published positive-route foundation

The PR first publishes the earlier fixed-radical and mode-8 theorem units:

```text
T-15101  fixed-radical finite diagonal RH criterion
L-15102  radical localization equals boundary leakage
T-15102  complete positive-prolate mode-8 gap
L-15107  Rayleigh-floor/coercivity bypass
T-15103  Rayleigh-floor finite diagonal RH criterion
L-15109  affine metric-safe prolate sandwich
M-15102  relative trace-form bridge
```

The pure prolate constants are

```text
mu_D/d_4 ->8/11,
g_D/d_8  ->176/211,
d_4/d_8  ~105/(4096 pi^4) lambda^-8.
```

Thus the target/complement ratio has an eight-power moat even after all modes
`8,12,16,...` are included.

## 2. Ambient obstruction

At fixed support the localized Weil form contains the unbounded Fourier
multiplier

```text
2 theta'(t)/(2pi),
```

which grows logarithmically. The rank-two term and finite prime-power sum are
bounded. Modulating one compactly supported logarithmic test function therefore
makes the Weil Rayleigh quotient tend to positive infinity.

Hence a bounded identity

```text
A=sigma G+a(I-K)+bounded R
```

cannot hold on the full localized Hilbert space.

The primary archimedean trace-form paper does contain the exact identity

```text
N_I=-2 epsilon'(1+)(Id-K_I),
```

but `K_I` is its own compact trace-remainder kernel, not the standard prolate
concentration operator. Semilocal prime terms are also load-bearing.

The corrected comparison must be a finite source compression or an unbounded
graph-form statement.

## 3. Exact affine falsifiers and sufficient sector theorem

`L-16201` gives three finite lower bounds on the best full affine fit after
whitening by `G`:

```text
commutator:
  epsilon >= ||[Ahat,Dhat]||/diam(spec Dhat);

off diagonal:
  epsilon >= max_(i!=j)|<u_i,Ahat u_j>|;

three-mode curvature:
  epsilon >= |C_ijk|/
   (|delta_i-delta_j|+|delta_j-delta_k|+|delta_k-delta_i|).
```

These are exact falsifiers for the original full-space hypothesis.

The same lemma proves a strictly weaker sufficient theorem using only:

```text
source projected affine sandwich,
independent global floor,
background complement gap,
source/background cross-block norm.
```

The full complement gap is the smallest eigenvalue of the associated `2 x 2`
scalar Schur matrix.

## 4. Exact-radical prolate repair

For positive finite-Fourier modes, let

```text
q_n=e_n(0),
ell_n=chi_n q_n,
d_n=1-chi_n.
```

The two source-radical constraints are

```text
sum c_n q_n=0,
sum c_n ell_n=0.
```

The exact `0/4/8` coefficient vector is

```text
c_0=q_4q_8(d_8-d_4),
c_4=q_8q_0(d_0-d_8),
c_8=q_0q_4(d_4-d_0).
```

The mode-8 coefficient is smaller than the leading coefficients by
`O(d_4/d_8)=O(lambda^-8)`. The repaired target retains

```text
mu_rad/d_4 ->8/11.
```

Under explicit finite tail-susceptibility gates, the first two eigenvalues of
the complete two-constraint source space satisfy

```text
nu_1/d_4 ->8/11,
nu_2/d_8 ->176/211.
```

Thus exact radicality does not destroy the mode hierarchy.

## 5. BV source radicality is exact

For compact BV sources with

```text
f(x)=O(x^2) near zero,
integral f=0,
```

Connes--Consani Lemma 6.1 makes `E(f)` well defined and integrable. Direct Mellin
calculation gives

```text
widehat(E(f))(z)
 =zeta(1/2-iz)
  integral_0^infinity f(x)x^(-1/2-iz)dx.
```

The zero integral cancels the zeta pole at `z=i/2`. At every nontrivial-zero
parameter both the displayed transform and its conjugate-parameter transform
vanish. Therefore `E(f)` is an exact weak Weil-radical vector.

This applies to the repaired compact prolate source.

## 6. Exact zero-side tail factorization

The localized source functions are compact BV in logarithmic coordinates, so
their Mellin transforms are `O(1/|gamma|)` uniformly in the critical strip.
The product zero sum is absolutely convergent because
`N(T)=O(T log T)`.

At every zero, the omitted-tail transform is the negative of the retained
transform. Therefore, term by term,

```text
localized source Weil matrix
 = omitted-tail Weil matrix.
```

The source/tail cross matrices are their negatives. This closes the abstract
factorization of `L-16203` without an imported graph-limit theorem.

## 7. Exact tail metric decomposition

Poisson summation gives the lower multiplicative tail as the arithmetic `E` sum
of the additive Fourier leakage `r_n`.

The first sample `k=1` has exact Gram

```text
int_lambda^infinity r_m(v)r_n(v)dv
 =[(1-chi_n^2)/2]delta_mn
 =d_n(1+o(1))delta_mn.
```

Every difference from the prolate defect is an explicit alias sum over
`r_n(kv)`, `k>=2`. If

```text
alpha_n
 =||sum_(k>=2)r_n(k .)||_(L2(lambda,infinity)),
eta_n=alpha_n/sqrt((1-chi_n^2)/2),
```

then a fixed packet obeys

```text
||D_0^-1/2 D_tail D_0^-1/2-I||
 <=r(2eta+eta^2).
```

The exact tail-metric problem is therefore only

```text
eta_n(lambda)->0,
n=0,4,8,12.
```

## 8. Local Weyl scalarization

Let a boundary tail have logarithmic width `R_lambda^-1` and rescaled transform
profile `Phi_j(s/R_lambda)`. For a fixed packet with uniform `C1` decay and a
nondegenerate profile Gram, the Riemann--von Mangoldt formula gives

```text
A_R=(log R)D_R+C_R+O(log R/R),
||C_R||=O(1).
```

This remains true off RH because the imaginary displacement of every centered
zero parameter is bounded by `1/2`, and after scaling contributes only
`O(log R/R)`.

Thus the generalized tail-Weil eigenvalues satisfy

```text
m_R=log R+O(1),
M_R=log R+O(1),
(M_R-m_R)/(M_R+m_R)=O(1/log R)->0.
```

The scalarization of the zeta-zero measure is universal. The only source-specific
input is a uniform rescaled boundary profile.

## 9. The ambient Hardy factor is unnecessary

CCM supplies, for each fixed low mode,

```text
sup_(|x|<=lambda)|f_(n,lambda)(x)-h_n(x)|
 <=C_n lambda^-2.
```

The finite arithmetic sum then gives

```text
||E(f_(n,lambda))-E(h_n)||_tau^2
 <=C lambda^(-1+2tau).
```

Choose

```text
tau_lambda=1/2-delta_lambda,
delta_lambda->0,
delta_lambda log lambda->infinity.
```

The error tends to zero. Fourier-invariant Hermite sources are rapidly
decreasing at both multiplicative ends, so the packet Hardy Gram converges to a
finite positive endpoint Gram. Therefore the correct source-sector remainder
condition is simply

```text
||R_source||/(a d_8)->0,
```

not the ambient worst-case condition multiplied by `lambda^(2tau)`.

## 10. Corrected remaining theorem

The source-sector part now follows from two prolate profile statements:

```text
A. alias suppression
   eta_n(lambda)->0 for n=0,4,8,12;

B. boundary-profile compactness
   after centering and scaling by R_lambda~lambda^2,
   the fixed tail profiles have a uniform C1-decay envelope and a
   nondegenerate Gram limit.
```

Then the exact factorization, local Weyl theorem, mode-8 hierarchy, and
source-specific Hardy convergence close the complete source block.

The global positive route additionally needs:

```text
C. an actual global ground floor with target excess O(a d_4);
D. a background complement gap >=c a d_8;
E. cross coupling squared=o(g_source g_background).
```

## 11. Exact finite audit

`X-16201` is a standard-library-only rational checker. It verifies affine
falsifiers, the background Schur gap, radical-tail factorization, and the exact
optimal two-dimensional scalarization invariant.

```text
9/9 adversarial tests pass
proof-object SHA-256
841bb98b828601ebb6257d0709c91e91ce6d8aad8e304721eed7b9369a3735e0
```

## 12. Status

The originally requested ambient theorem is refuted as a well-typed bounded
operator statement. A stronger and more relevant constrained-source route has
been proved down to two fixed-mode prolate boundary asymptotics and three global
floor/background gates.

No proof of RH is claimed.
