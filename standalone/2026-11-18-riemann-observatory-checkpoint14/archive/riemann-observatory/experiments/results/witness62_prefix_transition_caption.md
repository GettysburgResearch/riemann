# Finite Legendre prefix cost and its Bessel comparison

The finite cost is \(c_m(b)=m^2+2\int_1^{(1+b)/(1-b)}[P'_{m-1}(x)]^2\,dx\), with \(P_n(1)=1\). The left panel plots \(c_m(b)/m^2\) against \(r=m^2b/(1-b)\) for \(m=4,8,16,32\) on a logarithmic vertical scale. The dashed curve is the bounded-\(r\) limit \(F(r)=I_0(2\sqrt r)^2-I_1(2\sqrt r)^2\). The right panel fixes \(r=\lambda m^{4/3}\) and plots the ratio \([c_m(b)/m^2]/F(r)\) for \(m=32,128,512\). Its dashed curve is the limit \(\exp(-2\lambda^{3/2}/3)\) for fixed \(\lambda>0\).

Finite values are obtained by integrating the square of the positive coefficient polynomial for \(d[P_{m-1}(1+2r/m^2)]/dr\). The plotted curves illustrate the analytic joint-limit proofs for the finite model. [Exact finite identity](../../audits/adversarial_reviews/director_prefix_cost_round6.md) [Joint-limit proof](../../audits/adversarial_reviews/witness62_joint_prefix.md)

Original figure generated for the Riemann Observatory project. Run python experiments/code/witness62_prefix_transition.py from the repository root with NumPy, SciPy and Matplotlib. [Python](../code/witness62_prefix_transition.py) [PDF](witness62_prefix_transition.pdf) [SVG](witness62_prefix_transition.svg) [PNG](witness62_prefix_transition.png)
