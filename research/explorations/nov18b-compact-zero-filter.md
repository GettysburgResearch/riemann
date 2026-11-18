# Compact positive filters for the sparse zeros to the right of the critical line

Let $\rho_0=\beta_0+i\gamma_0$ be a nontrivial zero of zeta with $\beta_0>1/2$. Both $\psi(x)-x$ and $F(\log x)=\sum_{n\ge1}(\Lambda(n)-1)e^{-n/x}$ have the following property. For some $C>1$ depending on the zero and all sufficiently large $X$,
\[
 \int_X^{CX} E_\pm(x)\,dx\gg_{\rho_0}X^{1+\beta_0},
 \qquad E_\pm(x)=\max(\pm E(x),0).
 \tag{1}
\]
The two signs hold on the same interval even if no zero attains the supremum $\Theta$ of real parts. If $\Theta$ is unattained, **every prescribed $C>1$ works** for each fixed $\rho_0$, with constants that also depend on $C$. The same short-interval statement then holds for $\vartheta(x)-x$ by subtracting the contribution of prime powers. The estimates here are qualitative. For comparison, Montgomery and Vorhauer give explicit interval factors for $\psi(x)-x$ on RH. [Montgomery–Vorhauer](https://doi.org/10.7169/facm/1229442626) · [Montgomery–Vaughan, Ch. 15](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/19.0_pp_463_485_Oscillations_of_error_terms.pdf)

## Sparse ordinates and short compact filters

Fix $1/2<\alpha<\beta_0$. The Ingham zero-density estimate gives, for every fixed $\alpha$,
\[
 \sum_{\Re\rho\ge\alpha}\frac{1}{1+|\Im\rho|}<\infty ,
 \tag{2}
\]
by dyadic summation of $N(\alpha,T)\ll T^{3(1-\alpha)/(2-\alpha)}\log^5(2T)$. Multiplicity causes no difficulty. Zeta has no real zero in this region. For a finite measure $\mu$ on a compact real interval write $L_\mu(s)=\int e^{st}\,d\mu(t)$.

For $\rho=\beta+i\gamma$ with $\gamma\ne0$ take the positive probability measure with atoms of relative weights $1,e^{-\beta h}$ at $0,h$, where $h=\pi/|\gamma|$. Its bilateral Laplace transform vanishes at $\rho$. The convolution of these measures over the distinct zeros with $\Re\rho\ge\alpha$ is a probability measure $\mu$ on $[0,L]$ with $L=\sum h<\infty$. One can construct it as the law of a sum of independent bounded variables, whose series converges absolutely for every outcome. Finite-product transforms converge at every fixed $s$ by dominated convergence. Thus $L_\mu(\rho)=0$ throughout that zero set.

We also need a finite complex measure $\nu$ isolating $\rho_0$. Its supporting interval can be made **arbitrarily short**, while its total variation can depend on the entire chosen construction. For all zeros in (2) of sufficiently large ordinate use the preceding two-atom measures with $h=\pi/|\gamma-\gamma_0|$, and multiply their convolution by $e^{-i\gamma_0 t}$. This kills the large zeros and has strictly positive transform at $\rho_0$. The total support length of this tail tends to zero as the cutoff increases. For each remaining distinct $\rho\ne\rho_0$ with $\Re\rho\ge\alpha$, convolve with $\delta_h-e^{\rho h}\delta_0$ for a sufficiently small positive $h$ such that $e^{\rho_0 h}\ne e^{\rho h}$. There are only finitely many such choices to make, even if two distinct zeros have the same ordinate. The resulting $\nu$ satisfies $L_\nu(\rho_0)\ne0$ and kills every other zero in (2).

To use a single positive majorant for the two signs, let $g$ be a nonnegative smooth probability density supported on an arbitrarily small interval $[0,\eta]$. Write $\sigma^{[\gamma_0]}(dt)=e^{-i\gamma_0t}\sigma(dt)$, and define measures
\[
 D=\mu*|\nu|*g,\qquad V=\mu^{[\gamma_0]}*\nu*g^{[\gamma_0]}.
\]
Then $|V|\le D$. Both have smooth densities on the same compact support. The transform of $D$ kills every zero in (2); the transform of $V$ kills every such zero other than $\rho_0$, and
$L_V(\rho_0)=L_\mu(\beta_0)L_\nu(\rho_0)L_g(\beta_0)\ne0$. These two filters are fixed independently of $X$.

## Application of the explicit formula

Write $v=\log X$. For $F(v)$ the exponentially smoothed explicit formula has coefficient $-\Gamma(\rho)$ per zero, which is absolutely summable. For $\psi(e^v)-e^v$ the coefficient is $-1/\rho$ in the distributional explicit formula. Integration against either fixed smooth density now gives absolute convergence after any fixed number of integrations by parts, uniformly in the real parts $0<\Re\rho<1$. The remaining constant and trivial-zero terms are $O(1)$ for $v\ge1$. Equivalently, for the sharp prime sum one may first test the truncated explicit formula against the smooth density on a compact interval and then let its height tend to infinity. [Classical explicit formula](https://dlmf.nist.gov/25.16) · [Exponential sum and contour details](nov18b-variance-goldbach.md)

For either prime statistic this gives
\[
 \int E(Xe^t)\,dD(t)=O(e^{\alpha v}),\qquad
 \int E(Xe^t)\,dV(t)=c_{\rho_0}e^{\rho_0 v}+O(e^{\alpha v}),
\]
where $c_{\rho_0}\ne0$ includes the multiplicity. Hence $\int |E(Xe^t)|\,dD(t)\gg X^{\beta_0}$, while its signed integral is smaller. Its positive and negative integrals each exceed a fixed positive multiple of $X^{\beta_0}$. Boundedness of the density of $D$ and the change of variable $x=Xe^t$ prove (1).

If the supremum is unattained, the sum of $\pi/|\gamma|$ for $\Re\rho\ge\alpha$ tends to zero as $\alpha\uparrow\Theta$, by (2) at any fixed lower abscissa greater than $1/2$. Given $\log C>0$, choose such an $\alpha>\beta_0$ with this sum less than $(\log C)/2$, then select a zero with real part strictly greater than $\alpha$. Apply the construction to that zero with the remaining support widths smaller than $(\log C)/2$. This gives an exponent strictly larger than the originally requested $\beta_0$.

## Consequence for the sharp Goldbach convolution

For $B(x)=\sum_{m+n\le x}(\Lambda(m)-1)(\Lambda(n)-1)$, write $P_\pm(Y)=\int_0^\infty B_\pm(x)e^{-x/Y}\,dx$. The exact identity $P_+(Y)-P_-(Y)=Y F(\log Y)^2$ and monotonicity of each $P_\pm$ give an immediate use of the compact filters. From (1) and continuity of $F$, for every sufficiently large $X$ there are $X\le Y_1<Y_2\le C^2X$ with $|F(\log Y_1)|\gg X^{\beta_0}$ and $F(\log Y_2)=0$. Indeed the first interval supplies a large value, and the next supplies both signs. Then
\[
 P_-(C^2 X)\ \ge\ P_-(Y_2)=P_+(Y_2)
 \ \ge\ P_+(Y_1)\ \ge\ Y_1 F(\log Y_1)^2\gg X^{1+2\beta_0}.
\]
The positive part obeys the same bound by monotonicity. To truncate at $x=Z$, take $C^2X=Z/(10\log Z)$ and use $|B(x)|\ll (1+x)^2$ from Chebyshev to make the exterior tail $o(1)$. Thus for each such zero, at every sufficiently large $Z$,
\[
 \sum_{n\le Z} B_\pm(n)\gg_{\rho_0}(Z/\log Z)^{1+2\beta_0}.
\]
For a zero strictly below the supremum one can use a zero farther right and absorb this logarithm. For an attained supremum the [fixed-factor argument](nov18b-variance-goldbach.md) already gives the power without logarithmic loss, also on RH. The [independent theta-kernel proof](nov18b-goldbach-review.md) handles a zero on the critical line directly.

## The ordinary Mertens function, including multiple zeros

The same local result holds for $M(x)=\sum_{n\le x}\mu(n)$. If $\rho_0$ has multiplicity $m$, the lower bound for each integral in (1) is
\[
                   \gg_{\rho_0} X^{1+\beta_0}(\log X)^{m-1}.
 \tag{3}
\]
No bound on reciprocal derivatives at other zeros is required. The compact support can again lie in every prescribed logarithmic interval of positive length when the supremum is unattained.

In the construction repeat each annihilating factor according to the multiplicity of its zero. Estimate (2) counts multiplicities, so the support-length arguments continue to hold. Use as the last smooth density $g$ the law of a sum of independent uniforms on $[0,h_j]$, $h_j=c/j^2$, with $c$ as small as necessary. Its transform is the product of $(e^{s h_j}-1)/(s h_j)$. On any bounded real strip, at least a constant times $\sqrt{|\Im s|}$ of these factors have modulus at most $e^{A h_j}/2$, since $|\Im s|h_j\ge4$ there and $A$ bounds $|\Re s|$. The other factors have modulus at most $e^{A h_j}$. Its transform thus decays like $O(e^{-c'\sqrt{|\Im s|}})$ and Fourier inversion gives a smooth bounded density. The same decay holds for $D,V$, since the other factors are finite measures on compact intervals and modulation shifts the ordinate by a fixed amount.

Choose a real $\sigma_1$ strictly between $\alpha$ and $\beta_0$ with
$|\sigma_1-\Re\rho|\ge c_1/(1+|\Im\rho|)^2$ for every zero. Removing intervals of twice these radii costs arbitrarily little total length as $c_1\downarrow0$, by the classical zero count. On this line
\[
            |1/\zeta(\sigma_1+it)|\ll \exp(C\log^2(2+|t|)).
\]
Indeed in the bounded strip the local partial-fraction formula for $\zeta'/\zeta$, integrated in the real coordinate from $2+it$, gives the sum over $|t-\gamma|\le1$ of $\log|(\sigma_1+it-\rho)/(2+it-\rho)|$ with an $O(\log(2+|t|))$ error for $\log|\zeta(\sigma_1+it)/\zeta(2+it)|$ at large height. There are $O(\log(2+|t|))$ terms, each bounded below by $-O(\log(2+|t|))$. Values sharing an ordinate follow by continuity away from the zeros. Horizontal closures at a sequence $T\to\infty$ avoiding every zero ordinate by $\gg (1+T)^{-2}$ give the same estimate throughout the contour width.

For $W=D$ or $V$, smoothed Perron inversion gives
\[
 \int M(Xe^t)\,dW(t)
 =\frac{1}{2\pi i}\int_{(2)}
          \frac{X^s L_W(s)}{s\zeta(s)}\,ds .
\]
It follows by integrating the Perron kernel against the smooth compact density. Its horizontal integrals tend to zero by the square-root exponential decay, which dominates the reciprocal bound above. The integral on the displaced line is $O(X^{\sigma_1})$. Between these lines all reciprocal poles are removed for $D$. For $V$ only $\rho_0$ remains. Its residue is $X^{\rho_0}$ times a polynomial in $\log X$ of degree $m-1$ with nonzero leading coefficient, since $L_V(\rho_0)\ne0$, $\rho_0\ne0$ and $\zeta^{(m)}(\rho_0)\ne0$. The two-sign argument using $|V|\le D$ proves (3). To shrink the interval in the unattained case use a zero farther to the right as above, absorbing the original logarithmic power in the strictly larger exponent.

In particular, a single displaced zero would force substantial *both-signed local average mass* in the actual partial sums of the Möbius function on every sufficiently late interval of a suitable fixed multiplicative width. The argument does not impose simplicity and does not expand $M(x)$ into an assumed absolutely convergent sum of reciprocal residues. No instance of the required square-root bound for the actual Möbius sums is proved here.
