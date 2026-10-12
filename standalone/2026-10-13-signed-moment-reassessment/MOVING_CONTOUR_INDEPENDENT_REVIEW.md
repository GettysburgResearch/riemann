# Independent review of the moving-contour replacement

Reviewer: historical-obstruction audit agent, separate from the proof
author.

Disposition: accept the uniform factor theorem, its factor-only
threshold converse, and the conditional incidence implication at the
source hash below. The native arithmetic premises in Section 3 remain
open.

Reviewed source:

    MOVING_CONTOUR_WINDOW.md
    SHA-256 37407e4381ae6e056479c2847fad047e99ea9735156000983666361fc00b8412

This is a source-file content review. The publication's exact-commit
receipt must bind these unchanged bytes separately.

## 1. Source fidelity and attribution

I read the full note, checked the added spatial-measure paragraph in
Section 3, and independently recomputed its source hash. I also read
the relevant PR #911 identities at commit

    2f8b6a3898a722d0602a91dea73bac344a3bb7dd

in PRIME_SLOT_CANCELLATION.md and
SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md. Their SHA-256 values were
independently recomputed in the companion signed-trace review.

The finite rational factor, common norm cutoff, source exclusions,
independent left/right frequencies, and incidence labels agree with
those historical definitions. The exact filtered identity SC4 is
valid on every fixed positive real contour; choosing a different
positive contour for each fixed \(Y\) does not alter that identity.

The note correctly attributes the collision coefficients and critical
logarithmic kernel mass to PR #916. It does not claim that a smooth
moment estimate automatically controls the sharp norm truncations in
its new arithmetic premise.

## 2. Uniform upper bound

Write \(L=\log Y\), \(a=2\delta_YL\), and
\(\sigma_Y=1/2-\delta_Y\ge\sigma_0>1/3\). The local pair
factorization leaves a uniformly bounded product of degree-three
remainders. Finitely many small-prime denominators are uniformly
separated from zero; possible numerator zeros are harmless for
this upper bound. Removing primes through \(Q\) or the row changes
neither the uniform remainder bound nor the positive prime majorant.

It is therefore valid to bound the logarithm of the factor by a
constant times

\[
 \sum_{Np\le Y}(Np)^{-1+a/L}.
\]

The partial-summation calculation is uniform for
\(0\le a\le(1-2\sigma_0)L\). Its integral after logarithmic
substitution is

\[
 \int_{\log2}^{L}\frac{e^{av/L}}v\,dv.
\]

Subtracting the numerator one leaves at most
\(\sum_{m\ge1}a^m/(m\,m!)\). The bound
\(1/m\le2/(m+1)\) makes this \(O(e^a/a)\) for \(a\ge1\);
it is bounded for \(0\le a\le1\). The partial-summation endpoint
\(e^a/L\) is absorbed by \(e^a/(1+a)\) in the stipulated range.
Thus the claimed upper bound

\[
 \exp\!\left(C\left[\log\log Y+\frac{e^a}{1+a}\right]\right)
\]

holds uniformly in all independent frequencies, source rows and
incidence masks.

In particular \(e^a/(1+a)=o(\log Y)\) is sufficient for a uniform
subpower factor bound. The explicit choice \(a=\log\log Y\)
has this property. This conclusion is a bound on the factor,
with the remaining short-polynomial arithmetic still unpaid.

## 3. Converse threshold and the moving prime interval

The lower argument retains the actual unit row and one fixed
admissible cross-pair mask. At a good prime the sum of all pair
coefficients is exactly

\[
 \gamma_p=k^2+k(k-1)\Re(\nu(p)^2).
\]

The cross pairs contribute \(k^2\); the two collections of
same-side pairs give the second term. Thus
\(k\le\gamma_p\le k(2k-1)\) for every finite-order datum
\(\nu\). No cubic-order assumption on \(\nu\) is being made.

For \(x\in[1,5/4]\), primes with \(Np\ge Y^{9/10}\)
have
\(2x\log(Np)/\log Y\in[9/5,5/2]\).
The cosine is bounded above by a fixed negative constant there.
Under \(e^a/(1+a)\ge c_0L\), one has \(a\to\infty\).
The top interval

