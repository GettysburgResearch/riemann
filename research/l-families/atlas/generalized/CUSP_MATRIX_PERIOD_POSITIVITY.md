# What positivity survives upstairs in the completed period matrix?

Status: PROPOSED SOURCE-EXACT MATRIX/THETA-FLAG THEOREMS; review pending.
Base: `ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf`.
Scope: the actual completed Eisenstein period of a fixed finite-dimensional
cusp-form space; its native positive feature kernel and real-axis variance.
No new motive, RH/GRH, purity theorem, or canonical Hecke flag is claimed.

The target is to construct the positive kernel I(z+conjugate(w)) directly
from the unfolded period measure, and distinguish it from pointwise complex
positivity, a Herglotz function, and the proposed fixed-J scattering identity.
The full period matrix is retained; scalar Schur quotients are not substituted
for its source. The expected no-go statements concern this EXACT unrenormalized
matrix, not every possible normalization, scattering construction, or variable.

Preregistered bounded controls, before computation:

- Independently reconstruct the actual weight24 Miller-basis first four
  q rows and the stacked coefficient/logarithmic-frequency determinant.
  The predicted determinant is L2[211312800 L3+1159692288(L3-L2)], positive
  when L3>L2>0. No floating logarithm acceptance.
- For the fixed synthetic positive three-atom matrix
  D(q)=[[1+q,q],[q,q+q^2]], its Schur quotient is1+q^2/(1+q).
  Evaluate EVERY signed derivative (q d/dq)^r for1<=r<=16 at EACH
  q in{1/3,1/2,2/3}. Record every result, including failures of complete
  monotonicity, and do not extend the order/point grid after seeing it.
- Check the exact block-moment/variance identities on three declared
  rational-frequency feature systems, with Gaussian-rational changes of
  basis. Positive finite Gram controls authenticate their algebra, not an
  infinite period, gamma phase, or analytic continuation.

The three finite feature systems are fixed as follows (rows, frequencies,
positive weights, and invertible complex basis matrix):

1. Rows (1,0),(1,1),(0,1); frequencies0,1,2; weights1,1/2,1/4;
   basis matrix [[1,i],[0,1]].
2. The four literal (g,b) coefficient rows at n=1,2,3,4; frequencies1,2,3,4
   (declared rational proxies, NOT logarithms); weights n^-25;
   basis matrix [[1,1+i],[i,2]].
3. Rows (1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,-1,2);
   frequencies0,1/2,1,3/2,2; weights1,1/3,1/9,1/27,1/81;
   basis matrix [[1,i,0],[0,1,1],[1,0,1]].

Classical feature-kernel, matrix-variance, Schur-complement, Stirling, and
modular-form inputs will be credited. Analytic quantifiers require the
written proofs and subsequent independent exact-SHA review.

Constructive extension, recorded after the first derivative scout and before
its new matrix controls: retain the Petersson vacuum term at the theta-density
level, take a quotient metric there, subtract its quotient vacuum, and only
then take Mellin transforms. Test all three declared positive feature matrices
at t=3/2,2,5, with every nontrivial coordinate flag. Check reciprocal scaling,
positive quotient-vacuum difference, and congruence under a fixed lower block
triangular change of basis preserving the flag. These are algebra controls,
not evaluations of an actual modular theta integral.
For quotient dimension r=d-dim(W), that additional change of basis starts
with I_d and sets A00=1+i, A_(d-1,d-1)=2, A_(d-1,0)=1/2+i; if r>=2,
also A01=i. Its upper-right flag block is zero and its determinant is nonzero.

An additional post-scout countertest used the already declared q values
1/3,1/2,2/3 in the3x3 kernel of the synthetic Schur quotient. Its negative
determinant is recorded below as a discovered witness, not a held-out prediction.

## 1. The actual positive theta source, before taking a period

Let V be a nonzero finite-dimensional subspace of level-one holomorphic
weight-k cusp forms, k fixed. The Petersson Hermitian form is G>0, with
conjugate-linear first input. All quotient spaces and flags below are fixed
independently of the Mellin parameter. For z=x+iy in the upper half-plane,
put

    Theta_z(t)=sum_(m,n in Z) exp[-pi t |mz+n|^2/y],   t>0,
    B(t)(f,g)=1/2 integral_(Gamma\H) y^k bar(f(z))g(z)
                                      [Theta_z(t)-1] dmu(z).      (MP1)

