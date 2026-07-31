# T-16202 — One repaired two-profile theorem closes the complete source block

Claim ID: `T-16202`  
Status: **PROVED CONDITIONAL TRANSFER THEOREM; RADIAL PROFILE HYPOTHESIS OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Corrected: 2026-07-31 after `R-16202`  
Depends on: `T-16201`, `L-16206`, `L-16208`, `L-16210`

## 1. Scope correction

The first formulation attached an ordinary `L2` omitted-tail profile to each raw
positive prolate mode `n=0,4,8,12`. That is not well-defined. Exact Poisson
summation contains the correction

```text
(1/2)[u^(-1/2) integral f-u^(1/2)f(0)],
```

and neither source functional vanishes on an individual positive mode. The raw
tail therefore contains a non-`L2(d*u)` power term.

By `R-16202`, the tail theorem must be stated on the two-dimensional exact
radical coefficient space

```text
C_lambda=ker[q_lambda^T; ell_lambda^T]
          subset span{e_0,e_4,e_8,e_12}.                 (T-16202.1)
```

Here

```text
q_n=e_n(0),
ell_n=integral e_n=chi_n q_n.                           (T-16202.2)
```

The repaired target from `T-16201` belongs to `C_lambda`, and an independent
repaired complement vector supplies a basis.

## 2. Adapted exact-radical basis

Choose a `4 x 2` coefficient matrix `U_lambda` whose columns span
`C_lambda`. Its first column is the repaired target and its second column is
chosen so that the ordinary coefficient Gram is uniformly nonsingular. Put

```text
f_(j,lambda)=sum_(n in {0,4,8,12})
 U_(n,j)(lambda)e_(n,lambda),

J_(j,lambda)=E(f_(j,lambda)),
j=1,2.                                                     (T-16202.3)
```

Let `T_(j,lambda)` be the omitted multiplicative tail of `J_(j,lambda)` outside
`[lambda^-1,lambda]`. Both source cancellations hold exactly, so the Poisson
correction terms vanish and `T_(j,lambda)` belongs to the declared ordinary and
Hardy tail spaces.

Let

```text
delta_1(lambda)=d_4(lambda),
delta_2(lambda)=d_8(lambda).                              (T-16202.4)
```

Replacing these by any uniformly comparable positive scales leaves the theorem
unchanged.

## 3. Corrected normalized profile hypothesis

Assume there exist

```text
R_lambda->infinity,
x_lambda in R,
```

and a two-component repaired profile row

```text
Phi_lambda=(Phi_(1,lambda),Phi_(2,lambda))
```

such that

```text
boxed:
widehat(T_(j,lambda))(s)
 =sqrt(delta_j(lambda)/R_lambda)
  exp(-is x_lambda)
  Phi_(j,lambda)(s/R_lambda),
 j=1,2.                                                   (T-16202.5)
```

Define the profile density and Gram

```text
H_lambda(x)=Phi_lambda(x)^*Phi_lambda(x),

D_lambda^prof=(1/(2pi)) integral_R H_lambda(x)dx.         (T-16202.6)
```

Require the uniform nondegeneracy gate

```text
boxed:
0<cI<=D_lambda^prof<=CI.                                 (T-16202.7)
```

Instead of a uniform pointwise `C1` envelope, it is enough that the repaired
packet satisfies the fold-admissible budgets of `L-16210`:

```text
uniform logarithmic L1 moment,
V_lambda+U_lambda=o(R_lambda),                            (T-16202.8)
```

where `V_lambda` is the weighted matrix variation of `H_lambda` and
`U_lambda` controls the horizontal-zero displacement in the strip
`|Im z|<=1/(2R_lambda)`.

This permits Airy folds and other integrable caustics.

## 4. Exact tail-Gram hierarchy

Mellin Plancherel applied to (T-16202.5) gives

```text
D_tail,lambda
 =S_lambda D_lambda^prof S_lambda,

S_lambda=diag(sqrt(delta_1),sqrt(delta_2)).               (T-16202.9)
```

Hence

```text
c diag(d_4,d_8)
 <=D_tail,lambda
 <=C diag(d_4,d_8).                                      (T-16202.10)
```

Equivalently, in any exact-radical coefficient basis with uniformly controlled
condition number, the first repaired tail scale is `Theta(d_4)` and the second
is `Theta(d_8)`.

The conclusion is basis invariant: replacing `U_lambda` by
`U_lambda S_lambda^0`, with a uniformly conditioned invertible `2 x 2` matrix,
changes every source Gram and Weil matrix by simultaneous congruence.

## 5. Exact zero-side factorization

By `L-16205`--`L-16206`, the repaired packet is an exact weak Weil-radical
packet and

```text
A_tail,lambda,(jk)
 =sum_rho
  conjugate(widehat(T_j)(conjugate(s_rho)))
  widehat(T_k)(s_rho).                                   (T-16202.11)
```

