# Absolute Frobenius cutoff replay

Status: proof and preregistration independently reviewed before implementation;
new producer and tests have not been executed. Root runs all jobs under the
standing RAM gate. No author-side computation has taken place.

The source is the actual genus packet at
`32c4a249d188612729f093815b4a445b796893a0`. Its exact proof and producer are
authenticated before import; the producer in turn authenticates the entire
Frobenius and good-place source chain. The source multiplicities and matrix are
unchanged, and no new field is counted.

Twelve primary panels use e=1,2,3,4 and C_n=n,2n or n for 4|n and n/2
otherwise. Literal proper characteristic polynomials times their finite
exponential counterterms are compared with formal logs selected independently
by the inequality e*h≥C_n. The artifact retains both C_n and ceil(C_n/e).
Generator grades stop at16 and coefficient cutoff at64.

Twelve same-family norm panels use e=1,2, d=2,3 and the same three absolute
policies. Six additional exact phase controls use xi=-1,0,2; left phases are
xi^d. These are polynomial controls of the phase law, not natural-boundary
claims at arbitrary phase. The zero phase is explicitly the constant one.
Integer ceiling composition and actual zero-trace ambiguity are separately
checked, including equal and unequal individual source blocks. Oriented
frame-change counterterms also satisfy their additive norm law.

The e=2 coefficients -98 at degree8 and 1372/3 at degree12 are checked
against the e=1 square after substitution. Keeping the old relative slope
instead changes degree8 and is retained as a counterfeit. The new coherent
policy remains a chosen scalar regularization, not the native normalization.

The proof's blockwise classification is not inferred from these finite panels.
There is no unrestricted classification of accidental all-grade scalar
identities, sheaf sources, or archimedean factors. The fixture binds all owned
proof/contract/producer/test bytes and uses strict canonical JSON with
`allow_nan=False`. Parent commands are producer `--write`, ordinary and
optimized `--check`, then ordinary and optimized
`tests/test_graded_completion_absolute_cutoff.py`.
