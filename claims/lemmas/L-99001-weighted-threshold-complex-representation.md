# L-99001 — Weighted threshold-complex representation

**Status:** proved exactly.  **RH is not assumed.**

For a fixed threshold \(t\ge1\), form a finite labelled vertex set consisting
of

* two labels \(2_1,2_2\), each of cost \(2\) and activity \(2^{-1/2}\);
* one label \(2_3\), of cost \(2\) and activity \(2^{-3/2}\);
* one label \(p\), of cost \(p\) and activity \(p^{-1/2}\), for each odd prime
  \(p\le t\).

For a subset \(S\), let \(P(S)\) be the product of its costs and
\(r(S)\) the product of its activities.  Then
\[
\boxed{
\frac{\mathcal D(t)}6
 =\sum_{S:\,P(S)\le t}(-1)^{|S|}r(S)}
\]
(the empty subset is included), and therefore
\[
\boxed{
\frac{C(t)}6
 =\sum_{\varnothing\ne S:\,P(S)\le t}(-1)^{|S|+1}r(S)}.
\]

Indeed, with \(z=s+1/2\),
\[
\frac1{6}\sum_{n\ge1}\frac{d(n)}{n^z}
=(1-2^{-z})^2(1-2^{-z-1})
 \prod_{p\text{ odd}}(1-p^{-z}),
\]
where \(\mathcal D(t)=\sum_{n\le t}d(n)/\sqrt n\). Expanding the local factors
produces precisely the labelled-subset formula, coefficient by coefficient.

There is also a probabilistic formulation.  Select each label independently
with probability equal to its activity, and let \(K_t[R]\) be the induced
subcomplex of subsets whose cost product is at most \(t\).  With the ordinary
(non-reduced) Euler characteristic,
\[
\boxed{\frac{C(t)}6=\mathbb E\,\chi(K_t[R]).}
\]
This follows by expanding the expectation and using
\(\Pr(S\subseteq R)=r(S)\).
