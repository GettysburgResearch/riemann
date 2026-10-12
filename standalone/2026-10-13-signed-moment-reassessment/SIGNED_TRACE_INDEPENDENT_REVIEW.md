# Independent mathematical review of the signed-trace obstruction

Reviewer: historical-obstruction audit agent, separate from the proof
author.

Disposition: accept the mathematical argument at the exact file hash
below, with the stated restriction to the unfiltered pointwise contract.
No physical moment estimate or zero-free theorem is accepted by this
review.

Reviewed file:

    SIGNED_TRACE_OBSTRUCTION.md
    SHA-256 4e557f9ff04e88cdaea099c90a0c7c4420b44487f9ddc64a7c2649d8b1bb01b3
    26,266 bytes

This is a source-file review. The enclosing publication must separately
bind the unchanged source bytes to its frozen Git commit. This report
does not substitute a file hash for that commit-level receipt.

## 1. Exact historical assertion

I read the pinned PR #911 source at commit

    2f8b6a3898a722d0602a91dea73bac344a3bb7dd

and independently recomputed the five source hashes in the proof:

| Historical file under the two-hour continuation literature directory | Verified SHA-256 |
|---|---|
| PRIME_SLOT_CANCELLATION.md | d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13 |
| SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md | c538719277b1e7de70a7e3f872fb2720668bd43ca57c9cffff6ff29b6766d5ac |
| WIDE_SUBCRITICAL_TUBE.md | 53568631060432784811d8474e8d774257664826e8fb9fa59c0ba47959745f02 |
| COMPLEMENTARY_SHORT_TRACE_CONTRACT.md | 968a2bee6d47f0a92fded0ab32c23963d31332f649dc0046604b7b568d48640c |
| PRIME_SLOT_ROUTE_STATUS.md | a03572f0f7be44bdd40befe2c86290095b54f84f2ba48f3e35a980f1e3a4fdde |

SC1--SC4 use the same common prime cutoff \(Y=bD\), the same literal
short ideal polynomials, the same moving exclusion \(Q\), and the
rational local collision quotient used in the new proof. They assert
an identity after all coefficient norm tests. They do not identify the
unfiltered integrands.

The selected incidence \(q_{\{1,k+1\}}=P\), with every other incidence
equal to one, is squarefree and eligible once \(Y\ge NP\). Its exterior
row multiplier is exactly \(1_{(u,P)=1}\). The factors involving
\(\nu(P)\) and the Möbius signs are outside the trace and have modulus
one. No change to the source fixed set \(S\) is concealed in \(P\).

The scale quantifier is relevant. P8 states every \(D\ge2\), hence
every sufficiently large real cutoff \(Y=bD\), and CT1 inherits this
interface. The proof's choice between \(p^2-1/2\) and \(p^2\) therefore
tests the claimed contract. It does not prove a statement about a
different contract imposed only at lacunary cutoffs.

## 2. Complete row sum and analytic domain

The proof fixes nonnegative Schwartz \(\Phi\), positive at zero, and
retains all nonzero Eisenstein element rows. The majorant
\(\sum_u\Phi(u/\sqrt H)(Nu)^\delta\ll H^{1+\delta}\) is valid for
each fixed \(\delta>0\) as \(H\to\infty\). It supplies the normal
convergence needed for the holomorphic row sums.

For fixed \(Y\), the rational denominators are nonzero throughout
\(\Re s_i>0\). On \(\Re s_i\ge\sigma\), the finite trace has a
finite bound uniform in every imaginary part and every larger real
part. This bound may grow exponentially with \(Y\). The subsequent
maximum principles need boundedness for each fixed \(Y\), so that
growth is harmless for their application.

The small-prime incidence removes every possible local smallness issue
in the numerator expansions. With the specified \(\sigma_0<\sigma\),
every remaining prime variable has modulus less than \(1/(16r)\) on
\(\Re s_i\ge\sigma_0\). The asserted degree-three error products are
therefore uniformly summable because \(3\sigma_0>1\).

## 3. The positive anchor is genuinely the full native source

For one left and one right slot, I checked the exact local identity

\[
 \frac{1-(a+\bar a)x}{(1-ax)(1-\bar a x)}
 =
 (1-x^2)
 \frac{1-(a+\bar a)x}
      {(1-ax)(1-\bar a x)(1-x^2)}.
\]

The last factor differs from one first at degree three. Extracting
\(\prod_{Np\le Y,\;p\notin SP}(1-(Np)^{-2s})\) requires the exact
inverse factor at every prime dividing the row. The proof includes
that correction. Its absolute value is at most a fixed constant
times \((Nu)^\delta\); no principal nonunit zero is lost.

At real \(s=\sigma\), the residual local numerator is positive because
\(1-2\Re(a)(Np)^{-\sigma}>0\). Its denominators are positive real
quantities. The two short polynomials are complex conjugates at this
real point. Thus every term in the residual row sum is nonnegative.

The unit row gives a lower bound without deleting other rows from the
nonreal trace. For each good rational prime \(p\), the only nonzero
Möbius contribution of ideal norm \(p^2\) comes from \((p)\): a single
inert prime ideal, or the product of the two distinct split prime
ideals. Its coefficient is respectively \(-\nu((p))\) or
\(+\nu((p))\), of modulus one in either case. Hence the norm-truncated
unit-row polynomial has a jump of modulus \(p^{-2\sigma}\).

