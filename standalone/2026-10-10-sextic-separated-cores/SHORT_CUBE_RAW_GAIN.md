# A quantitative raw two-axis gain from the pruned theta estimate

Status: proposed source-conditional corollary of `PRUNED_COUPLED_MEAN_SQUARE.md`, Theorem 6.1, and the ordinary squarefree-row cubic/sextic large sieve. This is a bound for the raw squarefree Gauss polynomial at short squarefree dual-row heights. It is not a full-row theorem or a fourth-moment estimate.

Exact arithmetic input: PR #918's composition packet, `INTERFACE_COMPARISON.md`, Lemma 2.1 and equation (3.10), themselves derived from the source's literal cube completion and complete multiplicativity including zeros. The main theta estimate uses the pinned source dependencies listed in its companion. No new analytic hypothesis is introduced here.

## 1. The raw object and the finite truncated identity

Use the companion's fixed bad set and primary conventions. Write \(\lambda(a)=\overline{\alpha(a)}\xi(a)\); here \(\lambda\) denotes this multiplicative coefficient, not the generator of the ramified prime. Set
\[
P^{[d]}(A,B;k)=
\sum_{\substack{an\text{ squarefree}\\(an,S)=1}}
a_\xi(an)\chi_{an}(k)\mathbf1_{(a,d)=1}
W_1(Na/A)W_2(Nn/B),\qquad P=P^{[1]}.                   \tag{1.1}
\]
The mask is on the outer factor a. The inner squarefree n is allowed to share primes with d. Define \(v_d(a)=\mathbf1_{(a,d)=1}\) and write \(\mathcal C_{v_d}\) for the literal completed family with that outer mask.

The exact inverse is
\[
\frac{P(A,B;k)}{\sqrt{AB}}
=\sum_h\frac{\mu(h)\lambda(h)^3\chi_h(k)^3}{Nh}
 \mathcal C_{v_h}(A,B/(Nh)^3;k).                        \tag{1.2}
\]
Only squarefree h contribute, all outside S, and the sum is finite on physical support. Let \(R\ge1\) be a norm cutoff. Keep \(Nh\le R\) as the short part. For \(Nh>R\), expand the physical cube index b of each completion. Complete multiplicativity, including its zero on nonunits, gives
\[
\begin{split}
\mathcal C_{v_h}(A,B/(Nh)^3;k)
={}&\sum_b\frac{\lambda(b)^3\chi_b(k)^3}{Nb}
\frac{P^{[hb]}(A,B/(Nh\,Nb)^3;k)}
     {\sqrt{A B/(Nh\,Nb)^3}}.
\end{split}                                             \tag{1.3}
\]
Indeed the two restrictions \((a,h)=1\), \((a,b)=1\) are exactly \((a,hb)=1\). There is no condition \((h,b)=1\), and no condition \((n,hb)=1\) beyond zeros already present in \(\chi_{anb^3}(k)\). The repeated-prime masks in \(\chi_h(k)^3\chi_b(k)^3=\chi_{hb}(k)^3\) are retained.

Group the long part by \(d=hb\). Its exact formula is
\[
\mathcal L_R(k)=\sum_{Nd>R}
\frac{c_R(d)\lambda(d)^3\chi_d(k)^3}{Nd}
\frac{P^{[d]}(A,B/(Nd)^3;k)}{\sqrt{A B/(Nd)^3}},
\quad
c_R(d)=\sum_{\substack{h\mid d\\Nh>R}}\mu(h).           \tag{1.4}
\]
All indices avoid S; d may have arbitrary prime powers. On the finite support \(|c_R(d)|\le\tau(d)\ll D^\epsilon\). This regrouping does not replace the long inverse coefficients by independently chosen signs.

## 2. Exact short and long norm bounds

Now put \(A=B=D\), \(1\le H\), and average over squarefree good primary rows \(k\asymp H\). Take \(1\le R\le D^{1/3}\), allowing fixed support constants at endpoints. Constants may depend on fixed supports and finite seminorms as in the companion.

The companion bound, uniform for the mask \(v_h\), at \(B_h=D/(Nh)^3\), gives
\[
\sum_k^*|\mathcal C_{v_h}(D,B_h;k)|^2
\ll D^\epsilon\left[
HD+H^2D^{5/12}(Nh)^{7/4}
 +H^{4/3}D^{2/3}(Nh)^2\right].                         \tag{2.1}
\]
Here \(\min(D,\sqrt{B_h})=D^{1/2}(Nh)^{-3/2}\). The endpoint power \(5/12\) is interpreted with the arbitrary epsilon loss explained in the companion. Bounded nonempty scales are absorbed into fixed constants.

