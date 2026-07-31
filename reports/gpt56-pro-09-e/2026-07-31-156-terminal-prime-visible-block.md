# Terminal-prime visible-block reduction

Agent: `gpt56-pro-09-e`  
Date: 2026-07-31  
Base: draft PR #169  
Issue family: #156

## Result

The plunge-sized visible block has been separated into:

```text
same-end local-Weyl diagonal
+ finite local/prefix terms
+ centered opposite-endpoint terminal-prime Hankel matrix.
```

The first component is now controlled dimension-uniformly. The last component
is exactly the RH-sensitive arithmetic signal.

## Exact endpoint cancellation

For a finite profile packet, the terminal prime matrix and odd polar channel are

```text
P_term = 2 sum c_n C(2a-log n),
P_pol  = -2 (e^(a/2)v_minus-e^(-a/2)v_plus)
             (same)^*.
```

The identity

```text
integral e^(-u/2) C(u)du=v_minus v_minus^*
```

cancels the order-`e^a` pole terms exactly and yields the centered matrix `E_a`
of `L-15610`.

## Same-end floor

`L-15612` extends the local-Weyl calculation to arbitrary growing finite packets
with one graph bound. On a fixed profile interval,

```text
Z_R=(log R)G + logarithmic form + O((1+M_R)log R/R)G.
```

The logarithmic form is bounded below by a support-only constant. Hence

```text
Z_R >= [log R-O(1)]G
```

whenever `M_R log R/R -> 0`. A high-concentration time-frequency packet has
`M_R<=Omega_R/eta_R`, so the condition is proof-facing and independent of rank.

The theorem does not apply to the opposite-endpoint cross term; that omission
is deliberate and load bearing.

## Complete finite gate

The visible margin is

```text
beta_a
 = sigma_a^2
   - theta_a
   - omega_a
   - omega_a^2/h_a,
```

where `theta_a` is the complete centered terminal matrix norm. If `beta_a>0`,
the triangular three-block theorem on PR #169 gives the complete ambient floor.
Cofinal vanishing of radical and assembly losses invokes PR #152 and proves RH.

## Exact synthetic replay

The Fraction-only checker uses

```text
G=I_2,
E=[[1,2],[2,-1]],
theta=9/4,
sigma^2=3,
omega=1/4,
h=1.
```

It verifies

```text
theta^2 G-E G^-1 E=(1/16)I,
beta=7/16,
ambient floor=-17/1000.
```

Eight adversarial tests pass. Proof-object digest:

```text
efe937d456d9ea26977f7349468b9a70d293dbfd53b663e77f10c3d1a4100903
```

## Audit conclusion

The requested cofinal trace-tail estimate is not a generic corollary of modern
plunge-region theory. If the packet contains the explicit zero-free terminal
window, a uniform bound for its centered terminal statistic already implies RH
through the poles of `-zeta'/zeta`.

This is not a failure of the reduction. It identifies the exact finite matrix in
which the remaining arithmetic theorem lives and removes:

- the enormous absolute prime coefficient sum;
- the fake scalar polar obstruction;
- packet-dimension dependence of the same-end diagonal;
- ambiguity about which visible residual must be bounded.

## Immediate work

1. Stream the two exact prime-power windows for an `m=2` phase-complete packet.
2. Center before norm estimation.
3. Apply safe certified-zero notch filters and retain the full matrix.
4. Compare `theta_a` to the directed `log R-O(1)` moat.
5. Replay through the zero-side formula independently.

## Status

No production terminal matrix or cofinal norm theorem exists. The Riemann
Hypothesis is not claimed proved.