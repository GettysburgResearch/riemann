# Independent review: uniform effective depth for proper theta quotients

Verdict: **PASS** at exact scientific commit
`a7f9fae13c99d7542c764b777ca0d072f9a5c2c1`, immediate parent
`cec95a2b5e5acf91d0319f94b56fefe4e9fb80ca`.
Review date: 2026-08-31. This reviewer did not author the argument or
participate in its pre-freeze critique. No scientific source was edited.

## 1. Exact identity, parents and primary input

The complete 210-line [uniform-depth proof](PROPER_THETA_SOURCE_UNIFORM_DEPTH_ZEROS.md)
has Git blob `6db3b5d97b3164c2a87a6442fe16ba866b645ae8` and normalized-LF
SHA256 `033a76d069917020be5032c131e8acfbaf571c9d328ec599e1fc41872c229f11`.
The entire parent-to-science delta is that one added Markdown file.

| Imported result | Science | Independent review |
|---|---|---|
| Exact source central criterion | `0d1f90323c8d61abefee077b7bcaa4c024596a55` | `31e5ca265cc3be43cff30962041d93a2be4d8ee2` |
| Elementary effective bounds | `6e47a4b2604668eb88b977c9182f5a04a214638a` | `43c36f4c462bb008d7fb744ca52768d2591b1822` |

Both parent proofs and reviews were fully read in the immediately preceding
reviews and their bytes reauthenticated here. All four commits are ancestors
of this science. The resident LF-normalized identities are:

| File | Normalized-LF SHA256 |
|---|---|
| [TQ proof](PROPER_THETA_SOURCE_REAL_ZERO_COROLLARY.md) | `22cbe2797ac06ae37468e4da93d17b261d99675f50255fd6a2c67bf53ca1f70f` |
| [TQ review](PROPER_THETA_SOURCE_REAL_ZERO_COROLLARY_REVIEW.md) | `c4ae9eef856daf5c4df27d76ebfbc2b17c849ab6e3de03fb50efef96c6862b3b` |
| [E96 proof](PROPER_THETA_SOURCE_EFFECTIVE_WEIGHT96.md) | `a1ce66344ca96dbc828f405adeeb7d0deea73db62a0d7481fcdb1b2ede7a312e` |
| [E96 review](PROPER_THETA_SOURCE_EFFECTIVE_WEIGHT96_REVIEW.md) | `e8305aa28fa2361ad0883a10ea219b94a4974aeb9e73202842165a4030c410d6` |

