# T-16202 — One normalized tail-profile theorem closes the complete repaired source block

Claim ID: `T-16202`  
Status: **PROVED CONDITIONAL TRANSFER THEOREM; PROLATE PROFILE HYPOTHESIS OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: `T-16201`, `L-16206`, `L-16208`, `L-16209`

## 1. Why this replaces alias suppression

`L-16207` decomposes the arithmetic omitted-tail Gram into the first prolate
leakage sample plus aliases. Requiring the aliases to vanish relative to the
first sample is sufficient, but it is not necessary and is not the natural
fixed-mode theorem suggested by uniform radial PSWF asymptotics. Sharp support
produces oscillatory algebraic exterior tails, and the alias terms may survive
at leading normalized order.

The positive route needs only the **full arithmetic tail packet** to have a
nondegenerate normalized profile. This theorem proves that one such profile
statement simultaneously supplies:

1. the `d_4/d_8` source hierarchy;
2. the relative tail-Weil scalarization;
3. the source Hardy convergence.

## 2. Exact repaired packet

Fix a finite positive-prolate packet containing the modes

```text
I={0,4,8,12}                                               (T-16202.1)
```

or any fixed larger packet. Let `f_(n,lambda)` be the compact prolate sources,
let

```text
J_(n,lambda)=E(f_(n,lambda)),                             (T-16202.2)
```

and let `T_(n,lambda)` be their omitted multiplicative tails outside
`[lambda^-1,lambda]`.

Use the exact two-constraint repaired source space and target from `T-16201`.
Let

```text
d_n(lambda)=1-chi_n(lambda).                              (T-16202.3)
```

## 3. Normalized profile hypothesis

Assume there are:

```text
R_lambda->infinity,
x_lambda in R,
```

and functions `Phi_(n,lambda)` such that

```text
widehat(T_(n,lambda))(s)
 =sqrt(d_n(lambda)/R_lambda)
  exp(-is x_lambda)
  Phi_(n,lambda)(s/R_lambda).                             (T-16202.4)
```

Assume the fixed packet satisfies the uniform profile hypotheses of
`L-16209`:

```text
uniform holomorphic C1-decay envelope,
uniform logarithmic moments,                              (T-16202.5)
```

and its profile Gram

```text
H_lambda,(mn)
 =(1/(2pi)) integral_R
   conjugate(Phi_(m,lambda)(x))Phi_(n,lambda)(x)dx        (T-16202.6)
```

satisfies

```text
boxed:
0<cI<=H_lambda<=CI                                        (T-16202.7)
```

with constants independent of `lambda`.

No convergence of `H_lambda` is needed; uniform positive definiteness and
boundedness suffice.

## 4. Exact tail-Gram hierarchy

Mellin Plancherel gives

```text
D_tail,lambda
 =S_lambda H_lambda S_lambda,                             (T-16202.8)

S_lambda=diag(sqrt(d_n(lambda))).                         (T-16202.9)
```

Consequently

```text
c diag(d_n)
 <=D_tail,lambda
 <=C diag(d_n).                                           (T-16202.10)
```

Let

```text
nu_1^tail<=nu_2^tail<=...
```

be the eigenvalues of the tail Gram on the exact two-constraint source space,
measured against any fixed coefficient Gram uniformly equivalent to the source
Hardy Gram.

Then `T-16201` and the min--max principle give

```text
boxed:
nu_1^tail=Theta(d_4),
nu_2^tail=Theta(d_8).                                     (T-16202.11)
```

The constants are finite and strictly positive, although they need not equal
`8/11` and `176/211` when aliases survive at leading order.

## 5. Exact zero-side Weil factorization

By `L-16205`--`L-16206`, the repaired packet is an exact weak Weil-radical
packet and its localized source Weil matrix equals the omitted-tail zero-side
matrix term by term:

```text
A_tail,lambda,(mn)
 =sum_rho
  conjugate(widehat(T_m)(conjugate(s_rho)))
  widehat(T_n)(s_rho).                                   (T-16202.12)
```

No RH hypothesis occurs.

## 6. Universal scalarization

Apply `L-16209` to (T-16202.4). There are matrices `C_lambda,E_lambda` with

