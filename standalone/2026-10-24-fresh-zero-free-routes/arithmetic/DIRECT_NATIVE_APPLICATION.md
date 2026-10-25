# Direct continuation from ordinary squarefree sums to the native inverse

Status: proved source-dependent endpoint adapter and conditional continuum-to-native implication.
Scope: the physical sextic family over the Eisenstein field, with the source's fixed finite ray data, common smooth profiles and norm twists. No new bound for a noninteger coefficient parameter is claimed.
Exact dependencies: Xu–Sang [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), Theorem 2.2 and Corollary 2.3, which explicitly state the Eisenstein full plain-product input from OpenAI's 30 September source; the source-qualified inverse consumer in PR #1014 at `845225c2e7713b69766b95c5e6964d44bb62f6bb`, `standalone/2026-10-22-inverse-length-consumer/PROOF.md`. The latter itself imports the original Eisenstein framework and its separately proposed amplification interface. Liu's analogous Theorem 12.14 and Remark 12.16 are supporting context, not a substitution of a field containing `mu_12` for the Eisenstein field.
What was actually run: no numerical character sum is used as evidence for this analytic implication.
Smallest remaining gap: one of the continuous-coefficient mean estimates in Section 3, with the stated physical row, height, profile and mask scope.

## 1. The actual coefficient vector

Fix the source orientation `sign in {1,-1}` and finite ray data `nu`.
Keep every natural zero at a nonunit. For a physical row `u`, write

\[
 \psi_u(n)=\nu(n)\chi_n(u)^{\rm sign}
                1_{(n,Q)=1},                       \tag{1}
\]

where `Q` is any additional common puncture at the licensed source
scope. A norm twist `(Nn)^(it)` and the fixed smooth profile are kept
inside the common column. Define

\[
 V_{U,D}(z;u)=D^{-1/2}\sum_n
       \mu^2(n)z^{\omega(n)}\psi_u(n)(Nn)^{it}W(Nn/D),
                                                               \tag{2}
\]

and the physical second moment

\[
 \mathcal M_z(U,D)=\sum_{\substack{Nu\asymp U\\
                                  u\ {\rm sixth\text{-}power\text{-}free}}}
                     w(u)|V_{U,D}(z;u)|^2,           \tag{3}
\]

with the fixed nonnegative bounded row profile of the consumer. Rows
that the source requires remain in the sum; this is not a convenient
squarefree-row subfamily. The vector-valued polynomial is formed in
the Hilbert space with weight `w`.

The two exact endpoints are

\[
 V(1;u)=D^{-1/2}\sum_n\mu^2(n)\psi_u(n)(Nn)^{it}W(Nn/D),
\]

\[
 \boxed{\quad V(-1;u)=D^{-1/2}\sum_n
                 \mu(n)\psi_u(n)(Nn)^{it}W(Nn/D).
          \quad}                                   \tag{4}
\]

The latter is the native inverse of PR #1014. No Gauss coefficient,
Poisson transform, extra dual diagonal, or projection complement has
been introduced. The degree bound and the continuation lemmas apply
unchanged to (2).

## 2. The ordinary squarefree endpoint is already accessible

We explicitly state the imported analytic input needed for this
adapter. For the same nonprincipal inducing row characters, original
zero conventions, common extra punctures, fixed bounds on length
exponents, and fixed profile/height scope, suppose the full ordinary
polynomial

\[
 P_u(X)=X^{-1/2}\sum_n\psi_u(n)(Nn)^{it}W(Nn/X)
\]

satisfies the source's fourth moment

\[
 \sum_{u\in\mathcal U(U)}|P_u(X)|^4
       \ll U^{1+\epsilon}(1+|t|)^A p_J(W)^4          \tag{5}
\]

for all nonempty scales `X<=U^C`, for each fixed `C`. This is the
no-prime-factor, nonprincipal-row specialization of the cited full
plain-product framework, not a claim about arbitrary coefficients.
Its complete profile and common-extra-modulus hypotheses are retained.
The number of physical rows is `O(U)` up to fixed-field/subpower
factors. Cauchy therefore gives

