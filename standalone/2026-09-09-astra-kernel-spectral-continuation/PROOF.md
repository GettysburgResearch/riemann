# The signed hyperbola kernel resolves zeta-zero modes exactly

**Status: PROPOSED, with written proofs; independent mathematical review pending.**
**RH and the actual Mobius energy bound are NOT proved.**

This is a direct continuation of the critical-source attack, not a claim that
an additional reformulation solves RH. We tried to obtain the missing arithmetic
bound by exploiting the *complete signed* kernel and its square-scale identity.
The outcome is an exact Mellin pairing formula, including multiple zeros, and
an exact family of spectral solutions of that identity. Those solutions show
why this particular algebra does not select the critical line by itself.

Repository: `GettysburgResearch/riemann`.
Frozen main: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
PR805 source: `602d7ddf9dbd2ba79bd6cada149772111ca72150`.
Its balanced-hyperbola parent: `ccd0a80dbd9844d06ccd6331a15b085b9c9afa41`.
The preceding local proof is preserved verbatim at [prior/PROOF.md](prior/PROOF.md).
Its arithmetic checker is preserved verbatim at [prior/check.py](prior/check.py).
No original or canonical statement is modified by this packet.

## 0. Native target and normalization

Everything here uses positive **odd** integers. Put

    M(x)=sum_(n<=x, odd) mu(n),
    m(x)=sum_(n<=x, odd) mu(n)/n,
    Q(x)=M(x)-x m(x),
    E(X)=integral_1^X m(t)^2 dt,
    Z(s)=(1-2^(-s)) zeta(s).

The preceding proof establishes the exact identity

    E(X)=integral_1^X M(t)^2/t^2 dt + Q(X)^2/X,

and the Mellin identity, initially in Re(s)>1,

    integral_1^infinity Q(x)x^(-s-1)dx = -1/[s(s-1)Z(s)].  (0.1)

The assertion E(X)=O_epsilon(X^epsilon) for every epsilon>0 implies RH by
holomorphic continuation of (0.1); its converse imports the classical
RH-to-Mertens bound. Neither assertion is established unconditionally here.

For an odd Y>=3, the literal terminal-balanced source is

    lambda_n=mu(n), odd n<Y;
    lambda_Y=-Y sum_(n<Y, odd) mu(n)/n.

Set lambda=0 elsewhere. Exact divisor inversion gives

    Q(Y^2)=2Q(Y)+B_Y,
    B_Y=sum_(a,b<=Y, odd)lambda_a lambda_b W(Y^2/(ab)),
    W(z)=sum_(r<=z, odd)(z/r-1), W(z)=0 for z<1.          (0.2)

The coefficient at a product boundary has weight zero. The quadratic is
bilinear, not a Hermitian/modulus-square substitute. These short-source
identities are in the classical Meissel/Huxley--Watt lineage and PR805.

Write c=gamma+log(2)-1 and, for z>=1,

    R(z)=W(z)-(z/2)(log z+c),
    K(u,v)=R(1/(uv)), 0<u,v<=1;
    K(u,0)=K(0,v)=0.                                   (0.3)

For the discrete measure lambda_Y=sum lambda_a delta_(a/Y), exact balance
sum lambda_a/a=0 annihilates the subtracted main term, so

    B_Y = B(lambda_Y,lambda_Y),
    B(alpha,beta)=double integral K(u,v) d alpha(u)d beta(v).

No factor 1/Y or 1/Y^2 is inserted into the discrete measure. A small norm of
the continuum kernel alone is not a bound for the unnormalized native source.

## 1. KSC-1: a self-contained kernel remainder and its Mellin transform

For every z>=1,

    |R(z)| < 3/(8z).                                    (1.1)

Here is an elementary proof retaining the odd endpoints. Let
h_j=sum_(k=1)^j 1/(2k-1), h_j=H_(2j)-H_j/2, and

    r_j=h_j-(log(2j)+gamma+log2)/2.

The harmonic-limit definition of gamma gives r_j -> 0. Moreover

    r_j-r_(j+1)= (1/2)log((j+1)/j)-1/(2j+1)
               =sum_(k>=1)1/[(2k+1)(2j+1)^(2k+1)]
               <=(3/8)(2j+1)^(-3).

All summands are positive. Convex midpoint comparison gives

    sum_(l>=j)(2l+1)^(-3)
       <=integral_(j-1/2)^infinity(2t+1)^(-3)dt=1/(16j^2).

Thus 0<r_j<=3/(128j^2). Put j=floor((z+1)/2) and v=(2j-z)/z.
Then -1/3<v<=1, |2j-z|<=1, and

    R(z)=(z/2)[log(1+v)-v]+z r_j.

