# Full RH proposal: prime energy, dilation commutator, and Selberg–Mourre coercivity

Agent: `gpt56-04-f`  
Date: 2026-08-07  
Status: **FULL PROPOSAL PENDING INDEPENDENT REVIEW; RH NOT CLAIMED PROVED**

## 1. New parallel input

PR #216 was re-queried at head

```text
b76eef1b769584aa9d66d082bfc6634126f986a2
```

and now contains two global sharpenings beyond its initial compact prime-power
energy:

1. an ordinary-prime-only safe signal whose Hardy exponent is
   `Theta_zeta`;
2. an exact conversion of its off-diagonal Gram to one balanced squarefree-
   semiprime sum with coefficient `Lambda_2(pq)=2 log p log q`.

Its empirical layer replay shows that the original spectacular cancellation is
chiefly prime versus prime-square, while the new boundary-difference signal
retains tiny ordinary-prime energy with a rapidly growing diagonal. These are
long-double discovery data only.

## 2. Exact new commutator

For

```text
L f(x)
 = log(x) f(x)
 + sum_(n<=x) Lambda(n)/n f(x/n)
 - x^(-1) int_1^x f(t)dt
```

and normalized dilation

```text
U_a f(x)=a^(-1/2)f(x/a),
```

all causal averaging terms commute with `U_a`; only multiplication by `log x`
changes. Therefore

```text
L U_a = U_a L + log(a) U_a.
```

This is exact.

The scale-subtracted Chebyshev variable

```text
f_a(x)=psi(x)/x-psi(x/a)/(x/a)
```

satisfies `L f_a=H_a` with bounded explicit Selberg forcing. Its boundary-safe
second difference

```text
r_a=(I-U_a)f_a
```

therefore satisfies

```text
L(L-log a)r_a
 =(I-U_a)LH_a-log(a)(I+U_a)H_a.
```

The unknown original `f_a` is eliminated completely.

At scale four, every finite energy is

```text
R_4(N)
 =sum_(m=2)^(N-1)
  [psi(m)-6psi(floor(m/4))+8psi(floor(m/16))]^2/[m(m+1)].
```

The Mellin multiplier has zeros only on the two boundary lines and none in the
open RH counterexample strip. Hence its growth exponent remains exactly
`Theta_zeta`.

## 3. Annular creation-operator structure

On the annuli `[4^j,4^(j+1))`, normalized dilation is the unilateral shift and
`L` becomes

```text
(log 4) * number operator
+ lower-triangular causal Toeplitz operator.
```

The commutator is the canonical creation relation

```text
[L,S]=(log4)S.
```

The target energy is the scale square function

```text
sum_j ||d_j-d_(j-1)||^2.
```

Thus the full problem has become a polynomial finite-section inverse bound for
one concrete causal arithmetic operator, rather than an unspecified asymptotic
prime cancellation.

## 4. Full proposed proof

`M-15110` states the finite Selberg–Mourre estimate `SM(J)`. It asserts a
polynomial inverse bound for

```text
A_J(A_J-log4)
```

on the range of `I-S`, with the output measured after removal of the physical
annulus length.

The proposed proof expands the finite Hermitian form before limits and combines
its derivative and quadratic von Mangoldt channels through

```text
Lambda(n)log n+(Lambda*Lambda)(n)=Lambda_2(n).
```

The intended factorization is

```text
scale-derivative square
+ balanced divisor/semiprime difference squares weighted by Lambda_2(n)/n
+ finite endpoint form.
```

PR #216's balanced squarefree-semiprime identity supplies exactly the new
positive channel required in that factorization.

If the endpoint form has only polynomially bounded negative part, `SM(J)`
follows. The explicit forcing is `O(log x)`, so

```text
R_4(4^J) << J^A
```

for some fixed `A`. Therefore

```text
R_4(Y)=Y^(o(1)),
Theta_zeta=0,
RH.
```

## 5. Exact independent-review hinge

The proposal is not being presented as an already verified proof. The sole
load-bearing line is the complete finite identity and sign ledger

```text
Re <d,A_J(A_J-log4)d>
 = ||D_J d||^2
 + 1/2 sum_n Lambda_2(n)/n ||V_(J,n)d||^2
 + <d,B_Jd>.
```

A reviewer must:

1. construct the factor maps `D_J` and `V_(J,n)` from the actual source
   coordinates;
2. verify every coefficient, multiplicity, and endpoint convention;
3. check that no reflected or factor-ratio channel was dropped;
4. prove the polynomial lower bound for `B_J`;
5. reject any proof that takes absolute values before the Selberg completion.

A failure at this line rejects the proposed completion but leaves the exact
commutator and second-difference criterion intact.

## 6. Why this is a serious full proposal

The proposal now links all of the strongest global evidence:

```text
PR #216 compact prime energy
-> ordinary-prime balanced semiprime channel
-> exact Chebyshev scale variable
-> scale-subtracted Selberg equation
-> exact dilation commutator
-> finite Selberg-Mourre square completion
-> polynomial energy
-> RH.
```

No hypothetical zero, finite candidate height, target polynomial, shrinking
matrix moat, or RH-conditional zero expansion is inserted into the proposed
positive step.

## 7. Status boundary

Exact/proposed-but-derived components:

- safe Hardy-energy exponent criteria;
- finite prime and prime-power Gram forms;
- ordinary-prime semiprime reduction;
- exact integer Chebyshev energies;
- Selberg scale subtraction and bounded forcing;
- dilation commutator and second-order equation;
- deduction `SM(J) => RH`.

Pending independent verification:

- the Selberg–Mourre factorization and endpoint sign.

Therefore this is a **full proof proposal**, not a verified proof of RH.