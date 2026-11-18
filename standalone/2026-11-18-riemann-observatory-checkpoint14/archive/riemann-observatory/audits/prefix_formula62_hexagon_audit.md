# The zeta specialization of Liu's Hexagon 2611.00421v1

The paper claims $\zeta(s)\ne0$ for $\operatorname{Re}s>B_*=0.8733458561067185768\ldots$, with the pole at $1$ understood. The zeta specialization requires Theorems 8.12 and 8.14 over $F=\mathbb Q(\zeta_{12})$. It does not require the paper's Section 9 extension to infinite-order Hecke characters or Weil representations. This audit reproduces the scalar stage conditions and part of the analytic induction. It leaves certification of the analytic comparison open. [Primary PDF](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

## Dependency chain for zeta

1. Take $K=\mathbb Q$ and the trivial target with norm twist $t=0$. Over $F$, the finite-order theorem gives nonvanishing of $\zeta_F$. In $B_*<\operatorname{Re}s<1$, the full abelian factorization $\zeta_F(s)=\zeta(s)\prod_{\chi\ne1}L(s,\chi)$ has no factor with a pole. A zero of $\zeta$ there would imply a zero of $\zeta_F$. On $\operatorname{Re}s=1$ use classical nonvanishing away from the pole, and on $\operatorname{Re}s>1$ use the Euler product. An arithmetic argument for zeta alone still encounters the *family* of varying sextic characters over the cyclotomic field, so zeta-only information does not supply the input moments. [Theorem 8.14 and equation (62)](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)
2. The prior bound used here is $\beta_*(F)\le0.87488664704$, with $\beta_*$ the supremum over nontrivial zeros of **all finite-order** Hecke characters over the fixed field. Consequently $2\beta_*-1<\kappa_1=374887/500000$. This is the independent margin in the earlier Mellin prime bound (Lemma 12.7), inverse moments (Theorems 10.7 and 11.2), and the long inverse count (Lemma 10.10). The same predecessor supplies the simultaneous detector and common Sobolev treatment of its rowwise choices (Lemmas 13.7 and 13.9), the Mellin continuation in Sections 13–14, and general-field transport in Sections 17–19. The new paper assumes the prior bound from that predecessor. [arXiv:2610.26835v2](../sources/latest62_density_frontier/2610.26835.pdf)
3. The other predecessor supplies the ordinary coefficient-two moment (Theorem 4.9), arbitrary-length unmarked moments (§2.3), reflection with exact missing-prime restoration, and common-divisor identities, with the ordinary inducing-character group $\Theta$ excluded. Proposition 8.10 of the new work uses only its old face $P+(49/20)S\le99/100$, $S\le7/50$. The old coefficient-two bound covers this face with slack. Theorem 8.12 then advances the joint range. Theorem 8.14 invokes the finite rational approximants of Proposition 6.4 for any strict target $B>B_*$, the lower-limit Mellin argument in Proposition 8.13 with $a=509/1000$, and the predecessor continuation of the whole numerator. This order is needed to exclude contour contributions introduced by premature row restriction or absolute values. [Hexagon 2611.00082v1](../sources/latest62_density_frontier/hex_2611.00082v1.pdf) · [Hexagon 2611.00421v1](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

## One induction step

Let $(R,z_R)$ be an earlier joint rectangle and set $H=r/R$, $u=(1-H)/6$. The scale-normalized remaining marked width in the new rectangle is
$$
s=H\{(1-R)/2+z_R\}+u/k,\qquad S=s+u.
$$
In the inverse canonical block, choose whole original prime factors of total width $u'=u+O(\eta)$ with product $d$. Assuming the exact sextic reciprocity in Proposition 8.8, the selected frequency is $kd^4$. Divisor multiplicity of $kd^4$ is a subpower on the bounded exponent range. The factor $Z^{u'}$ from the tuple Cauchy estimate offsets the change in normalization when $N'=N-u'$. With $F_0=N+V$ and the cap $M=2F_0-1+O(\eta)$, the scale $K'=M+4u'$ gives
$$
H_0=2(N'+V)-K'=1-6u'+O(\eta),\qquad
(K'-N'-V)+(H_0+\kappa_P+u')=F_0+\kappa_P.
$$
Thus the target at the second Poisson stage is a moment of order $Z^{H_0+\kappa_P+u'}$. This reasoning uses the coefficient conversion and restoration of Propositions 8.6 and 8.8 and Lemma 8.7. Restored terms reusing a selected prime vanish because the transformed residue character on $kd^4$ has its natural zero at that prime. Dropping natural zeros before the restoration identity changes the polynomial.

For small amplitudes the excess width over the prior bound is $u/k$, removed at price $k$ per unit width; a fixed endpoint decrement gives a strict saving. For large amplitudes, write $\lambda(x)=a_0-a_1x$ and $D=1/2-a_1$. With $g=g(\nu)$ as in §8.6,
$$
D(g-r)=H\{z_R-\lambda(R)\}+u(1/k-1/\nu)\ge0.
$$
Hence the short count at $w=g/H+\omega$ lies to the right of $R$. It can use earlier moments provided the supporting line there certifies genuine earlier rectangles. This does not use the stage's own output. The key cancellation at an amplitude pair $(\nu,e)$ with $0\le e\le\nu$ is
$$
\begin{aligned}
C_s+\nu r+es
&\le H+\nu(r-g)+e(g-r+u/\nu)\\
&\quad+H\{-\nu\omega+e[(1/2+a_1)\omega+\pi]\}\\
&\le H+u-Hk\omega/20,
\end{aligned}
$$
where $a_1\le2/5$ and $0<\pi<\omega/20$. For the long branch the detector length is $t(w)=3w/2+\tau$. The prior general-row inverse estimate has exponent $\max\{1,(1+5r_{\rm det})/6\}$ at width $r_{\rm det}$. For $1\le r_{\rm det}\le t$ the inverse large-value threshold saves at least $\nu r_{\rm det}$, giving the exponent $1/6+(5/6-\nu)t$ on the scale $Z^H$. The same bound covers $r_{\rm det}$ just below 1 with the buffer loss. Condition 9 implies the derivative margin in Proposition 8.9 since $\nu\ge k$ and $32>3/2$. The long-branch margin can therefore be kept strictly positive by taking $\omega,\tau$ after condition 1.

For sixth-power cofactors, condition 13 is exactly the upper endpoint test ensuring $\nu w+e\sigma(w)<5/6$ across the permitted interval, since $w+\sigma(w)$ is nondecreasing under the stated slope bound. The short, long and small-core excesses have respective $M$-slopes bounded below by $-5/6$, and the same one-sided bound survives the optimization. Therefore if a sixth-power factor $\mathfrak B^6$ reduces the core width by $6\log_Z N\mathfrak B$, then the aggregate size exponent drops by at least $\log_Z N\mathfrak B$. The borderline exponent is handled by the stated extra $\delta$ loss and the convergent ideal series $\sum (N\mathfrak B)^{-1-6\delta}$. In particular no sixth powers can be dropped from the final moment count merely because the detector is formulated for primitive cores.

For the ordinary reference, the reflected widths satisfy the old face because
$$
\frac13+\frac7{25}+\frac{49}{20}\frac{137}{1000}
=0.94898333\ldots<\frac{99}{100}-\frac1{25}.
$$
Independently, the power $3(1/2-15/98)=51/49>1$ suffices for absolute convergence of the unmarked Euler products. The weighted marked exponent is $1-(k+m)/2+(15/98)(k-49m/20)$ in the notation of (51). At the least admissible degrees for ordinary-only, one mark, and collision terms, it equals respectively $-2/49,-87/392,-3/4$. These checks support the stated use of the earlier face, conditional on the exact application of the kernel identities to the original marked polynomial and its signed correction. [§§8.5–8.9](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

## Exact numerical check and remaining analytic obligation

I evaluated all fourteen margins, both branches of margin 13, at both endpoints of the 240 stages in equations (8)–(13), using rational arithmetic, cutoff padding $10^{-7}$, and $\rho_{\rm high}=10^{-7}$. All 7,200 signs were positive and the chain ended at $z_{240}=3850137/1250000000$. The smallest margin was approximately $4.1501572\cdot10^{-5}$, in condition 1. The 240 computed supporting lines were also strictly below all 480 stage endpoints of the profile $Y_j-\Delta z-p$, with minimum gap about $5.99010\cdot10^{-8}$. Since both the profile and each line are affine on a stage, this checks the global scalar line comparison in Proposition 5.1. The calculation leaves open the Bernstein covers of the final comparison, the limiting finite approximation, and the analytic moment estimates. [Script](../experiments/code/prefix_formula62_hexagon_stages.py) · [Retained results](../experiments/results/prefix_formula62_hexagon_stages.txt)

The ordinary part of the induction needs the exceptional inducing-character subtraction in the new reference geometry. In the older paper the centered exceptional excess is explicitly (4.71). With $X=L_1+L_{\rm pow}$ and $c=c_{\rm cor}$ it deducts
$$
9X/8+29c/6+(2/3)(\ell-X-5c)_+\ \ge\ (2/3)\ell.
$$
This shows how the claimed smaller gain $(3/5)\ell_{\rm ref}$ *could* arise if the same identity, centering at $\ell_{\rm ref}=7/50$, and its uniform remainder bounds are established after the enlarged range's complete-factor choices. Proposition 8.11 cites the earlier raw identities and asserts this gain as the explanation of (53), but does not display the transported exceptional excess or a decreasing induction rank for these enlarged ranges. Proposition 8.10 gives a reference moment on a starred family. That bound does not by itself bound the separate signed exceptional mean generated when arranging the centered difference. The old proof makes those operations explicit in (4.68)–(4.72), whereas the new range can extend beyond the centered interval available in that proof. To close this verification, one needs the transported signed identity and exponent bound on every branch before taking positive estimates, and the decreasing rank on subsequent recursive returns. The present audit found no algebraic circularity in the scale calculations and does not certify those two analytic steps. [Earlier proof, §4.7](../sources/latest62_density_frontier/hex_2611.00082v1.pdf) · [New proof, §§8.8–8.9](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

The exceptional hypothesis is necessary. For the unstarred version of the ordinary moment at the initial rectangle $R_0=311/400$, $z_0=0$, take $n_1=n_2=3/8$ and total marked width $S=1/10$, split across smooth positive prime windows of individual width less than the mesh and less than $1/6$. Take trivial fixed coefficient characters. Let the parameter run over sixth powers $\mathfrak B^6$, where $\mathfrak B$ is a prime ideal in a fixed trivial allowed ray class with norm comparable to $Z^{1/6}$. The fixed-field prime ideal theorem in ray classes gives $\gg Z^{1/6}/\log Z$ such rows. The sextic symbol is principal on its natural coprime support. The prime windows avoid $\mathfrak B$ by size, while omitting multiples of $\mathfrak B$ from the positive ordinary sums costs $O(Z^{3/8}/N\mathfrak B)$ in each unnormalized sum. Thus the squared normalized ordinary product with primes is $\gg Z^{3/4+1/10}/(\log Z)^C$ on these rows. The unstarred second moment is at least $Z^{61/60}/(\log Z)^{C+1}$ up to a fixed positive factor, contradicting an exponent $1+\varepsilon$ for $\varepsilon<1/60$. This example validates the need for the printed star and for the exact exceptional calculation through centering. It does not contradict the starred estimate.
