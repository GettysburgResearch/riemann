# Exact-SHA review addendum — L/T-105101

Review the entire-window residue-flux checkpoint independently. Do not infer
acceptance from the producer verdict.

## Source pins

- checkpoint base: 51c5619ef3c4b793de756b1c359b39df2ac35466
- draft context only: PR #720 at
  10bba584c01277e880aaa21e1fea09f396ca7246
- review source: use the exact checkpoint SHA posted on PR #723

PR #720 is open, draft, and post-freeze. It is prior-art context, not a
reviewed dependency.

## Proof review

1. Recompute the residues of \(F^2/(F'F'')\) at simple \(F'\)- and
   \(F''\)-zeros, including numerator-removable cases.
2. Check that the three rectangle hypotheses exclude every denominator pole
   on the finite boundary.
3. Re-derive all four counterclockwise edge signs before applying Schwarz
   reflection.
4. Under definite parity, verify that \(Q_F\) is odd and that opposite edges
   reinforce.
5. Check the real/nonreal/debt split and confirm that the nonreal term is an
   algebraic square sum.
6. Separate the direct fixed-window Xi representation from the still-open
   global \(V_2,V_4\) canonical-product route.
7. Reject any implication that Xi simplicity, an admissible asymptotic flux
   bound, RCMV104530, or RH has been established.

## Exact fixture targets

For \(p=x^3-3x+1\):

    T=1/2: B=-1/18, C=0, D=-1/18, M2=0
    T=3/2: B=2/9,  C=0, D=-1/18, M2=5/18

For \(p=x^3+3x+1\), with a wide strip:

    algebraic C=1/6
    absolute-square mutation=5/18
    D=1/18
    B=2/9
    M2=0

For
\(p=x^4-\frac43x^3-32x^2+64x+1\), \(T=3\):

    M2=2401/8100
    D=-20987563/3110400
    B=-20065579/3110400
    global K4=5437/3888

The replay must fail closed on incomplete or duplicate derivative-root
manifests and on roots lying on a finite edge or corner.

## Lightweight commands

    python -B experiments/X-105101-entire-window-residue-flux/verify.py

    python -B -m unittest discover \
      -s experiments/X-105101-entire-window-residue-flux/tests \
      -p "test_*.py" -v

Do not run broad repository campaigns for this review.
