# R-92100 — Low-order Bernstein shadows do not force a passive Xi network

Claim ID: R-92100
Status: EXACT OFF-LINE-ORBIT FIREWALL
RH status: unproved

For one off-line orbit lambda=a+ib, put c=b^2-a^2, B=2ab and U=t+c. Its admittance and reciprocal impedance are

p(t)=4m U/(U^2+B^2),
Z(t)=(U+B^2/U)/(4m).

In the zeta-height range, Z is increasing and the conjugate impedance t/Z=t p is increasing. Thus all scalar and two-node tests can pass.

However

Z''(t)=B^2/(2m U^3)>0.

A complete Bernstein function is concave. Hence the first off-line failure occurs exactly at the order-three curvature shadow, agreeing with R-91902 and R-92000.

This exact control proves that positive scalar values, monotonicity of Z and t/Z, all two-node tests, and safe asymptotics do not imply a passive network. Complete Loewner positivity is the load-bearing property.

Riemann Hypothesis remains unproved.
