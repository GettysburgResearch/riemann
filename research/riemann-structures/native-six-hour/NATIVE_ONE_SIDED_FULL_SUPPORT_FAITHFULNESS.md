# Full-support one-sided ratios distinguish the completed native source

This is an existence theorem for the fixed finite-prime source. It supplies a
replacement principle for a poorly chosen finite minor; it does not select a
new numerical minor or certify a finite horizon. The local argument proves
more than faithfulness of the actual curvature directions: it distinguishes
the full complex tensor space of dimension 4^r.

The literal source is L-102707 at
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, blob
`6810bcece309b0c54ae6c8fc84b314990004549c`. The source normalization and
absolute completion used here are frozen at
`822646ffea23d906c385f0273a8c45693e982c4d`:

- `FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md`, blob
  `851e4331c12d9f3f073ab73dca26baa33bd5e548`;
- `INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md`, blob
  `f7c42135e276a34d4da00279110666b0f4636080`.

No new source acquisition or computational test is used below.

## 1. Normalization and the selected side of the Fourier series

Fix distinct primes p_1,...,p_r and independent schedule variables u_i. Put

    A(z)=sqrt(1-z^2),  C(z)=sqrt(1-z),  B(z)=C(z)-A(z),
    S(u,z)=product_i [A(z_i)+u_i B(z_i)]
          =sum_n lambda_n(u) product_i z_i^(ord_(p_i)n),
    lambda_n(u)=sum_(a in {0,1}^r) v_(n,a) u^a.           (1)

The square roots are the branches with value 1 at zero. Indices n are
supported on the fixed primes. For a constant complex 2^r by 2^r matrix M,
the completed tensor observation is

    T_infinity(M)(t)
      =sum_(n,m) (v_n^t M v_m)/sqrt(nm) * (n/m)^(it).    (2)

The transpose is not a conjugate transpose. For an actual path current,
M_(a,b)=2 integral d(u^a) u^b. Thus (2) retains the literal derivative on
the n factor, the original factor 2, and the original physical weights.

We distinguish the two radii explicitly:

    rho_i=p_i^(-1/2),  q_i=rho_i^2=1/p_i,
    w_i=rho_i exp(-it log p_i),  q_i/w_i=rho_i exp(it log p_i). (3)

The positive Laurent powers in w therefore describe the physical ratios
1/b, not b. In particular, for beta_i>=0 and b=product_i p_i^beta_i, the
coefficient of exp(-it log b) in (2) is

    b^(-1/2) R_beta(M),
    R_beta(M)=sum_d (v_d^t M v_(db))/d.                  (4)

Here d is supported on the fixed primes. The exact alias weight is 1/d;
q_i=1/p_i, not p_i^(-1/2), occurs inside its local sums. All sums are
absolutely convergent by the frozen completion. A full-support row means
beta_i>=1 for every i, so every chosen prime divides b.

## 2. A one-sided local independence lemma

Fix 0<q<1 and let f_0=A, f_1=C. The four functions

    K_(i,j)(w)=f_i(q/w) f_j(w),  i,j in {0,1},           (5)

are holomorphic on q<|w|<1. Write f_i(z)=sum_(k>=0) f_(i,k) z^k.
Their positive Laurent coefficients are the four sequences

    k_(i,j)(beta)=sum_(k>=0) q^k f_(i,k) f_(j,k+beta),
    beta=1,2,... .                                      (6)

These sums converge absolutely. The four sequences in (6) are linearly
independent over C.

To prove this, suppose F(w)=sum_(i,j) c_(i,j) K_(i,j)(w) has every positive
Laurent coefficient zero. Its remaining nonpositive Laurent series defines
a holomorphic function on |w|>q, including neighborhoods of w=-1 and w=1.
Indeed, Cauchy estimates on any circle of radius r with q<r<1 show that its
negative-power series converges on |w|>r; allowing r to decrease to q gives
the stated extension. The constant term causes no difficulty.

