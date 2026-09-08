# The direct closing attempt: local sieve control does not bound cumulative drift

Status: FAILED COMPLETION ATTEMPT WITH PROVED COMPONENTS. RH is not proved.
This file identifies the missing upper estimate; reviewers are not being asked
to supply it under the label of checking a completed proof.

## 1. What was targeted and what was obtained

The parent requires finite complete energy

    J=integral_2^infinity R(x)^2 dx/x^3.

SSQ26 first proves a bounded invertible source adapter, then obtains an
UNCONDITIONAL bound for the orthogonal detail inside all square cells. This
uses the classical interval Brun--Titchmarsh inequality, not Cramer's
RH-conditional mean-square upper bound. In particular the all-scale detail
bound is not another deduction made under RH.

The exact remaining series is

    sum_(n>=2) w_n m_n^2 < infinity,

or, equivalently,

    sum_(n>=2) [pi(n^2)-Li_2(n^2)]^2/n^3 < infinity.       (OPEN)

No unconditional proof of (OPEN) is supplied. The results remove the infinite
within-cell approximation error with an explicit summable budget, but do not
pay the infinite inter-cell arithmetic correlation.

## 2. The full one-step relation retains the old cumulative level

Let s_n=pi(n^2)-Li_2(n^2), and write

    a_n=pi((n+1)^2)-pi(n^2)
                    -integral_(n^2)^((n+1)^2) dx/log x.

Exactly s_(n+1)=s_n+a_n. The sieve bounds the number of new primes, and
hence |a_n|<=2(2n+1)/log(2n+1), but not the cumulative s_n.
For every M>=3 the complete stopped coarse energy satisfies

    sum_(n=2)^(M-1)w_n s_n^2 +s_M^2/M^2
      =s_2^2/4+sum_(n=2)^(M-1)[2s_n a_n+a_n^2]/(n+1)^2.    (1)

This follows by telescoping s_(n+1)^2/(n+1)^2-s_n^2/n^2. The terminal
term is the entire norm of the held constant s_M on [M^2,infinity) in
measure dx/x^2. It cannot be deleted. Every cross term 2s_n a_n has its
literal sign. A positive quadratic energy gives a lower bound for this
work, not the missing upper bound.

Bounding |a_n| by the sieve upper estimate in (1) does not produce a finite
right side. Even the resulting bound for sum a_n^2/(n+1)^2 grows on the
order allowed by sum 1/log^2 n. The cross term cannot be replaced by zero
or by an independently centered prime model.

The unconditional PNT remainder only gives

    |s_n| << n^2 exp(-c sqrt(log n)),
    sum_(2<=n<M) w_n s_n^2 << M^2 exp(-c' sqrt(log M)).     (2)

The second bound follows by splitting at sqrt M and integrating the upper
half; constants are not certified here. It is not a finite-total-energy
estimate. No new power saving beyond the inherited classical scale has been
established. Under RH, finite energy follows from the conditional Cramer
input as recorded in the parent, not by treating (2) as sufficient.

## 3. Two tempting completions fail

### Resetting each block is not an approximation to the same source

Subtracting the actual mean m_n from each cell DOES give a globally finite
L2 detail. But it removes the very cumulative coarse vector whose norm is
uncontrolled. Equation (11) of PROOF.md retains that vector explicitly.
No bounded operator is proved which removes it while preserving the intended
zeta logarithm or the original causal-source domain.

### Several overlapping grids do not create a uniform global spectral gap

One can repeat the local sieve bound on displaced or modestly enlarged square
cells. This bounds local changes of the cumulative discrepancy, not its
whole level. A weighted discrete Poincare estimate converting those local
bounds into (OPEN), uniformly over arbitrarily large horizons, would be a
new theorem. No such uniform estimate follows from local projection.

Here is a precise control of the hypotheses actually used for local detail.
It is a positive CONTINUOUS counting density, NOT ordinary primes, NOT an
Euler product, and NOT a counterexample to RH. Fix beta in (1/2,1) and
0<eta<=1, and set for x>=2

    r_beta(x)=[1+eta x^(beta-1)]/log x,
    N_beta(x)=integral_2^x r_beta(u)du,
    E_beta(x)=N_beta(x)-Li_2(x).

This density is positive. On each square cell n>=3,

    N_beta((n+1)^2)-N_beta(n^2)
       <=(2n+1)/log n <=2(2n+1)/log(2n+1),

since 2n+1<=n^2 and r_beta(x)<=2/log x. Thus it satisfies the same cell
upper count used in the proof. Its discrepancy has

    E_beta(x) ~ eta x^beta/[beta log x].                 (3)

This follows by l'Hopital's rule applied to its positive defining integral,
or a single integration by parts with a smaller remainder. It is smaller
than x exp(-c sqrt(log x)) for every fixed c>0 eventually; thus it also
satisfies the classical PNT-shaped error bound. Nevertheless

    sum_n E_beta(n^2)^2/n^3
       is comparable to sum_n n^(4beta-3)/log^2 n
       and DIVERGES because beta>1/2.                   (4)

The within-cell detail is still summable by the same projection lemma.
Therefore the local upper count, positive counting measure, overlapping
local regularity, and PNT-shaped error do not establish (OPEN) in that class.
This does not exclude using additional multiplicative information specific
to the ordinary primes. It identifies exactly where that information is
still required.

## 4. Complete conditional ending, with no unproved step disguised

Assume (OPEN) is supplied by a new arithmetic argument. The explicit sample
error in SSQ26 (12) then makes e(x) square-integrable in dx/x^2. The exact
stable transfer gives J<infinity. Alternatively Section 6 of PROOF.md
constructs an analytic logarithm directly from that same e. Its exponential
is (s-1)zeta(s)/s^2 on Re s>1/2, hence zero-free there. Functional-equation
reflection gives RH, with full multiplicities. The source-domain completion
then follows from the predecessor's stated inner-factor classification.

The conditional implication is complete. Its premise is not proved. The
packet should be reviewed as an all-scale local-error theorem and an explicit
source adapter, not an RH completion or a new zero-free region.

## 5. Narrow next research target

The unbounded work is now a signed cumulative estimate on the prescribed
integer sequence s_n. Local prime-gap irregularities within a square cell
have a complete paid L2 budget. A useful next theorem must control the old
level times the new signed increment in (1), or directly bound the coarse
series. A larger local prime table, a finite positive Hessian, or faster
quadrature of the sample sums does not supply that theorem.
