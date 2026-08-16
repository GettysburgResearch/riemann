# L-93850 — The centered-Q4 cubic scalar has an exact heat-resolvent prime-block decomposition

Claim ID: `L-93850`  
Status: **PROPOSED EXACT BRIDGE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Base: PR #498 at `6cc0da2fa5711017e260ebdcea4ba8c22e453288`  
RH status: **unproved**

This packet is a separate proposed successor. It is not part of the review
verdict on PR #498.

Let

\[
H_t(\theta)=1+2\sum_{a\ge1}e^{-4\pi^2a^2t}\cos(2\pi a\theta)
\]

be the periodic heat kernel. PR #498 proves

\[
w(\theta)=-2\int_0^\infty(H_t(\theta)-1)dt.
\]

For one complete prime block `Q_(p,N)`, define

\[
h_{p,N}(t)=\int_0^1(H_t(\theta)-1)Q_{p,N}(\theta)d\theta.
\]

Then finite source support, boundedness of the step field, and heat decay give

\[
\boxed{Z_{p,N}=-2\int_0^\infty h_{p,N}(t)dt.}
\tag{L-93850.1}
\]

Summing over prime bases gives

\[
\boxed{
\mathcal A_\circ(N)
=-2\int_0^\infty h_N(t)dt,
\qquad
h_N(t)=\sum_ph_{p,N}(t).
}
\tag{L-93850.2}
\]

Weighted Cauchy with `e^(-t/2)` gives

\[
\boxed{
|\mathcal A_\circ(N)|^2
\le4\int_0^\infty e^t|h_N(t)|^2dt.
}
\tag{L-93850.3}
\]

## Safe heat diagonal

Let

\[
A_{p,N}=\sum_{m\le N}|c_{\circ,p}(m)|.
\]

Every block field satisfies

\[
\|Q_{p,N}\|_\infty\le3A_{p,N}.
\]

Because `H_t>=0` and `int H_t=1`,

\[
\|H_t-1\|_1\le2,
\]

so

\[
|h_{p,N}(t)|\le6A_{p,N}.
\]

For `t>=1`, use `pi^2>9` and `a^2>=a`:

\[
\|H_t-1\|_1
\le2\sum_{a\ge1}e^{-4\pi^2a^2t}
<4e^{-36t},
\]

hence

\[
|h_{p,N}(t)|<12A_{p,N}e^{-36t}.
\]

With `e<3`, these bounds give the deliberately safe estimate

\[
\boxed{
\int_0^\infty e^t|h_{p,N}(t)|^2dt
<112A_{p,N}^2.
}
\tag{L-93850.4}
\]

Using the complete-tower bound from PR #498,

\[
\sum_pA_{p,N}^2\le80N\log(2N),
\]

one obtains the unconditional heat diagonal

\[
\boxed{
\sum_p\int_0^\infty e^t|h_{p,N}(t)|^2dt
<8960N\log(2N).
}
\tag{L-93850.5}
\]

## Resolvent form

If

\[
\widehat Q_{p,N}(a)
=\int_0^1Q_{p,N}(\theta)\cos(2\pi a\theta)d\theta,
\]

then

\[
h_{p,N}(t)
=2\sum_{a\ge1}e^{-4\pi^2a^2t}\widehat Q_{p,N}(a).
\]

Consequently

\[
\boxed{
\int_0^\infty e^th_{p,N}(t)h_{r,N}(t)dt
=4\sum_{a,b\ge1}
\frac{\widehat Q_{p,N}(a)\widehat Q_{r,N}(b)}
{4\pi^2(a^2+b^2)-1}.
}
\tag{L-93850.6}
\]

This is an exact positive heat-resolvent kernel on the mode pair `(a,b)`. It
turns the static cubic scalar into a time-resolved distinct-prime coherence
problem while retaining the complete prime towers.

```text
heat representation                    exact
prime-block heat amplitudes             exact
weighted Cauchy bridge                   exact
same-prime heat diagonal O(N log N)      proposed exact proof above
cross-prime heat-resolvent estimate      open
Riemann Hypothesis                       unproved
```
