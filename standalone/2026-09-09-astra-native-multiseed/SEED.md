# Exact arithmetic seed and complete numerical contract

Status: one specified seed is certified by bounded computation plus the explicit
analytic tail theorem below. The domain and feedback theorems are paper proofs.
The coefficients are extracted from the unpublished NJP26 handoff, not invented
from its printed decimal energy. That whole old package is NOT represented as
published by this extraction. Its one seed is fully specified and freshly replayed.

## 1. Literal coefficients and exact normalization

Let q(s)=sum_(n=1)^16 A_n n^-s / D, D=562949953421312. In increasing n order,

    A=(562949953421312,-562949953421312,-532205406349296,
       -58291156654044,-441882648513420,328445548501212,
       -366102615428543,18872698772432,-57317966477307,
       250457476590930,-252425357406167,20023818681228,
       -248939343231540,204789481170078,157840018622805,
       -149164455120992).

Exactly q[1]=1, q[2]=-1, q(1)=0 and q(0)=-2. Put

    delta=1+sum_(n=1)^16 A_n log(n)/(D n),
    s0(s)=q(s)+(2delta/log2)3^(1-s)(1-2^(1-s))(1-2^-s).

The added terms have coefficients (6,-18,12)delta/log2 at indices3,6,12.
They have value zero at0 and1 and derivative delta at1. Thus s0'(1)=1.
These coefficients are exact REAL logarithmic values, not rational numbers.

The checker encloses delta/log2 by directed rational intervals, using100
terms of the reduced atanh series for each log and its complete positive
remainder. It selects a rational c=k/[D 2^64] within a specified distance.
Replace delta/log2 by c to get s_tilde. Both s_tilde and s0 are balanced
and centered; only the exact s0 has the exact derivative normalization.

The profile of 3^(1-s)(1-2^(1-s))(1-2^-s) is

    3[floor(x/3)-3floor(x/6)+2floor(x/12)].

The bracket has period12 in x and four unit-in-x/3 cell values0,1,-1,0.
It is zero below3 and has absolute value at most1. Therefore the full
output-norm difference is at most6|c-delta/log2|; the checker calls this
upper bound eta. No numerical derivative equality is accepted in place of
the exact formula for s0. If E(s_tilde)<1, enlarge its energy interval by
2eta+eta^2 to obtain an enclosure for E(s0).

## 2. Complete infinite future of a rational balanced polynomial

For rational a_n=A_n/D, support<=N, balance sum a_n/n=0, let

    u(j)=1-sum a_n floor(j/n),
    V=|1+(sum a_n)/2|^2
                  +(1/12)sum_(m,n<=N) a_m a_n gcd(m,n)^2/(mn),
    C_N=N^2(1+2ceil(log2 N)).

Then for any integer H>=1,

    |E- sum_(j=1)^(H-1) u(j)^2/[j(j+1)]-V/H|
                              <= C_N V/[H(H+1)].          (S1)

This is RC1 from the pinned #803 rational-residual capture, reconstructed
here to state the complete coverage. It is not claimed as a new norm formula.

Proof. Balance makes u periodic with any common multiple of1,...,N.
For uniform integer j over a full period,

    mean{j/n}=(n-1)/(2n),
    Cov({j/m},{j/n})=[gcd(m,n)^2-1]/(12mn).

Condition on j modulo gcd(m,n); the remaining two coprime residues are
independent by finite CRT. The variance of the shared residue proves the
covariance formula. Balance cancels its rank-one minus1 term. Thus V is the
EXACT full-period mean square, including the coherent term.

The periodic u is a finite Fourier sum over reduced rational frequencies
with denominators<=N, including zero. Combine equal frequencies first.
Their separation on the circle is at least1/N^2, and their number is at
mostN^2. Parseval identifies the sum of squared Fourier coefficients with V.
For two distinct frequencies, a geometric sum on ANY interval is bounded
by1/[2||theta-phi||]. Ordering neighbors clockwise/counterclockwise bounds
the absolute off-diagonal row sum by N^2 H_(N^2-1)<=C_N. Consequently

    |sum_(j=M)^(M+L-1) u(j)^2 - L V|<=C_N V

for every M,L, independently of the potentially enormous common period.
Abel summation with decreasing weights1/[j(j+1)] now proves(S1); its entire
mean tail is V/H and its entire discrepancy radius is as displayed. QED.

## 3. What is executed

For s_tilde, N=16 and H=2^20. At EVERY one of the1,048,575 integer cells the
new code evaluates u(j) directly from all16 floor terms. It uses integer
numerators and denominator D 2^64; each squared cell contribution is rounded
outward to128-bit dyadic endpoints by integer division. This differs from
NJP26's running divisor-event accumulation. The period mean is reconstructed
by the full pairwise gcd formula rather than its Jordan divisor-loop formula.
The same analytic tail theorem is shared, so this is not an independent
mathematical proof of RC1 or an independent human referee.

The full result after coefficient-interval correction is

    0.019530763932 < E(s0) < 0.019530764725 <49/2500.

Exact retained endpoints, the rationalized coefficient, period mean and tail
radius are in result.json. No future period is enumerated or set to zero.
The new three seeds are s0 and its two explicit perturbations from PROOF.md.
Their FULL errors are below (7/50+1/2048)^2<1/50 by that analytic norm bound.
No optimizer or root list defines them. The previous six larger-prefix trial
certificates were NOT rerun here, and their full handoff is not silently copied.
