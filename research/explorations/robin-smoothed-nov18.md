# A smoothed tangent bound for a finite range of Robin's inequality

**Proposed theorem.** For every integer $5040<n\le \exp(3\cdot10^{46})$ one has $\sigma(n)<e^\gamma n\log\log n$. This is a finite range. The verified critical-line height, the previous low-range Robin computation and the explicit partial-RH prime theorem are imported. The calculation below uses no zero-density estimate.

Our low-range input is the [finite Robin theorem and source audit](robin-finite-horizon-nov18.md), which covers $\log n\le0.99\cdot10^{22}$. We prove the rest on $10^{21}\le y=\log n\le 3\cdot10^{46}$. The overlap avoids any rounding of the integer endpoint. Write $L=\log y$. The source of the additional range is the freedom to choose the tangent point $v$ independently of $y$. The cost of changing its logarithm has zero first derivative at $\log v=L$, which makes positive smoothing possible.

## Averaging the arithmetic inequality

Use the [arbitrary-integer tangent inequality (1)](robin-tangent-nov18.md) with its notation $K(v)$, $A(v)$ and $R(v)\ge0$. Let $H=3\cdot10^{12}$, $\sigma_0=8/H$, $a=16\sigma_0$, and let $U$ have the real Gaussian law of mean zero and standard deviation $\sigma_0$, conditioned on $|U|\le a$. In this note $\sigma_0$ denotes a Gaussian width; $\sigma(n)$ remains the arithmetic divisor sum. Choose $v=ye^U$. Every $v$ in this small interval satisfies the tangent inequality for the same integer $n$. Consequently it suffices to prove

$$
 \sqrt y\,L\{\mathbb E[-K(v)]+\mathbb E P(U)\}
 < \sqrt y\,L\,\mathbb E A(v),                             \tag{1}
$$

where $P(u)=\log(1+u/L)+(e^{-u}-1)/(L+u)$. Indeed $P$ is exactly the tangent error, and we have dropped $-R(v)\le0$. From

$$
 P'(u)=(1-e^{-u})\{(L+u)^{-1}+(L+u)^{-2}\},\qquad P(0)=0,
$$

and $\mathbb E U^2\le\sigma_0^2$ (conditioning a centered Gaussian on this central interval decreases the second moment), we get

$$
 \sqrt y L\,\mathbb E P(U)\le
 \tfrac12\sqrt y\,\sigma_0^2 e^a\frac L{L-a}\left(1+\frac1{L-a}\right). \tag{2}
$$

## The entire zero sum after smoothing

We use the [integrated explicit formula and signed-tail bounds (2)–(4)](robin-finite-horizon-nov18.md). They are unconditional given the verified zero census through $H$. In their notation $-K(v)=-J(v)+\int_v^\infty(\psi-\vartheta)(t)w(t)\,dt$. The contribution of each nontrivial zero $\rho=\beta+i\gamma_\rho$ to $-J(v)$ is $F_\rho(v)/\rho$, where

$$
 F_\rho(ye^u)=y^{\rho-1}\int_0^\infty
 \frac{(1+w)e^{-Lw}e^{(\rho-1-w)u}}{1-\rho+w}\,dw.             \tag{3}
$$

The bound $|1-\rho+w|\ge|1-\rho|$ holds for $w\ge0$. Bounded $|U|$ and absolute convergence of the integrated zero sum justify taking expectations termwise. For the low zeros $|\gamma_\rho|\le H$ we use $\beta=1/2$ and $\sum_{\rm low}1/(|\rho||1-\rho|)<0.047$. The scaled contribution in absolute value is at most

$$
 0.047 e^{a/2}\frac L{L-a}\left(1+\frac1{L-a}\right).          \tag{4}
$$

For high zeros split (3) at $w=1$. If $0\le w\le1$, put $z=\rho-1-w$, so $-2\le\Re z\le0$. The unconditioned normal transform is $\exp(\sigma_0^2 z^2/2)$. Its modulus is at most $\exp(2\sigma_0^2-32)$ because $|\gamma_\rho|>H$. For a standard real normal $Z$, $\Pr(|Z|>16)\le2e^{-128}$ by its exponential moment bound. By Cauchy–Schwarz the omitted tails of the complex expectation are bounded by $\sqrt2\exp(4\sigma_0^2-64)$. Dividing by the mass of the retained interval gives

