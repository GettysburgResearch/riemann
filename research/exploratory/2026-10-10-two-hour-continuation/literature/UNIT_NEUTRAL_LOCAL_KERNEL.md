# The exact unit projector does not repair every local Euler kernel

Status: exact local source counterexample to a positive-kernel adapter.
No assertion that the complete radial row trace is indefinite, and no
obstruction to a different mixed-moment estimate, is claimed.

The local determinant argument PF5 of `PAIRED_FREQUENCY_COLLISION.md`,
SHA256 `d057fd4138a4f9c7fcb5455c51e8eabe04b707b8817d4a6ae3359cdfdb85df9a`,
uses norm7. That prime's nonzero unit charge can be killed by an exact
radial unit average. The following different literal good prime avoids
that issue while preserving the same local obstruction.

In the source Eisenstein ring, pi=7+3omega and its conjugate 4-3omega
are primary good primes of norm37. Their finite-field roots are 10 and
26. For every sixth unit epsilon the source residue symbol satisfies

\[
 \chi_\pi(\epsilon)=\epsilon^{(37-1)/6}=\epsilon^6=1.
\tag{UN1}
\]

Thus the source row orbit u=epsilon of u=1 has identical character
values at this prime. The exact radial projector `(1/6)sum_epsilon`
leaves its local Euler kernel unchanged. This uses actual residue
symbols and retains the nonunit zero at multiples of pi.

At real part one half take two left frequency vectors whose sums of
local variables are A1=0 and A2=1/4. The first uses variables
`+i/sqrt37,-i/sqrt37`. The second uses conjugate unit phases divided
by sqrt37, with cos(theta)=sqrt37/8; this is feasible because 37<64.
Every phase is realized by a real Mellin frequency at this prime.
The right vectors are the Hermitian conjugates. The local coprime
Euler kernel is `K(x,y)=1-A(x)-conjugate(A(y))`, hence

\[
 K=\begin{pmatrix}1&3/4\\3/4&1/2\end{pmatrix},
                 \qquad\det K=-1/16.
\tag{UN2}
\]

Both paired diagonal values are positive, but the local kernel is
indefinite even after unit projection. The two single-factor products
are F1=38/37 and F2=115/148. Dividing by those exact nonzero factors
gives the collision kernel

\[
 Q=\begin{pmatrix}1369/1444&4107/4370\\
                   4107/4370&10952/13225\end{pmatrix},
                 \qquad\det Q=-1874161/19096900<0.
\tag{UN3}
\]

The projector does not supply a local positive-kernel Cauchy extension
from paired frequencies to independent left/right frequencies.
This is a local factor and an exact native unit orbit, not a claim
that a whole finite Euler cutoff, complete physical norm-weighted
moment, or full radial row sum has this inertia. Those aggregates
have additional factors and rows. The full moment remains positive;
its centered critical remainder needs a separate signed estimate.

`check_unit_neutral_local_kernel.py` checks both actual finite fields,
all six unit symbols, the primary generators, and the exact rational
matrices and determinants. It does not authenticate a full source trace.