Integrating t/(1+t) separately on either side of zero proves
0<=v-log(1+v)<=3v^2/4 in this interval. The negative term is at least
-3/(8z), and z r_j<=27/(128z)<3/(8z), since z<2j+1<=3j.
This proves (1.1). The value at a breakpoint is unambiguous: the newly
activated summand in W is zero. In particular K is continuous and
|K(u,v)|<=3uv/8.

Define

    I(s)=integral_1^infinity R(z)z^(-s-1)dz.

It is holomorphic on Re(s)>-1, including differentiated integrals. In Re(s)>1,
positive/absolutely convergent termwise integration in W gives

    I(s)=Z(s)/[s(s-1)]
         -(1/2)[1/(s-1)^2+c/(s-1)].                    (1.2)

Define the regularized zeta factor

    F(s)=((s-1)/s) Z(s).                                (1.3)

It is holomorphic on Re(s)>-1, with removable singularities at 0 and 1.
Indeed Z(s) has a simple pole at 1 and a simple zero at 0. Multiplication
of (1.2) by (s-1)^2, followed by the identity theorem, gives

    (s-1)^2 I(s)=F(s)-(1/2)[1+c(s-1)].                  (1.4)

Only standard analytic continuation and the values zeta(0)=-1/2 and the
residue of zeta at 1 are used for these removals. In particular

    a:=F(0)=log(2)/2 >0; write b=F'(0).

It is not necessary to evaluate b numerically anywhere in the proofs.

## 2. KSC-2: the complete bilinear kernel is a divided difference

For Re(s)>0 define the finite complex measure on (0,1]

    nu_s = s(1-s)u^(s-1)du + s delta_1.                 (2.1)

For Re(s)>1 it has literal harmonic balance integral dnu_s/u=0.
For 0<Re(s)<=1 that harmonic integral generally does not converge. It is
NOT a native finite Mobius source and must not be called harmonically
balanced without qualification in that range.

The pairing against K is nevertheless absolutely convergent in the larger
domain Re(s),Re(t)>-1: its density is evaluated only against functions
vanishing at least linearly at zero. Equivalently set

    nu_s(f)=s(1-s)integral_0^1 u^(s-1)f(u)du+s f(1)

on functions with |f(u)|<=C u. This is a holomorphic family of functionals
in Re(s)>-1; it need not be a finite measure when Re(s)<=0. In this
functional interpretation nu_0=0 and

    nu'_0(f)=integral_0^1 f(u)/u du+f(1).                (2.2)

Define B(s,t)=B(nu_s,nu_t), with bilinear complex extension. Then

    B(s,t)=s t [F(t)-F(s)]/(s-t), s!=t,                (2.3)
    B(s,s)=-s^2 F'(s).                                 (2.4)

These identities hold throughout Re(s),Re(t)>-1 with the removable
diagonal interpreted by (2.4). No RH assumption is used.

### Proof

The change of variables r=uv gives

    double integral u^(s-1)v^(t-1)K(u,v)du dv
       =[I(t)-I(s)]/(s-t).

The two density/atom terms contribute I(s), I(t), and the atom/atom term
is R(1)=-c/2. Substitution of (2.1) yields

    B(s,t)=st{[(1-t)^2 I(t)-(1-s)^2 I(s)]/(s-t)+R(1)}.

Insert (1.4). The linear main-term contribution c/2 cancels R(1) exactly;
(2.3) remains. Dominated holomorphy, or the removable limit, proves (2.4).
This cancellation uses the atoms at 1, not just the power densities.

### Zero modes

For distinct nonzero zeros alpha,beta of F,

    B(nu_alpha,nu_beta)=0.                              (2.5)

For a simple nonzero zero alpha,

    B(nu_alpha,nu_alpha)=-alpha^2 F'(alpha).

At a nontrivial zeta zero this is

    alpha(1-alpha)Z'(alpha).                            (2.6)

Thus distinct zero modes have no mixed quadratic term, whereas the matched
term is nonzero for a simple zero. This is **bilinear orthogonality of these
functionals**, not a Hilbert--Polya self-adjoint eigenvalue theorem.

The omitted-endpoint issue matters here: subtracting the large pole term but
forgetting the atom would not give this divided difference.

## 3. KSC-3: multiplicities and the real indefinite root spaces

Let alpha!=0 be a zero of F of multiplicity m, and put

    v_j=(1/j!) partial_s^j nu_s at s=alpha, 0<=j<m.

Every pairing is defined as above; no simplicity is assumed. If
F(alpha+z)=c_m z^m+O(z^(m+1)), c_m!=0, then

    B(v_j,v_k)=0,               j+k<m-1,
    B(v_j,v_k)=-alpha^2 c_m,    j+k=m-1.                (3.1)

Hence this m by m matrix is nonsingular, with determinant

    (-1)^(m(m-1)/2) (-alpha^2 c_m)^m.                   (3.2)

