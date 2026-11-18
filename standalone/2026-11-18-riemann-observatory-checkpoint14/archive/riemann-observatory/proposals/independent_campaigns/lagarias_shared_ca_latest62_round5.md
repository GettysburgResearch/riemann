# A Lagarias certificate from 55,440 through 720,720

17 November 2026. At \(\epsilon_*=\log(14/13)/\log 13\), the integers \(u=55{,}440\) and \(v=720{,}720\) are the only global maximizers of \(\sigma(n)/n^{1+\epsilon_*}\). They also satisfy \(\sigma(u)<B(u)\) and \(\sigma(v)<B(v)\), where \(B(n)=H_n+e^{H_n}\log H_n\). Global concavity of \(\log(B(e^t)/e^t)\) then certifies the strict Lagarias inequality at all 665,281 integers in \([u,v]\). [Global concavity proof](lagarias_global_concavity_round2.md)

## A global maximum from prime-power increments

For \(\epsilon>0\), put \(R_{p,\epsilon}(k)=\sigma(p^k)/p^{k(1+\epsilon)}\) for \(k\ge0\). For \(k\ge1\),
\[
\frac{R_{p,\epsilon}(k)}{R_{p,\epsilon}(k-1)}
=p^{-\epsilon}\frac{p^{k+1}-1}{p(p^k-1)}
=p^{\epsilon_{p,k}-\epsilon},\qquad
\epsilon_{p,k}=\frac{\log\!\left(1+\frac{p-1}{p(p^k-1)}\right)}{\log p}.
\]
The denominator \(p^k-1\) grows strictly, so \(\epsilon_{p,k}\) decreases strictly to zero. Thus two adjacent strict threshold signs certify the unique maximizing exponent. If a threshold equals \(\epsilon\), its two neighboring exponents tie and strict decrease excludes any further tie at that prime.

The first threshold \(\epsilon_{p,1}=\log(1+1/p)/\log p\) decreases strictly in real \(p>1\), since its positive numerator decreases and its positive denominator increases. The directed calculation certifies \(\epsilon_{17,1}<\epsilon_*\), so every prime \(p\ge17\) has unique maximizing exponent zero. The exact list of primes below 17 and all the remaining checks are as follows.

| Prime | Maximizing exponents | Check |
|---|---:|---|
| 2 | 4 | \(\epsilon_{2,4}>\epsilon_*>\epsilon_{2,5}\) |
| 3 | 2 | \(\epsilon_{3,2}>\epsilon_*>\epsilon_{3,3}\) |
| 5 | 1 | \(\epsilon_{5,1}>\epsilon_*>\epsilon_{5,2}\) |
| 7 | 1 | \(\epsilon_{7,1}>\epsilon_*>\epsilon_{7,2}\) |
| 11 | 1 | \(\epsilon_{11,1}>\epsilon_*>\epsilon_{11,2}\) |
| 13 | 0, 1 | \(\epsilon_{13,1}=\epsilon_*\) exactly, and \(\epsilon_*>\epsilon_{13,2}\) |

By multiplicativity, every integer's value is at most the finite product of the local maxima. Equality forces every local exponent to maximize. The only possible products are \(2^4 3^2 5\cdot7\cdot11=u\) and \(13u=v\).

They are consecutive among integers that maximize at some \(\epsilon>0\). At \(\epsilon>\epsilon_*\), all maximizing exponents are at most the corresponding exponents of \(u\), since increasing \(\epsilon\) decreases every increment ratio. Thus every maximizing integer divides \(u\). At \(0<\epsilon<\epsilon_*\), all maximizing exponents are at least the exponents of \(v\), including the exponent at 13 because the first increment there is strictly above one. Every maximizing integer is a multiple of \(v\). Together with the equality case this excludes an intervening colossally abundant integer.

## Directed endpoint bounds

For scale \(S=2^{192}\), put \(h_n=\sum_{j=1}^n\lfloor S/j\rfloor\). Then \(h_n/S\le H_n\le(h_n+n)/S\). The replay computes this sum once, saves the intervals at the two endpoints, and evaluates \(H+e^H\log H\) with directed log and exponential intervals. The exact divisor sums come from the prime factorizations. All signs use integer comparisons. The logarithm threshold inputs are exact rational ratios before rounding. The log and exp remainder bounds are those of the standard-library compact concavity certificate.

| \(n\) | Exact \(\sigma(n)\) | Certified lower bound on \(B(n)-\sigma(n)\) |
|---:|---:|---:|
| 55,440 | 232,128 | \(>9051\) |
| 720,720 | 3,249,792 | \(>143828\) |

The result stores the threshold margins and endpoint intervals as integer numerators over \(S\). The script rechecks prime identities below 17 by trial division. Replay from the repository root with `python3 experiments/code/lagarias_latest62_ca.py`. [Replay code](../../experiments/code/lagarias_latest62_ca.py) · [Exact result](../../experiments/results/lagarias_latest62_ca.json)

## Interpolation

Let \(M_*=\sigma(u)/u^{1+\epsilon_*}=\sigma(v)/v^{1+\epsilon_*}\). For every positive integer \(n\),
\[
\log(\sigma(n)/n)\le\log M_*+\epsilon_*\log n.
\]
The affine right-hand side passes through the arithmetic endpoint values. At both endpoints the directed calculation puts it strictly below \(g(t)=\log(B(e^t)/e^t)\). Concavity puts \(g\) at least as high as the chord through its two endpoint values. Hence it lies strictly above the arithmetic support throughout the closed interval.

The existing finite certificate through 55,440 joins this interval with no gap, giving \(B(n)\ge \sigma(n)\) through 720,720 and equality only at 1. This certificate is finite. [Initial certificate](../../experiments/results/lagarias_55440_summary.json)
