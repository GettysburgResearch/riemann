# PCR26 — bounded completion and the native off-diagonal energy attack

**PROPOSED pending independent mathematical review. No RH proof or all-scale
native covariance bound is claimed.** This is an additive continuation of PR848
at `6671339d48c7f9bb846c15d8265e53f6856c2852`.

## The positive result

The last packet made Newton extension an exact operation in reciprocal-Mobius
coordinates. This pass changes the completion so that EVERY coefficient is
bounded by three, while the entire input energy remains within a factor two of
the exact optimum. It then proves that the COMPLETE coincident-product part of
the new energy is polylogarithmic at every scale.

Write m(k)=sum_(n<=k)mu(n)/n and F_Y=sum_(k<=Y)m(k)^2. Preserve mu through Y,
then spend at most three units of coefficient per new index until the reciprocal
sum becomes zero. This clipped tail stops by Y+ceil(Y/2), and is the unique
minimum-energy completion in that bounded-tail class:

```
|c_n|<=3, P_c(1)=0, support(c)<=Y+ceil(Y/2),
F_Y<=J(c)<=2F_Y.
```

It does NOT replace the earlier unrestricted optimum F_Y or alter its proof.
The complete divisor relations still give

```
v=2c-1*c*c,
v(n)=mu(n) for every n<(Y+1)^2.
```

Every raw future is retained and has a proved finite norm.

## Exact product grouping, then a real all-scale bound

Put b=Y+1, B=b^2-1, L=max support(c), z(d)=(c*c)(d), and

```
kappa_d(k)=[H_floor(k/d)-H_k+log d]/d,
Q_Y(k)=sum_d z(d)kappa_d(k).
```

Every pair with the SAME ordinary integer product is coalesced into z(d)
before any square. The reciprocal and prime-log moments cancel exactly, so
Q_Y(k) is rational despite the individual logarithms. On the native annulus,

```
m(k)=2m_c(k)-Q_Y(k).
```

The full packet bound sum_(k>=1)kappa_d(k)^2<=18/d and the elementary divisor
estimate yield

```
D_Y:=sum_d z(d)^2 sum_(k=b)^B kappa_d(k)^2
    <=1458 H_(L^2)^4 = O((1+log Y)^4).
```

This pays all product collisions and all omitted times in the packet bound.
It does not assert independence of different product indices.

## The precise remaining signed term

Define the ordered cross covariance

```
C_Y=sum_(d!=e) z(d)z(e) sum_(k=b)^B kappa_d(k)kappa_e(k).
```

The theorem gives the unconditional reduction

```
F_B <= 9F_Y+2916 H_(L^2)^4+2C_Y.
```

Thus C_Y<=0 on all sufficiently late square-ladder stages would give
F_X=O(log^4 X), hence RH. A polylogarithmic or appropriate subquadratic upper
budget also suffices. **No such all-scale native inequality is proved.**
The positive part of C_Y contains the remaining arithmetic difficulty; it
has not been bounded by calling the Gram matrix positive.

The 28 complete finite native annuli Y=1,...,24,31,32,47,63 have rigorously
negative TOTAL C_Y. They are not a cofinal theorem. At Y=3 one individual
pair contribution is >1/40, so pairwise nonpositivity is already false.
A bounded non-native prefix satisfying the same moment/size conditions has
C_Y=Omega(Y^2). The complete native divisor equations, not just normalization
or bounded coefficients, are indispensable to the still-missing estimate.

## Claims and review priority

| Claim | Content | Boundary |
|---|---|---|
| PCR26-1 | Optimal clipped completion, bounded support/coefficient, paid trace inequality | A different restricted optimum; not a new subpower estimate |
| PCR26-2 | Exact native prefix and whole centered dilation representation | All integer endpoints; no fictitious orthogonality |
| PCR26-3 | Complete O(log^4 Y) coalesced product-diagonal bound | Does not bound the off-diagonal term |
| PCR26-4 | Exact covariance identity and native scalar bound | Signed cross term retained |
| PCR26-5 | Conditional all-height RH ending and finite sign tests | The native covariance hypothesis remains OPEN |
| PCR26-6 | All-scale non-native quadratic covariance control | Refutes generic replacements, not the Mobius target |

Read [PROOF.md](PROOF.md), especially Sections 1, 3 and 4. Review the clipping
trace comparison, whole-packet norm, product grouping and exact collar term
before considering the sign target. [VALIDATION.md](VALIDATION.md) states the
primitive coverage, rounding contracts, attempted shortcuts and actual limits.
[Source lock](SOURCE_LOCK.json) pins the inherited work and literature scope.

From this directory:

```bash
python -S -B produce.py --check result.json
python -S -B verify.py result.json --self-test
python -S -O -B produce.py --check result.json
python -S -O -B verify.py result.json --self-test
```

Both programs have one author. Implementation independence and finite negative
covariance are NOT independent mathematical acceptance or an RH proof. No old
file, registry, source review, workflow or setting is changed by this packet.
