# Inactive sixth powers and the marked reflected energy

Status: proposed native refinement of the pinned QRH source's positive energy bound; no improved zero-free boundary is claimed.
Scope: the actual marked cubic reflection, all powerful-row branches and fixed punctures. The low-probe specialization below keeps all rescaled subsets and actual row dyads.
Source: OpenAI, *The Quasi-Riemann Hypothesis*, pinned commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, local `_source-original-quasi.tex`, SHA256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`; §14, `lem:reflected-energy`, formulas `old-eq:4.4`–`old-eq:4.7`, and §15, `lem:probe-row-norm`. The reflection and the hybrid quadratic–cubic large sieve are imported exactly as in that source.
What was run: algebraic derivation and inspection of all local branch rules. No numerical data prove the result. An independent source and inequality review is required.
Smallest remaining gap toward a boundary: neither this positive energy improvement nor an ideal inverse row count removes the high-side floor-bin obstruction of the original physical probe.

## 1. Count the actual active and inactive powerful primes

Fix the source's squarefree label f and puncture rho, with polynomial norm, and its fixed bad-prime set S. Let k_pow be the maximal powerful part of an element row, with Nk_pow approximately Z^O. In each literal reflected branch let A0 be the logarithmic norm of the active non-slot radical outside the residual valuation-one row product, exactly as in the source. Then the number of powerful parts in a dyadic O,A0 branch, including their finitely many local choices, is

\[
 \ll Z^{C(O,A_0)+\epsilon},\qquad
 C(O,A_0)=\min\{O/2,\ O/6+2A_0/3\}.                 \tag{1}
\]

**Proof.** The O/2 bound is the usual powerful-ideal count. For the second bound, put every prime supported on the fixed ideal f rad(rho) or S into a supported factor. For a fixed positive epsilon, polynomially bounded ideals supported on this fixed-in-the-row-sum prime set number at most Z^epsilon, uniformly with the source's allowed polynomial norm bound. This follows from the same Rankin/Euler-product argument used by the source for supported ideals; their norm need not be bounded independently of Z.

Outside that support the local exponent is precisely v_p(k) modulo six. Every nonzero exponent is forced active. Consequently an inactive powerful prime has exponent divisible by six. Write the product of the inactive primes and their powers as t^6. Let a be the product of the remaining active powerful primes and let R=rad(a). Then (a,t)=1, R^2 divides a, and NR is at most a fixed factor times Z^{A0}. On a norm dyad NR approximately Z^r there are O(Z^{r+epsilon}) choices of R. For each R the allowed powers forming a cost Z^epsilon, by the same supported-prime counting. As Na is at least (NR)^2, the remaining sixth-power variable satisfies Nt at most a fixed factor times Z^{(O-2r)/6}. Counting t, and then the logarithmically many r dyads, gives

\[
 Z^{\epsilon}\max_{0\le r\le\min(A_0,O/2)}
 Z^{r+(O-2r)/6}
 \le Z^{O/6+2A_0/3+\epsilon}.
\]

The fixed support contributes only the previously reserved small power. Its actual norm only shortens the available t range. Active primes belonging to f or rho but not to k_pow may be counted in A0; this only enlarges the upper bound. Unit choices and the source's divisor-bounded local branch choices cost another small power. This proves (1).

This count is made with f and rho fixed, as required by the source. It does not erase an outer sum over those labels or prove a smaller conductor. It also does not alter the common profile or any zero-extended local factor.

## 2. Refined version of the source energy lemma

Use all the source's reflected block data. In particular

\[
 T_d=2H+2A_0+2z_a-N_*-N_0-3B_0,
 \qquad
 u=\min\{v,z_a,(v+z_a)/3\},
\]

and retained dyads satisfy
\(v+3\ell_b+e_\lambda\le T_d+\tau_{\rm ref}\).
For each fixed powerful part the source proves an energy with exponent

\[
 \max(H,v+\ell_b)-S_0-B_0+z_a-u-\ell_b-2e_\lambda/3
       -\tfrac12(T_d-v-3\ell_b-e_\lambda)_+ .       \tag{2}
\]

The source then adds O/2 solely to count the powerful parts. Replacing that count by (1) gives the same conclusion with aggregate exponent

\[
\boxed{\begin{aligned}
 E_{\rm new}={}&C(O,A_0)+\max(H,v+\ell_b)-S_0-B_0+z_a-u-\ell_b
                 -2e_\lambda/3\\
 &-\tfrac12(T_d-v-3\ell_b-e_\lambda)_+.
\end{aligned}}                                                   \tag{3}
\]

No analytic step of the fixed-part proof changes: retain the finite reflection vector, all natural zeros, common smooth density, small-kernel extraction before squaring, actual residual-row dyads, permitted bad-prime support, and the original polynomial height cost. The full source proof already provides uniformity in the frozen powerful part. The count is therefore applied after that bound, without interchanging a label-dependent profile with the row sum.

## 3. Exact optimization of the cube variable

For nonnegative T,z,v,b,e with v+3b+e at most T,

\[
 \min\{v,z,(v+z)/3\}+b+2e/3
          +\tfrac12(T-v-3b-e)
 \ge \min\{z,T/3\}.                               \tag{4}
\]

To prove this, put u=min{v,z,(v+z)/3}. Since b at most (T-v-e)/3, the left side equals

\[
 u+T/2-v/2-b/2+e/6
 \ge u+(T-v)/3+e/3.
\]

Each of v+(T-v)/3 and (v+z)/3+(T-v)/3 is at least T/3. The third possibility z+(T-v)/3 is at least z. Taking their minimum proves (4). The same assertion with an O(tau+epsilon_Z) loss holds for the source's retained ranges and bounded subunit dyads: changing a variable or T by that amount changes every linear or positive-part expression by O(tau+epsilon_Z). No strict positivity of a unit-dyad exponent is needed.

The exact optimum is min(z,T/3): the T/3 branch is attained at v=e=0,b=T/3, and the z branch is attained at v=T,b=e=0 whenever T at least 3z. The pure cube face, rather than a generic v/2 relaxation, determines the first branch.

## 4. The general balanced physical low-probe range

Assume the source's finite compensated probe has total slot length ell, balanced total physical row length M=1-ell, and a rescaled subset of total length d in [0,ell]. Set

\[
 M'=1-\ell-2d,\quad \ell'=\ell-d,\quad
 N_*=1+\ell'+\theta_N,
\]

with the same Gaussian annular parameter theta_N as in the source. Require the actual physical and row scales to remain polynomially large; for example ell<1/3 ensures M'>0 even at d=ell. The low specialization has f=1 and rho=1, so

\[
 H\le M'-O+O(\epsilon_Z),\quad
 2A_0\le O+O(\epsilon_Z),\quad
 N_0\le A_0,\quad z_a\le\ell'.                      \tag{5}
\]

Write Delta=M'-O-H, allowing the source's O(epsilon_Z) negative offset. Directly,

\[
 T_d-H\le M'+\ell'-1+O(\epsilon_Z+|\theta_N|)
              =-3d+O(\epsilon_Z+|\theta_N|).
\]

Thus max(H,v+ell_b)=H up to the reserved tail and annular losses. By (4), (3) gives

\[
 E_{\rm new}-M'
 \le C(O,A_0)-O-\Delta-S_0-B_0
            +(z_a-T_d/3)_+ + O(\epsilon_Z+\tau_{\rm ref}+|\theta_N|).
                                                               \tag{6}
\]

The zero branch of the positive part is nonpositive, since C at most O/2. On its other branch use C at most O/6+2A0/3, H=M'-O-Delta and the exact T_d formula. The terms containing B0 and A0 cancel, and the result is

\[
 \frac{z_a+1+\ell'-2M'}3
       -\frac O6+\frac{N_0}3-\frac\Delta3-S_0
       + O(\epsilon_Z+\tau_{\rm ref}+|\theta_N|).
\]

The O,N0 combination is nonpositive by 2N0 at most 2A0 at most O. Therefore

\[
\boxed{\displaystyle
 E_{\rm new}\le M'+\left(\frac{4\ell+2d-1}{3}\right)_+
                         +O(\epsilon_Z+\tau_{\rm ref}+|\theta_N|).}
                                                               \tag{7}
\]

Choose the source's Gaussian annular and truncation tolerances within a prescribed epsilon, use the unchanged seminorm integrability, and sum all actual row dyads. This proves the source-dependent proposed improvement

\[
 \sum_{0<Nm\ll Q}|B^J_{m,\sigma}(Z)|^2
       \ll Z^{M'+((4\ell+2d-1)/3)_++\epsilon}.       \tag{8}
\]

The source's fixed ell=1/6 specialization retains its old exponent; this is a genuine improvement in the larger-slot range needed for a more ambitious probe.

## 5. Sum every rescaled subset

In the source's additive-Gram regime, assume the actual x,y geometry satisfies the same sufficient scale conditions, in particular P_a=Y'^2/Q at least one and Y' at least a fixed multiple of P_a^{11/6}. For the rescaled subset d, the original tuple count and compensation coefficients contribute -d to the low exponent after additive Cauchy, exactly as in source `old-eq:5.5`. Thus the additional cost from (8) is

\[
 -d+\frac16(4\ell+2d-1)_+
 \le\frac16(4\ell-1)_+,\qquad 0\le d\le\ell.        \tag{9}
\]

The function on the left has slope -1 before its kink and -2/3 after it, so its maximum is at d=0. Hence every subset is included and the strengthened low estimate is

\[
 \boxed{|I_{\eta,\mathrm{modified}}(Z)|
       \ll Z^{l_x/2+b/12+(4\ell-1)_+/6+\epsilon}.}    \tag{10}
\]

Equation (10) is only a low-side physical estimate. In the formal zero-gap geometry its comparison exponent is

\[
 11/12-\ell/4+(4\ell-1)_+/6,
\]

whose minimum is 41/48 at ell=1/4. But the unchanged high-side floor-bin inequality requires beta at least 2/3+ell (at b=0). Those two requirements cannot be replaced by the low-only minimum. Consequently (10) does not supply a new zero-free boundary.

## 6. Relation to the raw inverse goal

The refined count (3) is available in the source's full f,puncture marked energy because these labels are fixed during the powerful-part sum. However, it does not by itself remove the canonical residual-row diagonal: when O=0 and A0=0 the count and the energy exponent are unchanged. Any deduction of a raw inverse bound for H<D must track the full signed Poisson/gcd reconstruction. In particular, the formula cannot simply delete the row-volume term from an already positive canonical norm.
