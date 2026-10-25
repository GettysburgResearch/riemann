# Coherent gcd grouping in the native inverse

Status: **source-dependent component theorem; independent internal review
recorded in `REVIEW_GCD_NATIVE_COEFFICIENT.md`**. This note keeps the two original Möbius signs through the
whole reflected Heath--Brown sum. It obtains a further estimate for an
actual component of that sum. It does not bound its entire complement,
prove RH, or establish a new zero-free region.

The new distinction is that the component is indexed by the numerator
of the reduced ratio of the two reflected ideals. All original outer
product scales contribute coherently to its coefficient. A short outer
product truncation is not being substituted for that coefficient.

Under the scalar zero-free premise specified below, the conclusion is

\[
 \boxed{\quad
 J_B(U,D;Q)\ll (UDNQ)^\epsilon(1+|t|)^C p_j(V)^2
     \left(\frac BD\right)^{2-2\beta}
     \frac{UB}{D}\{U+B+(UB)^{2/3}\},\qquad \beta_0<\beta<1.
 \quad}                                                       \tag{1}
\]

Here \(\beta_0<1\) is a zero-free boundary only for the scalar Dedekind
zeta function of \(E=\mathbb Q(\omega)\). The row characters may have
the same fixed angular order as in `SIGNED_NATIVE.md`; no zero-free
premise for those angular characters is used. When the imported
source's scalar boundary \(\beta_0=7/8\) is used, (1) gives

\[
 \boxed{\quad
 J_{\le B_0}\ll (UDNQ)^\epsilon(1+|t|)^C p_j(V)^2
        U^2\left(\frac{B_0}{D}\right)^{5/4},
       \qquad 1\le B_0\le\min(\sqrt U,4y^2).
 \quad}                                                       \tag{2}
\]

The small loss from choosing \(\beta>7/8\) has been included in the
displayed epsilon. In particular, the entire component with reduced
numerator norm at most \(D/U^{4/5}\) has a volume bound when this cutoff
lies between 1 and \(\sqrt U\). The reduced numerators above the cutoff
remain in the exact identity.

## 1. Exact premises and conventions

Use the arithmetic conventions, common profile, natural zero
extensions, fixed finite ray data, fixed angular order, and bounded
nonnegative physical row weight of `SIGNED_NATIVE.md`, Sections 1--4.
The physical rows are all the specified sixth-power-free ideals of norm
comparable to U, including nonsquarefree rows. Their primitive inducing
characters are nonprincipal. The common norm height t lies in V and
has the same fixed polynomial seminorm cost as in that note.

The exact primitive reflection and the divisor-bounded full-column
sieve are the pinned premises there. In particular, the latter is
equation (6) of

`GettysburgResearch/riemann@c690f96fe6876f945398b3e2779810c563a64743`,

`standalone/2026-10-23-structured-moment-gains/fifth-pass/SEXTIC_ROW_PHASE_CANCELLATION.md`,

Git blob `3a5d7adcc24ec8907be5c8fd6879d81736d44788`.
It applies to a common divisor-bounded coefficient sequence, squarefree
rows, and unrestricted ideal columns:

\[
 \sum_{Nw\asymp W}^{\rm sf}
  \left|\sum_{Na\asymp B}b_a\chi_a(w)^{\pm1}\right|^2
       \ll (WB)^\epsilon B\{W+B+(WB)^{2/3}\}.                 \tag{3}
\]

This is not a claim about a stronger arbitrary-coefficient operator
norm. The sequence produced below has the divisor bound needed by (3).

There is one additional analytic premise for (1):

\[
                  \zeta_E(s)\ne0\qquad(\Re s>\beta_0),
                  \quad 0<\beta_0<1.                         \tag{4}
\]

The value \(\beta_0=7/8\) is imported from `thm:main` in
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
Git blob `268c4e3206d460c617d3d2129742a72b831b3def`. The present proof
does not independently certify that source theorem. A scalar premise
suffices here because the character of the gcd cancels exactly.

