# Inserting a moving calibration prime into the cubic-theta probe

The auxiliary character in the Eisenstein-field zero-free probe can serve as a prime average on its transformed rows. A specific choice keeps the character in the completed cubic row fixed and forces an exceptional Fourier frequency in the additive Gram estimate to have valuation four modulo six. This gives complementary estimates on both sides of the same finite expression. The long reflected sum and its simultaneous use with the moving puncture require a further estimate for a new zero-free boundary.

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
The unramified estimate in the proof of (7.14) bounds $H_l-1$ by $O(q_l^{-1-c_e})$ with $c_e>0$. Hence $P_l^{-1}=1+O(q_l^{-w_r})$ uniformly in the heights and row, since $w_r<s_r$. Equations (1) and (4) show that the actual high row multiplier is $O(K^{-1/8+6e}Z^\epsilon)$ after averaging. The principal multiplier on the residue $(w,z)=(1,1/6)$ equals $1+O(K^{-\min(s_r,1)})$ in the principal region (7.15). The original signal survives. Bounded unit rows can be treated separately as in the source. These assertions concern an average of the identical, unnormalized finite probes with the same $X,Y,Z$; there is no row-dependent choice of calibration.

## The outstanding comparison

In the range $P\ge D^4$ and $DP^2/Y'\le(P/D^4)^{1/6}$, the square root of the right-hand side in (2) differs in its power from the fixed-calibration bound by just $D^{1/12}$, including the increase in $Q$. This is an additive-factor calculation. The completed cubic row now has a new puncture and a larger row ball, and the Cauchy prefactor also changes. Any comparison of complete exponents must include both effects. Moreover, the change to the principal multiplier is handled as a remainder in an attempted continuation argument, rather than identifying a $Z$-dependent factor with a fixed Mellin signal. Equations (1)–(4) establish the potential gain and the costs that have to be compared.
