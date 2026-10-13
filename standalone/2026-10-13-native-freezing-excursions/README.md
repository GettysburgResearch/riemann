# Native freezing envelopes and forced signed excursions

**PROPOSED research; full native moments and RH remain unproved.**
This continuation of PR #937 gives a sharp native restriction on its freezing
path, an explicit signed cancellation that the return must preserve, and a
centered fluctuation theorem. No zero-free exponent is improved.

Read [MATHEMATICS.md](MATHEMATICS.md) for complete statements and proofs,
[SOURCES.md](SOURCES.md) for attribution, and [VALIDATION.md](VALIDATION.md)
for test and review boundaries.

## The substantive change

The earlier universal counterexamples used changed coefficients or local phases
realized at uncontrolled row height. The new lower results keep nu=1, the actual
Mobius coefficients, the original smooth test, and actual sixth-power rows
inside the physical norm ball. Randomness only remains in the un-restored primes.

Write B_Y(D) for the native Mobius sum restricted to prime factors of norm <=Y.
It is exactly the mean of the partially frozen random polynomial P_(u,Y) at u=1.

### 1. Sharp native logarithmic-cutoff envelope

For every fixed A>2 and every nonzero fixed compact smooth W,

    limsup log(1+sup_(Y<=(log D)^A)|B_Y(D)|)/log D = 1-1/A.

The principal-row 2k-th moment envelope has exact exponent 2k(1-1/A).
At all actual rows 0<Nu<=D^h its limsup exponent lambda obeys

    2k(1-1/A)+h/6 <= lambda <= 2k(1-1/A)+h.

This is a SUPREMUM OVER CUTOFFS, not a lower theorem at the single curve
Y=(log D)^A or at every scale. Its proof uses a finite Euler product at
s=sigma+i*pi/log Y and an exact Mellin identity. The lower rows are literal
sixth powers of prime-ideal generators, with no uncontrolled CRT height.

The upper tradeoff overlaps #936 and is credited. The new lower conclusion
rules out a uniform native freezing extension whenever h<(6k/5)(1-2/A).
For A=4,k=2,h=1 the lower exponent is 19/6, versus diagonal exponent 3.
This does not refute the original, fully restored moment.

### 2. A large, explicitly computed intermediate mean

For fixed 1/2<theta<1, uniformly on compact theta intervals, put
G(s)=W_hat(s)/zeta_K^S(s). The written reconstruction proves, for every fixed J,

    B_(D^theta)(D)
      = D sum_(j=0)^J (-1)^j G^(j)(1)/(log D)^(j+1)
          + O(D/(log D)^(J+2)).

For nonnegative nonzero W, its leading term is
-(integral W)/Res_(s=1)zeta_K^S(s) * D/(log D)^2.
More generally finite Mellin balancing only changes the logarithmic power:
no nonzero fixed compact smooth test eliminates this exponent-one excursion.
Friable Mobius asymptotics are classical; this is their explicit fixed-window
reconstruction and application to the native restoration path, not a claim to
originate the underlying asymptotic theory.

### 3. Two actual opposite flux blocks; centered moments still controlled

On the SAME physical prime sixth-power replica set, the hybrid moment at
Y=D^theta is asymptotic to

    Q_k(D)=R(D)|c_W|^(2k) D^(2k)/(log D)^(2k(r+2)),
    R(D) asymp D^(h/6)/log D,

while both the log-square starting moment and fully restored endpoint are
o(Q_k). Thus the first prime block adds +Q_k and the remaining block adds
-Q_k. For the fourth-moment J in #937, these are -Q_2/4 and +Q_2/4.
An estimate bounding the blocks separately at diagonal size, uniformly in
physical row measures, is false when h<6k/5. Other rows may cancel these
blocks: no lower bound for a signed block summed over ALL rows is asserted.

The centered random part nevertheless has an unconditional all-order bound

    sum_u w(u) E|P_(u,Y)-E P_(u,Y)|^(2k)
       << H (D^2/(Y log Y))^k,       Y^2>bD.

At Y=D/(log D)^C this is diagonal up to logarithms, uniformly over all rows
and zero masks. It controls random fluctuations, not the deterministic means
or the fully restored endpoint. The fixed-theta expansion is not asserted
uniformly at this moving-theta cutoff.

## What remains open

The terminal one-sided signed estimate from #937 remains unproved. The present
results identify a mandatory cancellation inside that estimate; they do not
supply it for the full family. A revised attack must reunite the explicit
smooth-number mean excursions before bounding the remaining correlations,
without changing the source, masks, prime cofactors or physical row height.

## Publication and verification boundary

Parent: #937, `9f3250198a9b0551f42eb73dfd74a265c2a66854`.
Only this new standalone directory is intended to change.
The standard-library checker passed 12,630 explicit finite predicates in
ordinary and optimized Python, with identical output. It uses all 27 permitted
squarefree ideal columns of norm <=96, not a selected-prime column model.
Proof and code have the same author; no independent reviewer, Lean build,
full-repository validator, remote CI, or human acceptance is claimed.