The sum is absolutely convergent under the profile budgets. No RH hypothesis
is used.

## 6. Fold-admissible scalarization

Apply `L-16210` with `R=R_lambda`. There are Hermitian matrices
`C_lambda,E_lambda` such that

```text
A_tail,lambda
 =a_lambda D_tail,lambda+C_lambda+E_lambda,               (T-16202.12)

a_lambda=log R_lambda+O(1),                              (T-16202.13)
```

and, after whitening by `D_tail,lambda`,

```text
boxed:
inf_a ||A_tail,lambda-aD_tail,lambda||_(D_tail)/a
 ->0.                                                     (T-16202.14)
```

Equivalently, for the extreme generalized eigenvalues `m_lambda,M_lambda` of
`(A_tail,D_tail)`,

```text
boxed:
(M_lambda-m_lambda)/(M_lambda+m_lambda)->0.               (T-16202.15)
```

A quantitative sufficient bound is

```text
O(1/log R_lambda)
 +O((V_lambda+U_lambda)/R_lambda).                        (T-16202.16)
```

## 7. Source target and complement gap

Let `mu_source` be the repaired target Rayleigh value in the localized source
Weil matrix and let `g_source` be its shifted one-dimensional complement gap in
the repaired two-packet. Equations (T-16202.10)--(T-16202.15) imply

```text
boxed:
mu_source=Theta(a_lambda d_4),

g_source=Theta(a_lambda d_8),                            (T-16202.17)

mu_source/g_source=O(d_4/d_8)=O(lambda^-8).               (T-16202.18)
```

The constants need not equal `8/11` and `176/211`, because the full arithmetic
tail Gram may have a nontrivial limiting `2 x 2` metric. Uniform positive
definiteness is sufficient.

## 8. Source Hardy geometry

Choose

```text
tau_lambda->1/2,
(1/2-tau_lambda)log lambda->infinity.                     (T-16202.19)
```

By `L-16208`, the repaired source Hardy Gram is uniformly equivalent to a fixed
positive coefficient Gram. Thus no ambient `lambda^(2tau)` penalty appears.
The source ground line approaches the repaired target at rate

```text
O(sqrt(d_4/d_8))=O(lambda^-4)                             (T-16202.20)
```

through `L-15107`, once an actual source-sector floor is supplied by the
scalarized matrix.

## 9. Proof

Equation (T-16202.9) is Plancherel after `s=R_lambda x`. The Gram gate proves
(T-16202.10). The exact radical basis has first two prolate scales `d_4,d_8` by
`T-16201`, and uniform congruence preserves those orders.

The zero-side identity is `L-16206`. The fold-admissible hypotheses permit
application of `L-16210`, proving (T-16202.12)--(T-16202.16). A positive scalar
multiple of the tail Gram plus a vanishing relative perturbation has the same
two generalized scales by min--max, proving (T-16202.17). Fuchs gives
`d_4/d_8=Theta(lambda^-8)`, proving (T-16202.18). The Hardy conclusion follows
from `L-16208` and `L-15107`. QED.

## 10. Radial prolate translation

Dunster's fixed-mode radial PSWF asymptotics provide a Bessel approximation
uniformly on `1<x<infinity`, with explicit high-frequency errors. In the CCM
normalization

```text
gamma=2pi lambda^2,                                      (T-16202.21)
```

so the natural Mellin-frequency scale is

```text
R_lambda=gamma asymptotic to lambda^2.                   (T-16202.22)
```

The remaining source-specific proof must:

1. apply the radial approximation to the two repaired combinations, not to four
   inadmissible raw tails;
2. insert the complete arithmetic Poisson sum;
3. treat the stationary fold in logarithmic coordinates with an Airy or
   equivalent uniform estimate;
4. prove `V_lambda+U_lambda=o(R_lambda)`;
5. prove a uniform positive lower bound for the repaired `2 x 2` profile Gram.

The fold theorem `L-16210` shows that pointwise derivative blow-up is harmless:
variation of order `R_lambda^(1/3) polylog R_lambda` already suffices.

## 11. Exact remaining source theorem

The source block is now reduced to

```text
boxed:
The two exact-radical omitted tails satisfy
(T-16202.5)--(T-16202.8) with R_lambda~2pi lambda^2.
                                                               (T-16202.23)
```

This is strictly smaller and correctly typed compared with the original
four-raw-mode profile gate.

## 12. Remaining global gates

After (T-16202.23), the complete RH route still needs:

```text
an independent global floor with target excess O(a_lambda d_4),
a complete complementary gap >=c a_lambda d_8,
source/complement coupling controlled in the relative-energy metric.          (T-16202.24)
```

The last three requirements are reorganized by `T-16203`: a single strict
energy-angle estimate implies the floor and coupling bounds once the source and
background diagonal gaps are known.

No proof of (T-16202.23), no proof of the background diagonal gap, and no proof
of RH is claimed here.
