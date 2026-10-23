# Independent review of the weighted Ford and Poisson-tail adapters

Reviewed 23 October 2026 by the type-I research agent, independently of the derivation. Verdict: the analytic inequalities reviewed below pass; this receipt does not certify a complete new zero-free region or its numerical endpoints.

Frozen inputs:

- `../two-hour-global-20261023/GENERAL_WEIGHTED_FORD_DETECTOR.md`, SHA256 `c52fa826706a26aec19cf0ed448ca4944dd86ad45ec67cc69da106fef5e6bf50`.
- `../two-hour-global-20261023/POISSON_KERNEL_ZERO_TAIL.md`, SHA256 `c862b1e3087fd4d8e8cf52c7463f9e5786121a3f71cae1dc602bf18948b35c3b`.

I read both files in full and checked the relevant formulas against the live [corrected Ford v5 primary source](https://arxiv.org/pdf/1910.08205v5), especially Lemmas 4.4--4.6 and equations (6.3), (7.2)--(7.8), (9.1), and (9.7). The local extracted source was also read around these equations.

The following points were checked explicitly.

1. The theta/b1 relation enters the later simplification (7.12), not the convolution identity, the rational W remainder, or the local half-disc argument. Retaining W itself therefore permits a freely selected theta. The polynomial argument uses nonnegative coefficients for combining inequalities and P>=0 for the prime sum and the right-line Euler integral. Those arguments apply to any fixed finite degree. The right-line constant .851 follows from the source's Euler integral and b0=1, without a degree-four assumption.

2. The remainder coefficients c4 and c5 are the compatible pair obtained directly from (7.5) and (7.8). With eta=1/2, their local-count coefficient is exactly pi^2*c5-4*c4=-4/R0. In particular the adapter does not rely on the inconsistent inequality direction printed in the later discussion or on the later alternate c5 expression. The condition lambda<=1/[2(R0+1)] is correctly retained.

3. Keeping each j separately gives the stated weighted version of the source inequality. The selected zero contributes the actual V value; bounding the remaining local zeros by the half-disc lower bound remains valid if the count includes the selected zero too, since that only enlarges the upper bound. The cotangent loss and every power of lambda and w0 in G7--G8 agree with the source normalization.

4. The new pointwise Poisson comparison is exact. For d=1-beta and r^2=d^2+(q-gamma)^2, the outside inequality is equivalent to (4d+1)r^2>=d+1/4 and is equality at r^2=1/4. Inside the disc the positive kernel is at least one. Assigning the boundary to the closed local disc makes Z2 valid without double counting. This is compatible with the source proof, whose outside remainder can be summed on the open complement.

5. Differentiating xi and using the digamma recurrence gives Z3 with precisely psi(1+s/2)/2; the 1/s term has not been dropped. The real-part zero sum is absolutely convergent at s=3/2+iq. The Euler bound 1.506 is explicitly present in Ford v5. The Euler-summation remainder yields pi/(2q) for the digamma error, and the logarithm contributes 49/(16q^2) after the factor 1/2. Together with the pole term this is 57/(16q^2), as written. Hence Z4 and Z5 have the claimed slack for q>=10000.

6. Replacing only the outside-zero estimate changes the frequency bracket to (7/3)h_j+4.8 and preserves the exact -4N subtraction. It does not alter the smoothing or gamma remainder. The global-minimum argument supplies the whole zero-free window for each frequency: lambda=B/log(Kt+1), and every zero in the relevant window has gap at least this value. A finite verified range deals with the low heights. Attainment of a minimum still requires the separately imported asymptotic region, as explicitly stated.

7. The endpoint substitution in G11 and Z8 uses adverse monotonicity only. In Z8 the positive linear prime gain is first combined at the actual B before replacing B by A; it is not enlarged by substituting an upper bound for lambda. The stated height monotonicities of W, s_j/h0^2, log(s_j)/h0^2, and q(s_j)/h0 follow with the written margins for l>=60 and K<=32.

This review covers the derivation of G1--G11 and Z1--Z8, conditional on their explicitly imported critical-line envelope and the separate retained-prime lemma. It does not independently certify the prime Bernstein calculation, the numerical values of c4 or w0, the finite endpoint checker, or the complementary logistic rectangle. Those remain separate, reviewable inputs. No claim about a fixed zero-free half-plane or RH follows from these classical-strip adapters.
