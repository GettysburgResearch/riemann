# Uniform log-phase port of the canonical dyadic wavelet

**Status:** exact operator theorem on norm-step extensions.  It evaluates no
L-function family and proves no arithmetic statement about `XD`, `HCNC`, or
`BPOE`.  It is not an RH or GRH result.

**Exact dependencies:** the norm-lattice obstruction packet and the integrated
minimal-wavelet/XD residency summary, locked by LF-normalized SHA-256 in the
producer.

**What was run:** exact symbolic arithmetic in
\(\mathbf Q(\sqrt2)[\alpha]\), with fewer than 4096 symbolic term updates and
no numerical approximation to a logarithm or square root.

**Smallest remaining gap:** attach this continuous phase ledger to an actual
source-faithful function-field analogue, including its carrier and owner
coordinates.  Nothing here supplies that arithmetic adapter.

## 1. Retaining the phase

Fix an integer base \(q\geq 2\), put

\[
        \alpha=\log_q 2,
\]

and extend a degree sequence \((a_n)_{n\in\mathbf Z}\) to a right-continuous
norm-step function by

\[
        F(q^{n+t})=a_n,\qquad 0\leq t<1.
\]

For the literal physical dilation \(2^j\), direct use of the step extension
gives

\[
 (S_{2^j}F)(q^{n+t})=a_{n-d_j(t)},
 \qquad
 d_j(t)=\lceil j\alpha-t\rceil.
\tag{1}
\]

Thus the phase-dependent symbol of the canonical kernel

\[
 K_1=(I-\sqrt2S_2)(I-S_2)^2
\]

is

\[
 k_{q,t}(z)=\sum_{j=0}^3c_jz^{d_j(t)},
 \qquad
 (c_0,c_1,c_2,c_3)
 =\bigl(1,-(2+\sqrt2),1+2\sqrt2,-\sqrt2\bigr).
\tag{2}
\]

This retains the continuous log-phase that endpoint sampling discarded in the
norm-lattice obstruction packet.  The object studied below is the uniform
operator average

\[
             \bar k_q(z)=\int_0^1 k_{q,t}(z)\,dt.
\tag{3}
\]

It is an operator average, not an average over curves, characters, or
L-functions.

## 2. The double zero is restored formally

Write \(x=m+\beta\), with \(m\in\mathbf Z\) and \(0\leq\beta<1\).  Apart from
an irrelevant endpoint,

\[
 \lceil x-t\rceil=
 \begin{cases}
 m+1,&0\leq t<\beta,\\
 m,&\beta\leq t<1.
 \end{cases}
\]

Consequently,

\[
       \int_0^1\lceil x-t\rceil\,dt=x,
\qquad
       \boxed{\int_0^1d_j(t)\,dt=j\alpha.}
\tag{4}
\]

The two coefficient identities

\[
       \sum_{j=0}^3c_j=0,
       \qquad
       \sum_{j=0}^3j c_j=0
\tag{5}
\]

now imply

\[
 \bar k_q(1)=0,
 \qquad
 \bar k_q'(1)
 =\sum_jc_j\int_0^1d_j(t)\,dt
 =\alpha\sum_jj c_j=0.
\tag{6}
\]

Therefore uniform phase averaging always restores at least the two formal
constant/linear cancellations of the literal kernel.  The next calculation
shows that this can mean either a genuine second difference or complete
annihilation.

## 3. Exact piecewise collapse

For each \(j\), if \(m_j=\lfloor j\alpha\rfloor\) and
\(\beta_j=j\alpha-m_j\), then

\[
 \int_0^1z^{d_j(t)}\,dt
 =(1-\beta_j)z^{m_j}+\beta_jz^{m_j+1}.
\tag{7}
\]

Substitution in (2) gives the following complete integer-base result:

| integer base | exact phase-averaged symbol |
|---|---|
| \(q=2\) | \(1-(2+\sqrt2)z+(1+2\sqrt2)z^2-\sqrt2z^3\) |
| \(q=3\) | \(\bigl((2+\sqrt2)\alpha-(1+\sqrt2)\bigr)(1-z)^2\) |
| \(q=4\) | \(-\frac{\sqrt2}{2}(1-z)^2\) |
| \(5\leq q\leq7\) | \(\sqrt2(1-3\alpha)(1-z)^2\) |
| \(q\geq8\) | \(0\) |

In particular, for the odd prime-power panels requested by the atlas,

\[
\boxed{
\begin{aligned}
q=3:&\quad
 \bar k_q(z)=\bigl((2+\sqrt2)\alpha-(1+\sqrt2)\bigr)(1-z)^2,\\
q=5,7:&\quad
 \bar k_q(z)=\sqrt2(1-3\alpha)(1-z)^2,\\
q\geq9\text{ odd}:&\quad \bar k_q(z)=0.
\end{aligned}}
\tag{8}
\]