Every fixed omitted prime is included in S. Let Q_s be the common
union of S, the redundant original zero factors in the fixed
presentation sector, and rad(Q). For a physical row u, let

\[
       P_u=\operatorname{rad}(\mathfrak f_u Q_s),              \tag{5}
\]

where \(\mathfrak f_u\) is the primitive conductor. All natural
coprimality restrictions are retained. In particular, a dual ideal is
not required to avoid Q_s unless its actual primitive character value
vanishes there.

## 2. Grouping the full reflected identity

Fix once and for all a smooth real cutoff w with \(0\le w\le1\),
w equal to one on \([0,1]\), and w equal to zero on \([2,\infty)\).
Take \(D\ge8\), \(y=\sqrt{2D}\), and

\[
                       m_y(n)=\mu(n)w(Nn/y).
\]

The difference \(\mu-m_y\) is supported above y, so the proof by
squaring \(\delta_1-m_y*1\) still gives the exact ordinary identity
\(\mu=2m_y-m_y*m_y*1\) through norm \(y^2=2D\). Since
\(2y\le D\), the \(2m_y\) term vanishes throughout the original
V annulus. Define the complete smooth coefficient

\[
 A_y(r)=\sum_{h_1h_2=r}
           \mu(h_1)\mu(h_2)w(Nh_1/y)w(Nh_2/y).               \tag{6}
\]

There is no restriction \((h_1,h_2)=1\). Its full support is
\(Nr<4y^2=8D\), and its absolute size is at most \(d_E(r)\).
The resulting native inverse is exactly

\[
\begin{split}
 M_u={}&-\varepsilon_u\sqrt{D/q_u}
 \sum_r\frac{A_y(r)\psi_u(r)}{Nr}
 \sum_{e\mid Q_s}\frac{\mu(e)\psi_u^*(e)}{Ne}
 \sum_n\overline{\psi_u^*(n)}
      \Phi\!\left(\frac{NnD}{q_uNrNe}\right).                 \tag{7}
\end{split}
\]

This is the full finite r sum of `SIGNED_NATIVE.md` (11), with the
equally licensed smooth coefficient (6). There is no dyadic r
truncation in (7). In particular all terms \(Nr>2D\) up to \(8D\)
are retained. Each such term is zero in the original primal sum,
but its full reflected dual sum is needed for the exact coherent
regrouping below. Truncating the r sum at \(2D\) would destroy the
factorized coefficient that we use.
The full ordinary L function is reflected, so (7) itself uses no
zero-free premise. The n sum is absolutely convergent because Phi is
rapidly decreasing. The r and e sums are finite.

Write uniquely

\[
                  r=d a,\qquad n=d b,\qquad (a,b)=1.
\]

On the actual natural support,

\[
 \psi_u(da)\overline{\psi_u^*(db)}
   =\psi_u(a)\overline{\psi_u^*(b)}1_{(d,P_u)=1}.              \tag{8}
\]

This includes both primitive and redundant zero factors. It uses
\(|\psi_u^*(d)|^2=1\) only when d is a unit at every relevant prime.
The argument of Phi becomes \(NbD/(q_uNaNe)\), independent of d.
Define

\[
 C_a(P;y_1,y_2)=
       \sum_{(d,P)=1}\frac{A_{y_1,y_2}(ad)}{Nd},\qquad
 A_{y_1,y_2}(r)=\sum_{h_1h_2=r}
      \mu(h_1)\mu(h_2)w(Nh_1/y_1)w(Nh_2/y_2).
                                                                  \tag{9}
\]

The d sum is finite. Substitution in the complete (7) gives

