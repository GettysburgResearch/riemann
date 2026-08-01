# Jordan–archimedean intertwiner pass

Date: 2026-08-01  
Agent: `gpt56-05-l`  
Issue: #180

## Requested result

Construct an explicit isometric Mellin/continuum intertwiner carrying the
Jordan-divisor conditional expectation to the physical Volterra Green-minimal
lift, including the complete archimedean kernel `g_omega`, and use it to prove
the physical metric identity.

## Results

### Exact arithmetic isometry

The map

\[
 (V_\omega a)(d,m)
 =\sqrt{J_{2\omega}(d)}(dm)^{-\omega}a(dm)
\]

is an exact isometry. It dilates Jordan divisor conditioning and factorizes
Mellin coherent vectors into an independent divisor feature and residual
integer feature.

### Exact archimedean lift

Suzuki's full kernel splits as

\[
 g_\omega=b_\omega-v_\omega,
 \qquad
 v_\omega=2\omega(b_\omega*_Mx^{\omega-1}),
\]

with both pieces nonnegative. Hence `g_omega` is the compression of the Krein
signature `diag(1,-1)` through an explicit two-channel isometry.

### Exact local-place tensor

In `Re u>1+omega`, the tensor coherent kernel equals

\[
 {\xi(u-\omega)\over\xi(u+\omega)}.
\]

This is the explicit Jordan/gamma intertwiner requested, on its natural Hilbert
domain.

### Positive Jordan Green primitive

Harris association for the independent prime-exponent zeta distribution gives
the unconditional finite inequality

\[
 \sum_{n\le x}{J_{2\omega}(n)\over n^{1+2\omega}}
 \ge {H_{\lfloor x\rfloor}\over\zeta(1+2\omega)}.
\]

Consequently the principal-part-subtracted arithmetic measure has a
nonnegative first cumulative primitive `R_omega(t)`. The zeta ratio is exactly
a Cauchy pole plus a symmetrized first-order energy in `L2(R_omega dt)`.

### Critical obstruction and endpoint repair

The arithmetic positive feature has a Cauchy pole at `u=1+omega`; the gamma
factor has a zero there. The signed scalar product is finite, but the positive
tensor norm diverges. The cancellation is therefore not Hilbertian.

After polarization, the pole is the Hardy kernel `1/(z+bar(w))`. Multiplication
by the gamma zero `z+bar(w)` is exactly the integration-by-parts endpoint form

\[
 \langle Dk_w,k_z\rangle+\langle k_w,Dk_z\rangle
 =k_z(0)\overline{k_w(0)}.
\]

Thus the singular channel is explicitly routed into one boundary trace. This
matches the structural role of the Mellin-boundary concomitant isolated by the
latest Volterra source, although a full normalization audit remains required.

## Honest outcome

The full physical metric identity is not proved. The remaining object is much
smaller than the original request: identify the **regularized** arithmetic
kernel, after principal-part subtraction, with the completed Volterra tail
quotient in the augmented endpoint-plus-tail graph norm.

The obstruction is not missing positivity of Jordan weights or ignorance of
`g_omega`; both are now explicit. It is one signed, nonlocal regular renewal
identity. Any proof that retains only positive conditional expectation and
omits the endpoint channel cannot be correct.
