# Exact-SHA review addendum — L/T-105102

Review the paired first/second residue-coherence checkpoint independently.
Do not infer acceptance from the producer verdict.

## Source pins

- checkpoint base: fd3ef43a6964e502f00ad906482eae5b3c544fba
- frozen base proof digest:
  3e54ec6406ae1c37ceb43049ec433a29f7e2b269b293d84d9663b3480774a196
- draft context only: PR #720 at
  10bba584c01277e880aaa21e1fea09f396ca7246
- review source: use the exact checkpoint SHA posted on PR #723

## Proof audit

1. Recompute the residue of \(F/F'\) at a simple \(F'\)-zero.
2. Check the sign
   \(\mathcal M_{1,F}=-\Phi_{1,F}+C_{1,F}\).
3. Re-derive the complete counterclockwise edge formula and parity reduction.
4. Pair it with L-105101 without changing the signs of \(C_{2,F}\) or
   \(D_{2,F}\).
5. Apply the positive part only after correcting the first boundary charge.
6. Check that the coherence quotient is stated only when its denominator is
   positive.
7. Do not let a large negative first moment pass through the literal square;
   transfer requires the positive-part gate or a separate positivity proof.
8. Keep the fixed-window identity separate from every asymptotic estimate and
   from the draft PR #720 transfer hypotheses.

## Exact targets

For \(p=x^3-3x+1\) on the full window:

    Phi1=-2/3
    M1=2/3
    M2=5/18
    R=2
    coherence=4/5
    transfer constant=3/5

For \(p=x^5-x^3+x\):

    R=0
    Phi1=-2/25
    C1=-2/25
    corrected M1=0
    dropped-correction false carrier=2/25

For \(p=x^4-2x^2+2\):

    M1=1/4
    M2=9/32
    R=3
    coherence=2/27

On the unit square for \(p=z^2+1\), the first edge contributions must be
\(-1/\pi+1/4\) and \(1/\pi+1/4\), summing to residue \(1/2\).

Transfer-hypothesis firewalls:

    p=x^2-1, T=1:
      coherence=1, formal excess=1, endpoint nonvanishing=false,
      certified transfer constant=None

    p=x^4-(4/3)x^3-32x^2+64x-95/3, T=5:
      coherence=76832/133971, formal excess=19693/133971,
      common-zero-free=false, certified transfer constant=None

## Lightweight commands

    python -B experiments/X-105102-paired-residue-coherence-flux/verify.py

    python -B -m unittest discover \
      -s experiments/X-105102-paired-residue-coherence-flux/tests \
      -p "test_*.py" -v

Do not run broad repository campaigns.
