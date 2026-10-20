# Independent review of the signed common-divisor tail

20 October 2026. Reviewed `../global/SIGNED_MOBIUS_GCD_TAIL.md`, SHA256
`803307e8281f1015b403a8532301db64340e1b4521bb7e2405821c9902efdc84`.
The reviewer did not author that note, but did author the earlier centered
interface used as one of its dependencies. This is a scoped mathematical
review, not an independent certification of the inherited Liu theorem.

The exact common-extraction phase is a finite-order cubic character of
the common divisor, with the canceled local character zeros retained as
punctures. The source's extracted Gauss factors cancel on support. Thus
the stated finite-order Hecke premise suffices; growing angular uniformity
is unnecessary. The punctured reciprocal Euler product has the claimed
arbitrarily small conductor loss on a fixed line strictly to the right
of the common zero-free boundary.

The review checked the full common smooth kernel before partial summation,
including both original windows and the dependence on `s^2 n1 n2` in the
Fourier argument. Its Euler derivatives have uniform Schwartz decay at
frequency scale `L=D^2 Nd'/(H NC^2)`. Summing the entire nonzero fixed
Eisenstein lattice costs `L`, including `L<1` by decay. The two normalized
column sums cost `D/(CS)`. Combining these with `H/(D Nd')`, the signed
`s` bound `S^(beta-1)`, and the `O(C)` overlap count gives exactly
`D^2 C^(-2) S^(beta-2)`, up to the stated seminorm and small powers.

Both threshold formulas and their feasibility conditions check:
`H>=D^beta` for the original row scale at `C=1`, and
`H>=D^(6 beta-5)` for the inherited amplified scale. These are signed
component estimates before triangle in the common divisor. They do not
bound an individual positive canonical child. The original diagonal,
principal restoration and raw tails remain separate, as stated.

No defect was found in this scoped argument. The critical short common
divisor sector, including `s=1`, remains the smallest missing input for
a full inverse improvement; no numerical boundary decrease follows.