The genuinely new input is the FULL off-diagonal Petersson formula.
Using the PDF skill, I freshly rendered and personally inspected the
complete printed pages68--69 of
[Iwaniec--Luo--Sarnak, Low lying zeros of families of L-functions](https://www.numdam.org/article/PMIHES_2000__91__55_0.pdf),
especially (2.1)--(2.3), (2.7)--(2.9) and Proposition2.1.
The personally read local PDF has SHA256
`1b4df950ece54ff89f53bcbe50f1cdc00703eed900e7b2df9df3d2634fb43d3e`.
This is an analytic primary-source check, not an assertion that an offline
Git checker authenticates the current remote PDF or its whole contents.
No RH-dependent part of that paper is imported.

## 2. Off-diagonal normalization and conjugations

The printed (2.1) is linear in its first argument, whereas the repository's
G is conjugate-linear first. Printed (2.3) is
psi_f(m)=sqrt(A_m)*a_f(m)/||f||, and (2.7) is
Delta(m,n)=sum_f conjugate(psi_f(m))*psi_f(n).
The factors A_m and the order of the conjugations must be retained.

To reconstruct the conversion independently, choose a G-orthonormal basis
e_l of the actual cusp space. The reproducing identity gives
G(v_m,e_l)=sqrt(A_m)*a_(e_l)(m), so

    v_m=sum_l conjugate(psi_(e_l)(m))*e_l,
    G(v_m,v_n)=sum_l psi_(e_l)(m)*conjugate(psi_(e_l)(n))
              =Delta(n,m).

At level one with trivial character the sum (2.9) is real by replacing
each unit with its negative, and symmetric in m,n by replacing it with
its inverse. The factor i^k is real for even k. Therefore Delta(n,m)
equals Delta(m,n) here, exactly as U2 states. This reality argument is
not silently extended to general characters or levels.

Proposition2.1 has factor2pi*i^k, argument4pi*sqrt(m*n)/c and the
condition c=0 modulo N. For N=1 this is the entire positive-c sum.
Equivalently a_(P_n)(m)=(m/n)^(nu/2)Delta(n,m), which cancels the
factor sqrt(A_m/A_n) in G(P_m,P_n)/sqrt(A_m*A_n).
The normalization is correct off the diagonal, not merely for m=n.
No Hecke eigenbasis or Euclidean coefficient metric has been substituted.

## 3. The whole growing coefficient block stays controlled

The absolute defining Bessel series gives
|J_nu(x)|<=(x/2)^nu/nu!*exp(x^2/(4(nu+1))) for positive real x.
For every m,n<=j, the trivial Kloosterman bound and
sum_(c>=1)c^(-nu)<=2 give U3, including the complete tail.
Here nu=k-1>=95j>=95 lies safely in the convergence domain.

For the Hermitian error E=K-I,
|u*E*u|<=max|E_mn|*(sum|u_m|)^2<=j*max|E_mn|*||u||^2.
Thus the extra factor j in the operator bound pays the whole block.
A bound only on the diagonal would not justify the next argument.

The condition k>=96j gives
4pi^2*j^2/k<(121/294)j<j. Its exponential is bounded by e^j<3^j;
it is NOT replaced by a constant. Also, integrating log t from1 to nu
gives log(nu!)>=nu*log(nu)-nu+1, and hence
nu!>(nu/e)^nu>(nu/3)^nu. Consequently

    delta<13*j*3^j*(21*j/nu)^nu
          <=13*j*3^j*(21/95)^nu
           <13*j*4^(j-nu)<=13*j*4^(-94j).

Every inequality is uniform in BOTH j and k in the stated range.
The exact base13000<4^94 and the ratio
(j+1)/(j*4^94)<=2/4^94<1 prove delta<1/1000 for all j>=1.
This is an all-integer proof, not a sampled block-size experiment.
The positive lower bound K>=(1-delta)I proves independence of the
first j coefficient functionals.

## 4. All coefficient constraints and the exact quotient vacuum

The conditions a_f(m)=0 for m<j and a_f(j)=1 become
G(v_m,f)=c_m with c=sqrt(A_j)e_j. The least-norm vector is in the
span of the v_m: an orthogonal component changes none of these
coefficients and only adds to the squared Petersson norm.
For f=sum_n v_n alpha_n the equations are K alpha=c. Therefore

    min G[f]=c* K^(-1)c=A_j*(K^(-1))_jj<=A_j/(1-delta).

The order and conjugations in this matrix expression are correct.
For j>1 the diagonal shortcut A_j/a_(P_j)(j) would omit the earlier
constraints and is not used. This minimum is over the whole cusp
space, not a chosen finite Fourier prefix or restricted collection
of lifts. Nor is its minimizing vector asserted to minimize H(t).

The classical level-one dimension bound gives
dim S_k>=floor(k/12)-1>=8j-1>=j+1 for every allowed pair.
Together with independence this yields dim V=dim S_k-j+1 and
dim W=dim S_k-j>=1. Thus the quotient is genuinely proper throughout
the entire region, including the even-weight class2 modulo12.

## 5. Uniform source ratio without an asymptotic onset

TQ's Poisson/Parseval bound holds for every admissible lift at each
depth, with no fixed-depth constant. Hence H_(Q,j)(t)>=J_(k,j)/sqrt(t)
remains valid here. The old fixed-j norm asymptotic is not imported.
The omitted interval (0,1) in J is less than1/(nu+1/2), independently
of j, so U6 has the correct subtraction after dividing by A_j.

Since 4pi<13 and nu>=95j, the explicit factorial estimate gives

    A_j> (nu/(39j))^nu/nu >= (95/39)^nu/nu >2^nu/nu>1000.

The last inequality follows from2^95>95000 and the successive ratio
2nu/(nu+1)>1. Thus the omitted contribution is less than1/1000
uniformly, with no unknown Gamma or cusp-tail threshold.

Integral Cauchy--Schwarz gives the exact lower bound
Gamma(nu+1/2)/Gamma(nu)>=nu/sqrt(nu+1/2).
The function x^2/(x+1/2) is increasing for x>0, and
j/(95j+1/2)>=1/(95+1/2) for j>=1. These prove U8 in both variables.
Combining4pi<88/7 with the rational base case E9 gives uniformly
J_(k,j)/A_j>2739/1000. Thus

    J_(k,j)/G_(Q,j)> (999/1000)*(2739/1000)
                   =2736261/1000000>273/100>e.

Independent standard-library integer/Fraction checks, with no author-code
imports, passed normally and under Python -O. Fourteen transient guards
verified the integer bases, rational constants and monotonicity bases.
In particular:

| Independent exact check | Result |
|---|---|
| 4^94-13000 | `392318858461667547739736838950479151006397215279002144056 > 0` |
| 2^95-95000 | `39614081257132168796771880168 > 0` |
| E9 squared-bound reserve | `25353/2626250 > 0` |
| Final R floor minus273/100 | `6261/1000000 > 0` |

The signs for all larger indices were proved above, not inferred from
those finite checks. The complete exponential-series estimate
e<=11743/4320<273/100 retains its geometric infinite tail.
No central values, Bessel values, Gamma values or zeros were sampled.

## 6. Accepted conclusion and exact boundary

For EVERY integer j>=1 and EVERY even k>=96j, the proper native
theta-source quotient at depth j has positive central value. TQ's
endpoint residue, real analyticity and reflection give a reflected
sign-changing real zero pair, of odd order for at least one such pair.
Multiplication by s(s-1) preserves the zeros. The MP completion is
applied separately to each actual finite-dimensional source; no uniform
analytic-continuation bound across all dimensions is needed or asserted.

Different j mean DIFFERENT quotient objects. This does not count many
distinct pairs in Q_1, cover depths near k/12, supply an all-zero census,
prove simplicity or uniqueness, locate zeros on a12j/k scale, optimize96,
or settle weight24. No Euler product, preferred Hecke-stable operation,
new automorphic representation, RH or GRH conclusion follows.

This is an analytic-only review with finite checks of its elementary
constants, not a new computational module or zero-location certificate.
The37-module G suite was not rerun for this note and its denominator
does not increase. The review adds one Markdown file; source, programme
fronts, tests, producers, remote refs, PRs and main remain untouched.
No mathematical repair is required at the reviewed scientific identity.
