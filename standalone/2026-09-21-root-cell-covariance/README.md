# RSC26 — full residual covariance control and sparse native gain certificates

**Proposed component proofs for independent review. The unbounded coarse-energy estimate, full all-scale Newton gain, and RH/GRH remain open.** Additive continuation of #903 at `f80aa1346bbc457d5726977c0b720162c05bb70e`; all previous packets and statuses are preserved.

This pass stops selecting another sparse set of product pairs. Instead it orthogonally averages the actual OUTPUT over root-sized integer intervals. It controls the entire remaining within-cell covariance at once, with all product pairs retained. The unresolved arithmetic contribution is the explicit coarse output energy.

## 1. Exact local bridge between the two previously separate metrics

For any real arithmetic source a, let A(k)=sum_(n<=k)a(n), r(k)=sum_(n<=k)a(n)/n. On EVERY integer interval C=[s,t],

    weighted variance of A, weights 1/[k(k+1)]
      = ordinary variance of r.                         (1)

Only the centered residuals are equal. The coarse terms and boundary completion costs are not numerically identified. The proof is a finite summation-by-parts identity, polarized for cross covariances.

Applied columnwise to PCR26's original centered harmonic kernel,

    K_d(k)=[H_floor(k/d)-H_k+log d]/d,

it gives a completely RATIONAL expression for every residual Gram entry as the weighted covariance of floor(k/d)-k/d and floor(k/e)-k/e. Products above the observation endpoint remain nonzero. Logarithms disappear only after cell centering.

## 2. Full signed residual, not another near-pair sector

Let P average on cells defined by floor(q sqrt(k)), q a fixed positive integer. For the native Mertens cumulative and reciprocal cumulative, the entire residual over b<=k<b^2 is bounded by the exact computable ramp budget

    U_(b,q)=sum_C [ell-h-h^2/W],
    ell=t-s+1, W=ell/[s(t+1)], h=H_(t+1)-H_s,
    U_(b,q)=(log b)/(3q^2)+O_q(b^(-1/2)).                (2)

No prime-distribution theorem enters. The ramp a(n)=1 attains this worst-case residual in the general bounded-increment class.

For the full native capped-completion harmonic source Q, the collar is explicitly paid and

    ||(I-P)Q||^2 <= U_Q
      <= (log b)/(3q^2)+16log(3/2)/q^2+O_q(b^(-1/2)).    (3)

For ANY reciprocal-balanced finite source |c(n)|<=K, a separate universal proof gives

    ||(I-P)Q||^2 <= (5/8)K^4 H_(b^2-1)^9.               (4)

The exact decomposition is

    ||Q||^2=||P Q||^2+||(I-P)Q||^2.

The estimate controls the SIGNED residual matrix after observation-space projection. It is NOT an absolute pairwise envelope and NOT an upper bound for ||P Q||^2. It does not on its own close DCN26's far covariance gap.

## 3. A complete endpoint-only state certificate

Write eta_k=m(k)-M(k)/(k+1). Cell means are determined by endpoint data:

    sum_C M(k)/[k(k+1)] = eta_t-eta_(s-1),
    sum_C m(k) = (t+1)eta_t-s eta_(s-1).

Thus

    A_B <= E_Y + sum_C (eta_t-eta_(s-1))^2/W_C
                 +U_(b,q)+2b^2 eta_B^2,
    F_B <= F_Y + sum_C [(t+1)eta_t-s eta_(s-1)]^2/ell_C
                 +U_(b,q),        B=b^2-1.              (5)

No measured fine-scale energy is used in these upper certificates. The full mean/completion term is retained. Mathematically one scalar eta per boundary suffices; the report stores M and m separately for arithmetic verification.

The certificate has O(qb) cells instead of Theta(b^2) observations. The current implementation still generates the entire arithmetic prefix to verify its endpoints; this is not claimed as a new fast Mertens-evaluation algorithm.

## 4. The inherited gain is certified for EVERY cutoff 1<=Y<=2047

The maximum endpoint is N=4,194,303. One q=4 endpoint certificate proves

    F_N <1.858259550206,    (1+2F_N)^2<32.

Since F is monotone and F_n<=A_n<=2F_n, while A_Y>=F_1=1, this single upper certificate implies

    1+A_((Y+1)^2-1) <=2(1+A_Y)^(3/2)

simultaneously for all 2,047 integer cutoffs in that range. This is a FINITE result, not an inference from ten sampled cutoffs and not an all-scale theorem.

At the largest displayed stage Y=2047:

| Resolution q | Cells | Complete A_B upper certificate |
|---|---:|---:|
| 1 | 2,003 | 4.229144516385 |
| 2 | 4,006 | 2.331844104680 |
| 4 | 8,011 | 1.858260296638 |

The actual complete A_B is about 1.701819058480. All three bounds pass the stage's gain test. The q=4 harmonic Q decomposition is

    coarse energy       0.219261420966,
    actual residual     0.002429779704,
    proved residual cap 0.170291462549.

The residual cap is deliberately not replaced by the smaller measured residual. It is the universal cap plus native collar accounting that makes the finite certificate rigorous.

## 5. Limitation tested, not concealed

The cap-three, reciprocal-balanced fake Newton source has Q-energy about 968.75 at Y=31, of which about 966.13 is coarse and only 2.62 is residual. Small residual does not imply small total energy. Native arithmetic must control the coarse term; no such unbounded inequality is established in this packet.

An all-scale polynomial-in-log bound for the coarse expression in (5) would suffice through the existing innovation/Mellin argument, but is NOT proved or called an easier replacement problem.

## 6. Bounded L-family extension

LFAMILY.md proves a root-cell residual estimate <=36 H_N^4 in the correct arithmetic center-one measure dx/x^3, assuming the standard elliptic inverse-coefficient bound |nu(n)|^2<=n tau(n)^2. No Euler factors are removed and the central singularity is unchanged. The coarse statistic is nevertheless not itself a completed L-function and must not be substituted into the earlier Pick/deflation test.

A finite good-Euler inverse model for E_17 through 4095 checks coefficient bounds and the physical decomposition. This is not the complete elliptic reciprocal sequence, global rank, zero, height, or L-value data.

## 7. Replay and source boundaries

Read PROOF.md, LFAMILY.md, VALIDATION.md and SOURCES.json. Python standard library only:

```sh
python -S -B replay.py
python -S -O -B replay.py
```

Each replay regenerates reports, checks semantic receipts, reconstructs all 4,194,303 coefficients from the short prefix via an independent Newton implementation, checks every endpoint and complete input/output state, and runs sixteen regression methods. Exact Fraction checks independently sum small full cells; 600 product-pair residual identities and 3,645 local isometries are checked exactly.

The verifier imports no producer, but the scalar interval utilities and grid definition are shared. The implementations have one author and are not independent mathematical review. No full-repository validator, external formal build, all-scale coarse bound, or RH/GRH proof is claimed.
