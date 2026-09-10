# Real-zero crowding obstructs equivalent Hilbert metrics on the spectral core

Date: 2026-09-10. Research continuation of PR #834.
Status: PROPOSED COMPLETE COMPONENT PROOF; independent review required.
RH and positivity of the nonzero spectrum of the actual operator T remain unproved.
No novelty claim is made for eigenvector-angle arguments or Riesz-basis theory.
Local labels ZC1--ZC5 are not canonical accepted claim identifiers.

## 0. What this closes, and what it does not

The preceding centered-theta determinant manuscript rules out a bounded positive
symmetrizing metric on the full space and every finite derivative cut. It leaves
open such a metric on W_infinity, the intersection of all those cuts. Here the
already-known REAL zeros rule out that metric there as well. This obstruction
persists on the closed span of just the simple real-zero eigenvectors. It does
not require any nonreal zero, and therefore is not evidence against RH.

The proof uses the actual theta-weighted metric. Two distinct real zeros with
nearby ordinates give nearly parallel eigenvectors, whereas a coercive metric
making the operator self-adjoint must make these vectors orthogonal. A uniform
change of norm cannot do that. A stronger local statement rules out every finite
positive-measure reweighting for the exponential eigenvectors, even when it is
not equivalent to the theta metric.

## 1. Source, spaces, and the limited imported facts

Keep exactly the source of the parent:

    Xi(z)=xi(1/2+iz)=integral_R phi(t) exp(izt)dt,
    phi(t)=sum_(n>=1) [4 pi^2 n^4 exp(9t/2)-6 pi n^2 exp(5t/2)]
                                      exp(-pi n^2 exp(2t)),
    w=phi/Xi(0), H_w=L2(R,w(t)dt),
    Phi(a)=integral_R exp(iat)w(t)dt=Xi(a)/Xi(0),
    sigma^2=integral_R t^2 w(t)dt in (0,infinity).

The completion xi is entire, with xi(0)=xi(1)=1/2. The theta identity and its
normalization are classical and reconstructed in the parent. The weight w is
strictly positive, even, smooth, and has every exponential moment. Its tails and
all their fixed derivatives decrease faster than any exponential.

Put F(t)=integral_(-infinity)^t w, Q=1-F, and

    (Kf)(x)=integral_R [1_(t<x)-Q(t)]f(t)dt,
    T=-K^2 restricted to H_odd.

The displayed integral uses Lebesgue dt, not w(t)dt. The parent proves
||K||_HS^2=integral FQ/w<infinity, (Kf)'=f, and mean_w(Kf)=0. These facts can also
be checked directly: averaging the squared kernel gives FQ/w, while the theta
tails give Q/w=O(exp(-2t)) at +infinity and its reflected bound at -infinity.
Distributional differentiation and the bounded mean functional extend the two
identities from compact inputs to all H_w. Thus K is bounded, and T is compact.

Define q_j=w^(j)/w and

    W_infinity={f in H_w: <q_j,f>=0 for every integer j>=0}.

All q_j belong to H_w. Integration by parts gives K*q_0=0 and
K*q_(j+1)=-q_j, so W_infinity is closed and K-invariant. Parity preserves it.
We do NOT assume completeness of any eigenvector family in W_infinity.

For the arithmetic counting input we import the classical unconditional result
of Bui--Conrey--Young [E1, Theorem 1.1]: the lower limiting proportion of simple
critical-line zeros among all nontrivial zeros is at least 0.4058. Only the
weaker bound 2/5 is used. We also import the classical Riemann--von Mangoldt
asymptotic [E2],

    N(U)=(U/(2pi))log U+O(U).

Here N counts positive ordinates with multiplicity; N_s counts simple zeros on
the critical line. Neither input assumes RH. Neither external proof or numerical
optimization is rerun here. No recent stronger zero-proportion claim is needed.

### 1.1 Every real-zero eigenvector survives the infinite cut

For real gamma !=0, the unique centered antiderivative gives

    K exp(i gamma t)=[exp(i gamma t)-Phi(gamma)]/(i gamma).

If Xi(gamma)=0, therefore

    e_gamma(t)=exp(i gamma t), ||e_gamma||=1,
    K e_gamma=(-i/gamma)e_gamma.                         (1)

For every j, integration by parts, with all endpoint terms zero, yields

    <q_j,e_gamma>=integral w^(j)(t)exp(i gamma t)dt
                  =(-i gamma)^j Phi(gamma)=0.           (2)

Thus e_gamma belongs to W_infinity. The same holds at -gamma, and hence

    s_gamma(t)=sin(gamma t) in W_infinity intersect H_odd,
    T s_gamma=gamma^(-2)s_gamma.                        (3)

These deductions use neither the Fredholm determinant nor a simplicity theorem
for all zeros. Simplicity is used below only to select a known large collection
of distinct real zeros, not to assert that all zeros are simple.