In (1.2), the exterior \(\chi_h(k)^3\) is a contraction. Minkowski and ideal counting give the following squared norm for the short sum:
\[
\boxed{\|\mathcal S_R\|_2^2
\ll D^\epsilon[
HD+H^2D^{5/12}R^{7/4}+H^{4/3}D^{2/3}R^2].}             \tag{2.2}
\]
The three norm-level sums are respectively \(\sum_{Nh\le R}(Nh)^{-1}\ll\log(2R)\), \(\sum (Nh)^{-1/8}\ll R^{7/8}\), and \(\sum1\ll R\). Thus no count of h has been silently replaced by a divisor count.

For fixed d, group the squarefree product an in (1.1). The coefficient is divisor bounded and independent of k, even with its outer mask. The ordinary squarefree-row large sieve gives
\[
\sum_k^*\left|
\frac{P^{[d]}(D,D/(Nd)^3;k)}{\sqrt{D^2/(Nd)^3}}
\right|^2
\ll D^\epsilon\left[
H+\frac{D^2}{(Nd)^3}
 +\frac{H^{2/3}D^{4/3}}{(Nd)^2}\right].                 \tag{2.3}
\]
This use of the sieve concerns a squarefree column an; it does not require d squarefree. In (1.4), \(Nd\ll D^{1/3}\) on nonempty support. The H term has only a finite harmonic sum. The other norm terms satisfy
\[
\sum_{Nd>R}(Nd)^{-5/2}\ll R^{-3/2},\qquad
\sum_{Nd>R}(Nd)^{-2}\ll R^{-1}.
\]
Therefore
\[
\boxed{\|\mathcal L_R\|_2^2
\ll D^\epsilon[H+D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}].}      \tag{2.4}
\]
All inequalities use the literal masks in (1.3)–(1.4); no primitive-character convention replaces them.

### Theorem 2.1: an optimized raw bound

For every \(1\le R\le D^{1/3}\),
\[
\boxed{\sum_{k\asymp H}^*
\left|\frac{P(D,D;k)}D\right|^2
\ll D^\epsilon\left[
HD+H^2D^{5/12}R^{7/4}+H^{4/3}D^{2/3}R^2
 +D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}+H\right].}             \tag{2.5}
\]
This follows from (1.2), (1.4), (2.2), (2.4), and the triangle inequality in the row norm. It retains the imported analytic dependencies of the companion theta bound.

## 3. Two explicit regimes with a power saving

If \(1\le H\le D^{19/44}\), choose
\[
R=D^{4/15}H^{-4/15}.
\]
The third and fourth terms of (2.5) equal \(D^{6/5}H^{4/5}\). The other terms are bounded by that quantity: the only restrictive comparison is
\[
H^2D^{5/12}R^{7/4}
=D^{53/60}H^{23/15}\le D^{6/5}H^{4/5}
\iff H\le D^{19/44}.
\]
The HD and remaining tail comparisons follow from \(H\le D\). Thus
\[
\boxed{\sum_{k\asymp H}^*|P(D,D;k)/D|^2
\ll D^{6/5+\epsilon}H^{4/5},\qquad 1\le H\le D^{19/44}.} \tag{3.1}
\]

If \(D^{19/44}\le H\le D^{19/24}\), take
\[
R=D^{1/3}H^{-8/19}.
\]
The second and fourth terms of (2.5) equal \(D H^{24/19}\). Its third term is \(D^{4/3}H^{28/57}\), which is at most this common bound precisely when \(H\ge D^{19/44}\). The remaining terms are smaller throughout this range. Hence
\[
\boxed{\sum_{k\asymp H}^*|P(D,D;k)/D|^2
\ll D^{1+\epsilon}H^{24/19},\quad
D^{19/44}\le H\le D^{19/24}.}                           \tag{3.2}
\]
The two expressions agree at \(H=D^{19/44}\). Both choices of R lie in \([1,D^{1/3}]\).

For example, with \(H=D^{1/2}\), choose \(R=D^{7/57}\). Then
\[
\boxed{\sum_{k\asymp D^{1/2}}^*|P(D,D;k)/D|^2
\ll D^{31/19+\epsilon}.}                               \tag{3.3}
\]
The ordinary squarefree-row envelope gives only \(D^{2+\epsilon}\) in this regime. This is a power saving for the actual raw two-axis Gauss polynomial, with its balanced squarefree-divisor coefficient; it is stronger than merely naming a target estimate.

## 4. Scope after this additional gain

This corollary handles cube inversion for the literal q=f=1 family by estimating its short part analytically and its long part classically. It does not require every shortened child to lie in the companion's diagonal-size range, and therefore improves on an unoptimized all-child comparison.

It still concerns squarefree dual rows at short height. The fourth-moment initialization has unrestricted dual rows near \(D^{3-\theta}\), whereas (3.2) stops far below that scale. Moving A2 exclusions and auxiliary factors are not supplied by (2.1), and the inverse all-order collision kernel is not a substitute for those local analytic adapters. No full fourth moment or new zeta zero-free boundary follows from this note alone.