Near w=-1 the inner factors A(q/w), C(q/w) are analytic. The outer C(w)
is analytic there, whereas the outer A(w) changes sign around its simple
branch point. The holomorphic extension of F has no such monodromy, so

    c_(0,0) A(q/w)+c_(1,0) C(q/w)=0                    (7)

as an analytic identity on a punctured neighborhood, hence on its
continuation. Since

    A(q/w)/C(q/w)=sqrt(1+q/w)

is nonconstant, c_(0,0)=c_(1,0)=0. Of the remaining terms, the outer C(w)
changes sign around w=1 and both inner factors are analytic there.
Single-valuedness similarly gives

    c_(0,1) A(q/w)+c_(1,1) C(q/w)=0,

so these two constants vanish as well. This proves the lemma. The argument
requires q>0; it does not assert a uniform statement at q=0.

In particular the vectors

    k(beta)=(k_(0,0)(beta), k_(0,1)(beta),
             k_(1,0)(beta), k_(1,1)(beta)),  beta>=1,

span C^4. Consequently some four distinct positive integer shifts give
an invertible 4 by 4 evaluation matrix. This is finite-dimensional linear
algebra applied to the proved independence. It does not identify those
shifts, or claim that shifts 1,2,3,4 suffice.

## 3. Tensoring only full-support positive indices

For each prime p_i choose four positive shifts as supplied by the lemma
with q=q_i. In the (A,C) basis, the completed source tensor is spanned by

    product_i f_(a_i)(q_i/w_i) f_(b_i)(w_i),
    a_i,b_i in {0,1}.                                  (8)

By absolute convergence, the coefficient at a multi-index beta is the
product of the local coefficients (6). The matrix of the 4^r evaluations
whose beta_i range independently over the chosen four shifts is therefore
the Kronecker product of the r invertible local matrices. It is invertible.

The original local basis (A,B) is related to (A,C) by the invertible
constant matrix sending (A,C) to (A,C-A). Applying this change in each
tensor factor transfers the same conclusion to the literal source (1).
Finally, the physical coefficients in (4) differ from those Laurent
coefficients by the nonzero row scalars b^(-1/2). They too form an
invertible evaluation matrix.

Thus there exist 4^r distinct ratios 1/b, each with b divisible by every
chosen prime, which distinguish every tensor M in (2). In particular the
entire family of full-support ratios 1/b is faithful on this tensor space.
This theorem does not require any pure-prime row or any numerator a>1.

For r=3 the actual path-variation current space has dimension 20, as in the
frozen literal curvature theorem. It embeds in the 64-dimensional tensor
space through M_(a,b)=2 integral d(u^a) u^b: equivalently its dual is the
image of these literal one-form evaluations. Restricting the invertible
64-row observation to this subspace is injective. Hence some 20 of the
64 full-support rows have rank 20 on the actual curvature directions.
The selection is existential and is not the previously tested 20-row minor.

## 4. What this implies, and what it does not

For the selected finite family, the entries obtained by truncating (4) to
d^2 b<=H converge absolutely to their infinite values. A nonzero infinite
determinant therefore remains nonzero for all sufficiently large H.
The same holds for the selected 20-row restriction when r=3. This yields
an eventual finite-horizon minor, but no effective threshold H_0, no
conditioning estimate, and no assertion about every smaller H.

The fixed-prime strip analyticity and the continuous prime-phase density
from the frozen faithfulness theorem identify these Laurent/Fourier
coefficients with the actual completed physical field. Equality in the
original weighted physical Hilbert space implies equality of the analytic
fields and hence of these coefficients. We do not assert that coefficient
extraction from a finite weighted interval is a bounded observation
operator, or supply a stable numerical decoder.

In particular, the argument does not certify the former fixed minor,
prescribe a replacement set of shifts, guarantee that a fixed truncation
of an absolute-tail majorant will be contractive, or identify a full
retained-gamma arithmetic decoder. It concerns finitely many fixed primes
and their completed literal source only.