\[
\boxed{
\begin{split}
 M_u={}&-\varepsilon_u\sqrt{D/q_u}
 \sum_a \frac{\psi_u(a)C_a(P_u;y,y)}{Na}
 \sum_{e\mid Q_s}\frac{\mu(e)\psi_u^*(e)}{Ne}\\
 &\hspace{8mm}\times\sum_{b\,:(a,b)=1}
      \overline{\psi_u^*(b)}
      \Phi\!\left(\frac{NbD}{q_uNaNe}\right).
\end{split}}                                                   \tag{10}
\]

There is no condition \((b,Q_s)=1\) in (10). Original terms with
arbitrarily large gcd d are part of \(C_a\). All the original outer
product dyads contribute before any norm is taken. Formula (10) is
obtained from the genuine native identity (7), not from a formal
extension already inside a positive majorant.

For a dyadic common window eta_B on \(Na\asymp B\), define M_(u,B)
by inserting eta_B in the a sum in (10), and set

\[
                 J_B=\sum_u w_U(u)|M_{u,B}|^2.                \tag{11}
\]

Define \(M_{u,\le B_0}\) by the literal common cutoff \(Na\le B_0\)
in (10), and \(J_{\le B_0}=\sum_u w_U(u)|M_{u,\le B_0}|^2\).
Thus (2) concerns the norm of the coherent partial sum, with its
original coefficients and its full collection of original r scales.
These pieces sum to M_u because \(Na<4y^2=8D\). They use this
complete smooth decomposition, including its coherent primal-zero
terms; they are not obtained by truncating the sharp decomposition
from `SIGNED_NATIVE.md` after reflection.

## 3. Exact allocation of the two Möbius signs

We need \(C_a\) only when \((a,P)=1\), since \(\psi_u(a)=0\)
otherwise. If a contains a prime to exponent at least three, then
\(C_a=0\). Otherwise write uniquely

\[
              a=a_1a_2^2,\qquad
              a_1,a_2\text{ squarefree},\quad(a_1,a_2)=1.
\]

Put

\[
 H_M(X)=\sum_{(h,M)=1}\frac{\mu(h)}{Nh}w(Nh/X),
                     \qquad X>0.
\]

Then the exact coefficient identity is

\[
\boxed{
 C_a(P;y_1,y_2)=\mu(a_1)
 \sum_{l r h=a_1\atop\text{pairwise coprime}}
 \frac1{Nh}
 H_{P a_2 l h}\!\left(\frac{y_1}{N(a_2 l h)}\right)
 H_{P a_2 r h}\!\left(\frac{y_2}{N(a_2 r h)}\right).
}                                                               \tag{12}
\]

Proof. From (9) and \((a,P)=1\),

\[
 C_a=Na\sum_{a\mid h_1h_2\atop(h_1h_2,P)=1}
       \frac{\mu(h_1)\mu(h_2)}{Nh_1Nh_2}
                             w(Nh_1/y_1)w(Nh_2/y_2).
\]

Both h_i are squarefree. A prime in a_2 must divide both h_i. For a
prime p in a_1, expand the exact condition that p divide at least one
of the two factors as

\[
       1_{p\mid h_1h_2}
        =1_{p\mid h_1}+1_{p\mid h_2}-1_{p\mid h_1}1_{p\mid h_2}.
\]

Assign the primes of a_1 to l, r, h according to these three terms.
Set \(d_L=a_2lh\), \(d_R=a_2rh\), and substitute
\(h_1=d_Lx\), \(h_2=d_Rz\). The nonzero Möbius terms require
\((x,d_L)=(z,d_R)=1\), exactly as in (12). There is no extra
restriction on \((x,z)\), \((x,r)\), or \((z,l)\). The inclusion
sign and the two fixed Möbius signs combine to \(\mu(a_1)\), and

\[
                 \frac{Na}{Nd_LNd_R}=\frac1{Nh}.
\]

This proves (12), including every repeated-prime contribution. The
both-divisible allocation is essential: its inclusion sign combines
with the two fixed Möbius signs to give the same common
\(\mu(a_1)\) as in the other allocations. It cannot be dropped.

