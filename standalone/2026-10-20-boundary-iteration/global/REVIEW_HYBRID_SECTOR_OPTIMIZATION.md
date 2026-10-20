# Independent review of the all-ratio sector optimization

20 October 2026. Reviewer: root agent. This review concerns the
algebraic consequence authored by the global-route agent, not an
independent proof of the underlying hybrid mean. The reviewer did not
derive this full-ratio optimization before receiving the author's note.

Reviewed file: `HYBRID_SECTOR_OPTIMIZATION.md`, SHA256
`65da092a1641fb71839f3e54cd06ce71def3fbb183a44afcc9375ecc9e6ba555`.
Its input is the frozen hybrid mean with SHA256
`dcf9f71ae9d828f71741ae255be7d41323b9ea3ca7ab184b1c9fbeb31de82ae8`.

I independently substituted the three H7/H18 error powers into
comparison with `X Delta`. This gives G2 and both branches of G3;
the middle values coincide at displacement `1/6` and equal `1/5`.
The zero-angular Fourier coefficient remains exact.

For `a<=5/9`, differentiating the third constraint gives
`(30-54a)/(10-12d)^2`. The first/third crossing reduces to
`12ad^2-(7a+3)d+2a=0`. The smaller root lies in `(0,1/5]`,
crosses `d=1/6` precisely at `a=3/7`, and gives the first branch
of G1. Thus both proved row normalizations are needed and are used.

I also checked that the middle constraint cannot invalidate this
crossing. In the enlarged range its ratio to the first is
`1/(2a(1-d))>1`. In the original range its difference, multiplied
by `8(1-d)`, is `1+2d+a(-3+6d-8d^2)`. Substitution of
`a=3d/(2-7d+12d^2)` gives exactly the positive expression G7.

For the remaining two length ranges, the sign of the relevant
derivative bounds the minimum by its zero-displacement limit.
All other constraints are at least that value in the limit.
A sufficiently small fixed positive displacement therefore gives
every strictly smaller exponent; no endpoint estimate is inferred.
The values at `a=5/9,5/7,1` agree across branches, and balance
recovers `(sqrt(73)-1)/48`.

No algebraic or scope defect was found in this consequence. The
review is a direct symbolic argument, not a floating optimization.
It does not certify the imported theta or sieve theorems, make the
constants uniform as `a` tends to zero, insert prime coefficients
into the inner variable, or establish a smaller zero-free boundary.
