# Executed validation and remaining review

The Python checker executes 16 named unit tests in exact Fraction and
Gaussian-rational arithmetic. The identical suite was executed normally
and with Python -O, and both full JSON outputs matched checks.json byte for
byte. Six deliberate corruptions were rejected with the expected error:
an altered RH flag, a float alias for the integer test count, and an altered
matrix-positivity flag, each in both interpreter modes.

The tests cover the beta second-moment identity, its half-integer extension,
positive-coefficient polynomial certificate, Gamma-integral Fourier-sign
constants, gamma/log constant certificates,
the m=42/X=10^18 and m=25/X=100 cutoff instances, inverse Laplace formulas, the inherited L2
norm, exact I_m normalization, the ENTIRE-tail ratio bound's finite base and
geometric ratio, the full-form normalization, and high-index synthetic
negative vectors. They do not evaluate actual prime sums or actual xi
matrices. They do not machine-prove dominated convergence, the explicit
formula, infinite negative index, the imported verified zero prefix, or RH.

The original interval Xi(14)/Xi(15) script was rerun in both modes and
reproduced its retained JSON. Its code and result Git blob identities,
and the complete pass5 parent proof blob, match the supplied published
identities. mpmath 1.3.0 interval Gamma remains a software trust dependency;
this is not a new interval implementation, zero census, or kernel proof.
The published Platt--Trudgian verification was not rerun. No entire older
project suite, Lean build, independent referee review, or remote CI ran.
REPLAY.json records output hashes and the exact parent identities checked.

Commands from this directory:

    python verify.py --check checks.json
    python -O verify.py --check checks.json
    sha256sum -c SHA256SUMS

The submitted mathematical note is provisional pending independent review.
Its new cutoff statements concern the actual FINITE arithmetic truncation;
they are not counterexamples to the full xi kernel. Its full-source
positivity is a restricted-family consequence of previously known b=2
positivity, here rederived from a low-prefix plus full-tail estimate.
The arbitrary-signed-vector theorem was attempted and was not proved.
