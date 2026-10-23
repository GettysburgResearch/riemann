# Independent review of the squared-frequency detector

2026-10-21. This review binds
`../three-hour-boundary/QUADRATIC_SIGMA_LOGISTIC_DETECTOR.md`, SHA256
`2922cbb84355ead8db6af9bcce8cf35bfb71cf5051798b2bf521296f1dadf68a`,
its producer SHA256
`74ea91d3c34d430110f8a3c7d1b42374e9accc27eaf0d935169971b0fc27acf1`,
and its margin source SHA256
`4d2a19785b947f3ecd1b766237b9eee8ee5eed2edf349aee470a2df584c6eb15`.

No issue was found in the new mechanism. Complete monotonicity of
h(s)=sech(sqrt(s)) gives the positive Gaussian mixture for
h(v^2*a^2+v^2*lambda*k^2) directly. The exact sum-of-squares polynomial
therefore still supplies termwise arithmetic positivity. This argument
allows the squared-frequency increment; it does not incorrectly require
sigma_k itself to be affine in k.

The square-root concavity bound is in the required direction, with
sigma_k-sigma_0<=d*(eta/l)*k^2. The prime perturbation cost is consequently
(3/2)*14*16*d*eta^2/l=336*d*eta^2/l. All omitted prime terms retain a
definite sign. The cutoff comparison can be squared because a>0 and the
target is positive. For L_k>c it gives exactly(Q6); for L_k<=c it is
automatic. The uniform replacement of eta/(2*a*l) is an upper bound.
The k=3 gap remains strictly positive under exact rational enclosures.

The rationalized selected-zero argument rho is algebraically correct
and continuous at A=0. The two selected transforms use alpha_1, and the
pole uses alpha_0. The gamma, real-axis and tail bounds remain in their
previously reviewed uniform domains. Thus the per-frequency cutoffs and
global minimum-zero assembly reviewed in REVIEW_VARIABLE_SIGMA_DETECTOR.md
apply without an additional analytic hypothesis.

`verify_quadratic_sigma_fraction.py`, SHA256
`68f31c13bbc906e99dfdb283648415cf52473861b825ffa15ee608c301fafb3a`,
independently certifies the full rectangle

    A in[0,500/2403],       log(t) in[28,83].

It uses exact integers and Fractions. Square roots are enclosed by
integer square roots after192-bit outward scaling; the older rational
Taylor/logarithm/moment engine remains SHA-pinned. Normal and optimized
Python runs agree exactly. There are43 accepted closed rectangles after
85 evaluations, with minimum lower bound greater than1.282548e-6 and
exact coverage area27500/2403. Containment, disjoint interiors, total
area, cutoff inequalities, prime constants and endpoint bounds are all
checked exactly. The unsupported A=1/4 is rejected.

The certificate `QUADRATIC_SIGMA_FRACTION_CERTIFICATE.json` has SHA256
`731a07586b7cd970441b7aedb4c1a41700ed34673e25b0d26aaf54a3c2eff964`.

The proposed classical denominator4.806 uses the same published
Littlewood constant21.233 and the same imported finite verification and
zero-count estimates as the earlier certificates. This receipt does not
claim an improved fixed-width Hecke boundary, RH, or external priority.
Independent human review of the assembled proof remains outstanding.
