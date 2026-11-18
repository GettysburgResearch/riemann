# Inserting a moving calibration prime into the cubic-theta probe

The auxiliary character in the Eisenstein-field zero-free probe can serve as a prime average on its transformed rows. A specific choice keeps the character in the completed cubic row fixed and forces an exceptional Fourier frequency in the additive Gram estimate to have valuation four modulo six. This gives complementary estimates on both sides of the same finite expression. The source also yields a uniform bound for the punctured completed row. Its long-dual term and the additive Gram loss determine what this calibration can save in the positive comparison.

Use $F=\mathbb Q(\sqrt{-3})$ and the primary generators, fixed set $S$, ray group $T$, primitive calibration $\xi$, and $b_*$ of §§4 and 6 of the source. We write $q_a=N(a)$, including for prime ideals. Take a good prime $\mathfrak l$ of norm $D$ in the identity class of $T$. Enlarge $S$ by this one prime, use $b_*'=b_*l$, and use
\[
 \xi'(m)=\xi(m)\overline{\chi_l(m)}.
\]
The Chinese remainder interpretation uses the old and new factors on their respective moduli. This character is primitive and has order dividing six. All primal and transformed sums keep the zero extensions at the enlarged set. Choose the prime outside all the physical mark windows when marks are present. The proofs below use the original fixed $T$ throughout. [Source, equations (6.1)–(6.2), (7.5), (13.7), (15.4)](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)

## Exact characters on both sides

On the units at $l$, reciprocity gives $\chi_A(l)=\chi_l(A)$ because $l$ maps to the identity in $T$. Thus $\Xi'(A)=\Xi(A)$, and the extra condition on the completed row is $(A,l)=1$. Its character and the finite set of cusps originating in the base calibration stay fixed before treatment of this puncture. The additive column coefficient on $s$ changes by $\chi_l(s)^2$ and a scalar of absolute value one, with columns divisible by $l$ deleted. Equivalently, on the surviving columns its Gauss sum at $-m$ with this extra twist is the old Gauss sum at $-ml^4$. This identity follows by rescaling the variable of summation by the unit $l^4$ modulo $s$.

On the transformed side equation (7.5) has the conjugate of $\xi'(u)$. Thus at $l\nmid u$ the original row is multiplied by
\[
                         \chi_l(u) P_l(s,w,z;u)^{-1},
 \tag{1}
\]
where $P_l$ is the **full** original unmarked scalar Euler factor in (7.11)–(7.13). The row is zero when $l\mid u$. This follows first in absolute convergence by the exact local factorization and then on contours where the deleted factors are invertible. It applies to the compensated probe as well when the $l$-window is disjoint from the marks. At the principal row the leading multiplier is one. In particular the auxiliary character has left the original sixth-power pole present.

## A uniform additive Gram bound

