# An explicit Li positivity horizon at the verified height

**Proposed finite corollary.** With $T=3\,000\,175\,332\,800$, all the classical Li coefficients satisfy
$$
 \lambda_n>0\qquad(1\le n\le 100T^2=900\,105\,202\,754\,159\,075\,584\,000\,000).
$$
This conclusion uses the published Platt–Trudgian census, explicit zero-density theorems and a finite interval calculation. It does not involve computing these coefficients individually. [Height source lock](../../formal/registry/deltas/C_EXTERNAL_SOURCE_STATEMENTS/EXT.XI.PLATT_TRUDGIAN.2021.txt) · [Companion analytic Li argument](observatory-nov18.md)

**1. A positive reference sum.** Put $M=100T^2$. The companion proof covers $n\le2T^2\log T$, which exceeds $5\cdot10^{26}$. For the remaining $n$ define $\phi_0(t)=2\arctan(1/(2t))$ and $L_n^0=2\sum_{\gamma>0}(1-\cos(n\phi_0(\gamma)))$, using the actual ordinates and their multiplicities. Then
$$
 L_n^0\ge \tfrac12 n(\log n+\gamma_E-1-\log(2\pi))-100\sqrt n\log n>29n .
$$
For explicit error accounting take $A=\sqrt n$ and drop the nonnegative summands through $A$. Above $A$, replacing $\phi_0(t)$ by $1/t$ costs at most $(n/6)\sum_{\gamma>A}\gamma^{-3}$. For $A\ge100$, $N(t)\le t\log t$ gives $\sum_{\gamma>A}\gamma^{-3}\le4\log(2A)/A^2$ by summing over dyadic intervals. In the Stieltjes integral with $1-\cos(n/t)$ the counting error has magnitude at most $10\log t$ for $t\ge100$, by the explicit Riemann–von Mangoldt estimate in the companion source (the constant term $7/8$ may be included in the main term). Including the factor two, integration by parts bounds the resulting error by $40\log A+20n(1+\log A)/A$. Extending the main integral to zero costs at most $(2/\pi)\int_0^A|\log(t/(2\pi))|dt$. These three errors total less than $100\sqrt n\log n$ in the range used. The full main integral evaluated by the Mellin identity in the companion note is precisely the displayed leading term.

The phase difference of actual zeros from their on-line projections costs at most $2n\sum_{\gamma>T}\gamma^{-3}<0.01n$, since below $T$ the census applies and above it $|\phi-\phi_0|\le\gamma^{-3}$ by the cubic arctangent bound. The remaining possible loss is radial:
$$
 D(n)=2\sum_{\gamma>T}\left[\cosh\big(n|\beta-1/2|/\gamma^2\big)-1\right].
$$
This follows by averaging each quartet, bounding the true absolute logarithmic radius by $|\beta-1/2|/\gamma^2$ and using $|\cos(n\phi)|\le1$. For $n\le M$, $D(n)/n\le D(M)/M$ by the power series. It suffices to prove $D(M)<28.2M$.

**2. Density bounds with both endpoints specified.** On $T<\gamma\le2T$ reflect the left zeros to the right, giving the factor four for a right-hand zero. Set $s_i=i/1000$, $500\le i\le994$, $h_j=T(1+j/200)$ for $0\le j\le200$. The rightmost possible real part is at most $b=1-1/[5.57\log(2T)]\in(0.993,0.994)$ by the classical zero-free region. For every $500\le i\le993$ let $B_{ij}$ bound the number of zeros with $T<\gamma\le h_{j+1}$, $\beta>s_i$. The checker takes the least of the following admissible bounds, including all density rows at thresholds at most $s_i$.

