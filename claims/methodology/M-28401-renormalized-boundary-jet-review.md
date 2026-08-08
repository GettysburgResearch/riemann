# M-28401 — Review protocol for the renormalized boundary-jet cascade

Methodology ID: `M-28401`  
Status: **PROPOSED FAIL-CLOSED REVIEW PROTOCOL**  
Issue: #284

## 1. Review order

1. `R-28401-fixed-third-abel-producer-positivity-fails.md`
2. `X-28401-boundary-jet/verify.py`
3. `L-28401-shifted-central-dirichlet-taylor-contraction.md`
4. `L-28402-finite-cutoff-euler-boundary-jet-ledger.md`
5. PR #280 `L-27701/L-27702/T-27701`
6. PR #262 finite Euler and one-variable Peano formulas
7. PR #269 parity/boundary scope corrections
8. `T-28401-renormalized-boundary-jet-cascade-rh-proposal.md`
9. production `RBJC(M)` matrix and source ledger
10. PR #272 capacity/debt adapter and the square-screw/Landau consumer

## 2. Exact checks for `L-28401`

A reviewer should independently verify:

```text
paired convergence for s>0;
coefficient 1-eta(s) on the same-power channel;
coefficient (s)_ell 2^(-s-ell) zeta(s+ell)/ell! on every faster channel;
weighted radius r=1/4;
zeta(3/2)<3;
monotonicity of 3(4/7)^s-2*2^(-s);
6/sqrt(7)-sqrt(2)<6/7;
logarithmic differentiation and its Jordan factor.
```

Any omitted shifted term invalidates the claimed reserve.

## 3. Exact checks for `L-28402`

The finite review object must emit:

```text
the first omitted even and odd quotient at every q;
all endpoint conventions;
Euler jets of orders 0,...,M-1;
the exact 2^-M remainder;
shifted and unshifted legs separately;
all parity and common-destination collisions;
the next formal endpoint;
the capacity weight assigned to every jet.
```

The one-variable Peano formula may be used. A two-variable conditional-Hankel positivity assertion may not.

## 4. Production requirements for `RBJC(M)`

A claimed completion must provide one fixed integer `M` and an exact finite source map proving

\[
\mathcal J_{a+1}
\le\theta\mathcal J_a+\operatorname{poly}(a,\log X),
\qquad\theta<1.
\]

The following do not qualify:

- a floating spectral radius;
- a matrix omitting a cutoff or parity channel;
- a norm on an ambient arbitrary-vector space;
- a finite endpoint ladder;
- an asymptotic `o(1)` without explicit uniform quantifiers;
- a carry-only physical coercivity after the zeta factor has canceled.

## 5. Mandatory mutations

Reject a certificate that survives any of these altered inputs:

```text
replace 2kq-1 by 2kq;
delete the Q=520,n=15 third-Abel mutation;
omit one first-omitted quotient;
reverse one Euler finite-difference sign;
remove the 2^-M remainder;
treat repeated destinations independently before recombination;
route a boundary jet above floor((N+1)/2);
drop one parity phase;
replace the physical boundary by a pure carry window;
mutate the 6/7 bulk reserve upward to one;
```

## 6. Proof-status discipline

```text
fixed-third-Abel universal sign          false
shifted analytic bulk contraction        proposed complete
finite boundary-jet reduction            proposed complete
RBJC(M)                                  open / RH-bearing
RBJC -> DCCS -> sharp prime ramp -> RH   complete conditional chain
accepted proof of RH                     no
```
