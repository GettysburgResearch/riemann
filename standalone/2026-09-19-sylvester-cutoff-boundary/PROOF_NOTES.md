# SBC26: the actual boundary operator, its covariance, and a native obstruction

Status: proposed component proofs for independent review. These arguments do
not establish an all-scale Newton gain or RH. The elementary identities below
carry no priority claim. They replace the underspecified first #903 notes;
[CORRECTIONS.md](CORRECTIONS.md) records what changed.

## 1. Freeze the source and the output being studied

Let Y>=2 be an integer, b=Y+1, L=b^2, B=L-1. All convolutions are Dirichlet
convolutions. Write g(n)=mu(n) for n<=Y and zero otherwise, and

```text
e = delta - 1*g,
N(g) = 2g - 1*g*g = g + g*e.
```

Here 1(n)=1 and delta is the convolution identity. Since 1*mu=delta,

```text
mu - N(g) = mu*e*e.
```

The divisor identities imply e(n)=0 for n<b. Thus e*e is zero at EVERY n<L.
Consequently N(g)(n)=mu(n) there. The error formula is a verification of the
reconstruction horizon, NOT a nonzero driver of energy in this annulus. At
n=L its error is e(b)^2, which may be zero; for Y=2 it is one.

Classical short-source inversion is prior art: Huxley--Watt,
arXiv:1807.05890, and its antecedents. The source-first implementation and
canonical norm state are inherited from #848, NSR26 and BNR26.

The observable here is the ACTUAL Mertens cumulative M(x), not the infinite
uncompleted N(g) source. For b<=x<L,

```text
M(x) = M(Y) + sum_(r<=Y) mu(r) sum_(b<=n<=x/r) e(n).       (1)
```

The canonical two-moment consumer retains BOTH energy and mean:

```text
E_Y = sum_(k=1)^Y M(k)^2/[k(k+1)],
u_Y = sum_(k=1)^Y M(k)/[k(k+1)],
A_B = E_Y + integral_b^L M(x)^2 dx/x^2
            + 2L (u_Y + integral_b^L M(x) dx/x^2)^2.       (2)
```

No whole-line norm is assigned to uncompleted g in this calculation.

## 2. Exact boundary atoms, including their incidence kernel

For a prime p|n, write n=p^a m, (p,m)=1. Pair the squarefree divisors d and
pd. For every positive real Y,

```text
R_Y(n) := sum_(d|n,d<=Y) mu(d)
        = sum_(d|m,Y/p<d<=Y) mu(d).                       (3)
```

For n>1, e(n)=-R_Y(n). When p is the least prime of n, every contributing d
is squarefree and all its primes exceed p. This boundary support is an
antichain: two comparable distinct divisors have ratio at least a prime >p,
whereas two elements of (Y/p,Y] have ratio <p.

The two-prime version, for n=p^a q^c m with (m,pq)=1, is

```text
R_Y(n) = sum_(d|m) mu(d)
 [1_(d<=Y)-1_(pd<=Y)-1_(qd<=Y)+1_(pqd<=Y)].              (4)
```

This is inclusion-exclusion, not a newly discovered cohomology theory.

Here is the missing kernel from the first pass. Define

```text
Phi_p(t) = #{h>=1: h<=t and every prime factor of h is >p},
Phi_p(t)=0 for t<1; h=1 is included.
```

For p prime and squarefree d with P^-(d)>p and Y/p<d<=Y, put

```text
v_(p,d)(x) = -mu(d) sum_(r<=Y) mu(r)
                       sum_(a>=1) Phi_p(x/(r p^a d)).    (5)
```

Then the right side of (1) is exactly M(Y)+sum_(p,d) v_(p,d)(x).
All sums are finite at x<L. Indeed, writing n=p^a d h with h p-rough is
exactly the incidence d|m in (3); no coprimality between d and h is imposed.
Each boundary divisor of a given n contributes once, with its sign.

