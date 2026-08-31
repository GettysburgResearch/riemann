# Prime-collision law for the original physical frame

Status: proposed theorem; independent review required. This is a
varying-prime refinement of `INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md`, which
already proves injectivity for every fixed finite prime set. It does not
repeat that theorem and does not change the source or observation norm.

## 1. The two-prime source and its exact fields

Fix distinct primes p,q and two monotone schedule coordinates u,v. The
three-dimensional curvature source may be represented by

    M_A=integral v du, M_C=integral v^2 du, M_D=integral u^2 dv.

Put `z_p=p^(-1/2+it)`, `A(z)=sqrt(1-z^2)`,
`D(z)=sqrt(1-z)-A(z)` and

    P_p(t)=D(z_p) conjugate(A(z_p)).

Applying the literal ordered decoder before any norm or quotient gives

    Z_A=2(P_p conjugate(P_q)-conjugate(P_p)P_q),
    Z_C=(P_p-conjugate(P_p)) |D(z_q)|^2,
    Z_D=|D(z_p)|^2(P_q-conjugate(P_q)).                 (1)

The coefficient two in the first line is load-bearing. These formulas can
also be obtained by integrating all sixteen ordered subset pairs: total
multi-degree `(1,1)` has the two opposite coefficients `+2,-2`; degrees
`(1,2)` and `(2,1)` have coefficients `+1,-1`. Thus (1) is an actual source
identity, rather than a chosen linear frame.

Define three real physical fields

    E_A=-i sqrt(pq) Z_A,
    E_C= 4i q sqrt(p) Z_C,
    E_D= 4i p sqrt(q) Z_D.                              (2)

Multiplication by `i` only identifies the purely imaginary source directions
with a real Hilbert space. The prime factors in (2) remove the elementary
coefficient amplitude. They do not whiten the physical observation.

## 2. Complete scaling limit

Let `Gamma(v)=integral exp(itv) dnu(t)` be the unchanged physical
autocorrelation and let `nu_0=Gamma(0)`. Suppose p and q tend to infinity
through distinct primes and `q/p -> r>=1`. Put `h=log r`. In the ordered
basis `(E_A,E_C,E_D)`, the original `L2(nu)` Gram converges to

    [ (nu_0-Gamma(2h))/2       0                 0       ]
    [          0             nu_0/2          Gamma(h)/2 ] .   (3)
    [          0             Gamma(h)/2       nu_0/2    ]

If the orientation p,q is reversed, only the sign of E_A changes and (3)
is unchanged. The conclusion is uniform along any sequence with the stated
ratio limit; no prime search or finite panel proves it.

To prove (3), uniformly for real t,

    A(z)=1+O(|z|^2), D(z)=-z/2+O(|z|^2),
    P_p=-z_p/2+O(p^-1), |D(z_p)|^2=1/(4p)+O(p^-3/2).

The constants are absolute because all variables eventually lie in a fixed
closed subdisk. Equations (1)--(2) therefore give in `L-infinity(dt)`

    E_A=sin(t log(p/q))+O(p^-1/2+q^-1/2),
    E_C=sin(t log p)+O(p^-1/2+q^-1/2),
    E_D=sin(t log q)+O(p^-1/2+q^-1/2).                    (4)

The measure nu has finite mass, so the same errors tend to zero in its L2
space. For real even Gamma,

    integral sin(at)sin(bt)dnu=[Gamma(a-b)-Gamma(a+b)]/2. (5)

The kernel in L-102880 is supported on a logarithmic interval of length
`log 8`; hence Gamma(v)=0 for `|v|>=log 8`. The high-frequency terms and
all mixed low/high entries in (5) consequently vanish exactly for sufficiently
large p,q. Taking the remaining limits proves (3).

For every h>0, (3) is positive definite. Indeed Cauchy--Schwarz gives
`|Gamma(h)|<=nu_0`. Equality at a nonzero shift would make the nonzero
compactly supported logarithmic kernel a scalar multiple of its translate,
which is impossible by comparing supports. The same argument gives
`Gamma(2h)<nu_0`. This agrees with fixed-prime faithfulness. At h=0 the
limit has rank one: E_A tends to zero and E_C,E_D coalesce.

If r>=8, both nonzero autocorrelations in (3) vanish and the limiting Gram is
exactly `(nu_0/2)I`. Thus logarithmic separation, rather than prime size by
itself, controls this normalized two-prime frame.

