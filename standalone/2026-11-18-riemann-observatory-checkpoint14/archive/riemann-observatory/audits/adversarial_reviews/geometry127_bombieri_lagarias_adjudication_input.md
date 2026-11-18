# Bombieri–Lagarias | Third check of the pinned manuscript issues

I reverified SHA-256 cd13c8560f961c68e21256e5ba107bdd08fa7f34ce1e2cffbd4b63a16e8d48e0 for the 204,958-byte, twelve-page author manuscript and checked the rendered pages 2–3 and 5–8. The equations below are from that copy, whose internal title is final11aug.dvi. The 1999 journal identity is established, but I make no publisher-PDF claim. This targeted adjudication input follows the two independent full readings. [Pinned manuscript](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf) · [Advocate](uniform121_bombieri_lagarias_whole_advocate.md) · [Skeptic](weighted121_bombieri_lagarias_whole_skeptic.md) · [Pending version pin](../../quality/pending_round15/uniform121_bombieri_lagarias_source_pin.jsonl)

## Exact finite mismatch in (3.5)

The printed p. 6 explicit formula integrates the normalized archimedean kernel over \([1,\infty)\). The p. 8 display (3.5) integrates the entire last bracket only to \(1/\epsilon\). For \(x>1/\epsilon\), the term \(g_{n,\epsilon}(1/x)/x\) is zero, but the subtractor \(2g_{n,\epsilon}(1)/x^2=n/x^2\) is present. The outer minus sign makes the omitted contribution **positive**:
\[
 n\int_{1/\epsilon}^{\infty}\frac{dx}{x(x^2-1)}
 =-\frac n2\log(1-\epsilon^2).
\]

Here is a concrete endpoint-safe test computed directly from the compact test formula. At \(n=1,\epsilon=2/3\), \(g_{1,\epsilon}\) is the indicator of \((2/3,1)\) with half-values at the endpoints. The prime sum is zero, as \(1/\epsilon=3/2\) and \(\Lambda(1)=0\). The first two smooth terms are \(\log(3/2)+1/3\), the gamma constant is \(-(\log\pi+\gamma)/2\), and the finite archimedean term in (3.5) is
\[
 -\int_1^{3/2}\frac{dx}{x(x+1)}=-\log(6/5).
\]
The correct right side adds \(+\tfrac12\log(9/5)\) to this exact finite value. There is no integer or prime-power endpoint and no value-at-jump ambiguity in this difference. The compact test falls within Weil's cited hypotheses, so the independent derivation from p. 6 applies. The missing term is \(O_n(\epsilon^2)\), leaving the \(\epsilon\downarrow0\) arithmetic formula intact.

## The intended finite part can be recovered from Weil's coefficient

In p. 6 (3.2) the paper writes a generic integrand \(a(x)\) and the subtraction \(2a(1)\log\lambda\), but it inserts \(a(x)=f(x)\max(1,x)/|x-x^{-1}|\), which generally has a singularity at one. Ordinary point evaluation \(a(1)\) is undefined. In logarithmic coordinates \(x=e^t\) the measure becomes \(dt\), and that integrand becomes \(F(t)/|e^{t/2}-e^{-t/2}|\) with \(F(t)=e^{t/2}f(e^t)\). In Weil's definite finite-part convention the coefficient is the midpoint of the one-sided values of \(|t|a(e^t)\), namely \(f(1)/2\). Thus \(2a(1)\) in the generic printed formula must here be interpreted as the total singular coefficient \(f(1)\), not a value of the singular product.

The later source computation corroborates this interpretation independently. On folding about \(x=1\), the compensation is \(2f(1)/x^2\). Its integral against \((1-x^{-\lambda})x\,dx/(x^2-1)\), before multiplying by \(2f(1)\), becomes
\[
 \frac12\int_0^1\frac{1-v^{\lambda/2}}{1-v}\,dv,\qquad v=x^{-2}.
\]
At \(\lambda=2m\) this is \(H_m/2\). Monotonicity of the integral between adjacent even \(\lambda\) gives \(\tfrac12(\log(\lambda/2)+\gamma)+o(1)\). The \(\log\lambda\) coefficient is exactly \(f(1)\). This checks the full archimedean normalization \(-(\log\pi+\gamma)f(1)\) after adding the \(-\log2\pi\) term of (3.1). The problem is local notation, with a unique interpretation from its cited normalization and subsequent calculation. [Weil 1952, transcription pp. 6–7](https://denisevellachemla.eu/transc-Weil-1952.pdf)

## Weil's derivative hypothesis and what the example actually shows

I read conditions (A), (B) before the Fourier limit and the finite-part definition in the transcription of Weil's 1952 article. The downloaded transcription SHA-256 is 1edd4a831d2fcc3a5d01d82d7bbb933b7916b84d4e87b60bbe144dd883c8ce26. It expressly bounds both \(F\) and \(F'\) by \(O(e^{-(1/2+b_W)|t|})\) for some \(b_W>0\). On p. 5 of the Bombieri–Lagarias manuscript, condition (B) instead gives only endpoint decay of \(f\), and (A) is local piecewise \(C^1\) regularity with finitely many first-kind jumps.

