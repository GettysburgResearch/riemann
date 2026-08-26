# Odd-notch profile chi-square bridge

Status: **rigorous profile-averaged bridge across the first
growing-modulus transition; raw detector zeros, not zeros of an individual
`L`-function**.

Exact bounded replay:
[`quadratic_family_profile_chi_square_bridge.py`](quadratic_family_profile_chi_square_bridge.py).

## 0. Outcome

Fix an odd prime power `q`.  Put

\[
 n=2h+1,\qquad M=4h+1,
\]

and, for `j>=1`, set

\[
 d=h-j,\qquad r=2j+1,
 \qquad
 \mathcal A_r=\prod_{\deg P\le r}P,
 \qquad
 \ell_r=\deg\mathcal A_r.
\tag{0.1}
\]

Assume `d>r`.  Let `Z_(q,h,j)` be the raw detector-zero population in the
squarefree degree-`M` layer of minimum factor degree exactly `d`, and put

\[
 \beta_r=2^{-I_q(r)}{I_q(r)\choose\lfloor I_q(r)/2\rfloor}.
\tag{0.2}
\]

The logarithmic-depth firewall conditioned on one complement and required
`ell_r<=d/4`.  Averaging complete factor-degree profiles gives a stronger
exact gate.  Define the profile-weighted relative chi-square discrepancy
`mathfrak D_j` in Section 2.  Then

\[
\boxed{
 Z_{q,h,j}\le T_j
 \left(\beta_r+\sqrt{\beta_r}\,\mathfrak D_j\right),}
\tag{0.3}
\]

where `T_j` is the complete population of the minimum-`d` layer and

\[
 T_j\le {q^M\over d^2}.
\tag{0.4}
\]

Function-field RH for Dirichlet characters, Newton identities for repeated
factor degrees, and elementary profile counting prove the unconditional
bound

\[
\boxed{
 \mathfrak D_j^2
 \le C_*M^{11}(\ell_r+1)^{10}q^{\ell_r-M},
 \qquad C_*=614400.}
\tag{0.5}
\]

Also

\[
 \beta_r\ge {1\over I_q(r)+1}
 \ge {r\over q^r+r}
 \ge {1\over2q^r}.
\tag{0.6}
\]

Consequently the explicit near-wall condition

\[
\boxed{
 q^{M-\ell_r-r}
 \ge 2C_*M^{11}(\ell_r+1)^{10}}
\tag{0.7}
\]

implies `mathfrak D_j^2<=beta_r` and therefore

\[
\boxed{
 {Z_{q,h,j}\over q^M}\le {2\beta_r\over d^2}.}
\tag{0.8}
\]

Equivalently, (0.7) follows from

\[
 M-\ell_r
 \ge r+\log_q(2C_*)+11\log_qM
       +10\log_q(\ell_r+1).
\tag{0.9}
\]

Thus the bridge reaches to within an explicit logarithmic margin of the
finite-residue entropy wall.  The simpler condition

\[
 \boxed{\ell_r\le M/2}
\tag{0.10}
\]

implies (0.7) for all sufficiently large `M`.

If a terminal depth `J=J(h)` satisfies `h-J>2J+1` and (0.7) with
`r=2J+1`, then all `1<=j<=J` satisfy it and

\[
\boxed{
 {1\over q^M}\sum_{j=1}^{J}Z_{q,h,j}=O_q(h^{-2})=O_q(M^{-2}).}
\tag{0.11}
\]

This crosses the transition `q^(2j) asymp h` that blocked the
one-marked-prime argument.  It enlarges the constant inside the logarithmic
window but cannot change its scale: `ell_r=Theta_q(q^r)`, so even the
near-wall range still has

\[
 J={1\over2}\log_qM+O_q(1).
\tag{0.12}
\]

## 1. Frozen source and claim boundary

The packet locks the corrected predecessor quartet at commit
`9f439e623ccafc12ffe4d434e511fd41a415c12f`.

