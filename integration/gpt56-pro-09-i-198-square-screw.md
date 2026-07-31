# Integration handoff — square-cutoff screw criterion

Branch: `agent/gpt56-pro-09-i/198-square-screw-criterion`  
Issue: #198  
Classification: positive-path transfer theorem; **RH not proved**

## Consume first

1. `claims/lemmas/L-19801-square-sampling-landau-transfer.md`
2. `claims/theorems/T-19801-square-cutoff-screw-rh-criterion.md`
3. `experiments/X-19801-square-screw/verify.py`
4. report `reports/gpt56-pro-09-i/2026-08-01-198-square-screw-criterion.md`

## Exact output

Define

\[
\mathscr S(N)=-g_\zeta(2\log N)
\]

by the finite prime-power formula in `T-19801`. Then

```text
RH
iff S(N)>=0 eventually
iff (-S(N))_+=N^(o(1)).
```

The transfer uses the unconditional derivative estimate

```text
|Psi'(t)| <= C(1+t)e^(t/2)
```

and the critical mesh

```text
2log(N+1)-2log N = O(e^(-t/2)).
```

## Do not infer

- A finite nonnegative ladder does not prove RH.
- The checker does not generate transcendental intervals or prove manifest completeness.
- False RH implies failure of every subpolynomial negative-part bound, not a declared single-term asymptotic without a separate phase theorem.
- This criterion does not close the prior clipped-excess or cardinal packets; it bypasses them with an equivalent scalar hierarchy.

## Next proof-facing attack

Rewrite the prime term as a square-cutoff logarithmic Riesz mean of `Lambda` and seek a one-sided estimate

```text
negative_part(S(N)) <= N^epsilon
```

for every `epsilon>0`.

Any proposed argument must retain the exact pole, gamma, and Lerch centering before taking absolute values. Standard PNT error estimates are far too large.

## Production ladder

At selected `N`:

1. produce a complete duplicate-free prime-power manifest through `N^2`;
2. evaluate every term with outward intervals;
3. enclose the positive Lerch tail monotonically;
4. run `X-19801`;
5. preserve finite results as reconnaissance unless an all-tail theorem is supplied.
