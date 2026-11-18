# Removing the regularity assumption in Zhao's third Mertens mean theorem

**Proposed resolution of Zhao's §8, question (1).** Let
$$
 E_2(x)=\sum_{p\le x}1/p-\log\log x-B_1,\qquad
 E_3(x)=\frac1{\log x}\prod_{p\le x}(1-1/p)^{-1}-e^{\gamma_E},
$$
where $B_1$ is the prime harmonic Mertens constant. If $\Theta=\sup_\rho\Re\rho=1$, then $\int_2^X E_3(x)dx$ changes sign infinitely often, with positive and negative excursions of size $X^{1-o(1)}$. No regular boundary function for the zeros is assumed. Together with Zhao's other cases this gives
$$
 \mathrm{RH}\quad\Longleftrightarrow\quad
 \int_2^X E_3(x)dx>0\quad\hbox{for every }X>2.
$$
The first proof imports Zhao's published Lemma 10, including its uniformity in the ordinate. A [second proof of the needed lower bound](zhao-native-oscillation-nov18.md) uses the explicit formula and a classical power-sum inequality directly, correcting the sign and endpoint constant in the printed Mellin identity. The upper bound below follows from the classical truncated explicit formula and Ingham density. The new step chooses a scale at which an actual minimizing zero has a sufficiently large horizontal contribution, using only a power lower bound for a concave envelope. [Zhao, Research in Number Theory 11 (2025), Theorem 2, Lemmas 10–11 and §8(1)](https://doi.org/10.1007/s40993-025-00640-y)

## An exposed zero at a useful scale

Assume $\Theta=1$. For $u\ge1$ define
$$
 F(u)=\min\left(\frac u2,\ \inf_{\rho=\beta+i\gamma,\ \gamma>0}
 \{(1-\beta)u+\log\gamma\}\right).
$$
The minimum on each compact $u$ interval involves only finitely many lines, since $\log\gamma\to\infty$. The resulting positive, increasing, concave function is locally absolutely continuous. It is $o(u)$ because $1-\beta$ takes arbitrarily small values. The classical zero-free region $1-\beta\gg1/\log(2+\gamma)$ gives $F(u)\gg\sqrt u$ by minimizing $cu/v+v$ (the finitely many bounded ordinates cause no issue). Consequently there are arbitrarily large differentiability points with
$$
 u F'(u)\ge \tfrac{9}{20}F(u).
 \tag{1}
$$
Otherwise integration of $(\log F)'<9/(20u)$ almost everywhere past a threshold gives $F(u)\ll u^{9/20}$. The dummy line is inactive for large $u$. Choose a minimizing zero there, and put $d=1-\beta$, $b=\log\gamma$. At a differentiability point every active line has slope $d=F'(u)$. Thus
$$
 du+b=F(u),\quad du\ge0.45 F(u),\quad b\le0.55F(u)=o(u).
 \tag{2}
$$
Moreover $d\to0$ and $\gamma\to\infty$ along these points: $d\le F(u)/u$ and a bounded set of ordinates has defects bounded below. These are all the boundary properties needed.

## An upper bound for the quadratic correction

For every fixed sufficiently small $\delta>0$, standard truncation of the von Mangoldt formula gives
$$
 |\vartheta(e^v)-e^v|\ll_\delta e^v e^{-(1-\delta)F(v)} .
 \tag{3}
$$
Here are details independent of any smooth boundary theorem. Use the half-integer $z=\lfloor e^v\rfloor+1/2$ in the classical truncated formula with an admissible height $T\asymp z^2$; its remainder is $O((\log z)^2)$ (or any fixed polylogarithm suffices). The prime-power difference is $O(\sqrt z\log^2 z)$. For a fixed $b_0<1$ sufficiently near 1, zeros with $\beta\le b_0$ give at most $O(e^{-(1-b_0)v}(1+v)^2)$ after division by $e^v$, by the full zero count. This is negligible since $F(v)=o(v)$. Choose $b_0$ so Ingham's density estimate gives $N(b_0,T)\ll_\delta T^{\delta/2}$. For the remaining zeros use
$$
 e^{-(1-\beta)v}/|\gamma|
 \le e^{-(1-\delta)F(v)} |\gamma|^{-\delta}.
