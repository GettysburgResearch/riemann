# Bind the absorbed coefficient to the native Taylor jet

Status: proposed complete-source identity and directed certificate; native
replay passed, independent review pending. Scope: the actual Xi normalization, the same imported
complete census through 8192, and the complete paired order-one product.
This refines the interval for a single native tail coefficient. It does
not authenticate an infinite zero list, remove the residual tail, or
produce a companion-sector certificate by itself.

Keep the exact decomposition in (G1)--(G3). Write the native Taylor series

\[
\Xi(z)=c_0+c_2z^2+O(z^4),\qquad c_0=\xi(1/2)>0.
\tag{TB1}
\]

The complete even product, with every zero and multiplicity included and
no exponential prefactor, is

\[
\frac{\Xi(z)}{\Xi(0)}
=\prod_{\operatorname{Re}\rho>0}(1-z^2/\rho^2)^{m_\rho}.
\tag{TB2}
\]

Absolute convergence of `sum m/|rho|^2` justifies coefficient extraction
or logarithmic differentiation at zero. Consequently

\[
-\frac{c_2}{c_0}
=\sum_{\operatorname{Re}\rho>0}m_\rho\rho^{-2},
\qquad
a_1=-\frac{c_2}{c_0}-\sum_{0<\gamma\le8192}\gamma^{-2}.
\tag{TB3}
\]

The finite sum is over the authenticated **complete** simple real census;
every unseen tail block, including possible nonreal zeros, remains in
`a_1`. This is an actual Taylor-jet identity, rather than an estimate
based on omitted roots being real. The complete-strip conjugate-block
proof (G2) separately shows that `a_1` is real and positive.

The native coefficients are evaluated directly by outward acb series
arithmetic applied to

\[
s=\tfrac12+iz,\qquad
\Xi(z)=\frac{s(s-1)}2\exp[-(s/2)\log\pi]\Gamma(s/2)\zeta(s).
\tag{TB4}
\]

Degree two suffices for (TB3). The checker guards the nonzero constant,
the exact even-real normalization through reality/parity enclosures, and
the actual `c_0>1/4` seed. It replays all 8,049 native Hardy-Z sign brackets
and the exact complete-count library output before summing the directed
root balls. The historical FLINT complete-count dependency is imported
with precisely the scope in NATIVE_SLAB_CERTIFICATE.md; its finite Rosser
rule input is not independently rerun. The series uses the same directed
FLINT implementation, rather than an independent backend.

If the resulting exact rational enclosure is `[a_-,a_+]`, then the actual
coefficient is in that interval and in `[0,S]`. A Gaussian transport checker
may enclose this **whole source-bound interval** in place of the larger
conservative family. The residual bounds (G6) must still include the
complete unseen tail; binding `a_1` does not set its higher coefficients to
zero. Choosing the interval midpoint alone would not be a certificate.

The full directed replay in [check_taylor_tail.py](check_taylor_tail.py)
passed and wrote [taylor_tail_certificate.json](taylor_tail_certificate.json).
Its exact rational bounds imply

\[
0.0001587903<a_1<0.0001587905,
\qquad\text{certified interval width}<8.7\times10^{-11}.
\tag{TB5}
\]

Every native census bracket is replayed before this conclusion. The receipt
binds the native Taylor-series values, complete-census inputs, proof sources,
checker and backend binaries; its exact rational endpoints are tighter than
the deliberately loose decimal interval displayed in (TB5).

This supplies a sharper native parameter input. Further domain, derivative
and denominator protection remains necessary before concluding any strict
companion sector, and no unbounded-domain/RH conclusion follows.