Equivalently use primitive steps at t=rn with signed coefficient
a_t=-mu(r)mu(d), one for each boundary divisor d of n. Different atoms
may share t.
Include the constant atom (t=b, coefficient=M(Y)). Then

```text
M(x) = sum_atoms a_t 1_(x>=t),     b<=x<L.                (6)
```

Neither a prime assignment nor an antichain marginal alone determines these
coefficients. For Y=3,n=6 the boundary is the singleton d=3. Reversing its
sign preserves its support and antichain property but changes the output.

## 3. Closed Gram kernel and complete mean restoration

For t,u<L define

```text
K_L(t,u) = 1/max(b,t,u) - 1/L,
eta_L(t) = K_L(t,t).
```

Set both to zero when an argument forces empty support. Integrating (6)
gives the exact quadratic form

```text
I_Y = integral_b^L M(x)^2 dx/x^2
    = sum_atoms(t,u) a_t a_u K_L(t,u),
u_B = u_Y + sum_atoms(t) a_t eta_L(t).                   (7)
```

This includes all ordered off-diagonal interactions, including different
atoms at the same product. The completed interaction kernel is

```text
K_L(t,u) + 2L eta_L(t) eta_L(u),
```

together with the history cross term 4L u_Y sum a_t eta_L(t), the constant
2L u_Y^2, and E_Y. These terms must not be omitted.

For ANY partition into channels v_i, report

```text
G_ij = integral_b^L v_i v_j dx/x^2,
ell_i = integral_b^L v_i dx/x^2,
A_B = E_Y + sum_ij G_ij + 2L (u_Y+sum_i ell_i)^2.         (8)
```

The separately squared diagonal of this augmented form, treating the history
as its own coordinate, is

```text
sum_i G_ii + 2L[u_Y^2+sum_i ell_i^2].                    (9)
```

It is diagnostic, NOT an upper bound on (8). At Y=255 it is about 1928.69
for the coarse least-prime partition; even the inherited P=210 causal bank
has about 19.27. The actual completed A_B is about 1.58758. The exact intervals
are in boundary_results.json. This is why reporting annular energy alone is
not adequate.

## 4. A native all-scale obstruction to the proposed least-prime partition

Sum the channels whose least prime p exceeds Y. Below L=b^2 such an n is
necessarily the prime p itself: two prime factors, counted with multiplicity,
would give n>=b^2. Its boundary is d=1 and e(p)=-1. Therefore this entire
coalesced channel is

```text
V_>(x) = -sum_(Y<p<=x) M(x/p).                           (10)
```

Every argument x/p is below b, so only the known prefix is used. In the
initial shell Y<=x<=2Y, M(x/p)=1 except at irrelevant endpoints. Hence

```text
V_>(x) = -[pi(x)-pi(Y)]                                 (11)
```

on that shell. In particular its FULL annular energy is at least

```text
integral_Y^(2Y) [pi(x)-pi(Y)]^2 dx/x^2
  ~ (3/2-2 log 2) Y/(log Y)^2.                           (12)
```

Proof of the asymptotic: the prime number theorem gives uniformly for
1<=u<=2,

```text
[pi(Yu)-pi(Y)] / [Y/log Y] -> u-1.
```

Uniformity follows by taking the supremum of the PNT relative error for
arguments >=Y, and log(Yu)/log Y->1 uniformly. Substitute x=Yu and integrate
the squared limiting function; integral_1^2 (u-1)^2/u^2 du=3/2-2 log 2>0.
The negligible interval [Y,Y+1) contributes zero. This uses the classical
PNT, not RH; see SOURCE_NOTE.md for its imported status.

Thus any nonnegative block majorant retaining V_> as a separately squared
block has an Omega(Y/log^2 Y) cost even on the literal native source. It
cannot be a subpower-in-Y estimate. This is a refutation of MY first proposed
partition as a positive-norm proof strategy, not a counterexample to RH.

Scope: (12) does not refute every possible signed full-annulus covariance
inequality. Cancellation with composite channels, and cancellation between
different output shells, may matter. The theorem specifically forbids
bounding this isolated prime block by a subpower majorant.