## 2. ZC1: a close pair in every sufficiently large multiplicative height band

From the two arithmetic inputs,

    N_s(4U)-N_s(U)
      >=N_s(4U)-N(U)
      >=(3/5+o(1)) U log U/(2pi)
      >=U log U/(4pi)                                  (4)

for all sufficiently large real U. List these distinct ordinates in (U,4U].
There are at least the number in (4), and their consecutive gaps sum to at most
3U. For large U there are therefore two such ordinates gamma != eta with

    0<Delta=|gamma-eta|<=24pi/log U.                    (5)

The factor two pays the difference between the number of points and gaps.
Their heights both tend to infinity. No explicit initial U is certified. These
are actual simple critical-line zeros, not roots of a surrogate function, a
chosen finite zero table, or an independence model for ordinates.

## 3. ZC2: the sharp two-vector metric bound

Let u,v be independent unit vectors in any complex Hilbert space. Set
c=|<u,v>|<1. Suppose G is bounded, self-adjoint, and

    0<m I<=G<=M I,             <u,Gv>=0.

Then

    cond(G)=||G|| ||G^(-1)|| >=(1+c)/(1-c).             (6)

Proof. Multiply v by a unit scalar so <u,v>=c is real and nonnegative. The
G-orthogonality makes the squared G-norms of u+v and u-v equal. Their original
squared norms are 2(1+c) and 2(1-c). Lower-bound the first G-norm by m times its
norm and upper-bound the second by M times its norm. Optimizing m,M proves (6).
The bound is sharp on this two-dimensional space: assign the reciprocal norm
factors to the orthogonal bisectors u+v and u-v.

If K_Z is the restriction of K to a closed invariant subspace Z, a relation

    K_Z* G+G K_Z=0                                     (7)

makes eigenvectors at distinct imaginary eigenvalues G-orthogonal. Likewise,
T_Z*G=GT_Z makes eigenvectors at distinct real eigenvalues G-orthogonal.
The stars here are the adjoints of the RESTRICTED operators in the inherited
metric, not an unjustified restriction of the full-space adjoint. One obtains
orthogonality directly by evaluating the displayed relations on the two vectors.

For the actual exponential vectors, their overlap is exactly

    <e_gamma,e_eta>=Phi(eta-gamma).

The elementary inequality 1-cos x<=x^2/2 gives

    Phi(Delta)>=1-sigma^2 Delta^2/2.                   (8)

For small nonzero Delta this is positive and strictly below one. Strictness
follows because w is positive on R, so exp(i Delta t) is not constant w-almost
everywhere. Combining (6)--(8), every G obeying (7) on a space containing the
pair satisfies

    cond(G)>=4/(sigma^2 Delta^2)-1.                    (9)

Take the pair in (5). Any such metric that includes all the selected modes
through height 4U must satisfy, for all sufficiently large U,

    cond(G)>=log^2 U/(144pi^2 sigma^2)-1.               (10)

The metric may depend on U. Formula (10) is a lower bound, not a construction or
a sharp asymptotic for an optimal growing metric.

**Conclusion.** No bounded coercive positive G satisfies (7) on W_infinity,
or on any closed K-invariant subspace containing every simple real-zero
eigenvector. In particular it fails already on their closed linear span.
This extends the parent's finite-cut obstruction by a different mechanism:
all vectors used here survive EVERY derivative cut.

## 4. ZC3: the ordinary trace-class operator has the same obstruction

Riemann--Lebesgue applies since w is integrable, so Phi(a)->0 as |a|->infinity.
Consequently

    ||s_gamma||^2=[1-Phi(2gamma)]/2 ->1/2.              (11)

For sufficiently large gamma this norm is at least 1/2 (the norm, not its
square). The mean-value inequality for sine gives

    ||s_gamma-s_eta||<=sigma Delta.

For normalized u_gamma=s_gamma/||s_gamma||, the standard triangle estimate
||a/||a||-b/||b||||<=2||a-b||/min(||a||,||b||) gives

    ||u_gamma-u_eta||<=4sigma Delta,
    <u_gamma,u_eta>>=1-8sigma^2 Delta^2.                (12)

The last inner product is real. At a sufficiently close pair it is positive.
Applying (6) now proves

    cond(G)>=1/(4sigma^2 Delta^2)-1
            >=log^2 U/(2304pi^2 sigma^2)-1             (13)

for a metric satisfying T_Z*G=GT_Z and retaining the two sine eigenvectors.
Thus no bounded positive equivalent metric makes T self-adjoint on
W_infinity intersect H_odd, or even on the closed span of its real sine modes.
The eigenvalues gamma^(-2),eta^(-2) are distinct since both ordinates are positive.
No eigenvector completeness or absence of nonreal eigenvalues is used.

Equations (10),(13) also rule out bounded similarity of the stated restrictions
to normal operators: distinct eigenvectors of a normal operator are orthogonal,
and a bounded similarity would pull that orthogonality back to a coercive G.

