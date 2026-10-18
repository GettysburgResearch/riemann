# A finite obstruction to pure paired-tilt strip models

**Status: PROPOSED, finite computer-assisted obstruction.** This excludes a
specific approximation class at degree28. It does not exclude mixed
architectures with real-zero factors, and it makes no assertion about RH.

Related repository work: #1001 at
`f6beb3774ae7ff5eca4cb046786eae10e4f88abc`, strip/PROOF.md, proves a
stronger cofinal obstruction for independent elementary three-point factors
with **all** parameters `a>=0`, using persistence of an arithmetic
progression of zeros and the Li--Radziwill nonvanishing theorem. That
result is credited here. The present obstruction is an explicit **finite
degree-28** test and additionally excludes pure paired opposite tilts of
arbitrary correlated real-zero blocks, since their real-axis transforms
are nonnegative. Neither statement excludes all correlated-field models.

Let `T` have the original normalized, symmetric theta density used in
PROOF22.md, so its characteristic function is `Xi(z)/Xi(0)`. A fresh
complete directed source computation gives

\[
 E\left[\sum_{j=0}^{14}\frac{(-1)^j(15T)^{2j}}{(2j)!}\right]<-10^{-3}.
 \tag{1}
\]

All theta indices and the complete time range are retained through explicit
Taylor, time-tail and omitted-index bounds. The verifier reconstructs
orders0,2,...,28 from the original source, rather than trusting saved
moments, fitted parameters, sampled Fourier values or numerical zeros.

## 1. A global polynomial majorant

For an integer `n>=0`, put

\[
 P_{2n}(u)=\sum_{j=0}^{n}\frac{(-1)^j u^{2j}}{(2j)!},
 \qquad R_n(u)=P_{2n}(u)-\cos u.
\]

For every real `u`,

\[
 (-1)^nR_n(u)\ge0. \tag{2}
\]

Indeed `R_0=1-cos u>=0`. For `n>=1`, `R_n''=-R_{n-1}` and
`R_n(0)=R_n'(0)=0`. Integrating twice proves (2) on `[0,infinity)` by
induction, and evenness covers negative `u`. This argument is global;
no assumption about a decreasing alternating Taylor remainder is used.

Taking `n=14` gives `cos u<=P_28(u)` for every real `u`.

## 2. Finite moment obstruction

Suppose a symmetric probability law `X` has finite moments through28
and agrees with `T` through that degree. Then (1) and (2) imply

\[
 E\cos(15X)\le E P_{28}(15X)=E P_{28}(15T)<-10^{-3}.
 \tag{3}
\]

Therefore no such law has a nonnegative characteristic function on the
entire real axis. Symmetry is only needed to identify its Fourier transform
with the real cosine expectation. The real-part obstruction itself also
holds without symmetry.

The conclusion applies equally to standardized matching: if
`Y=T/sqrt(v)` with `v=Var(T)`, and a law matches the moments of `Y`
through28, rescaling it by `sqrt(v)` gives the hypothesis above.
Nonnegativity of a real Fourier transform is preserved by this rescaling.
The test frequency in the standardized variable is `15sqrt(v)`.

There is also a quantitative stability margin. If a law `X` has moment
errors `epsilon_(2j)>=|E X^(2j)-E T^(2j)|` and

\[
 \sum_{j=1}^{14}\frac{15^{2j}\epsilon_{2j}}{(2j)!}<10^{-3},
\]

then its cosine expectation at15 is still strictly negative.

## 3. The excluded strip architecture

Let `phi` be the characteristic function of a symmetric real law with
finite exponential moments at `+-h`. The opposite-tilt construction from
PROOF.md has characteristic function

\[
 g_h(z)=\frac{\phi(z+ih)\phi(z-ih)}{\phi(ih)^2}.
\]

For every real `x`, symmetry and reality of the law give

\[
 g_h(x)=\frac{|\phi(x+ih)|^2}{\phi(ih)^2}\ge0. \tag{4}
\]

Consequently **any finite independent product consisting only of these
opposite-tilt blocks fails to match the theta moments through28**. This
does not require the base blocks to have real zeros, their supports to be
uniformly bounded, their shifts to obey any particular strip width, or
any complex normal-family hypothesis.

In particular, all factors `(a+cos(wz))/(a+1)` with `a>=1` are nonnegative
on the real axis, so their pure finite products are excluded as well.
For `a=1` this is the paired fair-spin endpoint. Allowing arbitrarily many
different weights and shifts cannot remove this finite obstruction.

Multiplying by an unpaired real-zero factor can change the sign on the
real axis and escapes (4). Thus the appropriate remaining research class
is a **mixed architecture**. The degree22 connected ferromagnet in
PROOF22.md is not contradicted by this result.

## 4. Reproduction and boundary

Run the standard-library checker from the repository root:

```text
python standalone/2026-10-18-three-direction-sprint/theta/certify_nonnegative_obstruction.py --emit standalone/2026-10-18-three-direction-sprint/theta/nonnegative_obstruction28.json
python standalone/2026-10-18-three-direction-sprint/theta/certify_nonnegative_obstruction.py --check standalone/2026-10-18-three-direction-sprint/theta/nonnegative_obstruction28.json
```

The checker pins the same320-bit outward-integer primitive as PROOF22.md,
checks the strict negative rational margin, and records all source and
term intervals. Saved JSON is accepted only by equality with a fresh
reconstruction. The inherited source identity and tail formulas are
documented in INHERITED.json and PROOF22.md. The cosine-majorant argument
above is the complete analytic consumer; numerical zero locations are
not inputs.