This is a matrix of source forms, not a scalar factor fitted after taking
traces. The covolume-one lattice ((mx+n)/sqrt(y),m sqrt(y)) is self-dual
up to a right-angle rotation; Poisson summation of the two-dimensional
Gaussian gives

    Theta_z(t)=t^-1 Theta_z(1/t).                                 (MP2)

The lattice rotation under modular changes of z also shows that the source
integral is intrinsic on Gamma\H. The normalization is precisely
[Zagier, equations(2),(4),(6),(7), printed pp275--277](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf):

    E*(z,s)=1/2 integral_0^infinity [Theta_z(t)-1] t^(s-1)dt.

Thus the source-pinned completed Eisenstein period is

    I(s)=integral_0^infinity B(t)t^(s-1)dt,      Re s>1.            (MP3)

Cusp decay makes MP1 finite for every t>0: the lattice theta sum is bounded
by a fixed-t polynomial in y in the cusp, while cusp forms decay exponentially.
The same statement holds locally uniformly in t. Positivity and Tonelli prove
MP3 on real s>1; polarization and absolute domination extend it to Re s>1.
The needed absolute convergence is also the frozen period-parent unfolding.

For every t>0, B(t)>0: Theta_z(t)-1 is strictly positive and a nonzero cusp
form is not zero almost everywhere. B(t) decreases in the Loewner order as
t increases. Its positive moments MP3 imply rapid decay at infinity:
for every A>1, integrating tr B(u)u^(A-1) on[t/2,t] gives
tr B(t)<=C_A t^-A. Hence B(t)=O_A(t^-A) for every A. This is an all-A
analytic argument, not a finite theta cutoff.

Poisson summation, integrated BEFORE any quotient, gives the affine identity

    B(t)=t^-1 B(1/t)+(t^-1-1)G/2.                                (MP4)

Consequently H(t)=G+2B(t)>G has the homogeneous law

    H(t)=t^-1 H(1/t).                                           (MP5)

The Petersson identity/vacuum term in H is essential. Schur-complementing
B alone does not turn its additive G correction into a homogeneous law.

## 2. A new completed theta-source flag family

Fix a subspace W of V, with0<=dim W<dim V. For a positive form A on V,
write A/W for its quotient form on V/W:

    (A/W)([v],[v])=min_(w in W) A(v+w,v+w).

This is an intrinsic quotient metric, independent of lifts or basis, with
the polarization of the displayed quadratic form. It is homogeneous under
positive scalar multiplication and monotone in A. Define

    G_Q=G/W,
    C_W(t)=1/2[H(t)/W-G_Q].                                    (MP6)

**Theorem MP1 (theta-source flag completion).** C_W(t)>0 for every t>0,
decays faster than every inverse power as t->infinity, and

    C_W(t)=t^-1 C_W(1/t)+(t^-1-1)G_Q/2.                         (MP7)

Its Mellin transform, initially on Re s>1,

    L_W(s)=integral_0^infinity C_W(t)t^(s-1)dt,                  (MP8)

has meromorphic continuation to all C with ONLY simple poles0 and1,
residues respectively-G_Q/2 and+G_Q/2, and

    L_W(s)=L_W(1-s),      L_W(bar s)=L_W(s)*.                    (MP9)

In particular s(s-1)L_W(s) is an entire matrix-valued family with the same
reflection; at0 and1 its value isG_Q/2, so these poles do not cancel.
There is NO claimed critical-line theorem for its zeros.

Proof. Use a G-orthonormal decomposition V=W^perp plus W and put
R(t)=2G^(-1/2)B(t)G^(-1/2)>0. In these coordinates,

    2C_W=R11-R12(I+R22)^(-1)R21.                               (MP10)

Equivalently, for a quotient vector c,

    2C_W[c]=min_u { R[(c,u)]+||u||^2 }.                         (MP11)

This is a source-level variational principle with a fixed Petersson penalty.
Since I+R> I, its quotient exceeds I strictly. Choosing u=0 gives
0<2C_W<=R11, which pays rapid decay by MP1. Homogeneity of quotient forms
applied to MP5 gives MP7 with no commutation assumption. Splitting MP8 at1,
substituting u=1/t in the lower half, and using MP7 gives exactly

    L_W(s)=G_Q/[2s(s-1)]
            + integral_1^infinity [t^(s-1)+t^(-s)] C_W(t)dt.     (MP12)

Rapid decay makes the second term entire, locally uniformly in s, and the
formula proves the continuation, reflection and residues. The positive
real-axis form and Schwarz symmetry follow from the Hermitian density.
All operations are source-specified before the scalar/matrix Mellin transform.