| predecessor file | blob |
|---|---|
| `QUADRATIC_FAMILY_LOGARITHMIC_DEPTH_ZERO_FIREWALL.md` | `0aa9cd103cc48aaf56a64f45a3902cca63a2d3c5` |
| `quadratic_family_logarithmic_depth_zero_firewall.py` | `2e6eb61536833ef924ed703099a11de42126ea24` |
| `quadratic_family_logarithmic_depth_zero_firewall.json` | `b4d56f8184734018422c35e84ef8d87bdf886872` |
| `test_quadratic_family_logarithmic_depth_zero_firewall.py` | `9286c3944f9de377e9ebecf1d3fc8aa538dc935a` |

The analytic input is the standard Weil bound for function-field Dirichlet
characters.  It is a proved function-field theorem, not an assumption about
the Riemann hypothesis over the integers.  The result concerns a raw family
detector, not an individual `L`-function zero, RH, GRH, a number-field
transfer, or external novelty.

## 2. The exact profile-weighted chi-square gate

Let `Lambda_j` be the set of nonempty factor-degree profiles

\[
 \lambda=(m_e)_{e\ge d},\qquad
 m_d\ge1,\qquad \sum_{e\ge d}em_e=M.
\tag{2.1}
\]

Write

\[
 T_\lambda=\prod_e{I_q(e)\choose m_e},
 \qquad T_j=\sum_{\lambda\in\Lambda_j}T_\lambda.
\tag{2.2}
\]

Every conductor in this layer is a unit modulo `A_r`, because `d>r`.
For `a` in

\[
 G_r=(\mathbf F_q[T]/\mathcal A_r)^*,
 \qquad \Phi_r=|G_r|,
\]

put

\[
 N_\lambda(a)
 =\#\{Q\text{ in profile }\lambda:Q\equiv a\pmod{\mathcal A_r}\}.
\tag{2.3}
\]

For a fixed profile, every reciprocal coefficient `a_k` in the locked notch
formula is fixed and `a_d=m_d>=1`.  The top-degree isolation is therefore

\[
 S_{n,Q}=m_dS_r+H_\lambda(\epsilon_P:\deg P<r),
 \qquad S_r=\sum_{\deg P=r}\epsilon_P.
\tag{2.4}
\]

Uniform units modulo `A_r` give independent signs, so the zero set
`E_lambda` in `G_r` obeys

\[
 |E_\lambda|\le\beta_r\Phi_r.
\tag{2.5}
\]

Define

\[
\boxed{
 \mathfrak D_j^2
 ={\Phi_r\over T_j}
 \sum_{\lambda\in\Lambda_j}{1\over T_\lambda}
 \sum_{a\in G_r}
 \left|N_\lambda(a)-{T_\lambda\over\Phi_r}\right|^2.}
\tag{2.6}
\]

The zero count is

\[
 Z_{q,h,j}=\sum_\lambda\sum_{a\in E_\lambda}N_\lambda(a).
\]

The uniform parts contribute at most `beta_r*T_j`.  For the discrepancies,
Cauchy first inside each profile and then across profiles gives

\[
\begin{aligned}
 \sum_\lambda\left|
  \sum_{a\in E_\lambda}
  \left(N_\lambda(a)-{T_\lambda\over\Phi_r}\right)
 \right|
 &\le \sqrt{\beta_r\Phi_r}
       \sum_\lambda\|N_\lambda-T_\lambda/\Phi_r\|_2\\
 &\le \sqrt{\beta_r}\,T_j\mathfrak D_j.
\end{aligned}
\tag{2.7}
\]

This proves (0.3).  The weights `1/T_lambda` in (2.6) are what prevent a
spurious raw factor equal to the number of profiles.

With Fourier transform

\[
 \widehat N_\lambda(\chi)
 =\sum_{a\in G_r}N_\lambda(a)\overline{\chi(a)}
 =\sum_{Q\in\lambda}\overline{\chi(Q)},
\]

Parseval gives the exact bilinear/spectral form

\[
\boxed{
 \mathfrak D_j^2
 ={1\over T_j}
 \sum_{\lambda\in\Lambda_j}{1\over T_\lambda}
 \sum_{\substack{\chi\bmod\mathcal A_r\\\chi\ne1}}
 |\widehat N_\lambda(\chi)|^2.}
\tag{2.8}
\]