## 5. A controlled part: individual large-prime diagonals

Do not coalesce those primes. For V_p(x)=-M(x/p), substitution x=pt gives

```text
D_>(Y) := sum_(Y<p<L) integral_b^L V_p(x)^2 dx/x^2
        = sum_(Y<p<L) (1/p) integral_1^(L/p) M(t)^2 dt/t^2
        <= E_Y sum_(Y<p<L) 1/p
        = (log 2+o(1)) E_Y.                              (13)
```

The upper endpoint L/p<=b and M(t)=0 below 1 justify the exact source bound.
The final asymptotic follows by partial summation from the PNT. The finite
inequality preceding it is exact without an asymptotic input.

This controls self-interactions, not the covariance between distinct primes.
At Y=255 the individual-prime diagonal is about 0.705516 while their merged
channel has energy about 10.644638. Treating different primes as orthogonal
would lose the essential phenomenon. Equations (12)-(13) are compatible.

## 6. Exact adapter to the ACTUAL PCR26/RCB26 harmonic source

This section prevents a second possible source substitution. Let c be the
PCR26 clipped completion: preserve mu through Y, then cancel its reciprocal
sum using coefficients of magnitude at most three. Its support is at most
Y+ceil(Y/2); that bound is an inherited PCR26 result, not needed to prove the
following finite identity. Write

```text
m_c(k)=sum_(n<=k)c(n)/n,   sum_n c(n)/n=0,
z=c*c,
K_d(k)=[H_floor(k/d)-H_k+log d]/d,
Q(k)=sum_(d<=support(c)^2) z(d)K_d(k).
```

The complete product source satisfies

```text
sum_d z(d)/d=0,
sum_d z(d)log(d)/d=2[sum c(n)/n][sum c(n)log(n)/n]=0.
```

Consequently Q(k)=sum_d z(d)H_floor(k/d)/d. Taking the difference at k and
k-1 gives (1*z)(k)/k. Native Newton reproduction therefore implies, for k<L,

```text
Q(k)=2m_c(k)-m(k),    m(k)=sum_(n<=k)mu(n)/n.             (14)
```

The EXACT boundary realization of the same quantity on b<=k<L is

```text
Q(k)=2m_c(k)-m(Y)
     -sum_(r<=Y) [mu(r)/r] sum_(b<=n<=k/r) e(n)/n.        (15)
```

Insert (3) here to recover the signed boundary atoms. This is an equality
to PCR26/RCB26's Q, not an analogy of norms. In these reciprocal coordinates
the elementary step kernel is

```text
sum_(k=b)^B [1_(k>=t)/t][1_(k>=u)/u]
       = (B-max(b,t,u)+1)_+/(tu),                        (16)
```

with the explicit background 2m_c(k)-m(Y). Bounds on the physical Gram in
(7) are not silently identified with bounds on (16).

Although the uncentered harmonic floor is zero for d>k, the centered K_d is
not. Every above-B product is retained in harmonic_adapter.py. Removing the
above-B products fails its exact-interval controls. Their cancellation is
valid only after accounting for BOTH global moments of z.

The program computes the original distinct-product diagonal and covariance,
and the RCB26 rough-parity block versions for empty bank and {2,3}, at
Y=3,7,15. It also checks (14)-(15) coefficientwise through the entire
reconstructed prefix for Y=3,7,15,63,255. All logarithms have directed rational
atanh-series bounds; no floating-point sign decides a verdict.

## 7. What the computation establishes, and what remains

The full physical boundary Grams, original harmonic covariance panels,
complete updated means, and exact source adapters now exist and replay.
The coarser proposed partition fails for a proved arithmetic reason. The
inherited causal Euler regrouping is independently reproduced, not renamed
as a new improvement. The remaining all-scale signed estimate is still open.

The right continuation must preserve prime/composite signed interactions,
respect the coordinate change (15), and pay completion. Neither the antichain
lemma nor a finite negative covariance table supplies that estimate.
