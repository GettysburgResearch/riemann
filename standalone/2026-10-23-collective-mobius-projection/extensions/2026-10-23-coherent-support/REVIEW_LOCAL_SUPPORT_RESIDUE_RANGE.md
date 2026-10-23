# Review of the residue range extension

23 October 2026. Root reviewed the global-route derivation
`LOCAL_SUPPORT_RESIDUE_RANGE_EXTENSION.md`, SHA256
`a2b88fdc3f2d2685f5567b80d5a18d90d2b3de97e69a62960c52d2ddf53463e0`.
Root authored its physical-support input, but not this subsequent residue
derivation. This is an internal analytic review, not external peer review.

The reference-scale argument divides the original and reflected completed
energies by D^(1/3). The resulting terms are D^(2/3), K D^(1/6),
D^(1/2)K, D^(-1/3)K, D^(-1/3)K^(3/2), and D^(1/2)K^(1/6).
For 1<=K<=D they are covered by D^(2/3)+D^(1/2)K. This step uses
the finite-vector and functional-equation inputs, not the later residue
estimate, so there is no circularity.

In the primitive density expansion, the amplitude weight d^(-3/2)
combined with length D/d and label bound dK gives d^(-11/6) and
d^(-5/4) in the two head sums. The head condition is exactly d^2 K<=D.
The scalar tail amplitudes are d^(-11/6) and d^(-3/2), so their ideal
tails give A^(-5/6) and A^(-1/2). At A=sqrt(D/K), both squared costs
are D^(-1/6)K^(11/6). These sums have strict convergence margins.
The density identity and its fixed-puncture uniformity remain analytic
imports from the named predecessors; no continuous sixth-power reduction
is made. The residual-length support convention is explicitly retained.

For K<=D^(1/6), D^(1/2)K<=D^(2/3) and the tail exponent is at most
5/36. The full raw continuation only needs the residue range plus the
listed cost dominations. Its new mixed volume inequality permits K<=D^(4/7),
so K<=D^(1/6) is valid. At h=7/8,k=1/8 its exponents are 89/96 and
23/24; the old 47/48 exceeds their maximum by 1/48.

No issue was found in this derivation under the stated analytic imports.
It extends the full raw vector and residue range. It does not extend the
primitive continuous vector automatically or control its complement.