For a fixed \(\beta\in(\beta_0,1)\), the scalar premise implies

\[
                  H_M(X)\ll (NM)^\epsilon X^{\beta-1}
                  \qquad(X>0).                              \tag{13}
\]

This follows from the absolutely convergent shifted Mellin formula
proved in the next section. The Mellin pole at zero is removable
because \(\zeta_E(s)^{-1}\prod_{p\mid M}(1-Np^{-s})^{-1}\)
vanishes at s=1. Applying (13) in (12) gives

\[
                 |C_a(P;y,y)|
             \ll (NPD)^\epsilon (Na/D)^{1-\beta}.             \tag{14}
\]

Indeed, each allocation contributes at most

\[
 (NPD)^\epsilon y^{2\beta-2}(Na)^{1-\beta}(Nh)^{-\beta},
\]

and the allocation count is divisor-bounded. The formula applies
also to a harmonic scale X below one; only when \(2X\le1\) is
that smooth sum necessarily zero. The pointwise bound (14), on
its own, is not enough to apply a common-coefficient sieve. The next
section resolves that dependence rather than moving a pointwise
bound outside a family norm.

## 4. Common Mellin contours separate the row mask

### 4.1 A scalar reciprocal bound

For every fixed \(\beta>\beta_0\) and every \(\eta>0\), (4) gives

\[
  \zeta_E(\sigma+i\tau)^{-1}\ll_{\beta,\eta}
        (3+|\tau|)^\eta\qquad(\sigma\ge\beta).               \tag{15}
\]

Here is the needed implication. For large \(|\tau|\), center discs
at \(3+i\tau\). Choose
\(\beta_0<\beta_2<\beta_1<\beta\). The disc of radius
\(3-\beta_2\) is zero-free and avoids the pole. The Euler branch of
\(\log\zeta_E\) is bounded on the radius-one disc. Polynomial
growth of \(\zeta_E\) and Borel--Caratheodory bound that branch by
\(O(\log(3+|\tau|))\) on the radius \(3-\beta_1\) disc.
Three-circles at radius \(3-\beta\) then bounds it by
\(O((\log(3+|\tau|))^\theta)\), with a fixed \(\theta<1\).
Exponentiating proves (15). Bounded heights follow by compactness,
with the zero of the reciprocal at s=1 included. The Euler region
handles larger real parts.

For a squarefree ideal P, define

\[
 F_P(z)=\zeta_E(z)^{-1}\prod_{p\mid P}(1-Np^{-z})^{-1},
 \qquad E_d(z)=\prod_{p\mid d}(1-Np^{-z})^{-1}.               \tag{16}
\]

For every fixed positive beta, the local products on \(\Re z\ge\beta\)
are \(\ll_\eta (NP)^\eta\), uniformly in height. This follows by
absorbing each sufficiently large prime factor into \((Np)^\eta\)
and treating the finitely many small primes as a constant. Thus

\[
           F_P(\beta+i\tau)\ll(NP(3+|\tau|))^\eta.           \tag{17}
\]

### 4.2 The smooth harmonic Mellin identity

Let \(Z=2+UDNQ\). The common cutoff w has Mellin transform

\[
 \widehat w(s)=\int_0^\infty w(x)x^{s-1}\,dx
       =-\frac1s\int_1^2 w'(x)x^s\,dx.                      \tag{18}
\]

The first integral initially requires \(\Re s>0\); the second
continues it meromorphically to the plane. Its sole pole is the
simple pole at s=0, with residue one. On any fixed vertical line
away from that pole, repeated integration by parts gives rapid
decay in the imaginary part, with a fixed finite-seminorm cost in
w. The same bounds are uniform on the fixed horizontal strip
used below when the imaginary part is large.