## 3. Sharp collision order from the actual kernel jumps

Write `kappa(x)=K_L(exp x)`. Its jumps, including the support endpoints, are

    4, -8-4sqrt(2), 4+8sqrt(2), -4sqrt(2).

Their squared sum is `288+128sqrt(2)`. For a compactly supported piecewise
C1 function with finitely many jumps,

    ||kappa(.+h)-kappa||_2^2
       = |h| sum_j |jump_j|^2+o(|h|).                    (6)

This follows by taking disjoint intervals of length `|h|` at each jump; the
smooth complement contributes `O(h^2)`, and shrinking fixed neighborhoods
controls the remaining cross terms. Plancherel and the autocorrelation identity
turn (6) into

    nu_0-Gamma(h)=(144+64sqrt(2))|h|+o(|h|).             (7)

Consequently the two small eigenvalues of (3), as h tends to zero, are

    lambda_A=(144+64sqrt(2))|h|+o(|h|),
    lambda_primitive=(72+32sqrt(2))|h|+o(|h|).           (8)

The cusp is linear because the literal detector has jumps. Replacing it by a
smooth observation would change this rate and would be a different theorem.

## 4. Uniform diagonal normalization is impossible

The correlation coefficient of E_C and E_D tends to
`Gamma(h)/nu_0`, hence to one as h tends to zero. This coefficient is
unchanged by nonzero separate scalar rescalings of the two source coordinates.
For a positive two-by-two Gram with correlation rho, any diagonal rescaling
has condition number at least `(1+|rho|)/(1-|rho|)`; minimize the trace at
fixed determinant, with equality when its two diagonal entries match.

The prime number theorem gives consecutive primes p_n,q_n with q_n/p_n->1.
Along them, (7) makes the best diagonally rescaled condition number diverge at
least on the order of `1/log(q_n/p_n)`. Therefore:

    no coordinatewise amplitude normalization gives a uniform physical frame
    over all varying finite prime sets.                                  (9)

This is not a failure of fixed-prime injectivity, and it does not rule out a
frequency-aware observation family. Such a family would have to resolve the
primitive difference of colliding prime phases. A linear whitening matrix is
also not automatically an admissible morphism of monotone source paths.

The PNT input is classical; DLMF 27.12 records both `pi(x)~x/log x` and the
equivalent nth-prime asymptotic. Kronecker density and local-radical
independence are not re-imported in this proof because fixed-prime
faithfulness is already frozen in the predecessor. RH and the retained-gamma
decoder remain open.

## 5. The normalized primitive escapes into detector-edge channels

There is a sharper obstruction behind (9). Put `a=log p`, `b=log q`,
`h=|a-b|`, and consider the normalized primitive difference

    g_(a,b)(t)=[sin(at)-sin(bt)]/sqrt(h).

Along a prime-collision sequence, (5) and (7) give

    ||g_(a,b)||_(L2(nu))^2
       =[nu_0-Gamma(h)]/h -> 144+64sqrt(2).             (10)

Nevertheless `g_(a,b)` converges weakly to zero in the physical Hilbert
space and has no strongly convergent subsequence.

This has a direct source proof. Under Plancherel, multiplication of
`kappa_hat(t)` by `sin(at)` becomes, up to the fixed factor `1/(2i)`, the
difference of the two translates `kappa(x+a)-kappa(x-a)`. For large a,b,
the positive and negative translated support clusters are disjoint. Inside
each cluster the primitive is a translate of
`[kappa(x+h)-kappa(x)]/sqrt(h)`. Its support stays in one fixed compact set
before translation and its norm stays bounded by (6). Both clusters escape
to spatial infinity, so their inner product with any fixed L2 function tends
to zero. Equation (10) rules out strong convergence.

More locally, the squared mass of the difference quotient concentrates in
length-h intervals at the four jumps. The limiting proportions are the four
jump squares divided by `288+128sqrt(2)`. Thus the condition lost by nearby
primes is not repaired by a stable low-dimensional carrier: after the only
amplitude normalization that preserves its norm, the primitive becomes a
noncompact collection of translated detector-edge packets. A proposed
all-prime observation must either retain those moving edge channels or use a
different detector with an explicitly transported metric. This conclusion is
specific to the frozen discontinuous detector and is not called an RH
mechanism.