$$
 \left|\mathbb E e^{zU}\right|\le
 \epsilon=\frac{\exp(2\sigma_0^2-32)+\sqrt2\exp(4\sigma_0^2-64)}
                  {1-2e^{-128}}<1.27\cdot10^{-14}.             \tag{5}
$$

For $w>1$ use $|\mathbb E e^{(\rho-1-w)U}|\le e^{(1+w)a}$. The integral of $(1+w)e^{-(L-a)w}$ on $[1,\infty)$ is $e^{-(L-a)}(2/(L-a)+1/(L-a)^2)$. Since $\beta<1$, (3), (5) and the signed tail $\sum_{\rm high}1/(|\rho||1-\rho|)<3.1\cdot10^{-12}$ bound the entire scaled high-zero contribution by

$$
 3.1\cdot10^{-12}\left[
 \sqrt y\,\epsilon(1+1/L)+
 \frac{e^{2a}}{\sqrt y}\frac L{L-a}\left(2+\frac1{L-a}\right)
 \right].                                                      \tag{6}
$$

The upper bound for the remaining archimedean term is $\log(2\pi)e^a L/((L-a)\sqrt y)$ after scaling, since $F_0(v)=1/(v\log v)$. These estimates include all zeros beyond the verified height, in both half-planes, with their multiplicities.

## Prime powers and exponent cost

Set $X=2\cdot 10^{25}$, $v_0=10^{21}e^{-a}$, $\eta=0.0002$. The verified height and Büthe's Theorem 2 imply $|\vartheta(t)-t|\le\sqrt t\log^2t/(8\pi)$ for $599<t\le X$, since $4.92\sqrt{X/\log X}<H$. On $\sqrt{v_0}\le t\le X$ the resulting relative error is at most $\eta$ by monotonicity. The elementary all-range bound $\vartheta(t)\le2t$ is proved in the [preceding finite note](robin-finite-horizon-nov18.md). In the identity $\psi(t)-\vartheta(t)=\sum_{j\ge2}\vartheta(t^{1/j})$, the terms $j\ge3$ divided by $\sqrt t$ are at most $2v_0^{-1/6}+2(\log v_0)v_0^{-1/4}/\log2$ for $t\ge v_0$. This is the cubic term and at most $\log t/\log2$ remaining terms, followed by monotonicity. For $v_0\le t\le X^2$ include $\vartheta(\sqrt t)\le(1+\eta)\sqrt t$. Beyond $X^2$ use $2\sqrt t$ for that term. The directed endpoint checks give the single majorant

$$
 \psi(t)-\vartheta(t)\le\sqrt t\,\big(1.002+1_{t>X^2}\big),\qquad t\ge v_0.
$$

Using $\log t\ge L-a$ for $t\ge v$ and integrating $t^{-3/2}$, the total scaled prime-power contribution is at most

$$
 2\frac L{L-a}\left(1+\frac1{L-a}\right)
 \left(1.002e^{a/2}+\frac{\sqrt y}{X}\right).                 \tag{7}
$$

For completeness the local exponent bound only needs primes from $q=\sqrt{2v}$ to $75q$, which all lie within the Büthe range. We have $75q<v/2$ throughout. Put $\ell=\log v$ and $s=1/(v\ell)$. For $p\le q$ one has $\min(s\log p,p^{-2})\ge s\log p/(1+\log2/\ell)$, and for $p>q$ this minimum equals $p^{-2}$. On $(q,75q]$, integration of $d\vartheta(t)/(t^2\log t)$ with $|\vartheta(t)-t|\le\eta t$ gives

$$
 \sum_{q<p\le75q}p^{-2}\ge
 (1-\eta)\int_q^{75q}\frac{dt}{t^2\log t}-\frac{2\eta}{q\log q}.
$$

Indeed integration by parts bounds the endpoint and integral errors by $\eta[2/(q\log q)+\int_q^{75q}dt/(t^2\log t)]$. Integration from $q$ to infinity gives at least $(1-1/\log q)/(q\log q)$, and the omitted upper tail is at most $1/(75q\log q)$. Combining these inequalities with $\vartheta(q)\ge(1-\eta)q$ gives

$$
 \sqrt v\,\log v\,A(v)\ge\frac{\sqrt2}{1+\log2/\ell}
 \left[(1-\eta)+(1-\eta)(1-1/\log q-1/75)-2\eta\right].      \tag{8}
$$

To scale to $\sqrt y\,L$ multiply this by at least $e^{-a/2}L/(L+a)$. All factors of (8) are positive and nondecreasing with $\ell$ on our range.