Mellin inversion and absolute convergence on \(\Re s=1\) give
the harmonic sum H_(Pd)(X). Shift to \(\Re s=\beta-1\).
There is no residue: the pole of \(\widehat w\) at s=0 is
canceled by \(F_{P d}(1)=0\), and (4) excludes all reciprocal
poles in the rectangle. The rapid decay from (18) and the
reciprocal bound (15)--(17) make the horizontal integrals tend
to zero. Thus the following is an exact, absolutely convergent
formula on one common contour for every \(X>0\):

\[
 H_{P d}(X)=\frac1{2\pi i}\int_{(\beta-1)}
            F_{P d}(1+s)\widehat w(s)X^s\,ds.                \tag{19}
\]

It immediately proves (13). No sharp endpoint, finite Perron
remainder, or cutoff-dependent choice of height is required.
If \(2X\le1\), the original sum is zero and the same Mellin
integral equals zero; it is not deleted from the common formula.

### 4.3 The common coefficient representation

On the actual support \((a,P)=1\), every forced divisor d in (12)
is coprime to P. Consequently

\[
                         F_{P d}(1+s)=F_P(1+s)E_d(1+s).       \tag{20}
\]

This is precisely where the natural zeros are used. Applying two
copies of (19) in the finite allocation sum (12) gives

\[
\begin{split}
 C_a(P;y,y)={}&\frac1{(2\pi i)^2}
  \int_{(\beta-1)}\int_{(\beta-1)}
 F_P(1+s)F_P(1+z)y^{s+z}\,\mathcal B_a(s,z)
       \widehat w(s)\widehat w(z)\,ds\,dz,                  \tag{21}\\
 \mathcal B_a(s,z)={}&\mu(a_1)
  \sum_{l r h=a_1\atop\text{pairwise coprime}}
   \frac{E_{a_2lh}(1+s)E_{a_2rh}(1+z)}
        {Nh\,N(a_2lh)^sN(a_2rh)^z}.
\end{split}
\]

If a is not cube-free, set \(\mathcal B_a=0\). The complete
a support \(Na<4y^2=8D\) and any common dyadic cutoff are
retained explicitly. Both integrals are absolutely convergent.

For fixed s,z, \(\mathcal B_a\) is independent of the physical row.
On the indicated contours,

\[
               |\mathcal B_a(s,z)|
                  \le d_E(a)^{C_\beta}(Na)^{1-\beta}.        \tag{22}
\]

To see this, the norm powers in one allocation are
\((Na\,Nh)^{1-\beta}\). The displayed \(1/Nh\) leaves
\((Na)^{1-\beta}(Nh)^{-\beta}\). Each finite Euler factor is
bounded by a fixed constant per prime, uniformly in both heights,
and the allocation count is at most \(3^{\omega(a_1)}\).

All dependence of (21) on P is therefore in
\(F_P(1+s)F_P(1+z)\), a bounded row scalar at each pair of contour
points. Since \(NP_u\ll UNQ\), the two integrals have total
absolute scalar mass at most

\[
 Z^{2\eta}\left(
   \int_{\mathbb R}(3+|\tau|)^\eta
                |\widehat w(\beta-1+i\tau)|\,d\tau
                 \right)^2\ll_{\beta,\eta,w} Z^{2\eta}.     \tag{23}
\]

Choosing eta sufficiently small makes this \(Z^\epsilon\).
On \(Na\asymp B\), (21)--(23) extract the single common size

\[
                    y^{2\beta-2}B^{1-\beta}
                       \asymp (B/D)^{1-\beta}.              \tag{24}
\]

The remaining column sequence is divisor-bounded and common. Norm
phases from the Mellin variables are part of that sequence and do
not require differentiating it. Nor is the row scalar F_P
differentiated in the row variable. The original smooth coupled
kernel is separated independently, as in `SIGNED_NATIVE.md`.

## 5. The family estimate with all conductors and masks retained

Insert (21) in (10), keep \((a,b)=1\), and apply Minkowski to the
two absolutely convergent contour integrals only after that exact
substitution.
At fixed s,z, the extra row scalar is bounded by (17). After
extracting (24), one has exactly the kind of reflected block
estimated in `SIGNED_NATIVE.md`, Sections 4.1--4.3, with its
divisor-bounded outer coefficient and outer length now B.

