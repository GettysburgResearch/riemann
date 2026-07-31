# L-15107 — A Rayleigh floor bypasses the vector residual ratio

Claim ID: `L-15107`  
Status: **PROVED FINITE-DIMENSIONAL HILBERT-SPACE LEMMA**  
Authoring agent: `gpt56-pro-11`  
Created: 2026-07-31  
Depends on: the finite simple-even/coercivity gate of audited `L-14302`

## 1. Why this matters

The existing route controls the ground-state angle using

```text
vector residual / complement coercivity.
```

That is sufficient, but it is not necessary. If one can certify a lower floor
for the actual ground eigenvalue, then the exact block eigenvalue identities
control the angle using only

```text
Rayleigh excess above the floor / complement coercivity.
```

This removes the need to prove the delicate vector cancellation
`A c_lambda-b_lambda` directly.

## 2. Statement

Let `A` be self-adjoint on a finite-dimensional real Hilbert space. Let `Gamma`
be a self-adjoint involution commuting with `A`, and let `v` be a unit even
vector. Put

```text
W_+=H_+ intersect v^perp,
mu=<Av,v>,
b=P_(W_+)Av,
C_+=P_(W_+)A|_(W_+).
```

Let `M_+` be any positive-definite operator on `W_+`. Assume there are numbers

```text
U>=mu,
h>0,
g_->0
```

such that

```text
C_+-U I >= h M_+,
C_--U I >= g_- I.                                        (L-15107.1)
```

Then audited `L-14302` gives a unique simple-even normalized ground state

```text
xi_0=alpha v+w,
alpha>0,
w in W_+,
```

with ground eigenvalue `lambda_0<=mu`.

If a certified scalar lower floor satisfies

```text
lambda_0>=L,                                              (L-15107.2)
```

then

```text
boxed: ||w/alpha||_(M_+)^2 <=(mu-lambda_0)/h
                              <=(mu-L)/h.                 (L-15107.3)
```

This is the **Rayleigh-floor/coercivity bound**.

## 3. Unnormalized target form

Let `p=qv` with `q>0`, and let `k` be an ambient target whose ordinary
projection onto the finite space is `p`. Set

```text
t=||k-p||_M.
```

With the explicit scalar `c=q/alpha`,

```text
boxed:
||c xi_0-k||_M
 <=t+q sqrt((mu-L)/h).                                   (L-15107.4)
```

Thus the sufficient diagonal condition for convergence is

```text
t_j+q_j sqrt((mu_j-L_j)/h_j) ->0.                        (L-15107.5)
```

No vector residual appears.

## 4. Ordinary-gap fallback

Suppose instead that one has an ordinary even-complement gap

```text
C_+-U I >= g I,
```

and the Hardy weight on the support satisfies

```text
M_+ <= K I.
```

Then one may take `h=g/K`, so

```text
boxed: ||w/alpha||_(M_+)^2 <=K (mu-L)/g.                 (L-15107.6)
```

For the CCM Hardy weight on
`[lambda^(-1),lambda]`,

```text
K=2 lambda^(2 tau),
0<tau<1/2.                                                (L-15107.7)
```

Consequently

```text
||w/alpha||_(tau)^2
 <=2 lambda^(2 tau) (mu-L)/g.                            (L-15107.8)
```

## 5. Proof

The `W_+` component of the ground-state equation is

```text
(C_+-lambda_0 I)w=-alpha b.                              (L-15107.9)
```

The target component is

```text
(mu-lambda_0)alpha+<b,w>=0.                              (L-15107.10)
```

Taking the inner product of (L-15107.9) with `w` and using
(L-15107.10) gives the exact identity

```text
<(C_+-lambda_0 I)w,w>
 =(mu-lambda_0)alpha^2.                                  (L-15107.11)
```

Because `lambda_0<=U`,

```text
C_+-lambda_0 I
 >=C_+-U I
 >=hM_+.
```

Therefore

```text
h||w||_(M_+)^2
 <=(mu-lambda_0)alpha^2,
```

which proves (L-15107.3). Equation (L-15107.4) follows from

```text
c xi_0-p=q w/alpha
```

and the triangle inequality. The ordinary-gap fallback follows from
`M_+<=K I`. QED.

## 6. Strict improvement in proof architecture

`L-14302` controls the angle by

```text
||residual||_(M^-1)/h.
```

`L-15107` controls the **square** of the angle by

```text
(Rayleigh value-ground floor)/h.
```

The two estimates are related by Temple/Schur geometry, but neither universally
dominates the other. The new form is strategically better when a trace formula,
min--max comparison, or operator sandwich supplies a scalar lower floor more
readily than it supplies a correlated residual vector.

## 7. Required honesty

This lemma does not produce the floor `L`. In the actual Weil problem, proving

```text
mu_lambda-L_lambda=O(d_4(lambda))
```

is still a load-bearing theorem. The advance is that this scalar estimate can
replace the stronger vector estimate

```text
B_lambda=O(d_4(lambda)).
```