For W=0 this recovers the original I(s). For a proper nonzero W it is a
different construction from the meromorphic period quotient I(s)/W.
One must not move Schur elimination through the integral, discard G before
the quotient, or subtract a divergent Mellin transform of G separately.
The cancellation in MP6 is pointwise and MP12 pays it at the endpoints.

Canonicity is relative to the declared modular source V, its Petersson form,
and its flag W. The theorem selects neither a preferred W nor an automorphic
representation. No Euler product, ordinary Dirichlet series, motive, number-field
category, or exhaustive novelty claim is supplied. MP8--MP12 constitute an
honest globally completed positive-source family even without those additions.

## 3. Positive kernels and the distinction from period-side quotients

For Omega={z:Re z>1/2}, both

    K_I(z,w)=I(z+bar w),    K_W(z,w)=L_W(z+bar w)                (MP13)

are positive-definite matrix kernels. For any finite z_j and quotient
vectors v_j, their quadratic sum is the integral of a positive quadratic
form of sum_j t^(bar z_j)v_j against B(t) or C_W(t). Cauchy--Schwarz and
MP3/MP8 ensure convergence. These are canonical Mellin feature kernels.
This is classical feature-kernel positivity, not pointwise positivity at
nonreal arguments. It is compatible with zeros of individual scalar entries.

The original weight24 canonical period Schur quotient has, by frozen FI,
genuine poles in Re s>1. Therefore it cannot itself define a positive kernel
Q_period(z+bar w) on this whole Omega. To see the precise obstruction, near
a pole s=a+ib with a>1 use z=a/2+ib/2 and w=a/2-ib/2. Both diagonal entries
would be Q_period(a)>0 and finite, whereas their off-diagonal entry becomes
unbounded. The2x2 kernel Cauchy--Schwarz inequality is violated nearby.
The new theta-source flag L_W has no such interior poles. Thus the two
operations provably differ for the same canonical weight24 flag; this is
not merely an algebraic possibility in a synthetic matrix.

In G-orthonormal coordinates, MP10 also gives for real sigma>1

    0<L_W(sigma)<=I11(sigma),
    I11(sigma)-L_W(sigma)
      =1/2 integral_0^infinity R12(t)(I+R22(t))^(-1)R21(t)
                                                t^(sigma-1)dt. (MP14)

For weight24 and any line W, this inequality is strict. Otherwise the
nonnegative integral vanishes, so the cross theta density is identically
zero, hence the cross period is identically zero in one fixed basis.
The source-pinned first three Fourier directions rule out such a constant
diagonalizing congruence (RQ parent, section4). This proves the construction
is not simply the period of one fixed orthogonal lift.

## 4. Native matrix variance: real positivity that actually holds

For a positive matrix Mellin density M(t), all logarithmic moments at a real
sigma inside its convergence domain exist, because powers of|log t| are
bounded by a constant times t^epsilon+t^-epsilon. The block Gram integral gives

    [[J(sigma),J'(sigma)],[J'(sigma),J''(sigma)]] >=0,
    J''-J'J^(-1)J' >=0.                                      (MP15)

For J=I and J=L_W this last inequality is STRICTLY positive definite.
Indeed equality on a nonzero vector would require (log t)v=u for a fixed
vector u for almost every t with respect to an everywhere positive-definite
density. This is impossible on a positive interval of t. This is the
classical matrix moment/variance identity, with a native continuous source.
It is not a purity criterion.

The uncompleted Dirichlet Gram

    D(s)=sum_n a(n)*a(n)n^(-s-k+1)

also has (-1)^r D^(r)(sigma)>=0 for every r>=0, sigma>1, and the analogous
variance inequality. Its positive atomic frequencies are log n, rather than
the bilateral Mellin frequencies log t of the completed matrices.

For the actual weight24 Miller basis(g,b), the first four coefficient rows
are (1,0),(0,1),(195660,-48),(12080128,1080). Stack each row a(n) beside
(log n)a(n). With L2=log2 and L3=log3, its determinant is

    L2[211312800 L3+1159692288(L3-L2)]>0.                       (MP16)

Thus even the uncompleted D has STRICT positive variance throughout the
real half-line sigma>1. The determinant proof uses log3>log2>0, not rounded
logarithms. No finite coefficient test is being extrapolated: these four
rows alone make a positive sub-Gram of the full convergent positive sum.