## Endpoint calculations

For each row of the table replace $\sqrt y$ by the appropriate upper or lower endpoint in every upper bound. The factors $L/(L-a)$, $1+1/(L-a)$ and $1+1/L$ decrease as $y$ grows. For (8) use $\ell\ge \log y_{\rm low}-a$ and $L/(L+a)\ge (\log y_{\rm low})/(\log y_{\rm low}+a)$. These give directed bounds for (1) on the continuous ranges.

| Range of $y=\log n$ | Upper bound for scaled error, (2), (4), (6), archimedean term and (7) | Lower bound for scaled cost, (8) |
|---|---:|---:|
| $10^{21}\le y\le10^{40}$ | $2.094$ | $2.711$ |
| $10^{40}\le y\le3\cdot10^{46}$ | $2.721$ | $2.757$ |

This proves (1) and the proposed finite theorem. The [Arb script](check_robin_smoothed_nov18.py) checks the constants at 180-bit precision. The analytic reductions, the imported zero census, and the earlier finite Robin computation are distinct inputs. The script checks none of those imported computations. No claim of a first or best published range is made.

## Optional extension with a high-zero density bound

If we additionally use the explicit density tables underlying [the high-zero moment checker](check_robin_density_nov18.py), the same argument yields the finite endpoint $\exp(2.7\cdot10^{47})$. The additional arithmetic input, including both ordinate signs, is

$$
 D(Y):=\sum_{|\gamma_\rho|>H}Y^{(\beta-1/2)_+}/\gamma_\rho^2<8702,
 \qquad Y=2.7\cdot10^{47}.                                    \tag{9}
$$

Only the scalar bound (9) is required here. We do not reprove its published density estimates. For $3\cdot10^{46}\le y\le Y$ use $\sigma_0=\sqrt{24}/H$, $a=16\sigma_0$. In the first term in (6), replace $3.1\cdot10^{-12}\sqrt y\,\epsilon$ by $8702\,\epsilon$, now with $32$ replaced by $12$ in (5). This follows from $\sqrt y\,y^{\beta-1}\le Y^{(\beta-1/2)_+}$. The $w>1$ error in (6) remains valid as written. The tangent and low-zero bounds are unchanged apart from the new $\sigma_0$.

For a tight numerical margin use the published all-range estimate $|\vartheta(t)-t|\le 1.405\cdot10^{-10}t$ for $t\ge e^{55}$, together with the overlapping Büthe estimate up to $X=2\cdot10^{25}$. This gives relative error $\eta=10^{-9}$ on the full interval from $\sqrt{3\cdot10^{46}e^{-a}}$ to infinity. The same prime-power remainder as before now gives $\psi(t)-\vartheta(t)\le(1+2\cdot10^{-7})\sqrt t$ throughout $t\ge3\cdot10^{46}e^{-a}$. Two integrations by parts show that $F_{1/2}(v)\sqrt v\log v\le 2-2/\log v+8/(\log v)^2$. In fact $F_{1/2}(v)=2/(\sqrt v\log v)-\int_v^\infty t^{-3/2}(\log t)^{-2}\,dt$ and the last integral is at least $2/(\sqrt v(\log v)^2)-8/(\sqrt v(\log v)^3)$. Use $(1+2\cdot10^{-7})F_{1/2}(v)$ in place of the prime-power estimate in (7). [Morrill–Platt, Lemmas 5–6](https://arxiv.org/abs/1809.10813)

For the lower bound let $q>1$ now be the unique solution $q^2\log q=v\log v$. Then $\sqrt v<q<\sqrt{2v}$, and the minimum in $A(v)$ changes branches exactly at $q$. Moreover $q/\sqrt v=\sqrt v\log v/(q\log q)\ge\sqrt{2/(1+\log2/\log v)}$. Integrate the reciprocal-square tail up to $10^5q<v/2$. The same Stieltjes calculation as in (8) yields

$$
 \sqrt v\log v\, A(v)\ge
 \sqrt{\frac2{1+\log2/\log v}}\,
 \left[(1-\eta)+(1-\eta)(1-2/\log v-10^{-5})-2\eta\right].
$$

The checker gives a scaled total error below $2.784$ and a scaled cost above $2.792$ on this additional interval. Its optional density path recomputes (9); this extension is separately dependent on the density tables. The preceding $\exp(3\cdot10^{46})$ range remains independent of (9).
