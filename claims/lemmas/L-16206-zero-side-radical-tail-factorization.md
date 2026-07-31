# L-16206 — The repaired prolate source has an exact zero-side radical-tail factorization

Claim ID: `L-16206`  
Status: **PROVED ZERO-SIDE FACTORIZATION; TAIL SCALARIZATION REMAINS OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: `L-16205`; Riemann--von Mangoldt zero count

## 1. Purpose

`L-16203` proved the radical-tail identity abstractly but retained a common
closed-form-domain gate. For the compact BV sources of `T-16201`, that gate can
be bypassed completely. The zero-side Weil series is absolutely convergent
for every localized source pairing, and radicality becomes a termwise identity.

## 2. Setup

Let `f_1,...,f_r` satisfy the assumptions of `L-16205`, and put

```text
J_j=E(f_j).                                                (L-16206.1)
```

Then

```text
Jhat_j(s)=0
```

for every nontrivial-zero parameter `s` with `1/2+is` a zeta zero.

Fix `lambda>1` and let `P_lambda` be multiplication by the characteristic
function of `[lambda^-1,lambda]`. Define

```text
g_j=P_lambda J_j,
t_j=(I-P_lambda)J_j.                                      (L-16206.2)
```

At every zero parameter,

```text
that_j(s)=-ghat_j(s),
that_j(conjugate(s))=-ghat_j(conjugate(s)).               (L-16206.3)
```

## 3. BV decay of the localized transforms

In logarithmic coordinates `u=exp(x)`, the localized function

```text
G_j(x)=g_j(exp x)
```

has compact support in `[-log lambda,log lambda]` and bounded variation.
Indeed, on this interval the sum defining `E(f_j)` has only finitely many active
terms, each of bounded variation.

For every closed horizontal substrip

```text
|Im z|<=sigma<1/2,
```

Stieltjes integration by parts gives

```text
boxed:
|ghat_j(z)|<=C_(j,lambda,sigma)/(1+|Re z|).              (L-16206.4)
```

The endpoint jumps are included in the total variation measure.

## 4. Absolute convergence of the zero-side source matrix

The Riemann--von Mangoldt estimate gives

```text
N(T)=O(T log T).                                          (L-16206.5)
```

Every nontrivial-zero parameter lies in `|Im s|<1/2`. Therefore

```text
sum_(1/2+is in Z)
  |ghat_j(conjugate(s)) ghat_k(s)| <infinity.             (L-16206.6)
```

Thus the finite localized source matrix is unambiguously defined by

```text
A_(jk)
 :=sum_(1/2+is in Z)
   conjugate(ghat_j(conjugate(s))) ghat_k(s).             (L-16206.7)
```

Multiplicity is retained.

## 5. Exact termwise tail factorization

Define the omitted-tail zero-side form by

```text
A_tail,(jk)
 :=sum_(1/2+is in Z)
   conjugate(that_j(conjugate(s))) that_k(s).             (L-16206.8)
```

Equation (L-16206.3) and absolute convergence give, term by term,

```text
boxed:
A_tail=A.                                                 (L-16206.9)
```

The cross matrices are likewise

```text
QW(g_j,t_k)=-A_(jk),
QW(t_j,g_k)=-A_(jk).                                     (L-16206.10)
```

Consequently

```text
QW(J_j,J_k)
 =A_(jk)-A_(jk)-A_(jk)+A_(jk)=0.                         (L-16206.11)
```

This is the exact radical-tail factorization required by `L-16203`, proved
without placing the sharp cutoff vectors in an imported operator domain.

## 6. Pairing with the finite CCM Fourier space

Let `w` be any compactly supported logarithmic BV function, including every
finite CCM Fourier mode multiplied by the interval characteristic. Its Mellin
transform obeys the same `O(1/|Re z|)` bound. Hence

```text
QW(g_j,w),
QW(t_j,w)                                                 (L-16206.12)
```

are absolutely convergent zero-side sums, and

```text
boxed:
QW(g_j,w)=-QW(t_j,w).                                    (L-16206.13)
```

Thus the finite matrix residual/boundary-leakage identity of `L-15102` also
holds directly on the production Fourier space.

## 7. Proof of the BV transform bound

For `z=a+ib`, write

```text
ghat_j(z)=integral_(-L)^L G_j(x)e^(-iax)e^(bx)dx,
L=log lambda.                                             (L-16206.14)
```

For `|b|<=sigma`, the function

```text
H_(j,b)(x)=G_j(x)e^(bx)
```

has total variation bounded uniformly in `b`, including its endpoint jumps.
Stieltjes integration by parts gives, for `a!=0`,

```text
|ghat_j(a+ib)|
 <=Var(H_(j,b))/|a|.                                     (L-16206.15)
```

The trivial `L1` bound handles bounded `a`, proving (L-16206.4).

To prove (L-16206.6), group zeros with `m<=|Re s|<m+1`. Equation
(L-16206.5) bounds the number in the shell by `O(log(m+2))`; the transform
product is `O((m+1)^-2)`. The series

```text
sum_m log(m+2)/(m+1)^2
```

converges. All later identities may therefore be rearranged and compared
termwise. QED.

## 8. Exact production consequence

For the repaired `0/4/8` source packet of `T-16201`, let

```text
A_lambda=localized Weil source matrix,
D_tail,lambda=ordinary omitted-tail Gram.                 (L-16206.16)
```

Then the Weil matrix has the exact representation

```text
boxed:
A_lambda=T_lambda^* QW T_lambda                           (L-16206.17)
```

on the omitted-tail packet, with no approximate-radical remainder and no
form-closure remainder.

Therefore the remaining source-sector theorem is precisely the generalized
spectral clustering problem of `L-16204`:

```text
lambda^(2tau_lambda)
 [M_lambda-m_lambda]/[M_lambda+m_lambda] ->0,             (L-16206.18)
```

where `m_lambda,M_lambda` are the extreme generalized eigenvalues of

```text
(A_lambda,D_tail,lambda).                                 (L-16206.19)
```

The superexponential `d_8` scale is already carried by `D_tail,lambda`.

## 9. Remaining gap

This lemma proves exact zero-side factorization. It does not prove:

1. that the ordinary tail Gram agrees with the standard prolate defect Gram at
   relative mode-8 scale after the arithmetic map `E`;
2. that the normalized tail Weil eigenvalues cluster;
3. the global floor, background gap, and cross-block gates of `L-16201`.

No RH proof is claimed.