## 5. Two tempting matrix properties that the literal period does not have

**Theorem MP2 (fixed-J firewall).** No nonzero constant matrix J satisfies

    I(s)* J I(1-bar s)=J                                     (MP17)

for all s in a domain containing the real half-line s>1. This includes
indefinite and singular J. It does NOT exclude a changed normalization,
an s-dependent metric, a boundary-only identity, or a different scattering
matrix constructed from the source.

For real sigma, reflection and Hermitian positivity reduce MP17 to
I(sigma)J I(sigma)=J. Choose finitely many Fourier rows spanning V, with
indices<=N. Then D(sigma)>=N^(-sigma)D0 for a fixed D0>0.
The gamma factor is

    A_k(s)=pi^(-s)Gamma(s)(4pi)^(-s-k+1)Gamma(s+k-1),
    I(s)=A_k(s)zeta(2s)D(s).

Stirling gives A_k(sigma)N^(-sigma)->infinity, so the least eigenvalue of
I(sigma) tends to infinity. But MP17 would give
||J||<=||I(sigma)^(-1)||^2||J||, forcing J=0 for large sigma.

**Theorem MP3 (Herglotz/positive-real firewall).** The same literal I(s)
is neither a Herglotz matrix function nor its negative on the upper half-plane,
and is not a positive-real matrix function on Re s>1. More concretely, each
nonzero scalar compression takes both signs of its real part and both signs
of its imaginary part infinitely often on some fixed line sigma0+it, t>0.

For a nonzero f, let n0 be its first nonzero Fourier index. Absolute Dirichlet
convergence supplies a sufficiently large fixed sigma0 with

    I(s)(f,f)=c A_k(s)n0^(-s)[1+r(s)],  |r(s)|<1/2,
    c=|a_f(n0)|^2 n0^(-k+1)>0,     Re s=sigma0.

This includes the zeta(2s) factor: both it and the normalized Dirichlet tail
tend uniformly to1 and0, respectively, as sigma0 increases. The continuous
phase theta(t)=arg[A_k(sigma0+it)n0^(-it)] has

    theta'(t)=Re psi(sigma0+it)+Re psi(sigma0+k-1+it)
                  -log(4pi^2 n0)=2log t-log(4pi^2 n0)+o(1).

It is eventually increasing and unbounded. At its successive multiples of
pi/2, the indicated real or imaginary part has the alternating sign of
Re[1+r]>1/2. This proves the claim. The only imported asymptotic is the
classical [Gamma/digamma expansion](https://dlmf.nist.gov/5.11).
It is fully compatible with the positive kernels MP13: these are different
mathematical properties.

## 6. Exact finite counterfeits for decategorifying too early

With q=2^(-s), the three positive coefficient atoms give

    D(q)=[[1+q,q],[q,q+q^2]],
    F(q)=Schur D(q)=1+q^2/(1+q).

The full matrix has a positive Dirichlet feature source. Yet at q=1/3

    (q d/dq)^7 F=-3311/12288<0,                               (MP18)

so its scalar Schur quotient is not completely monotone on s>1. The factor
(log2)^7 in the signed s derivative is positive and does not change the sign.
The complete declared48 derivative values are retained, not only this witness.

Worse, taking q_i=1/3,1/2,2/3, the scalar pointwise-quotient kernel is

    [F(q_i q_j)]=[[91/90,43/42,103/99],
                  [43/42,21/20,13/12],
                  [103/99,13/12,133/117]],
    determinant=-81/8808800<0.                               (MP19)

All corresponding z_i=-log(q_i)/log2 lie in Re z_i>1/2. This exact witness
shows why a pointwise Schur operation on an already transformed positive
kernel is not the source-level quotient construction in MP6. It is not an
RH counterexample or an actual modular specialization.

## 7. Scientific boundary

The constructive output is MP6--MP12: a Petersson-polarized theta-source
flag family with a complete global continuation, reflection, positive Mellin
kernel and only the forced endpoint poles. It is not merely a meromorphic
quotient of entries after transformation. The old period-side quotients and
their genuine off-central poles remain intact and distinct.

The variance and kernel identities explain the precise positivity available;
the fixed-J and Herglotz tests prevent strengthening it silently. None of
these statements controls the nontrivial zeros of the new family. Its Euler
and archimedean categorical interpretation, any critical-line criterion,
and an independently motivated selection of flag remain open. Classical
Poisson, Mellin, quotient-metric and positive-kernel tools are credited;
external priority has not been exhaustively researched.
