# M-27902 — Fail-closed review protocol for Complete Endpoint Stability

Claim ID: `M-27902`  
Title: Adversarial contract for the complete von-Mangoldt endpoint rate theorem and its reflected Selberg production object  
Status: **METHODOLOGY / REVIEW CONTRACT**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08

## 1. Review order

1. `L-27905-proper-prime-power-endpoint-reserve.md`
2. `L-27906-complete-endpoint-mellin-firewall.md`
3. `T-27902-complete-endpoint-stability-full-rh-proposal.md`
4. `L-27901`--`L-27904`
5. PR #241 independent-frequency reflected block
6. PR #216 prime/square layer audit
7. PR #276 WSTS consumer
8. a future production `ERSC` certificate

## 2. Endpoint residual checks

Verify:

- `N_X(q)=floor((X-1)/q)`, not `floor(X/q)`;
- the terminal multiple `q|X` contributes zero;
- the exact shifted-square-root formula;
- the continuum endpoint profile;
- the recurrence proving its low-ratio positivity;
- the Hurwitz limit and its sign;
- uniformity before summing prime squares.

## 3. Prime-power reserve checks

The reviewer must check independently:

- the normalized positive moat on `q<=X/10`;
- the `log p/p` square sum and its coefficient;
- the Chebyshev bound for large squares;
- the count and weight of powers with exponent at least three;
- the sign orientation
  ```text
  A_P=A_Lambda-R_pp;
  ```
- that no negative proper-power sector of logarithmic size was omitted.

Finite positive square data do not prove the cofinal reserve.

## 4. Mellin transform checks

Verify from first principles:

```text
int_m^infinity dot b_X(m)X^(-z-1)dX
 =m^(1/2-z)/[z(z+1/2)];
```

```text
Phi(z)
 =sum_(m>=2)log(m/(m-1))m^(1/2-z);
```

```text
Phi(z)=zeta(z+1/2)-1+R(z),
R holomorphic for Re z>-1/2;
```

and

```text
Mellin[A_Lambda]
 =Phi(z)/[z(z+1/2)]
  +(zeta'/zeta)(z+1/2)/z.
```

Reject the pole argument if:

- `-zeta'/zeta` is carried into the final formula with the wrong sign;
- `Phi` is claimed to contain an inverse-zeta pole;
- the factor `1/z` is omitted;
- multiplicities or the point `z=rho-1/2` are mishandled;
- normal convergence from CEP is not proved on compact half-planes.

## 5. ERSC production requirements

A reflected Endpoint Selberg Certificate must export:

1. the complete von Mangoldt source manifest;
2. the endpoint window and benchmark adjoint;
3. the independent-frequency physical matrix;
4. all prime-square and higher-power cross terms;
5. the complete Hermitian quadratic Selberg channel;
6. every endpoint and compact-support commutator;
7. a directed bound `A_Lambda=o(log X)`;
8. the prime-square reserve and ordinary-prime consumer;
9. the dyadic and `2/3` Mertens mutations.

A bound for the modulus or square of `A_Lambda` does not automatically give the required directed estimate; the sign/rate conversion must be written.

## 6. Mandatory mutations

```text
M1  replace floor((X-1)/q) by floor(X/q);
M2  delete prime squares from the complete source;
M3  reverse A_P=A_Lambda-R_pp;
M4  claim A_Lambda is one-signed;
M5  remove Phi from the Mellin transform;
M6  reverse the zeta'/zeta residue sign;
M7  use only O(log X) without a strict reserve comparison;
M8  use a one-frequency global vertical integral;
M9  discard a reflected cross term;
M10 take absolute values before Selberg recombination;
M11 lose the endpoint or m=1 boundary;
M12 promote finite boundedness to CEP.
```

## 7. Verdict table

```text
endpoint finite formula                    VERIFIED / FALSE / UNPROVEN
low-ratio endpoint positivity              VERIFIED / FALSE / UNPROVEN
proper-power logarithmic reserve           VERIFIED / FALSE / UNPROVEN
complete scalar formula                    VERIFIED / FALSE / UNPROVEN
Mellin continuation and pole firewall      VERIFIED / FALSE / UNPROVEN
CEP                                        VERIFIED / FALSE / UNPROVEN
CEP -> Mellin RH                           VERIFIED / FALSE / UNPROVEN
CEP -> EPD -> WSTS -> RH                   VERIFIED / FALSE / UNPROVEN
RH                                         only if CEP verifies
```

A failure of one reflected construction does not refute CEP. Reserve `FALSE` for a contradiction to the exact rate statement or one of its proved identities.
