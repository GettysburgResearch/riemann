# T-15103 — A Rayleigh-floor/prolate-gap diagonal criterion implies RH

Claim ID: `T-15103`  
Status: **PROVED SUFFICIENT CRITERION; ACTUAL WEIL COMPARISON OPEN**  
Authoring agent: `gpt56-pro-11`  
Created: 2026-07-31  
Depends on: `T-14301` or `T-15101`, audited `L-14302`, `L-15107`

## 1. Statement

At level `j`, let `k_j` be a prescribed ambient CCM target, let

```text
p_j=P_j k_j=q_j v_j,
||v_j||_2=1,
```

and let `A_j` be the exact finite localized-Weil matrix. Let `mu_j` be the
Rayleigh quotient of `v_j`. Suppose the finite parity/coercivity gates certify

```text
C_(+,j)-U_j I >=h_j M_(+,j),
C_(-,j)-U_j I >=g_(-,j) I,
U_j>=mu_j,                                                (T-15103.1)
```

with `h_j,g_(-,j)>0`.

Suppose a rigorous lower endpoint `L_j` satisfies

```text
lambda_min(A_j)>=L_j.                                    (T-15103.2)
```

Put

```text
t_j=||k_j-p_j||_(tau_j).
```

If

```text
t_j+q_j sqrt((mu_j-L_j)/h_j) ->0                         (T-15103.3)
```

along a sequence

```text
lambda_j->infinity,
N_j->infinity,
tau_j->1/2 from below,
```

then the Riemann hypothesis is true, subject to the same explicitly imported
CCM finite-real-zero and transform-limit interfaces as `T-14301`.

## 2. Ordinary complement version

It is sufficient to have an ordinary complement gap `g_j` with

```text
C_(+,j)-U_j I >=g_j I                                    (T-15103.4)
```

and

```text
t_j+q_j sqrt(
  2 lambda_j^(2 tau_j) (mu_j-L_j)/g_j
)->0.                                                     (T-15103.5)
```

## 3. Pure-prolate model corollary

For the diagonal prolate defect model of `L-15106` and `T-15102`, take

```text
L=0,
mu/d_4 ->8/11,
g/d_8 ->176/211.
```

Then the ordinary projective angle obeys

```text
||w/alpha||_2
 <=sqrt(mu/g)
 ~ [sqrt(44310)/(1408*pi^2)] lambda^-4.                  (T-15103.6)
```

The numerical constant is approximately

```text
0.015147762066515325.
```

Using only the support Hardy bound and allowing `tau->1/2`,

```text
||w/alpha||_tau=O(lambda^-7/2).                           (T-15103.7)
```

Thus the complete positive diagonal criterion closes automatically in the pure
prolate model. The actual RH problem is precisely the transfer of the floor and
gap estimates to the localized Weil form.

## 4. Proof

The finite gates certify a unique simple-even ground state. Apply `L-15107` to
obtain

```text
||c_j xi_j-k_j||_(tau_j)
 <=t_j+q_j sqrt((mu_j-L_j)/h_j)
```

for an explicit nonzero scalar `c_j`. The right side tends to zero by
(T-15103.3). The support-independent Hardy-strip estimate then gives local
uniform convergence of the finite transforms to `Xi`. Every finite transform
has only real zeros by the imported CCM theorem, so Hurwitz excludes every
nonreal zero of `Xi`. This is RH.

The ordinary-gap version uses

```text
M_(+,j)<=2 lambda_j^(2tau_j) I.
```

For the prolate corollary, substitute the exact asymptotic constants from
`L-15105`, `L-15106`, and `T-15102`. The ordinary angle constant is

```text
sqrt[(8/11)/(176/211) * 105/(4096*pi^4)]
 =sqrt(44310)/(1408*pi^2).
```

QED.

## 5. What the criterion changes

The previous exact blocker was

```text
B_j/h_j ->0,
```

where `B_j` is a correlated vector residual. This remains a valid sufficient
route, but it is no longer the only one.

The new scalar route asks for

```text
mu_j-L_j=O(d_4),
g_j>=c d_8,
```

with a sufficiently small relative error in the actual Weil/prolate
comparison. Lower spectral floors and min--max gaps are often more accessible
to trace identities, operator sandwiches, and exact interval eigenvalue bounds
than a full residual vector is.

## 6. Remaining analytic bridge

After transporting the source sector into one exact Gram metric, a closing
theorem may take the affine form

```text
A_lambda
 =sigma_lambda G_lambda+a_lambda D_lambda+R_lambda.       (T-15103.8)
```

Here `D_lambda` is the prolate defect form in the `G_lambda` metric. By
`L-15109`, the scalar shift and the coordinate basis are immaterial. A
sufficient remainder estimate is

```text
||R_lambda||
 =o(a_lambda d_8(lambda)/lambda^(2tau_lambda)).           (T-15103.9)
```

The denominator in (T-15103.9) records the conservative Hardy-weight inflation.
A direct Hardy-form comparison could weaken this requirement.

Under the Loewner enclosure
`-epsilon G_lambda<=R_lambda<=epsilon G_lambda`, `L-15109` gives the exact
bounds

```text
mu_A-L_A <= a mu_D+2 epsilon,
g_A       >= a g_D-2 epsilon.
```

Together with `mu_D~(8/11)d_4` and `g_D~(176/211)d_8`, this proves
(T-15103.5) under the stated relative remainder condition.

No estimate of the form (T-15103.8)--(T-15103.9) is proved here.
