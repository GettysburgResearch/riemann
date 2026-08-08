# M-27901 — Fail-closed review protocol for dyadic sign rigidity

Claim ID: `M-27901`  
Title: Adversarial review contract for cofinal dyadic one-crossing and endpoint domination  
Status: **METHODOLOGY / REVIEW CONTRACT**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #276 at `a65a02b9463c1cc3a10d0af03ab359a637e357cd`

## 1. Review order

1. `L-27901-dyadic-shell-continuum-one-crossing.md`
2. `L-27902-uniform-shell-floor-error-and-crossing-reduction.md`
3. `L-27904-cofinal-finite-dyadic-shell-crossing.md`
4. `L-27903-one-crossing-collapses-wsts-to-one-total-shell.md`
5. `X-27901-dyadic-shell-one-crossing/`
6. `T-27901-dyadic-sign-rigidity-full-rh-proposal.md`
7. PR #276 `T-27501`
8. the future `ESC/EPD` production certificate

## 2. Continuum theorem checks

A reviewer must verify independently:

- the reciprocal-cell formula for `D(theta)`;
- continuity at every reciprocal knot;
- the derivative orientation and absence of interior minima;
- the odd/even sum–integral lower bounds;
- the six negative upper cells;
- the positive `N>=8` sector;
- uniqueness and simplicity of the cell-seven zero.

A numerical root bracket is not a proof of the all-cell sign theorem.

## 3. Shell-error checks

The critical identity is

```text
B_c(u)=2 sqrt(u) log(1/c)+4u(1-c^(-1/2)),  u<=c.
```

Reject the sharpening if:

- `c=floor(X/2)/X` is silently replaced by `1/2`;
- `m=floor(X/2)` is counted twice or omitted;
- `B(1)=B'(1)=0` is used with the wrong one-sided convention;
- a logarithmic factor remains in the final `q^-3/2` remainder;
- the target shell is normalized by `sqrt(Y)` rather than `sqrt(X)`.

## 4. Cofinal FSCR checks

`L-27904` is a proof claim, not a proposed production schema. Review all four of its cofinal mechanisms:

1. **normalized zero-ratio moat**
   ```text
   sqrt(theta)D(theta)
    -> -(zeta(1/2)+1)log2 >0;
   ```
2. **fixed-coordinate limit**
   ```text
   s_X(q)
    -> -(log2)/sqrt(q)
       [1+integral_0^1 zeta(1/2,1+t/q)dt] >0;
   ```
3. **transition derivative**
   ```text
   X^(3/2) d s_X(x)/dx
    =D'(x/X)+O(1/X)
   ```
   uniformly in quotient cell seven;
4. **negative upper sector**, including the exact outer-cell inequality.

Reject FSCR if:

- the Hurwitz derivative has the wrong sign;
- the eta-series bound does not imply `zeta(1/2)<-1`;
- the normalized `c_X`-dependent moat is not uniform near zero;
- the derivative error is only `O(1)` after scaling;
- reciprocal-cell boundaries or odd endpoints are omitted;
- finite scans are substituted for any cofinal step.

## 5. Endpoint domination production object

The sole open theorem is `EPD`, preferably through `ESC`.

A valid squarefree-collector certificate must export:

- the exact endpoint atom `dot b_X`;
- every ordinary-prime residual;
- a duplicate-free squarefree collector manifest;
- exact zero response on every proper prime power;
- nonnegative physical objective change;
- the complete Farkas dual;
- explicit treatment of `y_p=log p`;
- all endpoint and support terms.

A proof that controls every transverse dual mode but leaves the logarithmic ray assumed has not proved EPD.

A valid reflected-boundary alternative must retain independent frequencies and the endpoint commutator before any carry-window zeta cancellation.

## 6. Mandatory mutations

```text
M1  change floor(X/2) to X/2 at odd endpoints;
M2  delete shell subtraction before taking signs;
M3  reverse the derivative orientation in cell 7;
M4  replace the fixed-coordinate limit by a finite scan;
M5  reverse Hurwitz-zeta monotonicity;
M6  remove one low coordinate from the uniform argument;
M7  use the unweighted prime queue refuted on PR #274;
M8  use a collector endpoint divisible by a proper prime power;
M9  delete the logarithmic dual ray;
M10 infer EPD from continuum tail order alone;
M11 promote the X=10^7 scan to EPD;
M12 lose the dyadic or 2/3 Mertens mutation.
```

## 7. Verdict table

```text
continuum cell algebra                  VERIFIED / FALSE / UNPROVEN
continuum one-crossing                  VERIFIED / FALSE / UNPROVEN
uniform shell floor error               VERIFIED / FALSE / UNPROVEN
cofinal FSCR                            VERIFIED / FALSE / UNPROVEN
one-crossing tail collapse              VERIFIED / FALSE / UNPROVEN
endpoint derivative identity            VERIFIED / FALSE / UNPROVEN
ESC/EPD                                 VERIFIED / FALSE / UNPROVEN
EPD -> zero WSTS debt                   VERIFIED / FALSE / UNPROVEN
WSTS -> RH                              inherited, separately reviewed
RH                                      only if every prior row verifies
```

Reserve `FALSE` for a hypothesis-matching counterexample. A failure of one ESC construction leaves EPD open unless it contradicts the exact EPD statement.