Here are the details needed to check that reuse. Fix the powerful
part v of the physical row, put

\[
 u=vw,\qquad Nv\asymp V_0,\quad Nw\asymp W\asymp U/V_0,
 \quad P_v=N\operatorname{rad}(v)\le V_0^{1/2},
 \quad q_u=c_sP_vNw\asymp q_v=WP_v.                         \tag{25}
\]

All original row masks are kept. The twist
\(\nu(a)\chi_a(v)^{\varsigma}\), with the original orientation,
the Q mask, and the common a cutoffs remain in the common a sequence.
The extra scalar \(F_{P_u}(1+s)F_{P_u}(1+z)\)
may vary with w but is bounded uniformly. For a fixed dual b, its
primitive value is a bounded row scalar, and \((a,b)=1\) is a
common a mask. Thus no moving coefficient is submitted to (3).

For a fixed e of norm E, the dual b scale is

\[
                              L_0=q_vBE/D.                   \tag{26}
\]

Separating the common smooth profile on dyads of Nw, Na, and Nb
preserves the fixed seminorm cost and the common a coefficients.
The primitive values at b and e and the root number are bounded
row scalars. This does not enlarge a naturally zero value to a
nonzero character in the original identity. A positive row norm
may subsequently discard such zeros.

Apply (3) at each dual b, and use the rapid tail to sum the b norms
by Minkowski. For every positive L_0, including L_0 below one,

\[
            \sum_{L\ge1\ {\rm dyadic}}
                     L(1+L/L_0)^{-j}\ll_j L_0.
\]

Before the factor (24), the squared norm for this fixed v,e is

\[
                  \ll (UDNQ)^\epsilon
                       \frac{q_vB}{D}\{W+B+(WB)^{2/3}\}.
                                                                  \tag{27}
\]

The prefactor check is exact:

\[
 \frac{\sqrt{D/q_v}}{BE}\,L_0
                  \sqrt{B\{W+B+(WB)^{2/3}\}}
       =\sqrt{\frac{q_vB}{D}\{W+B+(WB)^{2/3}\}}.
\]

Thus E cancels. The finite e sum costs only a divisor factor. All
fixed-ray sectors are summed with their bounded finite multiplicity.

For the powerful physical rows use

\[
      \sum_{Nv\asymp V_0}^{\rm powerful} P_v\ll V_0^{1+\epsilon}.
\]

The three contributions in (27), summed on this v dyad, are

\[
       \frac{U^2B}{DV_0},\qquad
       \frac{UB^2}{D},\qquad
       \frac{U^{5/3}B^{5/3}}{DV_0^{2/3}}.
\]

The first and third dyadic V_0 sums converge geometrically and the
second is logarithmic. Multiply by the square of (24), absorb the
contour mass (23), and recover (1).

For completeness, the integral exchanges are justified before any
uniform family bound is claimed. There are only finitely many rows,
a, e and allocations. The absolute dual b sum for each a,e is
\(O(q_uNaNe/D)\), valid also when its scale is below one. The
coefficient bound (22), reciprocal bound (17), and rapid Mellin
decay in (23) give an integrable majorant independent of b. This
licenses the substitution, Fubini, and then the norm inequality.
It does not require an assertion about arbitrary row-dependent
column coefficients.

## 6. Actual component consequences and the remaining range

For \(B_0\le\sqrt U\), the bracket in (1) is O(U), and summing the
dyadic **norms** coherently gives

\[
                J_{\le B_0}\ll Z^\epsilon
                          U^2(B_0/D)^{3-2\beta}.             \tag{28}
\]

The positive exponent \(3-2\beta\) makes the dyadic sum geometric.
The profile and height factors from (1) are suppressed only in this
section's exponent displays. Taking beta arbitrarily close to 7/8
proves (2).