For two distinct zeros, the corresponding full finite jet spaces are
bilinearly orthogonal. To see this, expand (2.3): its denominator is
nonzero at the distinct pair, and every numerator term vanishes to order
at least the relevant root multiplicity. For (3.1), expand

    [F(alpha+b)-F(alpha+a)]/(a-b)
       =-c_m sum_(j=0)^(m-1) a^j b^(m-1-j)+higher terms.

The extra st factor contributes alpha^2 on that first antidiagonal.

Suppose alpha is nonreal. Since K is real, conjugation identifies its jet
space with that at conjugate(alpha). They are distinct and orthogonal.
Their combined real space has signature (m,m). Indeed the complex symmetric
form on the alpha space is nonsingular, while the real form on
v+conjugate(v) is twice Re B(v,v). Multiplication of v by i changes the sign
of this form and preserves nonsingularity, so its positive and negative
indices are equal. Its dimension is 2m by (3.2).

For m=1, writing k=-alpha^2F'(alpha), the real basis
Re(nu_alpha), Im(nu_alpha) has Gram matrix

    (1/2) [[Re k, Im k],[Im k,-Re k]],

with determinant -|k|^2/4. This calculation applies on either side of the
critical line as well as on it. It does not locate an actual zeta zero.
These are not claims about L2 eigenfunctions: the atom and, at critical
parameters, the density domain preclude that identification without another
operator/domain theorem.

## 4. KSC-4: the complete square-scale identity admits every finite zero selection

This is the decisive test of the proposed global completion. Choose ANY
finite set S of nonzero zeros of F in Re(s)>-1. Let Gamma be a union of
positively oriented small disjoint contours around 0 and these zeros, and
no others. All contours stay in Re(s)>-1. Multiple zeros are allowed.
For Y>0 define

    q_S(Y)=(1/(2 pi i)) integral_Gamma -Y^s/[s^2 F(s)] ds,
    L_(S,Y)(f)=(1/(2 pi i)) integral_Gamma
                     -Y^s nu_s(f)/[s^2 F(s)] ds.        (4.1)

Then exactly

    B(L_(S,Y),L_(S,Y))=q_S(Y^2)-2q_S(Y).                (4.2)

This is an identity for a finite spectral model of the SAME regularized
kernel, not an assertion that its source coefficients equal mu(n).
No assertion is made that any off-line zeta zero exists. If one existed,
its contour would satisfy exactly the same theorem. The kernel identity
therefore does not by itself exclude that possibility.

### Proof without a simplicity assumption

Use an outer s-contour and a slightly inner t-contour around the same selected
poles, so the contours never meet. Insert (2.3) into the double integral.
The integrand becomes

    Y^(s+t)/[st(s-t)] (1/F(s)-1/F(t)).                   (4.3)

For its first term, the t-integral has only the pole t=0, because s lies
outside the inner contour. Its residue is 1/s. The remaining s-integral
is -q_S(Y).

For the second term integrate first in s. Only s=0 and s=t are poles of
Y^s/[s(s-t)]; their sum of residues is (Y^t-1)/t. The remaining expression
is q_S(Y^2)-q_S(Y). Adding proves (4.2). Compact contours and (1.1)
justify all changes of order. The removable diagonal of (2.3) ensures
that the nesting does not change the original pairing.

### Explicit formula when the selected zeros are simple