\[
 A=Y^{1-1/a}\le Np\le Y
\]

then lies inside the negative-cosine region.

I independently checked the uniform prime-theorem error in
equation (2.8a). If
\(\pi_K(t)=\operatorname{Li}(t)+R(t)\), the unconditional
prime-ideal theorem provides
\(|R(t)|\le\varepsilon_Yt/\log t\), uniformly for
\(Y^{9/10}\le t\le Y\), with \(\varepsilon_Y\to0\).
The main weighted integral is exactly

\[
 \int_{L-L/a}^{L}\frac{e^{av/L}}v\,dv
 =
 \frac{e^a}{a}
 \int_0^1\frac{e^{-w}}{1-w/a}\,dw.
\]

It is comparable to \(e^a/a\) once \(a\ge10\).
The two endpoint errors are \(O(\varepsilon_Ye^a/L)\),
and the derivative term is at most \(\varepsilon_Y\) times
the same main integral. Since \(a/L\) is bounded, all errors
are \(O(\varepsilon_Ye^a/a)\). This remains valid when \(a\)
is a fixed fraction of \(L\); no unproved short-interval
prime theorem is required.

The lower primes contribute at most
\(O(\log L+e^{(9/10)a}/(1+a))\), which is
\(o(e^a/(1+a))\) under the assumed lower threshold.
The degree-three logarithmic remainder stays bounded.
It follows that the claimed positive lower bound for the
factor's logarithm is valid.

A failure of \(e^a/(1+a)=o(\log Y)\) therefore yields a
subsequence with a fixed positive power of \(Y\). An
unbounded ratio to \(\log Y\) yields unbounded powers.
Together with the upper bound, this proves the stated
subpower and polynomial thresholds for the factor alone.
It proves no corresponding necessity for the signed trace
or filtered physical moment.

The only prime-distribution input is the classical
unconditional prime-ideal theorem used in the companion
signed-trace proof. Its primary source was personally opened
and its scope checked in that independent review. No
conductor-uniform or GRH error term enters this calculation.

## 4. Conditional arithmetic transfer

The revised Section 3 explicitly fixes \(h>0\),
\(H=(Y/b)^h\), and a nonnegative Schwartz spatial majorant.
This makes the common row measure and the Hölder argument
unambiguous. Every short polynomial has the literal common
cutoff \(Y\), including for columns whose eventual norm
window is shorter.

If the stated positive product trace premise holds, the
subpower collision bound and \(|\omega_{\mathbf q}|\le1\)
give the required bound on one exact incidence trace.
The fixed smooth Mellin transforms are rapidly decreasing
uniformly for \(\sigma_Y\in[\sigma_0,1/2]\), so the
frequency integration has a scale-independent constant.

For incidence summation, the positive divisor loss
\(\eta>0\) in

\[
 \sum_{NQ\le Y^k}(NQ)^{-2\sigma_Y+\eta}
 \ll_\eta Y^{k(1-2\sigma_Y+\eta)}
\]

is necessary for the stated uniformity. The integration
exponent is at least \(\eta\), so its implicit constant
does not diverge as \(\sigma_Y\uparrow1/2\).
The note retains this buffer and assigns it a sufficiently
small preliminary loss.

The cancellation of scale exponents is exact:

\[
 D^{2k\sigma_Y}Y^{k(1-2\sigma_Y)}
 =D^k b^{k(1-2\sigma_Y)}.
\]

The last factor is bounded above and below by fixed
constants. This proves the conditional full-moment
implication with the additional arithmetic loss \(D^e\).
All eligible incidences, source phases, and row masks
remain included.

## 5. Scope of acceptance

The moving contour supplies an admissible region for the
uncompressed Euler representation. It avoids the
fixed-below-half factor obstruction without establishing
the new arithmetic input.

The review accepts neither that input nor its stronger
one-polynomial sufficient condition. It also accepts no
unstated transfer from smooth tests to sharp truncations,
no inherited negligible-tube result for another
representation, and no physical moment estimate obtained
without the premise.

The argument is analytic. No finite numerical experiment,
zero computation, or proof-assistant replay was used to
establish its asymptotic claims. The finite execution in
this review authenticated source bytes.