Thus the smallest sufficient spectral gate is that the final double sum in
(2.8) be at most `T_j*beta_r`.

## 3. At most five factors

The condition `d>r` is

\[
 h-j>2j+1,
\]

so `h>3j+1`.  Hence

\[
 6d=6h-6j>4h+2>M.
\tag{3.1}
\]

Every profile in `Lambda_j` therefore contains at most five irreducible
factors.  A nondecreasing degree tuple is determined by its first at most
four entries, so

\[
 |\Lambda_j|\le5M^4.
\tag{3.2}
\]

This bounded factor count, not an enumeration of fields or conductors, is
the reason the profile average remains polynomially controlled.

## 4. Repeated degrees and Newton identities

Fix a nonprincipal character `chi mod A_r`.  For a factor degree `e` and
an integer `b>=1`, put

\[
 P_{e,b}(\chi)=\sum_{\deg P=e}\chi(P)^b.
\tag{4.1}
\]

If `chi^b` is nonprincipal, the same function-field RH argument as in the
predecessor gives

\[
 |P_{e,b}(\chi)|
 \le{(\ell_r+1)q^{e/2}\over e}
 \le(\ell_r+1)q^{be/2}.
\tag{4.2}
\]

If `chi^b` is principal, then `b>=2`, because `chi` itself is
nonprincipal.  In that case

\[
 |P_{e,b}(\chi)|=I_q(e)\le {q^e\over e}\le q^{be/2}.
\tag{4.3}
\]

The squarefree choice of `m` distinct degree-`e` primes is the elementary
symmetric polynomial

\[
 E_{e,m}(\chi)
 =e_m(\chi(P):\deg P=e).
\]

Newton's permutation formula is

\[
 e_m={1\over m!}\sum_{\sigma\in S_m}
 (-1)^{m-c(\sigma)}
 \prod_{C\text{ cycle of }\sigma}p_{|C|}.
\tag{4.4}
\]

Each cycle of length `b` is controlled by (4.2) or (4.3).  The sum of its
cycle lengths is `m`, and the `m!` terms cancel the outer `1/m!` in the
triangle inequality.  Therefore

\[
\boxed{
 |E_{e,m}(\chi)|
 \le(\ell_r+1)^m q^{me/2}.}
\tag{4.5}
\]

The principal `chi^b` terms in (4.3) are diagonal correction terms inside
Newton's identity.  They do not mean that the conductor contains a repeated
prime; the original elementary symmetric polynomial is still squarefree.

Multiplying (4.5) over all degrees in a profile with
`k=sum_e m_e<=5` gives

\[
\boxed{
 |\widehat N_\lambda(\chi)|
 \le(\ell_r+1)^5q^{M/2}.}
\tag{4.6}
\]

## 5. Uniform lower bounds for every nonempty profile

For `e>=2`, Möbius inversion and `q>=3` give

\[
\begin{aligned}
 eI_q(e)
 &\ge q^e-\sum_{m\le e/2}q^m\\
 &>q^e-{3\over2}q^{e/2}
 \ge {q^e\over2}.
\end{aligned}
\tag{5.1}
\]

Here the last inequality is `3<=q^(e/2)`.  Since `d>r>=3`, every
participating `e` is at least four and

\[
 I_q(e)\ge {q^e\over2e}\ge2m
 \qquad(0\le m\le5).
\tag{5.2}
\]

Thus

\[
 {I_q(e)\choose m}
 \ge{(I_q(e)/2)^m\over m!}
 \ge {q^{em}\over4^me^mm!}.
\tag{5.3}
\]

For every nonempty profile with `k<=5`, equations (5.2)--(5.3) imply the
uniform bound

\[
\boxed{
 T_\lambda
 \ge {q^M\over4^5\,5!\,M^5}
 ={q^M\over122880M^5}.}
\tag{5.4}
\]

The two-factor profile `(d,M-d)` always exists and has distinct degrees.
It gives

\[
 T_j\ge I_q(d)I_q(M-d)
 \ge {q^M\over4d(M-d)}
 \ge {q^M\over M^2}.
\tag{5.5}
\]

The last inequality uses `4d(M-d)<=M^2`.