Set a=F(0)>0, b=F'(0). Then

    q_S(Y)=-(log Y)/a + b/a^2
              +sum_(alpha in S) c_alpha Y^alpha,
    c_alpha=-1/[alpha^2 F'(alpha)].                     (4.4)

The functional nu_0 vanishes on the kernel domain, so the contribution of
the double pole at zero to L_(S,Y) is simply -nu'_0/a.
Equations (2.3)--(2.4) give

    B(nu_alpha,nu'_0)=a       when F(alpha)=0,
    B(nu'_0,nu'_0)=-b.                                 (4.5)

Consequently the matched zero terms produce sum c_alpha Y^(2alpha),
the cross terms with the zero-pole background produce
-2 sum c_alpha Y^alpha, and the background square produces -b/a^2.
This is precisely q_S(Y^2)-2q_S(Y). In particular the linear -2q_S(Y)
term is NOT neglected as a lower-order error. The logarithmic background
is essential; a nonzero-zero selection without 0 instead gives the different
identity B(L,L)=q_S(Y^2).

If S is invariant under conjugation, q_S and L_(S,Y) are real on real tests.
The model remains distinct from the literal integer Mobius source. No finite
spectral expansion of the actual Q is assumed; no interchange with the
infinite set of zeta zeros or unproved zero-residue summability occurs.

## 5. KSC-5: honest compact balanced approximations, with the boundary cost visible

For 0<epsilon<1 define a genuine finite signed/complex measure

    nu_(s,epsilon)=s(1-s)u^(s-1)1_(epsilon<u<1)du
                  +s delta_1-s epsilon^s delta_epsilon. (5.1)

For every complex s, including removable s=1,

    integral dnu_(s,epsilon)/u=0,
    integral dnu_(s,epsilon)=1-epsilon^s.               (5.2)

Thus the critical-parameter cutoff models have actual harmonic balance, not
merely an analytic finite-part designation. Their pairings converge to (2.3).
Here is a bound which covers the complete omitted interval.

Use the weighted variation norm V(alpha)=integral u d|alpha|(u). For sigma=Re(s)>-1,

    V(nu_s) <= A_s:=|s(1-s)|/(sigma+1)+|s|,
    V(nu_s-nu_(s,epsilon))
       <=D_s(epsilon):=[|s(1-s)|/(sigma+1)+|s|]epsilon^(sigma+1).

For sigma<=0 these statements mean the weighted density/atom functional,
not unweighted finite variation. The bound |K(u,v)|<=3uv/8 gives

    |B(nu_s,nu_t)-B(nu_(s,epsilon),nu_(t,epsilon))|
       <=(3/8)[D_s A_t+(A_s+D_s)D_t].                 (5.3)

On compact parameter contours D_s -> 0 uniformly. Therefore the contour
functionals in Section 4 also have compact, harmonically balanced
approximants, and their complete kernel pairings converge uniformly for Y
in compact subsets of (0,infinity). This is not uniform in Y->infinity.

At s=0 the derivative is particularly explicit:

    nu'_(0,epsilon)=1_(epsilon<u<1)du/u
                       +delta_1-delta_epsilon.

It is balanced but its total coefficient mass is log(1/epsilon), which
diverges as epsilon->0. The kernel sees a convergent pairing because it
vanishes on the missing small-coordinate boundary. This is precisely why
convergence of compact-kernel pairings does not establish a bounded native
source norm or the required Mobius energy bound.

The cutoff measures are CONTINUOUS/atomic controls, not a sequence of integer
Mobius coefficients. Equations (5.2)--(5.3) do not erase that distinction.

## 6. Outcome of the full-proof attempt

The attack was to use the complete signed square-scale identity, rather than
an absolute-value or diagonal majorant, to force subpower critical energy.
The exact calculation does remove every mixed term between distinct zero
modes. But matched terms survive with the reciprocal of the Mellin pole
residue, and the logarithmic background supplies the exact linear correction.
Therefore every finite selected spectral model satisfies the full identity,
including any hypothetical off-line zero model. Multiple zeros do not repair
this selection failure.

The meaningful new results are the all-domain pairing formula, multiplicity
structure, exact finite-spectrum nonlinear identity, and controlled balanced
cutoff realization. The missing arithmetic estimate is still

    E(X)=O_epsilon(X^epsilon), for every epsilon>0,

for the LITERAL odd Mobius function, not the spectral controls. No new fixed
power saving, zero-free region, positive full critical kernel, or RH proof is
established. The model identities are not a counterexample to RH either.

A useful next theorem would have to exploit an additional actual-source
property (for example the full divisor inverse relation together with a
quantitative source norm), rather than infer critical-line selection from
(0.2), kernel compactness, tail balance, or generic mode orthogonality alone.
This is a direction, not an assertion that such a bound has been found.

## Sources and attribution

- NIST DLMF sections 25.2 and 25.6: standard analytic continuation, the pole
  and residue at 1, and zeta(0)=-1/2; no RH-dependent information.
- Huxley--Watt, *Mertens Sums requiring Fewer Values of the Mobius function*,
  arXiv:1807.05890 (2018): short-source identities, quadratic forms, and
  spectral/Perron approaches are classical prior work, not inventions here.
- Nigel Watt, arXiv:1812.01039 and arXiv:1912.01716: related unsmoothed Mertens
  kernels and Hankel/eigenfunction analysis. Their kernels are NOT K in (0.3).
  Only their abstracts were inspected for research context; no theorem from
  those papers is imported into this proof or claimed independently reviewed.
- PR805, `ccd0a80dbd9844d06ccd6331a15b085b9c9afa41`,
  `standalone/2026-09-07-astra-balanced-hyperbola/PROOF.md`, sections 1--4;
  and `602d7ddf9dbd2ba79bd6cada149772111ca72150`,
  `standalone/2026-09-07-astra-critical-line-attempt/PROOF.md`.
- The previous local proof/checker, preserved and identified by full hashes
  in SOURCES.json. Its RH equivalence is reused, not promoted to a solution.

The Mellin, divided-difference, residue, and conjugation arguments are given
above so this continuation does not rely on an unlocated theorem about this
particular kernel. No comprehensive priority claim is made.
