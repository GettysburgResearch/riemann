# Transporting a zero-free strip through the certified heat flow

Let $\Theta$ be the supremum of the real parts of the nontrivial zeta zeros and let $\Lambda$ have the Polymath normalization. In this normalization the squared imaginary height of every zero of $H_0$ is at most $q_*=(2\Theta-1)^2$. The following proposed deductions use the physical source, wall, compactness, and kernel theorems in Raymond's October 29 manuscript. The new finite computation evaluates two authenticated source files independently. It does not reverify the analytic theorems or the upstream physical-source certificates. [Raymond, §§2–4 and reproducibility record](https://doi.org/10.5281/zenodo.23752103)

## A bound directly relating the two unknown constants

With $r=12.380974$, the imported current estimates give
\[
 \boxed{\displaystyle
   \Lambda\le \frac{\log(1+r q_*/2)}{r},\qquad
   \Theta\ge\frac12+\frac12\sqrt{\frac{2(e^{r\Lambda}-1)}{r}} .}
 \tag{1}
\]
The second statement uses the known $\Lambda\ge0$. Both inequalities hold at $\Theta=1/2$, when $\Lambda=0$.

Here is a proof accounting for all thermal and contact-height domains. On row $i$, let $[a_i,b_i]$ denote its time interval, $c_i$ its squared-height cap, $S_i$ the physical source lower chord (86), and $O_i$ the whole signed own-pair contribution (87)–(88). At a simple highest exterior zero of height $y>0$, with $q=y^2\le c_i$, Raymond's (89) gives
\[
 q'(t)\le -2-2q(t)\{S_i(t)-O_i(q(t))\}.
 \tag{2}
\]
The kernel theorem proves $O_i$ is nondecreasing on the whole interval $[0,c_i]$. The source chord is nondecreasing throughout the closed time cell. Exact rational evaluation at the corner $(a_i,c_i)$ in each of the 67 rows gives
\[
 12.380974 < \min_i 2\{S_i(a_i)-O_i(c_i)\}<12.380975.
\]
The minimum occurs in the first row. The finite-head wall excludes the other physical zeros from a nonreal highest contact. Raymond's certified arcs imply that the actual maximal heights stay within the respective row caps up to $T=22101/204800$. Then ordinary de Bruijn contraction bounds the heights by their terminal cap until all zeros are real, by time $0.107964910079$, still within the last row ending at $87/800$. Thus (2) with its uniform rate applies at any relevant first contact, even if a trial comparison curve itself lies above the active cap at some earlier time. Raymond's full-height kernel statement and the removal of the former row-55 local credit explicitly cover values below that row's auxiliary tube. [Raymond, Theorems 2.10, 3.1, 3.4, Proposition 4.3 and §4.5](https://hexagonmath.org/pdf/2611.00460v1)

Starting at $q_*+\epsilon$, use the solution of $Q'=-2-rQ$ while it is positive. Its initial separation persists for a sufficiently short interval by ordinary de Bruijn strip contraction. The positive-time compactness and multiple-contact lemma of the source apply afterward. At an alleged first contact (2) gives a strictly smaller derivative than $Q'$. At a row junction use the incoming cell. Letting the curve decrease to zero gives reality by continuity, or by paying $Q(t)/2$ at each positive intermediate height and taking a limit. Send $\epsilon$ to zero. If its hitting time lies beyond the known all-real time the assertion already follows from that known time. This proves (1).

For sufficiently small $q_*$ the comparison returns to zero inside the first time cell. In that cell one may use the limiting rate $r(q_*)=2\{S_0(0)-O_0(q_*)\}$ by applying the same argument at $q_*+\epsilon$ before passage to the limit. The first row is analytic at zero, with $12.651018<r(0)<12.651019$. Consequently the leading refinement near the critical line is
\[
             \Lambda\le q_*/2-\frac{r(0)}8q_*^2+O(q_*^3).
\]
The rational evaluations underlying both rates are available in the checker's constants mode. [Exact rational checker](../../experiments/X-nov18b-heat-seed/check.py)

## Finite integration from three source strips

For a supplied zero-free abscissa $\theta$ in $[1/2,7/8]$, start with the strict squared-height ceiling $(2\theta-1)^2+10^{-13}$, rounded up on a $10^{-28}$ grid. Divide each of the 67 licensed time cells into steps of length $\Delta=1/N$. At an incoming state $(t,q)$ use the exact rationals from the source to form
\[
 k=\big\lfloor 10^{20}\,2(S_i(t)-O_i(q))\big\rfloor-1,\qquad R=k/10^{20}.
\]
All active incoming states satisfy $0<q\le c_i$ and $0<R\Delta<1$. On this step $S_i$ is at least its initial value and every positive point of the decreasing comparison arc has own contribution at most $O_i(q)$. Therefore $Q'=-2-RQ$ gives a strict first-contact comparison. Initial separation at a positive time follows as above. The wall and compactness inputs in (2) have the same scope for these new arcs.

If $q-(2+Rq)\Delta>0$, the true comparison arc remains strictly positive to its end. For $x=R\Delta$,
\[
 \frac{1-e^{-x}}{x}\ \ge\ 1-\frac x2+\frac{x^2}{6}-\frac{x^3}{24}.
\]
Subtracting $(2+Rq)\Delta$ times the right side from $q$ and rounding upward to the height grid gives an admissible outward reset. The code checks strict decrease after rounding, all time joins and the cap at every incoming state. If the positivity test fails, the code stops before that step and adds the full $q/2$ de Bruijn cleanup to $t$. It checks the source and wall horizons. Hence the printed rational endpoint is an upper bound for $\Lambda$. No transcendental floating-point evaluation enters the integration.

The reproduction packet contains Raymond's original two data files in compressed form with their published hashes and attribution. The subsequent explicit evaluations use their whole signed rational functions, including the joint derivatives in rows 0, 16 and 44. The checker obtains the joint derivative by the binomial expansion of the two reciprocal powers at $p\pm\sqrt q$. A separate implementation using their Newton recurrence gives the identical rational endpoint at $N=512000$ for the November seed. [Packet and commands](../../experiments/X-nov18b-heat-seed/README.md)