$$
Their remaining weight is summable by partial summation of the density bound. Replacing $\log z$ by $v$ costs a bounded factor since $F$ is Lipschitz. This proves (3).

Write $J_1(X)=\int_2^X E_2(x)dx$ and $J_2(X)=\int_2^X E_2(x)^2dx$. Partial summation with $\vartheta(t)-t$ gives
$$
 E_2(x)=\frac{\vartheta(x)-x}{x\log x}
 -\int_x^\infty (\vartheta(t)-t)t^{-2}
 ((\log t)^{-1}+(\log t)^{-2})dt .
$$
In its tail use $F(w)\ge F(v)$ for $w\ge v$, retaining the factor $e^{-\delta F(w)}$ for integration. Since $F(w)\gg\sqrt w$, this gives $E_2(e^v)\ll_\delta e^{-(1-2\delta)F(v)}/v$. Hence
$$
 J_2(e^v)\ll_\delta e^v e^{-2(1-2\delta)F(v)}/v^2 .
 \tag{4}
$$
Indeed $F'_+(z)\to0$ by concavity and sublinearity. On $w\in[v/2,v]$ the exponent $w-2(1-2\delta)F(w)$ increases at slope at least $1/2$ at large $v$, and the part below $v/2$ is $O(e^{v/2})$. This proves (4) at every sufficiently large $v$.

## Comparison at negative and positive excursions

Fix $\epsilon=1/100$, $\delta=1/100$, and take any sufficiently large point from (1). We have $e^u>\gamma^{C_2(\epsilon)}$ because $b=o(u)$, and the other hypotheses of Zhao's Lemma 10 hold because $d\to0$, $\gamma\to\infty$. In $[e^u,e^{(1+\epsilon)u}]$ that lemma gives a point $X=e^v$ of each sign of $J_1$, with
$$
 |J_1(X)|>\frac Xv\exp[-d v-(2+\epsilon)b].
 \tag{5}
$$
The exponent spent in (5) is at most
$$
 (1+\epsilon)du+(2+\epsilon)b=(2+\epsilon)F(u)-du
 \le1.56F(u).
$$
The exponent saved in the quadratic upper bound (4) is at least $1.96F(u)$ since $v\ge u$. Thus $J_2(X)=o(|J_1(X)|)$ at both selected points. Also $|J_1(X)|\ge X^{1-o(1)}$ as $F(u)=o(u)$.

For the actual product keep the omitted prime-power tail
$$
 R(x)=\sum_{p>x}\sum_{k\ge2}1/(kp^k),\qquad
 e^{-\gamma_E}E_3(x)=\exp(E_2(x)-R(x))-1.
$$
Here $0\le R(x)\le 1/(2\lfloor x\rfloor)\le1/x$ for $x\ge2$, by summing over integers. Since $E_2(x)\to0$, Taylor's theorem on a bounded real interval gives, on integration,
$$
 e^{-\gamma_E}\int_2^X E_3(x)dx=J_1(X)+O(J_2(X)+\log X).
$$
This normalization avoids treating the finite product as the exponential of $E_2$ alone. Equation (5) dominates both errors. The two signs therefore occur at arbitrarily large $X$, with the claimed exponents. This gives the proposed resolution of §8(1); the direct power-sum proof provides the same conclusion independently of the printed Lemma 10.

## The other cases and the finite lower endpoint

For $1/2<\Theta<1$ Zhao proves the two signs by comparing the linear excursions with $X^{2\Theta-1+o(1)}$; the retained $O(\log X)$ prime-power correction has no effect. On RH, Rosser–Schoenfeld's finite range, quoted in Zhao's introduction, gives $E_3(x)>0$ for $2\le x\le10^8$. For $X\ge10^8$, Zhao's equation (18) and the last estimate of §2 give $J_1(X)>1.73\sqrt X/\log X-1.26$. The elementary inequality $e^z-1\ge z$ gives $e^{-\gamma_E}\int_2^X E_3\ge J_1(X)-\log X>0$ on this range (already strict at $10^8$ and $\sqrt X/(\log X)^2$ increases). This supplies the RH direction while accounting for $R$ in the displayed expansion preceding Zhao's (27).
