# Attack using the October 2 optimal fixed-order large sieve

**Scope:** a source-qualified all-row adapter and an exact exponent audit. This note does not independently reconstruct the external large-sieve proof, and does not prove the missing Mobius-weighted covariance bound. The main `INTEGRATED_CRITERION.md` is independent of this external input.

## 1. External input and conventions

Alexandre de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1, posted October 2, 2026, Theorem 1.1, states the sixth-power-free operator bound

    Theta_6(A,B) << (AB)^epsilon
        [A+B+A^(5/6)B^(1/3)+A^(1/3)B^(5/6)].                (1.1)

Both ideal indices in Theta are sixth-power-free; arbitrary complex column coefficients are permitted. The field must contain the sixth roots of unity and the construction data are fixed. The cited HTML source was inspected at Theorem 1.1 and Sections 2.2-2.5:

https://arxiv.org/html/2610.04045v1

This is a literature input, not a repository discovery. In particular, 'optimal' does NOT mean A+B, and does NOT mean that all sixth-power rows are already included.

For the primary-generator family over K=Q(sqrt(-3)), the usual fixed-family comparison costs only fixed finite partitions. Here is why no moving-conductor uniformity is presumed. The Kummer representative defining a character and a primary generator of the same ideal differ, modulo sixth powers, by an S-unit. The S-unit group modulo sixth powers is finite. Partition the rows by that class; its symbol is then a fixed column multiplier of modulus at most one. Section 2.5.2 of the source gives the reciprocity discrepancy as a function of two fixed ray classes, so reversing character orientation is handled by a further fixed partition and Cauchy-Schwarz. Original nonunit zeros are retained. The six element units are a further finite partition. All constants may depend on these fixed data.

## 2. All nonzero rows, with masks kept

Let c(r) be supported on squarefree ideals r prime to S with Nr<=N. Then (1.1), with the preceding fixed-family comparison, implies

    sum_(u in O,0<Nu<=H) |sum_r c(r)(u/r)_6|^2
      << (HN)^epsilon [H + H^(1/6)N
                        + H^(5/6)N^(1/3)
                        + H^(1/3)N^(5/6)] sum_r |c(r)|^2.   (2.1)

**Proof.** First restrict u to be prime to S and take primary representatives. Factor its ideal uniquely as u=v d^6 with v sixth-power-free. The two factors may share primes. Exactly,

    (v d^6/r)_6 = (v/r)_6 1_((r,d)=1).                     (2.2)

For each fixed d, insert the mask in the column coefficient; its squared norm cannot increase. Apply (1.1) with A=H/(Nd)^6 and B=N, then sum over Nd<=H^(1/6). The four resulting sums are bounded by

    H sum_d (Nd)^(-6),
    N # {d:Nd<=H^(1/6)},
    H^(5/6)N^(1/3) sum_d (Nd)^(-5),
    H^(1/3)N^(5/6) sum_d (Nd)^(-2).

Ideal counting bounds these by the four terms in (2.1). Requested small powers absorb all preliminary losses.

To restore the S-part of u, write u=u_S u_0, with u_S supported on S. The multiplier (u_S/r)_6 goes into the coefficients and the good row bound becomes H/Nu_S. Each term of (2.1) has a positive H exponent. The sum of (Nu_S)^(-a), for each of a=1,1/6,5/6,1/3, is a convergent product over the FIXED finite set S. Thus this restoration costs a fixed constant. Restoring the six element units also costs only a fixed factor. QED.

The same argument works with arbitrary column masks fixed before each use of the source estimate. There is no claim that an arbitrary row-dependent coefficient can be inserted into (1.1).

## 3. What the improvement actually buys

The earlier BGL-based all-row bound has bracket

    H + H^(1/6)N + (HN)^(2/3).                              (3.1)

At H=N=T the new bracket has order T^(7/6), instead of T^(4/3): a factor T^(1/6) is saved in this generic, balanced row/column regime. The new mixed terms do not worsen the old full envelope: when a new mixed term exceeds (HN)^(2/3), it is covered by H or H^(1/6)N.

Apply (2.1) to the actual balanced coprime polynomial B_u(X) in the companion proof. Its product column has N of order X^k and squared coefficient mass at most X^(k+epsilon). Hence

    sum_(0<Nu<=H) |B_u(X)|^2 << (DH)^epsilon
        [H X^k + H^(1/6) X^(2k)
         + H^(5/6) X^(4k/3) + H^(1/3) X^(11k/6)]           (3.2)

for 1<=X<=D, with bounded smaller scales handled directly. This is a genuine improved upper-bound envelope imported through (1.1), not diagonal-size control.

With H=D^h, integrate (3.2) against X^(-k-2k delta) dX/X as in the companion criterion. The resulting excess is

    lambda_sieve = max(0,
        k-5h/6-2k delta,
        k/3-h/6-2k delta,
        5k/6-2h/3-2k delta).                               (3.3)

Zero exponents can introduce logarithms, absorbed by epsilon. For 0<h<=k and k-5h/6-2k delta>=0, the second entry in the maximum dominates. The conditional extraction then gives exactly

    1/2+delta + (lambda_sieve+5h/6)/(2k) = 1.               (3.4)

Thus the strongest new GENERIC sieve, by itself, does not yield the desired inverse-moment improvement. In the near-linear row regime relevant to 17/24, the obstructing term is H^(1/6) X^(2k). The improvement at H approximately N can still be useful for smaller transformed blocks; that requires a new source-sensitive transfer, not just substituting the top-scale envelope.

## 4. The sixth-power term is not a bookkeeping accident

There is a simple genuine arithmetic lower bound for the generic operator. Take column coefficients one on prime ideals with N/2<Np<=N outside S, and zero elsewhere. Choose N/2>H^(1/6). For every primary a with Na<=H^(1/6), all these primes are coprime to a, and

    (a^6/p)_6=1.

The corresponding row sum equals the number P(N) of selected prime ideals. Distinct ideals a give distinct primary sixth-power rows. Ideal counting gives order H^(1/6) such rows and the fixed-field prime ideal theorem gives P(N) of order N/log N. Therefore, in this regime,

    operator_norm >= c H^(1/6) P(N)
                  >= c' H^(1/6) N/log N.                    (4.1)

This matches the problematic term up to a logarithm. It is a lower bound for ARBITRARY coefficients, not a counterexample to the specified Mobius/smooth family: selecting only primes is a different coefficient source. It proves that simply deleting this term from a general all-row sieve is invalid.

## 5. Actionable surviving attack

The source-independent norm is now quantitatively understood more sharply. A successful next step must distinguish the actual coefficients mu(r)nu(r)w_X(r) from the prime-supported coherent coefficients in Section 4, while keeping the target-copy rows. The companion's signed integrated remainder retains exactly those coefficients. It is not replaced by the generic operator norm in the stated remaining conjectural input.

No bound for that remainder is obtained from (1.1) alone. No external novelty, full analytic audit of arXiv:2610.04045, or improved zero-free boundary is claimed.
