# Xi reverse--Rolle continuation: the high derivative tail is summably coherent

The 2026-08-22 integration stops at PR #707. Two post-integration programmes
then appeared: the common-mother scale--phase programme and the Xi
reverse--Rolle programme. The latter reached an exact first-residue root
variance identity in PR #720 and an exact second-residue/root-fourth-moment
ledger with cross-residue debt in PR #723.

The new observation is to compare three consecutive derivatives before taking
absolute values. The exact frequency

```text
kappa_m^2=M_(m+1)/M_(m-1)
```

centers the Fourier coefficient of

```text
Xi^(m+1)+kappa_m^2 Xi^(m-1)
```

to mean zero. The resulting covariance estimate gains a full square root and
is `O_T(1/m)` relative to the adjacent derivative amplitude. Critical
residues therefore differ from one negative harmonic carrier by `O_T(1/m)`.
Because coherence is insensitive to a common carrier and measures variance,
its loss is `O_T(1/m^2)`.

This proves that the product of all reverse--Rolle multiplicative coherence factors above order `M` is at least `exp(-O_T(1/M))`. The separate endpoint `-1` from the one-step count inequality is not accumulated and remains on the endpoint/winding ledger. The second-level debt of PR #723 is
quadratically small for the same reason: at a zero of the middle derivative,
the two-step harmonic recurrence forces the lower derivative itself to be
`O_T(1/m)`.

The conclusion is structural rather than RH-closing: the infinite high-order interior-coherence tail is no longer an open accumulation problem. Every serious Xi obstruction
is concentrated in a finite derivative prefix for each fixed height, together
with endpoint and winding transport. RH remains unproved.
