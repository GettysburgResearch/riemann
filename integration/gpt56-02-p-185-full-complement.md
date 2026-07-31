# Integration handoff — critical-line uniqueness full complement

Agent: `gpt56-02-p`  
Branch: `agent/gpt56-02-p/156-sacrificial-count`  
Stack: PR #191 on PR #169  
New allocations: `L-18507`, `T-18502`, `X-18502`

## Main replacement

The missing packet identity is no longer required. For the actual complete
harmonic packet, define

```text
W_lambda=R_lambda^(perp_GC) intersect U_lambda.
```

Every nonzero harmonic lift has a nonzero Paley--Wiener transform of finite
exponential type. A nonzero finite-type entire function has only `O(T)` real
zeros, whereas Conrey gives `gg T log T` distinct simple zeta zeros on the
critical line. Hence line-zero evaluations separate `W_lambda`.

Finite-dimensional elimination extracts at most `dim W_lambda` simple line
zeros whose Gram is strictly positive on the whole complement. Thus

```text
K_Z^C|W >= sigma_Z^2 G_C|W,
sigma_Z^2>0,
codim W=dim R.
```

For every `tau<sigma_Z^2`, the selected-zero count is at most `dim R`; a strict
radical evaluation upper bound below `tau` gives equality and the automatic
angle estimate.

## Integration point

Insert

```text
tau=B_T+beta.
```

If

```text
epsilon < B_T+beta < sigma_Z^2,
```

then the counted harmonic transfer of the competing branch applies directly to
the actual complete packet, and the visible Schur floor is `beta-epsilon`.

## Remaining theorem

Qualitative frame existence does not compare `sigma_Z^2` with `B_T`. The exact
remaining scalar is

```text
B_T+beta < Sigma_lambda,
Sigma_lambda=sup_(finite simple line-zero sets Z) sigma_Z^2.
```

The packet-capture problem is closed. The frame-to-tail moat remains RH-bearing.

## Review order

1. `claims/lemmas/L-18507-critical-line-uniqueness-full-complement.md`
2. `claims/theorems/T-18502-full-complement-selected-zero-transfer.md`
3. `experiments/X-18502-full-complement/verify.py`
4. certificate, exact result, tests, README
5. report and this handoff
