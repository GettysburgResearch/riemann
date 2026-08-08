# M-27901 — Fail-closed review protocol for dyadic sign rigidity

Claim ID: `M-27901`  
Title: Adversarial review contract for the dyadic one-crossing and endpoint-domination proposal  
Status: **METHODOLOGY / REVIEW CONTRACT**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #276 at `a65a02b9463c1cc3a10d0af03ab359a637e357cd`

## 1. Review order

1. `L-27901-dyadic-shell-continuum-one-crossing.md`
2. `L-27902-uniform-shell-floor-error-and-crossing-reduction.md`
3. `L-27903-one-crossing-collapses-wsts-to-one-total-shell.md`
4. `X-27901-dyadic-shell-one-crossing/`
5. `T-27901-dyadic-sign-rigidity-full-rh-proposal.md`
6. PR #276 `T-27501` only after the new reductions verify
7. the future `FSCR` and `ESC/EPD` production certificates

## 2. Continuum theorem checks

A reviewer must verify independently:

- the reciprocal-cell formula for `D(theta)`;
- continuity at every reciprocal knot;
- the derivative orientation and absence of interior minima;
- the odd/even sum–integral lower bounds;
- the six negative upper cells;
- the positive `N>=8` sector;
- uniqueness and simplicity of the cell-7 zero.

A numerical root bracket is not a proof of the all-cell sign theorem.

## 3. Shell-error checks

The critical identity is the exact cancellation

```text
B_c(u)=2 sqrt(u) log(1/c)+4u(1-c^(-1/2)),  u<=c.
```

A reviewer must reject the sharpening if:

- the floor ratio `c=floor(X/2)/X` is replaced silently by `1/2`;
- the endpoint `m=Y` is counted twice or omitted;
- `B(1)=B'(1)=0` is used with the wrong one-sided convention;
- a logarithmic factor reappears in the final `q^-3/2` remainder;
- the finite target shell is normalized by `sqrt(Y)` rather than `sqrt(X)`.

## 4. FSCR production object

A valid proof of finite shell-crossing rigidity must export:

1. an exact integer formula for the shell residual;
2. a rigorous positive lower sector;
3. a rigorous negative upper sector;
4. a monotone or single-root transition proof in quotient cell seven;
5. a cofinal certificate for every fixed low coordinate;
6. the odd-endpoint correction `Y=floor(X/2)`;
7. exact source and target endpoint conventions.

The bounded collar and finite low dictionary may be certified by rational interval arithmetic, but the proof must supply an analytic threshold beyond which the dictionary is complete.

## 5. Endpoint domination production object

A valid `ESC/EPD` proof must export:

- the exact endpoint atom `dot b_X`;
- every ordinary-prime residual;
- a squarefree collector manifest or an independent physical source map;
- exact zero response on every proper prime power if collectors are used;
- nonnegative physical objective change;
- the complete Farkas dual;
- explicit treatment of the logarithmic ray `y_p=log p`;
- all boundary and endpoint terms.

A proof that establishes feasibility for every transverse dual mode but leaves the logarithmic ray assumed has not proved `EPD`.

## 6. Mandatory mutations

A proof object must reject at least:

```text
M1  change floor(X/2) to X/2 at odd endpoints;
M2  delete the shell subtraction before taking signs;
M3  reverse the derivative orientation in cell 7;
M4  claim all-cell monotonicity from finite scans;
M5  omit one low coordinate;
M6  widen the transition collar with X;
M7  use the unweighted prime queue refuted on PR #274;
M8  use a composite collector with a proper prime-power divisor;
M9  delete the logarithmic dual ray;
M10 infer RH from continuum one-crossing alone;
M11 promote the X=10^7 scan to a theorem;
M12 lose the dyadic or 2/3 Mertens mutation.
```

## 7. Verdict table

```text
continuum cell algebra                  VERIFIED / FALSE / UNPROVEN
continuum one-crossing                  VERIFIED / FALSE / UNPROVEN
uniform shell floor error               VERIFIED / FALSE / UNPROVEN
bounded-gate reduction                  VERIFIED / FALSE / UNPROVEN
FSCR                                    VERIFIED / FALSE / UNPROVEN
one-crossing tail collapse              VERIFIED / FALSE / UNPROVEN
endpoint derivative identity            VERIFIED / FALSE / UNPROVEN
ESC/EPD                                 VERIFIED / FALSE / UNPROVEN
FSCR+EPD -> WSTS                        VERIFIED / FALSE / UNPROVEN
WSTS -> RH                              inherited, separately reviewed
RH                                      only if every prior row verifies
```

Reserve `FALSE` for a hypothesis-matching counterexample. A missing cofinal gate is `UNPROVEN`, not a refutation of the sign architecture.