- Half the difference of the main counting terms at $h_{j+1}$ and $T$, plus $5(\log h_{j+1}+\log T)$. Reflection pairs each positive-ordinate zero on the right with a different zero on the left. Line zeros are harmless.
- At the thresholds of KLN Table 1 use $A(\log H)^{5-2\sigma} H^{8(1-\sigma)/3}+6\log^2H$, $H=h_{j+1}$. The checker rounds the tabulated $A$ upwards and replaces $\log(kH)$ by $\log H$ since $k\le1$. It uses their displayed equation (4.71) and table, under Lemma 4.14. One input to that paper, the coefficient 0.63 in its Lemma 3.2 for $t\ge3$, was originally supported by an erroneous Kusmin–Landau bound. Hiary–Patel–Yang Theorem 1.1 subsequently proves the stronger 0.618 over the same domain. The small-$t$ part is separate in KLN Lemma 3.2. [Kadiri–Lumley–Ng](https://arxiv.org/pdf/2101.12263) · [Hiary–Patel–Yang](https://arxiv.org/pdf/2207.02366)
- At each thousandth from 0.980 to 0.993, Johnston–Yang Table 3 gives the same shape with $A\le17.5$ and second coefficient $\le2.3$. Their Lemma 2.7 also gives the slightly stronger constant 5.5666305 in the zero-free region. The published height density bound written with a strict upper height also holds at the closed height by taking a limit from above. [Johnston–Yang](https://arxiv.org/pdf/2204.01980)

**3. Count each zero once.** Define nonnegative weights for $j<200$ by
$$
 w_{ij}=\cosh\big(M(\min(b,s_{i+1})-1/2)/h_j^2\big)
         -\cosh\big(M(s_i-1/2)/h_j^2\big),
 \quad w_{i,200}=0 .
$$
They decrease with $j$ by the power series. For a zero in $(h_j,h_{j+1}]$ its radial weight is bounded by summing $w_{ij}$ over the lower real-part endpoints $s_i<\beta$. The sum telescopes to the upper rounded real part; equality at a grid endpoint is handled by the preceding cell. Abel summation in the height index therefore bounds the near contribution by $4\sum_{i,j}(w_{ij}-w_{i,j+1})B_{ij}$. In particular cumulative density bounds are not applied as independent counts in disjoint height bins. For $\gamma>2T$ the fourth-power tail estimate in the companion proof gives the upper bound
$$
 2(2T)^4 \frac{2(\log(2T/(2\pi))+1/3)}{3\pi(2T)^3}\,
       [\cosh(M/(8T^2))-1].
$$
It applies without any density information beyond $2T$.

Using python-flint 0.9.0 at 112 bits, the upper-bound expression divided by $M$ is enclosed in $28.137833385679677726077463501\pm4.30\cdot10^{-28}$. The script constructs all 98,800 real-part/height cells from integers and checks strict positivity of every Abel weight difference. Combining the radial, phase and positive reference bounds proves the stated finite corollary. The zero-density inputs and the verified census are imported theorems. This run recomputes the finite combination from their published bounds. [Interval checker](check_li_horizon_nov18.py)

## Extension using the 2025 density estimates

The same argument with \(M=107T^2\) proves strict positivity through index
\[
 963\,112\,566\,946\,950\,210\,874\,880\,000.
\]
For each height cell with upper endpoint \(H\), use the smaller of the symmetric counting estimate from §2 and the following upper bounds on its cumulative right-half count. With coefficients from Chourasiya–Simonič Corollary 1, Table 1, use
\[
 A H^{3(1-s)/(2-s)}(\log H)^{(7-5s)/(2-s)}+ B(\log H)^2+C\log H .
\]
At \(s\ge0.625\) also use their equation (119), Table 4,
\[
 A'H^{8(1-s)/3}(\log H)^{2(3-2s)}+B'(\log H)^2 .
\]
Their counts include the threshold real part and the upper height, so bound the strict real-part subsets used in the radial sum. At \(s=1/2\) the separate symmetric bound only counts the strict right half. All heights exceed \(3\cdot10^{12}\). The same 98,800 Abel cells and the same fourth-power tail give \(D(M)/M<23.601\); the 128-bit enclosure is \(23.60081928129162436871084543584925\pm4.33\cdot10^{-33}\). Since the phase and reference estimates of §1 remain valid in the larger range, the new loss is strictly below the positive reference margin. The script shares the exact decimal coefficient tables with the Robin density checker. [Chourasiya–Simonič](https://arxiv.org/abs/2507.15184) · [Extended interval checker](check_li_density_horizon_nov18.py)