At least one of the two adjacent cutoffs has polynomial modulus at
least \(p^{-2\sigma}/2\). The unit-row residual Euler product has a
uniform positive lower bound, and \(\Phi(1/\sqrt H)\) tends to
\(\Phi(0)>0\). This proves the asserted residual lower bound
\(G_Y(0)\gg Y^{-2\sigma}\) along an unbounded sequence, for every
fixed allowed \(\nu\). It is not an arbitrary coefficient
countermodel.

The residual \(G_Y(z)\) is holomorphic: the right character is
conjugated once in its fixed coefficients, not in the variable \(s\).
Its product with the left polynomial becomes an absolute square only
at the real anchor. This distinction is used correctly.

## 4. Analytic propagation and universal prime factor

The Lagrange interpolation argument uses \(n\) equally spaced nodes
in \([1,5/4]\). The denominator of the \(j\)-th basis value at zero
is exactly

\[
 (1/(4(n-1)))^{n-1}(j-1)!(n-j)!.
\]

Summing their absolute values gives the stated bound
\((10e)^{n-1}\). On the Cauchy circle of radius four, the remainder
ratio is at most \((5/11)^n\). Choosing \(n\) proportional to
\(\log Y\) makes that remainder smaller than half the positive anchor,
while the interpolation loss remains a fixed power of \(Y\).
It follows that \(|G_Y(x_Y)|\ge Y^{-C}\) somewhere in the indicated
interval. No derivative with respect to the discontinuous cutoff is
taken.

For \(\alpha=2\sigma<1\), the prime-ideal asymptotic gives the
weighted prime sum

\[
 \sum_{Np\le Y}(Np)^{-\alpha}
 e^{-2ix\log(Np)/\log Y}
 =
 \bigl(e^{-2ix}+o(1)\bigr)
 \frac{Y^{1-\alpha}}{(1-\alpha)\log Y}
\]

uniformly on that compact interval. Splitting at \(\delta Y\)
justifies the phase replacement: the lower portion has limiting
relative mass \(\delta^{1-\alpha}\), and the upper portion has
uniformly convergent phase. The logarithmic Euler-product remainder
is bounded because \(2\alpha>1\).

Since \(-\cos(2x)\) is bounded below by a positive constant on
\([1,5/4]\), the extracted principal product is at least
\(\exp(cY^{1-2\sigma}/\log Y)\). The polynomial residual lower bound
cannot cancel that growth at every point of the interval. This proves
the full two-slot trace lower bound.

I personally opened the primary reference cited in the proof:
Sami Omar, A note on the Prime Ideal Theorem, Corollary 1,
https://www.wseas.us/e-library/conferences/corfu2004/papers/488-336.pdf .
It states the classical prime-counting asymptotic used here. The
paper treats nonvanishing of the Dedekind zeta function on
\(\Re s=1\) as known. That is a classical unconditional input;
it is not a zero-free hypothesis inside the critical strip.
I did not reproduce the upstream proof of the prime-ideal theorem.
No error term assuming GRH is used in the new argument.

## 5. All-order transport

The higher-order step is not an unsupported embedding of a two-slot
counterexample. It derives a quantitative implication from an actual
boundary supremum for the full \(r\)-slot trace.

Let that supremum have the prescribed polynomial frequency weights,
and choose an integer \(J>B\). For one variable, division by
\((1+s)^J\) produces a holomorphic function that tends to zero on
large right semicircles, for each fixed \(Y\). Its boundary is
bounded by the full weighted supremum times the weights of the
remaining variables. The half-plane maximum principle is applicable.
Evaluation at real \(L\) costs only \((1+L)^J\).

Repeat this argument one variable at a time. The original finite
majorant remains available when some variables have already moved
right. Thus the repeated application is justified and costs
\((1+L)^{J(r-2)}\). The unchanged two variables stay on their
original boundary lines.

At \(L=Y\), every moved short polynomial is \(1+O(Y2^{-Y})\);
each additional local Euler variable has modulus at most \(q^{-Y}\).
Telescoping the finite products costs at most
\(Y2^{-Y}\exp(CY^{1-\sigma})\). Since \(1-\sigma<1\), this and the
remaining polynomial factors are exponentially small in \(Y\).
The bound is uniform before the entire Schwartz row summation.

Consequently the collapsed \(r\)-slot trace differs additively from
the exact two-slot trace by \(O(H e^{-cY})\). The polynomial cost
of the maximum principles cannot absorb the two-slot lower bound.

Finally, the source common-conjugate tube contributes only
\(O_M(HY^{-M})\). I checked its reproof: the cross pairs supply
\(k^2\cos(2\kappa)\), the same-side pairs cost at most \(k(k-1)\),
and their difference is positive at the stipulated width.
The row-prime removal cost is polynomial and is dominated by the
negative prime-sum exponential. The large full boundary supremum
must therefore occur on the complementary frequency set.

## 6. Corrections and conclusion

The first reviewed draft had a missing addition sign before the error
term in equation (6.4). I requested its correction. The author also
made the \(k=1\) case explicit before the repeated-variable argument
and stated the real-cutoff quantifier. All three changes are present
in the hash accepted above.

Theorem 1.1 proves the stated superpolynomial lower bound for every
fixed order and every fixed polynomial frequency weight. It refutes
CT1 even after adding an arbitrary fixed power loss in \(D\), for
the source's full real-scale quantifier and the fixed admissible
cross-pair allocation.

The argument does not refute the norm-filtered identity SC4, the
paid tube result, the actual second or higher physical moment, or
any Riemann-hypothesis statement. It instead identifies a false
sufficient condition introduced by the unfiltered representation.
Its conclusion and its stated limitations are mathematically
consistent.

No numerical experiment, prime search, zero census, or formal proof
assistant was used as evidence for the asymptotic conclusion.
The finite computations in this review were source-byte hashes.