```text
A_tail,lambda
 =a_lambda D_tail,lambda+C_lambda'+E_lambda',             (T-16202.13)

 a_lambda=log R_lambda+O(1),                              (T-16202.14)
```

and, in the tail-Gram metric,

```text
boxed:
inf_a ||A_tail,lambda-aD_tail,lambda||_(D_tail)
 /a
 =O(1/log R_lambda)->0.                                   (T-16202.15)
```

Equivalently, if `m_lambda,M_lambda` are the extreme generalized eigenvalues of
`(A_tail,D_tail)`,

```text
boxed:
(M_lambda-m_lambda)/(M_lambda+m_lambda)
 =O(1/log R_lambda)->0.                                   (T-16202.16)
```

## 7. Source target and gap

Let `mu_source` be the Rayleigh value of the exact repaired target in the
localized source Weil matrix, and let `g_source` be the first shifted
complement gap inside the repaired source sector. Equations
(T-16202.11)--(T-16202.16) imply

```text
boxed:
mu_source=Theta(a_lambda d_4),

g_source=Theta(a_lambda d_8),                            (T-16202.17)

mu_source/g_source=O(d_4/d_8)=O(lambda^-8).              (T-16202.18)
```

Thus the full arithmetic aliases may alter finite constants, but cannot alter
the target and next-mode scales.

## 8. Source Hardy geometry

Choose the schedule of `L-16208`:

```text
tau_lambda->1/2,
(1/2-tau_lambda)log lambda->infinity.                     (T-16202.19)
```

The fixed source-packet Hardy Gram converges to a finite positive limit. Hence
no ambient `lambda^(2tau)` factor enters the comparison, and the source ground
line approaches the repaired target at rate

```text
O(sqrt(d_4/d_8))=O(lambda^-4)                             (T-16202.20)
```

through the Rayleigh-floor identity, provided an actual source-sector floor is
chosen from the scalarized matrix.

## 9. Proof

Equation (T-16202.8) is Plancherel after the substitution `s=R_lambda x`.
The Loewner inequalities (T-16202.10) follow from (T-16202.7). The two-constraint
diagonal prolate compression has first two scales `d_4,d_8` by `T-16201`.
Applying the min--max principle to the uniformly equivalent forms in
(T-16202.10) proves (T-16202.11).

The exact zero-side identity is `L-16206`. The profile assumptions and uniform
Gram floor allow direct application of `L-16209`, proving
(T-16202.13)--(T-16202.16). Since the scalarized Weil form is a positive scalar
times the tail Gram up to a vanishing relative error, min--max transfers
(T-16202.11) to (T-16202.17). Fuchs gives
`d_4/d_8=Theta(lambda^-8)`, proving (T-16202.18). Finally apply the bounded
source Hardy Gram of `L-16208` and `L-15107`. QED.

## 10. Relation to radial PSWF asymptotics

Dunster's uniform high-frequency radial PSWF theorem gives a Bessel-function
approximation throughout `1<x<infinity`, with explicit `O(gamma^-1)` errors for
fixed mode, and the exact far-field behavior is oscillatory of order `1/x`.
This is the correct primary tool for proving (T-16202.4)--(T-16202.7) after:

1. translating `gamma=2pi lambda^2` and the CCM normalization;
2. inserting the arithmetic Poisson sum defining `E`;
3. centering the logarithmic tail and using `R_lambda` of order `lambda^2`;
4. proving the resulting finite profile Gram is nondegenerate.

The theorem does not assume that individual aliases vanish.

## 11. Correct source-level remaining theorem

The source block is now reduced to the single statement:

```text
boxed:
The normalized full arithmetic omitted tails of modes 0,4,8,12 satisfy
(T-16202.4)--(T-16202.7) for some R_lambda->infinity.     (T-16202.21)
```

Once this is proved, the source part of the requested trace-form bridge is
complete.

## 12. Remaining global gates

The complete RH route still requires the non-source statements from
`L-16201`:

```text
an independent global ground floor with target excess O(a_lambda d_4),
a background complement gap >=c a_lambda d_8,
cross coupling squared=o(g_source g_background).         (T-16202.22)
```

No proof of (T-16202.21), no proof of (T-16202.22), and no proof of RH is claimed
here.
