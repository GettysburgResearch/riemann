# Independent complete Xi kernel binding audit

Date: 2026-10-10. Read-only checkout/Git. Scoped PASS for the exact
literal-source identity and the all-window nonnegativity iff RH theorem.
No all-window sign or RH is proved by this audit. No heavy numerical
execution is needed for this analytic adapter.

Reviewed COMPLETE_XI_KERNEL_BINDING.md SHA256:
e81a3c22d4ace8ab2af0b01bb6afcd64e176ca986aacca5da58e1a63617094e6.
Inherited OPERATOR_AUDIT.md SHA256:
f42396ff962012e2e56a4bfa4cffebcff76870f42b1ce5c37366c76811a5b17b.
The new X1 at lines 10-20 is exactly O1.1 at inherited lines 18-31,
including the factor 1/(2b), prime powers, C_b, b=3/2 and c=1/2.
The native q normalization is inherited lines 42-46, with factor b.

## Complete zero source and product

New lines 32-65 correctly sum over all nontrivial zeros with analytic
multiplicity. The classical completed xi normalization has no extra zero
at 0 or 1. F(s)=xi(1/2+s) is even. Its center is nonzero: the paired
alternating eta series is strictly positive at 1/2, its denominator
1-sqrt(2) is negative, and the remaining xi factors make F(0)>0.

Writing F(s)=G(s^2) gives an entire G of order at most 1/2. Its genus-zero
Hadamard product has only a constant exponential factor. Each opposite
pair {a,-a} corresponds to one zero of G with the same analytic
multiplicity, so its logarithmic derivative is exactly 2m*s/(s^2-a^2).
The inverse-square zero sum is finite, and no linear exponential factor
or unpaired reflected zero remains. These are precisely the declared
classical Hadamard and completed-xi inputs, not RH assumptions.

For a=beta+i*gamma, the strip gives |beta|<1/2 and
Re(b^2-a^2)>2+gamma^2. Hence absolute local uniform convergence of
sum exp(a*x)/(b^2-a^2) follows directly from the inverse-square zero sum,
with an exponential-order 1/2 bound. Reflection and conjugation make
the sum even and real. Termwise Laplace integration for real s>b is
justified by an absolutely summable bound integrated against
exp(-(s-1/2)x). A complete opposite pair contributes exactly
2m*s/[(s^2-a^2)(b^2-a^2)]. The proposed X4 matches this algebra with
the stated multiplicities and signs; its apparent factor at s=b is
removable because L is analytic there.

## Exact arithmetic, gamma and growing-term normalization

Lines 69-77 correctly split each shifted exponential at log n. The
weighted prime transform is
[-zeta'(s+1/2)/zeta(s+1/2)-(s/b)P2]/(s^2-b^2).
Here q_n*n^(-b)=Lambda(n)/n^2 and q_n*n^(-s) is the complete logarithmic
derivative at s+1/2; no prime-power contribution is dropped. Absolute
integration of the entire source is valid for real s>b.

Lines 79-99 have the correct gamma partial fractions. Their three
coefficients sum to zero, which removes the digamma subtraction constant.
The arguments are 1/2, 2 and 5/4+s/2 because lambda_j=2j+1/2 starts
at j=1. Applying the digamma recurrence introduces precisely the
-1/(s+1/2) term. After adding the growing exponential and C_b pieces,
the numerator is exactly X6, including log(pi)/2 and both rational
pole-canceling terms. The completed-xi logarithmic derivative at
1/2+s then yields X7 and the required X4.

An independent exact normalization oracle checks seven symbolic
identities: opposite-pair Laplace algebra, shifted prime integral,
gamma partial fractions, cancellation of their coefficients, the full
digamma numerator, growing/constant/gamma combination, and the x=0
normalization W(0)=L(b)/b. It uses SymPy rational algebra, independent
of the native Arb source producer. Normal/-O outputs are byte-identical,
SHA256 65a662fc2a111141ff478ee032f13180bb031814419c80d15cfb95c1997d3701,
at /tmp/review-xi-kernel-binding-{normal,optimized}.json. Script:
/tmp/review_xi_kernel_binding_oracle.py.

Lines 109-114 legitimately apply Laplace uniqueness. The prime pairs
are bounded by 2 exp(b*x)n^(-b) on x>=0, so their q_n-weighted sum is
bounded by 2 exp(b*x)P2. Their compact uniform convergence, and the
uniform gamma convergence, give a continuous source of exponential
order b. Both functions meet the classical uniqueness assumptions.
Evenness then extends the identity to the full real line.

## Native form and exact all-window criterion

Lines 118-128 correctly exchange the locally uniform absolute zero sum
with the native double integral. A fixed-interval L2 test is L1, and
the conjugation and exp(a*t)/exp(-a*u) factors in X8 are correct for
the inherited antilinear-first q convention. Denominators are complex
away from RH and the paired source cannot be replaced by positive
squares there. Under RH each factor product is a true Fourier absolute
square, its denominator is b^2+gamma^2>0, and nonnegativity follows.
Simplicity is not required or claimed.

For the converse at lines 134-145, choose arbitrary finitely many real
points, translate them into one sufficiently long interval, and use
the same shrinking smooth bump for each complex coefficient. The
native tests remain L2 at each scale. Continuity of W makes the
limiting quadratic form exactly the finite kernel matrix. Thus the
all-L assumption yields positive definiteness on the real line.
Two-point minors give |W(x)|<=W(0); this is a global boundedness
conclusion, not a bounded-window consequence.

The one-sided Laplace transform of bounded W is holomorphic on
Re s>0. On the initial real s>b it agrees with X4, and the identity
theorem for meromorphic functions extends that agreement throughout
the connected right half-plane. A zero a with Re a>0 gives a simple
logarithmic-derivative pole of residue m_a; division in X4 gives the
nonzero residue -m_a/(a^2-b^2). The strip excludes a=+/-b, so no
cancellation by the denominator or numerator's linear term is possible.
This contradicts holomorphy. Reflection excludes Re a<0 as well.
Therefore the all-window criterion is exactly equivalent to RH.

No gap found. This closes the literal kernel's actual completed-Xi
source identification using the declared classical inputs. It does
not provide the missing all-window sign. A completed sign certificate
on 0<L<=1 supplies only that proper bounded-window subfamily and does
not invoke the converse hypothesis. No trace/coefficient criterion
or all-length extension is imported implicitly.
