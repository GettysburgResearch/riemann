# R-96200 — Native \(Y_4\) slack controls \(P_\Lambda-\mathcal H\), not \(J_\Lambda-\mathcal H\)

Claim ID: `R-96200`  
Status: **EXACT NORMALIZATION CORRECTION / BINDING FIREWALL**  
Created: 2026-08-16  
Primary input: PR #541 at `e381f444191e214cc992208b16d30a8d5fd461ac`  
RH status: unproved

Let
\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf 1_{q\le X},
\qquad
\Omega_X=\mathcal D_4w_X,
\]
and let \(d\) be any finitely supported physical row. With
\[
C_d(q)=\text{ordinary response},\qquad
\Xi_d=\mathcal D_4C_d,
\]
the exact radix-four duality is
\[
\boxed{\langle Y_4,\Omega_X-\Xi_d\rangle
=P_\Lambda(X)-\mathcal H(d),}
\]
where
\[
P_\Lambda(X)=\sum_{q\le X}\frac{\Lambda(q)}{\sqrt q}\log(X/q),
\qquad
\mathcal H(d)=\sum_q\Lambda(q)C_d(q).
\]

The deterministic parabolic benchmark is instead
\[
J_\Lambda(X)=\sum_{m\le X}b_X(m)\log\frac m{m-1},
\]
and
\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X).
\]
Therefore
\[
\boxed{
J_\Lambda(X)-\mathcal H(d)
=F_\Lambda(X)+\langle Y_4,\Omega_X-\Xi_d\rangle.
}
\]

Consequences:

1. all-column feasibility and small \(Y_4\) slack do not by themselves control the complete endpoint loss;
2. the `<3457` calculation in the original T-94000 packet is a bound for \(P_\Lambda-\mathcal H(d)\), not for \(J_\Lambda-\mathcal H(d)\);
3. the prime-square/Mellin endpoint consumer cannot be invoked until \(F_\Lambda\) is controlled independently;
4. a repaired successor must either prove a subquadratic bound for \(F_\Lambda\), or bypass the endpoint benchmark entirely.

The finite witness \(F_\Lambda(3)<-289/5000\) from PR #541 also forbids replacing the identity above by a nonnegative packing-slack formula.