To check the gap, use a smooth cutoff which vanishes near zero and equals one above \(x=2\), multiplying \(x^{-2}\sin(x^3)\). It satisfies the printed (A), (B). Writing \(x=e^t\), one has \(F'(t)=\tfrac12 x^{1/2}f(x)+x^{3/2}f'(x)\). At \(x=(2\pi m)^{1/3}\) large, the sine vanishes and \(f'(x)=3\), so \(F'(t)=3x^{3/2}\) diverges along the sequence. The example disproves implication of the cited hypothesis. I have not established whether its height-ordered spectral sum diverges, and it is not a counterexample to a separately proved extension of the explicit formula to the broader class. Adding \(f'(x)=O(x^{\delta-1})\) near zero and \(O(x^{-2-\delta})\) at infinity is a sufficient way to recover the cited condition. The actual compact truncated \(g_{n,\epsilon}\) meets the source's derivative condition and midpoint convention without this additional global assertion. [Weil 1952, transcription p. 6](https://denisevellachemla.eu/transc-Weil-1952.pdf)

## Relaxed multiset condition needs an orbit convention

The rendered p. 2 definition orders by \(|\Im\rho|\le T\). Under the original (2.1), the fixed-height sum is absolutely convergent even if infinitely many points occur there. Indeed \(|\Re\rho|\) is comparable to \(|\rho|\) outside a compact set in that strip, and large-\(|\rho|\) complex terms are \(O_n(|\rho|^{-1})\). The weakened inverse-square condition in the remark on p. 5 does not ensure this. The real multiset with pairs \(m+2,-m-1\) for \(m\ge1\) satisfies the relaxed weight and the stated symmetries. For \(n=1\) the summand is \(1/\rho\), so its positive and negative parts diverge in every height strip.

Even inserting a radial cutoff within each height strip would not give a universal remedy. Let \(A_j=2^j+2\) and include each \(A_j\) and \(1-A_j\) with multiplicity \(A_j-1\). This remains locally finite and its inverse-square weight is \(O(\sum_j A_j^{-1})\). Each complete pair contributes \(-1/A_j\) to the \(n=1\) sum. At radius \(A_j-1/2\) the negative member of the next pair appears alone and contributes \(-1\), while just beyond \(A_j\) the whole pair contributes only \(-1/A_j\). Consequently the two radius subsequences have limits differing by one. Both radii refer to the same entire height strip, since all points are real. This example requires no nonreal point, exceptional denominator, or broken multiplicity symmetry.

Reflection grouping repairs the relaxed statement. The orbit linear term is \(1/\rho+1/(1-\rho)=1/[\rho(1-\rho)]\), and the remainder of each fixed-power expansion is inverse-square. The grouped sum is therefore absolutely convergent and preserves height cutoff membership. If the height strips already have finitely many points, the original cutoff form coincides with this grouped convention. The direct maximal-modulus contradiction also works for the relaxed grouped version. Retain a finite reflection-invariant set containing the extrema of modulus \(R>1\) and their partners. Its partners have modulus \(1/R\). All smaller moduli are bounded by \(R_0<R\); pairs with both moduli at least \(4n\) have summed remainders \(O(n^2/|\rho|^2)\) with constant independent of \(n\) on this range, by the linear cancellation and the uniform exponential expansion. The total is \(O(n^2R_0^n+n^2)\) before the simultaneous-approximation argument. This is a qualification of the relaxation remark, with no counterexample to the original main hypotheses.

## Disposition of the main theorems

Theorem 1 uses its stated stronger summability and the real-part series, with the finite maximal-modulus set and simultaneous return of its arguments. Its direct proof needs neither the weakened remark nor the explicit formula. Theorem 2 uses compact two-cutoff tests initially, so its arithmetic proof can use the cited Weil theorem under the genuinely matched hypotheses. The exact repair of (3.5) vanishes in the limit, and the limiting constants can also be checked from the independent expansion of \(\log \xi(1+z/(1-z))\), using the classical prime number theorem remainder to identify the prime-limit constants. Thus the omitted finite tail is an exact local contradiction, the p. 6 finite-part symbol has the recovered normalization, and the broad-class statement remains a citation-hypothesis gap rather than a verified general-formula counterexample. No author flag or canonical change is proposed in this input.