## 6. Proof of the discrepancy bound and bridge

There are at most `Phi_r` nonprincipal characters.  Combining
(2.8), (3.2), (4.6), (5.4), (5.5), and `Phi_r<=q^ell_r` gives

\[
\begin{aligned}
 \mathfrak D_j^2
 &\le {M^2\over q^M}
 (5M^4)(122880M^5q^{-M})
 q^{\ell_r}(\ell_r+1)^{10}q^M\\
 &=614400M^{11}(\ell_r+1)^{10}q^{\ell_r-M}.
\end{aligned}
\tag{6.1}
\]

This proves (0.5).

The sum of `N=I_q(r)` signs has only `N+1` possible values, so its largest
atom is at least `1/(N+1)`.  Since `I_q(r)<=q^r/r`,

\[
 \beta_r\ge{1\over I_q(r)+1}
 \ge{r\over q^r+r}\ge{1\over2q^r},
\]

which proves (0.6).  Under (0.7), equation (0.5) gives

\[
 \mathfrak D_j^2\le {1\over2q^r}\le\beta_r.
\]

Equations (0.3)--(0.4) now prove (0.8).

For a fixed `M`, the left side of (0.7) decreases with `j`, while its right
side increases.  Thus a terminal safe depth makes every earlier depth safe.
The anti-concentration estimate

\[
 \beta_r=O_q(\sqrt j\,q^{-j})
\]

is summable, and `d>=h-J asymp h`; this proves (0.11).

If `ell_r<=M/2`, the predecessor's elementary lower bound
`ell_r>=2q^r/3` gives `q^r<=3M/4`.  Consequently

\[
 q^{M-\ell_r-r}\ge {4q^{M/2}\over3M},
\]

which eventually dominates the polynomial on the right side of (0.7).
This proves the simple corollary (0.10).

## 7. Why the bridge is still logarithmic

The chi-square method can approach the full residue-space entropy wall, but
it cannot cross it in scale.  For the probability distribution
`p_lambda(a)=N_lambda(a)/T_lambda`, Cauchy gives the exact support bound

\[
 \Phi_r\sum_ap_\lambda(a)^2-1
 \ge {\Phi_r\over|\operatorname{supp}p_\lambda|}-1
 \ge {\Phi_r\over T_\lambda}-1.
\tag{7.1}
\]

Thus full-residue chi-square equidistribution is impossible once the
residue group materially exceeds the conductor supply.  Since
`ell_r=Theta_q(q^r)`, reaching `ell_r=M-O(log M)` already means
`r=log_qM+O_q(1)` and hence (0.12).  The bridge improves the constant and
reaches the entropy wall to logarithmic accuracy; it does not establish a
mesoscopic window with `j/log M -> infinity`.

A theorem beyond this point would have to use the special detector-zero
sets more economically than full residue equidistribution, or import a new
conditional small-ball/growing-monodromy mechanism.

## 8. Proof ledger and bounded replay

Proved:

- the exact profile-weighted gate (0.3) and Parseval form (2.8);
- the at-most-five-factor reduction and polynomial profile count;
- all repeated-degree Newton terms, including principal character powers;
- the uniform nonempty-profile lower bound (5.4);
- the explicit discrepancy estimate (0.5);
- the near-wall condition (0.7), half-modulus corollary, and summed
  `O_q(M^-2)` theorem;
- the finite-support entropy fence.

Not proved or claimed:

- a depth window larger than logarithmic order;
- raw-zero cancellation density after the finite-residue entropy wall;
- an individual `L`-function zero or an integer-RH/GRH consequence;
- a number-field transfer or external novelty.

Run:

```text
python -B research/l-families/atlas/function_field/quadratic_family_profile_chi_square_bridge.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_profile_chi_square_bridge.py --check
python -B -m unittest tests.test_quadratic_family_profile_chi_square_bridge
python -B -O -m unittest tests.test_quadratic_family_profile_chi_square_bridge
```

The replay enumerates only small integer degree profiles and cycle
partitions through multiplicity five.  It enumerates no polynomial,
irreducible, residue class, character, finite-field element, conductor,
curve, point, or zero.