The first two scalars in (8) are nonzero.  For \(q=3\),
\(\alpha<2/3<1/\sqrt2\), while the scalar's unique zero is
\(\alpha=1/\sqrt2\).  For \(q=5,7\), one has \(\alpha>1/3\).
Thus the first two rows have a zero of exactly order two at \(z=1\).

For \(q>8\), all \(j\alpha\) with \(1\leq j\leq3\) lie in \((0,1)\), so
(7) is simply

\[
        (1-j\alpha)+j\alpha z.
\]

Both coefficients vanish after summing against \(c_j\), by (5).  The same
formula holds almost everywhere at the boundary \(q=8\), where
\(3\alpha=1\).  Hence the last row really is the zero operator, not merely a
higher-order zero.

At \(q=2\), \(\alpha=1\) and \(d_j(t)=j\) almost everywhere, so there is no
phase collapse at all.  This native control does not construct the separate
characteristic-two arithmetic family that a function-field application would
need.

## 4. The killed average retains phase energy

To quantify what averaging discards, use the degree-linear test sequence
\(a_n=n\).  Since \(\sum c_j=0\), (1)--(2) give

\[
 (K_{q,t}a)_n=-D_q(t),
 \qquad
 D_q(t)=\sum_{j=0}^3c_jd_j(t).
\tag{9}
\]

Equation (4) and the second identity in (5) show exactly that

\[
          \int_0^1D_q(t)\,dt=0.
\tag{10}
\]

The full phase cells and their values are:

| base regime | successive phase-cell lengths | successive values of \(D_q\) |
|---|---|---|
| \(q=2\) | \(1\) | \(0\) |
| \(3\leq q\leq4\) | \(2\alpha-1,\ 1-\alpha,\ 2\alpha-1,\ 2-3\alpha\) | \(\sqrt2,\ -(1+\sqrt2),\ 1,\ 1+\sqrt2\) |
| \(5\leq q\leq7\) | \(3\alpha-1,\ 1-2\alpha,\ \alpha,\ 1-2\alpha\) | \(-(1+\sqrt2),\ -1,\ 1+\sqrt2,\ -\sqrt2\) |
| \(q\geq8\) | \(\alpha,\alpha,\alpha,\ 1-3\alpha\) | \(-1,\ 1+\sqrt2,\ -\sqrt2,\ 0\) |

Zero-length cells at \(q=4\) and \(q=8\) are harmless.  Squaring and
integrating yields

\[
\boxed{
 \int_0^1|D_q(t)|^2\,dt=
 \begin{cases}
 0,&q=2,\\
 (6+6\sqrt2)-(6+8\sqrt2)\alpha,&3\leq q\leq4,\\
 -2\sqrt2+(6+8\sqrt2)\alpha,&5\leq q\leq7,\\
 (6+2\sqrt2)\alpha,&q\geq8.
 \end{cases}}
\tag{11}
\]

The last line confirms the proposed simplification

\[
       \boxed{\int_0^1|D_q(t)|^2\,dt
       =2(3+\sqrt2)\alpha\quad(q\geq8).}
\tag{12}
\]

It is strictly positive for every finite \(q\), even though
\(\bar k_q=0\).  Thus, in the large-base regime,

\[
 \left(\int_0^1K_{q,t}\,dt\right)a=0
 \quad\text{but}\quad
 \int_0^1|K_{q,t}a|^2\,dt>0.
\tag{13}
\]

Uniform phase integration kills the detector while retaining a nontrivial
phase-fluctuation ledger.  Any arithmetic port that averages the operator
before measuring its energy would erase precisely this information.

## 5. Interpretation and firewall

The result answers the narrow operator question.

* At \(q=3,5,7\), uniform phase averaging repairs the endpoint loss of the
  second cancellation, but collapses the literal four-shell kernel to a
  scalar native second difference.
* At every integer \(q\geq8\), it repairs the cancellation only by making the
  averaged operator identically zero.
* The phase-resolved operator remains nontrivial, as witnessed by the exact
  positive energy (11)--(12).

No L-function, Frobenius class, curve, character, owner coordinate, carrier,
or physical occupancy is evaluated.  In particular, this does not prove that
averaging is legitimate inside canonical `XD`, oriented `HCNC`, or `BPOE`,
and it does not produce a source-faithful function-field version of any of
them.  It is an exact warning about which information uniform phase averaging
retains and destroys on norm-step extensions.

## 6. Provenance and replay

The producer locks all four files of the preceding norm-lattice packet and
the integrated minimal-wavelet/XD summary.  The JSON claim payload represents
every scalar by its coefficients in
\(\mathbf Q(\sqrt2)[\alpha]\); it contains no floating-point values.

Replay from the repository root:

```text
python -B research/l-families/atlas/function_field/canonical_dyadic_log_phase_port.py --check
python -B -O research/l-families/atlas/function_field/canonical_dyadic_log_phase_port.py --check
python -B -m unittest tests.test_canonical_dyadic_log_phase_port
python -B -O -m unittest tests.test_canonical_dyadic_log_phase_port
```
