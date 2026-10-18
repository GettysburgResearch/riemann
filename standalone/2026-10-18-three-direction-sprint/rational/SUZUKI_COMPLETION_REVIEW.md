# Scoped reconstruction of the Suzuki completion attempt

**Independent internal reconstruction, not external acceptance.** Reviewed
`../theta/SUZUKI_COMPLETION_ATTEMPT.md`, actual SHA256
`bdaaf6f4279b6c3fb4612c2381fce6d510aeb5eece385b0f59e91b8ece0f4ad1`.
Suzuki's classical innerness and eventual-sign criteria remain explicit
imports. No eventual sign or new zero-free boundary is established.

I found no blocking error in the arithmetic and archimedean adapter.
The finite divisor convolution gives its exact unit term without a
divergent-series assignment. Differentiating `t^(2omega)I(t)` proves
the zero continuous mean. Direct integration by parts gives both
incomplete-beta powers at zero; the remaining function has bounded
variation, including its integrable endpoint derivative at one. Euler
summation consequently gives the stated two tail powers and uniform
error for real y.

I independently simplified the constants using Gamma recurrence and
the zeta functional equation. In particular the second beta coefficient
is `pi^omega Gamma((1/2-omega)/2)/Gamma((1/2+omega)/2)`, so its product
with `zeta(1/2-omega)` is exactly `zeta(1/2+omega)`. This verifies the
slow fractional-tail cancellation against the finite unit kernel. The
remaining constant is exactly `4[xi(2omega)-1/2]/(1-2omega)`.

The Mellin calculation first converges with real part greater than
`2omega`. Substituting `v=s+1-omega` in the beta transform gives the
displayed quotient of completed zeta functions, with the outside
`zeta(s+1)` factor removed only by the actual Mobius convolution. The
result retains a zero obstruction unless the horizontal companion zero
is present. The draft correctly keeps the interval of omega values,
and correctly distinguishes automatic boundary modulus one from causal
Hardy membership. These qualifications are essential to the scope.
