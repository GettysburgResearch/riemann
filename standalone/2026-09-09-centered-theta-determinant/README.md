# Whole-xi centered-integration determinant

Status: proposed component theorems; independent mathematical review required.
**RH is not proved.** This is a continuation of PR834, not a change to main,
prior research, the review record, or a formal proof library.

Read [PROOF.md](PROOF.md), then [REVIEW.md](REVIEW.md).

For the exact normalized theta density w=phi/Xi(0), let Q(t)=integral_t^infinity w
and work in H_w=L2(R,w dt). One fixed operator is

    (Kf)(x)=integral_R [1_(t<x)-Q(t)]f(t)dt.

It is Hilbert--Schmidt, with exactly

    ||K||_HS^2=integral_R F(t)Q(t)/w(t)dt <infinity.

The paper proves the entire identities

    det_2(I-izK)=Xi(z)/Xi(0),
    det_(odd H_w)(I-z^2 T)=Xi(z)/Xi(0), T=-K^2|_(odd H_w).

T is trace class. These are complete characteristic identities, with no
unknown entire multiplier, finite-height limitation, or zero-defined operator.
All algebraic multiplicities are retained. This construction is NOT positive
self-adjoint: RH is still equivalent to the nonzero spectrum of T being positive
real, and that property is not established here.

The connection to the preceding differential pencil is exact:

    U K* K U^(-1)=H^(-1), U f=sqrt(w)f.

Thus its positive base controls singular values, not eigenvalue arguments.
The new trace formulas identify cumulants of the whole theta density with
traces of powers of K and T, without inferring unproved higher-order signs.

The attempt to finish through an equivalent bounded positive Hilbert metric
fails rigorously. K is injective but K*1=0; T is injective but T*(w'/w)=0.
All finite derivative cuts have the same obstruction. The infinite derivative
orthogonal complement retains all nonzero algebraic root spaces, but no metric
or reality theorem is supplied on that remaining space.

The proof uses classical regularized-determinant/Volterra identities and the
literal theta source; it makes no novelty or independent-acceptance claim.
It does not strengthen the previously proposed source-spectrum equivalence into
an unconditional RH theorem.

## What was actually executed

    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json

The 110 bounded controls in five groups concern exact finite algebra, declared
compact probability laws, parity determinants and adjoint-chain identities.
They do not compute the actual theta spectrum, an infinite determinant or a
zero-free region. The real infinite arguments are paper proofs needing review.
[SOURCES.json](SOURCES.json) and [VALIDATION.md](VALIDATION.md) retain the scope.