\[
 \sum_{u\in\mathcal U(U)}|P_u(X)|^2
       \ll U^{1+\epsilon}(1+|t|)^{A'}p_J(W)^2.       \tag{6}
\]

Restricting this positive mean to sixth-power-free rows is legitimate.

**Proposition 1.** Under (5), on the same nonprincipal physical rows,
for any fixed `C`,

\[
 \mathcal M_1(U,D)
       \ll (UD)^\epsilon U(1+|t|)^{A'}p_J(W)^2,
 \qquad 1\le D\le U^C.                             \tag{7}
\]

**Proof.** Use the exact squarefree identity
`mu^2(n)=sum_(d^2|n) mu(d)`. Since the complete naturally zero-extended
character (1) is multiplicative, put `X_d=D/(Nd)^2` to obtain

\[
 V(1;u)=\sum_d\frac{\mu(d)\psi_u(d^2)(Nd)^{2it}}{Nd}
                        P_u(X_d).                  \tag{8}
\]

There is no new condition `(b,d)=1` on the residual ordinary column.
The outside row multiplier has modulus at most one and retains every
zero it originally had. If the support of `W` lies in `[a,c]`, then
only `Nd<=sqrt(cD)` can contribute. Minkowski in the row Hilbert space
and (6) show

\[
 \mathcal M_1(U,D)^{1/2}
    \ll U^{1/2+\epsilon}(1+|t|)^{A'/2}p_J(W)
             \sum_{Nd\le\sqrt{cD}}\frac1{Nd}.
\]

For a fixed field the last ideal harmonic sum is `O(1+log D)`, by
ordinary ideal counting and partial summation. Empty subunit scales
give zero; the finitely bounded nonempty scales are included in the
source estimate or bounded directly. Absorb the logarithm into the
requested small loss and square. QED.

If the common profile carries additional fixed Sobolev parameters,
apply the same calculation with the corresponding homogeneous
seminorm. No rowwise choice of the residual coefficient vector is
made. An additional common puncture is part of `psi_u`, so (8) cannot
erase it.

### Principal-inducing rows

The imported no-prime moment excludes them, and so does the proof of
(7). For fixed finite ray data in a genuinely sixth-power-free
physical parametrization, a principal inducing character can occur
only when every good prime divisor of `u` is in the fixed conductor
support. Each good exponent of `u` is at most five. Hence those row
norms are bounded in terms of the fixed data; with `D<=U^C` their
column lengths are bounded too, and their finite contribution can be
absorbed separately. In the source's common convention that every
fixed coefficient conductor is included in `S` and the nonunit
sixth-power-free rows are outside `S`, there are no such principal
exceptions to remove: a good prime of the row already gives a
nontrivial local character. The unit row is a bounded case.

This boundedness argument is **not** valid if the coefficient
character itself has a growing conductor, or if arbitrary sixth powers
have been retained in the physical row. Such rows require their own
principal contribution; they must not be discarded under this note's
wording. Additional common zeros alone do not turn a nonprincipal
inducing character into a principal one.

## 3. Two exact continuous-coefficient targets

### Target A: the native inverse-length bound itself

Let `I` be any nondegenerate real interval. For **each fixed** `z in I`
(or for each `z` in a fixed measurable positive-measure subset),
prove, for the same physical family (2)–(3),

\[
 \mathcal M_z(U,D)
   \ll_{z,\epsilon}(UD)^\epsilon (1+T)^{A_z}
                  p_{J_z}(W)^2
          \{U+U^{1/6}D^{4/5}\},                    \tag{9}
\]

through the complete native range
`1<=log D/log U<=3/2` and the robust neighborhoods stipulated in the
consumer. Every licensed moving mask is part of this statement.

Then coefficient continuation gives (9) at `z=-1`: exactly the open
native hypothesis (H) of PR #1014. With **all** its other pinned
analytic interfaces, that conditional consumer gives its stated
ordinary-zeta boundary `437/500`. This note proves the transfer
implication; it does not prove (9) or certify the imported consumer.

### Target B: a smaller raw row-volume rectangle

A stronger local estimate on a narrower rectangle would also be
useful:

\[
 \mathcal M_z(U,D)\ll_{z,\epsilon}
       (UD)^\epsilon U(1+T)^{A_z}p_{J_z}(W)^2,
       \qquad D\le U^{25/24},                      \tag{10}
\]

again on a real interval of `z`, with the needed fixed power margins.
Continuation transfers (10) directly to the raw native inverse.
PR #1014 records that, under its separately proposed amplification
interface, this raw range supplies the `D^(4/5)` exponent because
`5(1-1/25)/6=4/5`. This last amplification is an explicit dependency,
not a theorem proved by coefficient interpolation.

For a leap beyond `0.874`, a substantially larger raw row-volume
rectangle would be a natural ambitious target. The correspondence
between such a range and a new numerical half-plane still requires
the complete detector consumer; it cannot be guessed from one
rectangle.

## 4. The profile and height orders can be fixed before consumption

The nonconstructive continuation argument does not require assuming
that `A_z` and `J_z` in (9) are uniform beforehand. For a fixed requested
small exponent loss, form the Baire closed sets with integer indices
`m,A,J`, requiring the normalized bound for **every** admissible
`U,D,T,W` with one common seminorm order `J` and height order `A`.
The pointwise-in-`z` hypothesis covers the interval by these countably
many closed sets. One has a nondegenerate subinterval. Chebyshev then
transfers the estimate with those fixed finite `A,J` to `z=-1`.

The consumer may choose its small height allowance only after those
orders have been selected, exactly as required. This is an existence
argument and does not give useful numerical values for the orders.
It does not rescue a hypothesis whose constants are allowed to depend
on a growing modulus, or a statement that was proved only at selected
profiles rather than the declared profile class.

The positive-measure version uses the same countable cover and Lemma
1b of the continuation note instead of Baire. Thus an arithmetic
estimate for almost every real coefficient parameter would suffice;
no common exceptional null set in the physical indices is allowed to
replace the required estimate for every admissible physical index.

Alternatively use the quantitative shrinking-window version of the
continuation lemma. A uniform estimate on
`1-1/log log D <= z <= 1`, with bounded-length modifications, already
suffices at subpower cost. Proving it is still a substantive arithmetic
problem; the known endpoint (7) alone does not imply it.

## 5. Why this is an independent route and where it stops

The route starts with an accessible ordinary squarefree vector and
continues **the arithmetic coefficient**, rather than seeking higher
integer moments of the same inverse or estimating one more Gauss
projection. It targets the actual native Mobius vector before any
Poisson coefficient mismatch arises.

The obstruction is precise. For noninteger `z`, the ordinary Euler
series has the form `L(s,psi)^z H_z(s)` and acquires branch points at
zeros. The ordinary functional equation cannot simply be copied from
`z=1`. The companion note proves that an individual irrational
coefficient estimate would itself detect zeros, and calculates the
mean-density cost of their possible cuts. Thus the new work must bound
these cut contributions **in the actual family mean**, or find another
source-faithful argument for (9) or (10).

The established progress is the exact ordinary endpoint adapter and
the proof that continuous coefficient control, even with
parameter-dependent constants, supplies the full native input. The
continuous control is still open. The source-qualified working
boundary remains `B_flat=0.874886647039964...`.
