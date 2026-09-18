# 03 — A pole-canceling arithmetic upper bound and finite certificates

Source U3/A3, with the computational continuation from U4/A4. The analytic
upper-bound proof is reproduced; the limit E_N->0 is not proved. [BSY13], [B18],
[DH20], [B01], [BCF12] are identified in [SOURCES](SOURCES.md).

## The Hilbert-space approximation

Let b_n(k)={k/n} and w_k=1/[k(k+1)]. The target 1 has squared norm 1. Set

$$
G_{mn}=\sum_{k\ge1}w_k b_m(k)b_n(k),\quad v_n=\log n/n,
\quad E_N=\min_c\|1-\sum_{n=2}^N c_n b_n\|^2.
$$

Summation by parts gives <1,b_n>=v_n. Linear independence (also proved later by
finite-support duals) yields

$$
c_N=G_N^{-1}v,\qquad E_N=1-v^TG_N^{-1}v.
$$

This is a classical Nyman--Beurling--Baez-Duarte space, not a new RH criterion.
The conversation's concrete bridge is

$$
0\le\mathcal D\le\tfrac12\log\frac{c^TG_Nc}{|c^Tv|^2},\qquad c^Tv\ne0,
$$
$$
\boxed{0\le\mathcal D\le-\tfrac12\log(1-E_N).}
$$

## Proof with the pole and Jensen direction retained

For real finite c put P_c(s)=sum c_n(1/n-n^{-s}). Then P_c(1)=0 and
P_c'(1)=c^Tv. Extend A_c(k)=sum c_n b_n(k) to

    A_c(x)=sum c_n({x/n}-{x}/n).

It is zero below 1 and constant on [k,k+1). Floor-function summation gives

$$
\int_0^\infty A_c(x)x^{-s-1}dx=\zeta(s)P_c(s)/s.
$$

Prove first for Re(s)>1, then continue to Re(s)>0. The zeta pole has already
been canceled. Mellin Plancherel at Re(s)=1/2 gives

$$
\int|\zeta P_c|^2d\mu=c^TG_Nc,
\quad d\mu=dt/[2\pi(1/4+t^2)].
$$

The bounded analytic function H_c=P_c/(s-1) on Re(s)>1/2 has H_c(1)=c^Tv.
Poisson--Jensen, with zeros allowed, yields

$$
\int\log|H_c(1/2+it)|d\mu\ge\log|c^Tv|.
$$

Since integral log|-1/2+it| dmu=0, the same lower bound holds for log|P_c|.
Concavity of log gives integral log|zeta P_c| dmu <= (1/2)log(c^TGc).
Subtract the LOWER bound for log|P_c| to prove the upper bound for D. The
argument does not assume P_c is zero-free. For c=G^{-1}v, both c^TGc and c^Tv
equal 1-E_N; optimization gives the boxed result.

## Exact finite Gram evaluation

For L=lcm(m,n), periodic grouping gives

$$
G_{mn}=\frac1L\sum_{r=1}^L\{r/m\}\{r/n\}
\left[\psi_\Gamma((r+1)/L)-\psi_\Gamma(r/L)\right].
$$

This is a finite expression for an infinite sum. The first program enclosed
digamma at positive rational arguments by shifting by 20, using six Bernoulli
terms, and bounding the remainder by the first neglected term [DLMF5]. At N=20
it used exact rational coefficients, not a trusted floating inverse.

The later Vasyunin implementation uses, for coprime a,b,

$$
W(a,b)=\sum_{r=1}^{b-1}\{ar/b\}\cot(\pi r/b),\qquad W(a,1)=0.
$$

For g=gcd(m,n), a=m/g, b=n/g set

$$
R(m,n)=\frac{(m-n)\log(n/m)-\pi g(W(a,b)+W(b,a))}{2mn}.
$$

Then G_mn=R(m,n)-R(m,1)/n-R(1,n)/m. The universal constant in the classical
Vasyunin formula [DH20] cancels. Pairing terms and reusing gcd reductions yields
O(N^3) construction and O(N^2) storage. The suggested continued-fraction
O(log)-per-entry algorithm was NOT implemented. Neither 10^4 nor 10^5 was
certified. Dense solution cost remains an independent limitation.

## Historical numerical evidence, with its scope

| N | E_N (rounded) | Upper bound on D | Original arithmetic status |
|---|---:|---:|---|
| 5 | 0.036319018 | 0.018497485 | floating exploration |
| 20 | 0.016538252 | <0.00834 | fixed rational witness, directed interval |
| 40 | 0.012735835 | 0.006408816 | floating exploration |
| 80 | 0.010998796 | 0.005529865 | floating exploration |
| 200 | 0.008930778 | 0.004485448 | floating exploration |
| 256 | 0.008242256028257 | <0.00413821 | rational witness and optimum enclosure |
| 512 | 0.007393375337423 | <0.00371043 | rational witness and optimum enclosure |
| 1024 | 0.006534086495726 | <0.00327777 | rational witness and optimum enclosure |
| 2048 | 0.006111155075890 | not certified | floating exploration only |

The N=1024 retained interval is

    0.006534086495725705071841363599716880944407944913131916253
       <= E_1024 <=
    0.006534086495725705613429979556136169459741919053533166175.

The retained bound is D<0.00327777, not D approximately equal to that number.
These are not world-record claims or independent zero-free results. The
certificates' precise numerical meaning, implementations and historical runtime
fields are preserved in the source archive. Fresh replay is listed separately
in VALIDATION; a retained record is not a newly executed calculation.

For a rational candidate ctilde, define

    F=1-2v^T ctilde+ctilde^T G ctilde, d=v-G ctilde.

Completing the square gives F-E_N=d^TG^{-1}d. The coefficient estimates in
Chapter 04 imply G>=I/(6N^3), so F-6N^3||d||^2<=E_N<=F. This certifies the
optimum from an interval matrix-vector residual without an interval inverse.
The initial floating solver only proposes a witness; it is not trusted for the
bound's acceptance.

## The scale identity and the first overly strong target

Partition the next Gram matrix as [[G,B],[B^T,C]] and the source as (v,w).
With S=C-B^TG^{-1}B and r=w-B^TG^{-1}v,

$$
E_N-E_{2N}=r^TS^{-1}r.
$$

The initial proposed sufficient estimate was

    r^TS^{-1}r >= c E_N^2/(1+log N).

On dyadic N it would give E_N<<1/log log N and hence RH. It was NOT proved.
The user's next turn correctly weakened it; Chapter 04 records that improvement
and why a generic projection argument still cannot establish the lower gain.

Burnol's lower bound for the larger standard approximation class applies to
this subclass in the correct direction. A fixed-factor dyadic contraction of
E_N would imply power decay and contradict the positive 1/log N lower scale
[B01]. The benchmark 2+gamma_E-log(4*pi)~0.0461914179 is not an established limit
for this constrained E_N. The sharp result [BCF12] is conditional on RH and an
extra reciprocal-derivative bound. Finite values below the constant do not
contradict an asymptotic liminf theorem.