Write \(D=U^r\), \(B_0=U^b\), with \(0\le b\le1/2\). The new
component exponent is

\[
                    e_{\rm gcd}(r,b)=2+\frac54(b-r).         \tag{29}
\]

The following examples are statements about the components defined in
(10)--(11), with all original outer product scales coherently included:

| Reduced numerator cutoff | Component exponent | Consequence |
|---|---:|---|
| \(B_0=\sqrt U\) | \(21/8-5r/4\) | At \(r=7/5\), exponent \(7/8\). |
| \(B_0=D/U^{4/5}\) | \(1\) | Volume bound whenever this cutoff lies in \([1,\sqrt U]\). |
| \(B_0=U^{7/15}\) | \(31/12-5r/4\) | Below the inherited \((1+5r)/6\) whenever \(r>29/25\). |
| \(B_0=U^{9/20}\) | \(41/16-5r/4\) | At least \(1/48\) below the inherited exponent throughout \(29/25\le r\le117/100\). |

For the source's critical detector length
\(r_c=1.1639535765090109563\ldots\), as authenticated in
`SHORT_INVERSE.md`, the \(B_0=U^{7/15}\) line has exponent

\[
           1.1283913626970696379\ldots,
\]

and its saving relative to the inherited full-inverse resource is

\[
              \frac{25r_c-29}{12}
                      =0.0082366177271061590\ldots.           \tag{30}
\]

This is a new estimate at that actual length for a precisely defined
component. It covers reduced numerator norms up to \(U^{7/15}\)
and includes contributions from original outer products all the way
up to \(4y^2=8D\). It is not an estimate for the full native
inverse: the common a range \(Na>U^{7/15}\) remains.

The last table line gives a useful uniform separation. Let
\(e_0(r)=(1+5r)/6\). On \(29/25\le r\le117/100\),

\[
 e_0(r)-e_{\rm gcd}(r,9/20)
                  =\frac{100r-115}{48}\ge\frac1{48}.        \tag{31}
\]

Define the complete complementary component by
\(M_{u,>B_0}=M_u-M_{u,\le B_0}\) in this same smooth
gcd-ratio decomposition. If that component were bounded, uniformly
in the original masks, heights and presentations, by

\[
 \sum_u w_U(u)|M_{u,>U^{9/20}}|^2
            \ll U^{e_0(r)-\eta+\epsilon},\qquad0<\eta<1/48,
                                                                  \tag{32}
\]

then Minkowski and (31) would give the same improved exponent for
the full native mean. This isolates a complete, specified remaining
tail. Estimate (32) is not proved here. No original product cutoff
from `SIGNED_NATIVE.md` is combined with it without estimating the
overlap.

At \(Na\asymp D\), the extra coefficient factor in (24) is of
constant size. Its scalar harmonic cancellation gives no saving
there. Those terms include genuinely coprime long outer products
with small original gcd, and neither their signs nor their profile
can be omitted. The argument does not establish the full moment
required to move the worst detector crossing.

## 7. Finite verification and its limits

`check_gcd_native.py` checks the exact weighted allocation (12), including
repeated primes, nontrivial puncture masks, and harmonic scales below one. It
checks the full gcd grouping with a genuinely zero-extended finite
character, its primitive conjugate, and finite compact ratio kernels,
so that the grouping is exact without a dual-tail approximation.
It also checks the coprime Euler-factor separation and the rational
exponent consequences. Deliberately wrong variants drop the
both-divisible allocation, delete the gcd coprimality mask, impose a
false Q mask on the primitive dual variable, or factor overlapping
Euler masks; each must fail.

Those checks certify finite algebra in a free-prime integer model and
the displayed exponent arithmetic. They do not prove (4), the
large-sieve premise, functional equations, reciprocal bounds, or the
analytic contour estimates. Those are stated and proved, or imported
with the exact scope above, in the text.