Let $Q=q_{b_*}D X'Y'$, $P=Y'^2/Q\ge1$, with all lengths in polynomial ranges in $Z$, and $X',Y'\ge1$. Write $A_m^{(l)}$ for the additive polynomial (6.2) with the above data at a fixed old ray class and height $\nu$. For every $\epsilon>0$,
\[
 \sum_{q_m\ll Q}|A_m^{(l)}|^2
 \ll_{\epsilon,\mathrm{fixed}}(1+|\nu|)^J \frac Q{Y'} Z^\epsilon
 \left\{1+\left(\frac{P}{D^4}\right)^{1/6}
                    +\frac{D P^2}{Y'}\right\}.
 \tag{2}
\]
Here $J$ is a fixed derivative order. In particular the estimate is uniform as $l$ varies. With fixed old data, the parity of the quadratic reciprocity phase and its finite ray expansion cost only fixed constants.

To prove (2), apply the exact common-factor correlation (13.7) and the full coprimality inversion of §15.2. Write the two original columns $Cd m_1,Cd m_2$. Terms with $l\mid Cd$ vanish. In the residual columns retain the zero-extended factors $\chi_l(m_1)^2\overline{\chi_l(m_2)^2}$. At the new prime the first column of the periodic coefficient for a nonzero Fourier frequency $k$ is a fixed unit times the character of exponent $2+v_l(k)$, with its original unit mask. Consequently the complete two-column mean vanishes unless
\[
                  v_l(k)\equiv4\pmod6 .
 \tag{3}
\]
The old vanishing at every good prime outside $C,l,S$ whose valuation in $k$ is nonzero modulo six still holds. The periods used to prove vanishing are taken on the original lattice after exact inversion, so a divisor introduced by that inversion cannot change (3).

The zero frequency gives $O(Q/Y')$ by the source diagonal calculation. In a shell $q_C\asymp C_0$ with $q_k\ll K=RP/C_0$, the exceptional nonzero frequencies have ideal of the form $(l)^4 a^6 e$, with $e$ supported on primes of $C$ and the original fixed support and sixth-power-free. Their number is $\ll_\epsilon C_0^\epsilon(K/D^4)^{1/6}$ if the range is nonempty; otherwise it is zero. The old trivial residual bound and its convergent dyadic sums therefore give the middle term in (2).

For all other frequencies the norm of the period in the double column is $O_{\rm fixed}(D C_0 q_k)$, and the complete mean is zero. The homogeneous smooth bounds in §15.2 are unchanged because the new weight is purely arithmetic. Its lattice Poisson estimate on the $d$-dyad $d_0$ gives the old shell majorant
\[
 (1+|\nu|)^J R^{-A_1}\frac{Q}{Y'}\,
 \frac{RP}{C_0d_0}
 \min\left(1,\left(\frac{D RP C_0d_0}{Y'}\right)^{A_2}\right).
\]
Summing over positive dyadic $C_0,d_0$ costs $O(Z^\epsilon D RP/Y')$ in the factor after $RP$. The rapidly decaying $R$ sum gives the last term in (2). This accounts also for the additional prime in the period when $l$ does not divide $k$.

### Mixed calibrations at one auxiliary prime

The same argument applies to $\xi'_j=\xi\chi_l^j$ for $1\le j\le5$. These are exactly the nonprincipal local characters of order dividing six at $l$. The completed character acquires the factor $\chi_l^{j+1}$ in $\Xi$, and the additive column acquires $\chi_l^{1-j}$ up to a constant of modulus one and the zero mask. For a pair of indices $i,j$, the kernel after opening $A_m^{(l,i)}\overline{A_m^{(l,j)}}$ has an additional unit-sum condition in **each** residual variable. At $l$, its two character exponents, up to conjugation in the second column, are
\[
              1-i+v_l(k),\qquad 1-j+v_l(k).
\]
If $i\ne j$, the complete mean therefore vanishes at every nonzero frequency, even when all other valuations are multiples of six. For a fixed smooth nonnegative radial row cutoff $V(q_m/Q)$, supported in a fixed ball, the same Poisson calculation, with its zero-frequency diagonal bounded absolutely, gives
\[
 \left|\sum_m V(q_m/Q) A_m^{(l,i)}
                        \overline{A_m^{(l,j)}}\right|
 \ll (1+|\nu|)^J \frac Q{Y'} Z^\epsilon
                 \left(1+\frac{DP^2}{Y'}\right)\qquad(i\ne j).
\]
The smooth cutoff is kept in this signed estimate. For equal indices the middle term of (2) becomes $(P/D^{j-1})^{1/6}$, by counting $k$ with $v_l(k)\equiv j-1\bmod 6$. Consequently $j=5$ both leaves the completed character fixed and gives the largest forced valuation among these five prime calibrations. Mixed pairs have no exceptional nonzero term in this complete-mean analysis. These are upper bounds; a matching diagonal asymptotic would be required to deduce an intrinsic lower bound for the arithmetic Gram form.

The tempting remaining index \(j=0\) would force valuation five in the Gram count, but its local character is the principal unit mask, which is imprimitive modulo \(l\). Its transform on the physical side is the Ramanujan sum \(D1_{l\mid H}-1\), since \(s,A\) are units at \(l\); the fixed invertible factors in its additive argument do not affect this value. Relative to its value at a unit, the multiplier is \(1-D1_{l\mid H}\). In the putative principal row \(H=a^6\), the calibration now allows all valuations of \(a\) at \(l\). All other primal indices avoid \(l\), so the complete local sum over \(v_l(a)\) is
\[
 \sum_{m\ge0}D^{-6zm}(1-D1_{m\ge1})=
                \frac{1-D^{1-6z}}{1-D^{-6z}}.
\]
The numerator has a simple zero at \(z=1/6\); multiplication by the remaining Euler product cancels its sixth-power pole. Hence the zero-cost endpoint suggested by the Gram valuation does not retain the original principal Mellin signal. This calculation also explains directly why the primitivity condition in §6 is material for this strategy.

## A high-side saving uniform in the physical row

Let the calibration primes have norms in $[K,2K]$ and range over the identity class of $T$. Give them smooth nonnegative weights $W(q_l/K)\log q_l$, with a nonzero fixed $W$ supported inside $(1,2)$, and divide by their total weight. For a sixth-power-free $u$ divisible by a prime outside $S$, with $q_u\le Z^C$, one has
\[
                 \left|\operatorname{Avg}_{l}\chi_l(u)\right|
                 \ll_{\epsilon,C,S,T,W} K^{-1/8}Z^\epsilon .
 \tag{4}
\]
Suitable fixed tests have positive prime mass asymptotic to a fixed positive constant times $K$. To obtain (4) expand the old ray class in characters. In the running prime the sextic Kummer symbol attached to $u$ has nontrivial inertia at a prime outside $S$, because its valuation there is between one and five. Thus every ray twist in that expansion is nonprincipal. Its conductor has norm $\ll_{\rm fixed} q_u^{O(1)}$ by tame Kummer ramification away from six and finitely many local sixth-power classes at the primes above six. The ordinary smoothed explicit formula and the $7/8$ theorem bound the weighted prime sum by $O(K^{7/8}\log^2(2q_u K))$. Indeed the ordinate bands in the zero sum have population $O(\log(2q_u(|t|+2)))$ and the Mellin transform decays faster than any power; prime powers with exponent at least two cost $O(K^{1/2}\log^2 K)$. Removing finitely many additional primes or the primes dividing $u$ costs $O(\log(2q_u))$ when needed. This uses the Eisenstein-family assertion in the primary theorem.

In the nonprincipal central region of (20.4), $s_r=a+16e$, $w_r=1-a-6e$, $z_r=17/50$, with $51/100\le a\le7/8$ and $0<e<10^{-3}$. For $l\nmid u$, Euler identity (7.13) gives
\[
 P_l^{-1}=\frac{(1-D_l^{(z)})(1-W_l)}{(1-D_l^{(s)})H_l},
 \qquad
 |D_l^{(z)}|=q_l^{-6z_r},\quad
 |W_l|=q_l^{-w_r},\quad |D_l^{(s)}|=q_l^{-s_r}.
\]
The unramified estimate in the proof of (7.14) bounds $H_l-1$ by $O(q_l^{-1-c_e})$ with $c_e>0$. Hence $P_l^{-1}=1+O(q_l^{-w_r})$ uniformly in the heights and row, since $w_r<s_r$. Equations (1) and (4) show that the actual high row multiplier is $O(K^{-1/8+6e}Z^\epsilon)$ after averaging. The principal multiplier on the residue $(w,z)=(1,1/6)$ equals $1+O(K^{-\min(s_r,1)})$ in the principal region (7.15). The original signal survives. Bounded unit rows can be treated separately as in the source. These assertions concern an average of unnormalized finite probes with the same $X,Y,Z$ and prescribed varying calibration. The weights in the average are independent of $u$.

There is a stronger estimate inside each original buffered zero bin. Suppose $K=Z^\lambda$, $\lambda>0$ fixed, with the calibration annulus disjoint from the physical marks. Fix the shared detector and height allocations of §§8, 19 for the **old** family. For the actual central high row in bin $(i,a)$ one obtains
\[
 \left|\operatorname{Avg}_{l:\,l\nmid u}\chi_l(u)P_l^{-1}\right|
 \ll_{\epsilon,\lambda,e,\mathrm{fixed}} Z^\epsilon K^{a-1+O(e)}. \tag{5}
\]
Here the average includes zero for deleted $l\mid u$ and always has the original normalizer. To bound its first term, every ray twist of $\chi_\bullet(u)$ belongs to the old buffered family. The proof of the prime-bound lemma in §19.1 applies with norm twist zero and with the base weight $W$ itself in the von Mangoldt sum. Shifting its logarithmic derivative in the buffered rectangle and dividing by the mass $\asymp K$ gives $Z^\epsilon K^{a-1+O(e)}$. Prime powers cost $O(K^{-1/2+\epsilon})$. This uses the fixed polynomial annulus, so external Mellin tails can be discarded on the absolute line using the original $T_1$. The $P_l^{-1}-1$ term costs $O(K^{-w_r})=O(K^{a-1+6e})$ without cancellation. No new detector adapted to $l$ is involved.

## The punctured completed row and its long dual

Write $D=Z^\lambda$ for the individual prime norm and $m=\log_Z Q+O(1/\log Z)$ for the row length after inclusion of $D$. In this paragraph $\ell'$ is the surviving physical mark length, and the completed scale is $Z^{1+\ell'}$ as in §15.1. Denote the completed factor by $B_k^{(l)}$. In the region $m\ge4\ell'$ one has the following uniform squared norm bound from the original quadratic–cubic estimate:
\[
 \sum_{\substack{0<q_k\ll Z^m\\l\nmid k}} |B_k^{(l)}|^2
 \ll Z^{m+\max\{0,(1+3\ell'-2m)/4,\ m+\lambda+\ell'-1\}+\epsilon}.
 \tag{6}
\]
A bounded factor in $D/Z^\lambda$ is absorbed by the stated loss. In the physical probe $\xi'(k)$ already vanishes at $l\mid k$. The old finite character $\nu$ and old modulus remain fixed: the source's marked completion has $f=1$ and varying puncture $\rho(n)=1_{l\nmid n}$. Indeed $\rho(n)\rho(b)^3=1_{l\nmid nb^3}$ on its primal squarefree and cube indices. Section 14 treats exactly this input with puncture exponent $\lambda$ and uniform constants. The disjoint mark lists and the Gaussian annular decomposition of §15.1 are unchanged.

Here are the two branches of the estimate in the source notation. Tolerances and fixed dyadic offsets below cost at most $O(\epsilon)$ in the final exponent. Write $O,H$ for the powerful and residual row lengths, so $H+O\le m$. Write $z$ for the active marked length, $u_0=\min(v,z,(v+z)/3)$, $y=v+3\ell_b+e_\lambda$, and $T_d=2H+2A_0+2z-1-\ell'-N_0-3B_0$. The source gives $y\le T_d$ on retained dyads. The symbol $e_\lambda$ here is the dual ramified-prime valuation from §14, unrelated to $\log_ZD$; its negative part is $O(1/\log Z)$. The energy bound before summing the dyads is
\[
 E=\frac O2+\max(H,v+\ell_b)-S_0-B_0+z-u_0-\ell_b-2e_\lambda/3-(T_d-y)_+/2.
\]
If the maximum is $H$ and $u_0=z$, this is at most $m$. If the maximum is $H$ and $u_0<z$, then $u_0\ge v/2$. Consequently $u_0+\ell_b+2e_\lambda/3+(T_d-y)_+/2\ge T_d/4$ up to the stated tolerance. Substitution of $T_d$ and $H+O\le m$ gives
\[
 E-m\le (1+\ell'+2z-2m)/4-(2A_0-N_0+B_0+4S_0)/4.
\]
The subtracted numerator is nonnegative, and $z\le\ell'$.

If the maximum is $v+\ell_b$ and $u_0<z$, then $v<2z$, so that $v+z-u_0=\max(v,z,2(v+z)/3)\le2z$. It follows that $E\le O/2+2\ell'\le m$. In the remaining branch $u_0=z$ one instead gets $E\le O/2+T_d-S_0-B_0$. The actual conductor-width inequality at the end of §14, with puncture exponent $\lambda$ and label exponent zero, gives
\[
 T_d-S_0-B_0\le 2m-O+\lambda-(1+\ell')+2z .
\]
It accounts for an active zero-exponent prime $l$ with its $D^{-1/2}$ column and the extra conductor width. This gives the third exponent in (6). The Gaussian translate lengths differ from $1+\ell'$ by an arbitrarily small tolerance on the retained annuli, as in the source. The uniformity in its reflected-energy lemma handles the Gaussian tails and all polynomially bounded punctures. [Pinned primary source, reflected energy and conductor-width inequality in §14, and §15.1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)

## Effect on the two direct bounds

In the range $P\ge D^4$ and $DP^2/Y'\le(P/D^4)^{1/6}$, the square root in (2) costs $D^{1/12}$ relative to the fixed-calibration additive factor, including the increase in $Q$. In the Cauchy estimate the basic increase in the completed-row norm cancels against the prefactor $Q^{-1/2}$; its excess in (6) has to be paid separately. For zero rescaling, the old total length $M=l_x+l_y$ gives $m=M+\lambda$ and $\ell'=\ell$. Thus the long-dual excess in the **squared** norm in (6) is $(M+\ell+2\lambda-1)_+$. Near Liu's optimized geometry the other excess is strictly slack at zero rescaling.

There is an elementary test for the return on (5). Liu's Proposition 6.5 combines the necessary comparison planes $L_0,L_K,H$ with respective positive weights
\[
 u=\frac{25\delta+8}{6(4\delta+3)},\qquad
 v=\frac{4-\delta}{6(4\delta+3)},\qquad
 w=\frac1{4\delta+3},
\]
at $\delta=\delta_*=0.4258300\ldots$. Consider the explicit relaxed comparison which pays only $\lambda/12$ on both direct planes, allows the whole improvement $(1-a)\lambda=(1-\delta)\lambda/2$ on $H$, and grants free control of any additional completed-row excess. Its weighted lower bound exceeds the original by
\[
 \lambda\left(\frac{u+v}{12}-w\,\frac{1-\delta}{2}\right)
 =\lambda\,\frac{5\delta-2}{6(4\delta+3)}>0 .
\]
This calculation is about those three plane bounds. It shows why simply inserting (5) alongside the calibrated additive majorant is insufficient even under the favorable allowance on the long dual. A stronger joint estimate or a smaller actual cost on the additive side could change the calculation. A continuation theorem would also have to control contours away from the central bins and the $Z$-dependent principal remainder. [Liu, Proposition 6.5 and §7](https://hexagonmath.org/2611.00421v1)