## 5. ZC4: even a nonequivalent local finite-measure metric cannot work for K

Let nu be ANY nonzero finite positive Borel measure on R. The exponential
vectors have squared nu-norm nu(R), and

    <e_gamma,e_eta>_(L2(nu))=integral exp(i(eta-gamma)t)dnu(t).

For the pairs in (5), dominated convergence sends this overlap to nu(R)>0.
It cannot be zero at all distinct pairs. Hence no such measure makes all actual
simple real-zero exponentials orthogonal. A common multiplier on the functions
reduces to the same statement with dnu=|h(t)|^2 w(t)dt whenever the resulting
norms are finite and nonzero.

This is stronger than failure of a weight comparable to w: arbitrarily singular
finite positive measures and unbounded density ratios are included. Exponentials
have modulus one, so a local measure giving them finite nonzero norms must in
fact have finite nonzero total mass. A different NONLOCAL Hilbert norm is not
excluded by this argument.

For T the analogous conclusion holds for any nonzero finite positive measure
whose Fourier transform vanishes at infinity, in particular every finite
absolutely continuous reweighting. In that case the squared sine norms tend to nu(R)/2
and their mutual inner product

    Re[nu_hat(eta-gamma)-nu_hat(eta+gamma)]/2

has real part tending to nu(R)/2, not zero. No assertion for arbitrary
infinite-mass measures on the sine space is made.

## 6. ZC5: spectral projection norms must also diverge

If a bounded projection P obeys Pu=u and Pv=0 for unit u,v with real overlap
c>=0, apply it to u-cv. Its squared norm is 1-c^2 and its image is u, so

    ||P||>=1/sqrt(1-c^2).                              (14)

At the two eigenvalues above, the compact-operator Riesz projection has these
actions, both on the full space and on the stated invariant restriction.
Using (8) gives, for the exponential pair,

    ||P_gamma||>=1/(sigma Delta)
                  >=log U/(24pi sigma).               (15)

For the normalized sine pair (12) gives the analogous lower bound

    ||P_gamma^T||>=1/(4sigma Delta)
                    >=log U/(96pi sigma).             (16)

No actual projector has been numerically evaluated. These are analytic lower
bounds on exact projections. They imply that the normalized real eigenvectors
are not a Riesz sequence: their two-by-two Gram minima tend to zero. In
particular they cannot be part of a Riesz basis with fixed basis bounds in
these inherited spaces. This does not rule out non-Riesz completeness, grouping
nearby eigenvalues into blocks, or an unbounded nonlocal metric.

## 7. Consequence for the full proof attempt

The previous global determinant is not contradicted. Nor is positive real
spectrum contradicted. The obstruction uses only actual zeros that are already
known to be real, and would hold just as strongly if RH were true.

The particular proposed ending 'remove all adjoint-chain directions and find a
bounded positive metric on the remainder' is now ruled out, not merely left
unproved. A local reweighting of the same exponential eigenfunctions cannot
repair it. Any successful spectral ending would need a different realization,
a genuinely nonequivalent nonlocal topology with source-complete domain control,
or a spectral-sign argument not based on bounded similarity. None is supplied
here. Simply building a Hilbert space using ONLY real-frequency modes would
omit hypothetical nonreal modes and would not prove the whole determinant's sign.

The new proof does not establish an arithmetic upper bound, a new zero-free
region, or RH. It is not an independent acceptance of the preceding determinant
paper. Reviewers should reconstruct (2), the imported counting scope, (6), and
the sine normalization in (12) before using the infinite-cut conclusion.

## References and exact source

[P] PR #834, centered-theta-determinant/PROOF.md, commit
f0e34780f4fe91bd5d07e791e8855189838c3df5, blob
ef01f74c50d4efacb615176cbfed4a3de2fd1147. Full manuscript read; its boundedness,
centered derivative, eigenvectors, adjoint chain, and named infinite restriction
are the source. Its complete determinant proof is not needed for ZC1--ZC4.

[E1] H. M. Bui, J. B. Conrey, M. P. Young, More than 41% of the zeros of the
zeta function are on the critical line, Acta Arithmetica 150 (2011), 35--64;
arXiv:1002.4127v2, Theorem 1.1 and definitions on PDF page 1.
https://arxiv.org/abs/1002.4127v2
The theorem statement was read, not its complete mollifier proof independently
verified. It is imported as a classical published theorem. No optimal proportion
or post-2011 improvement is needed.

[E2] Classical Riemann--von Mangoldt formula, e.g. E. C. Titchmarsh,
The Theory of the Riemann Zeta-function, second edition, Chapter IX.
Only N(U)~U log U/(2pi) is used. This standard analytic input is not re-proved.

Basic integration by parts, Riemann--Lebesgue, eigenvector orthogonality and
Riesz projection facts are classical. The two-vector estimates used are proved
in full above rather than attributed as a new general theory.
