# Independent review of the adjacent derivative packet

Status: ACCEPTED AT THE STATED SYNTHETIC / CONDITIONAL ANALYTIC SCOPE by an
independent agent in this research wave. This is not external community review,
formal verification, or an RH progress verdict.
Scope: the four exact source hashes below and the inherited S06 / R16 arguments
read during this review. The author's files were not edited.
What was actually run: `python ../verify_derivative_controls.py` passed
576 derivative geometry cases, 30 finite companion-sector cases, six strict
ray-root brackets and 64 moment-drift identities. No actual-xi evaluator ran.
Smallest remaining gap: no mathematical gap found in the stated objects;
their actual-theta low-order descent application remains explicitly open.

| Source in the parent `xi/` directory | SHA256 reviewed |
| --- | --- |
| `DERIVATIVE_COUNTEREXAMPLE.md` | `b52474ca156c45ddb073f24cd3afe2c7ac8e0027195f29d016b843bf4c39ccf0` |
| `COMPANION_SECTOR.md` | `9132831b9371607c8b12ffe08c77565b6f0497f3ef9bc165eafc3106748d323c` |
| `THETA_TAIL_OBSTRUCTION.md` | `06fb421509408d40ff993a4804b526c769f32428aa5ff3ed955a2c1cf20b2d8b` |
| `verify_derivative_controls.py` | `aeaa99bdfe0584e8760e64d59dc00bbf947599134878d14be3935cd81b8761bc` |

## 1. Complete narrow-strip zeros and the frozen derivative chain

The factorization into \(\cos z+c\) and \(\cos z-1/(2c)\) is correct.
For \(-c<-1\), the complete first factor has zeros
\((2k+1)\pi\pm i\delta\). The second factor has only the stated real
zeros. Their simplicity follows from the nonzero sine at either cosine
root. For a positive even derivative the cosine quadratic has one root in
\((-1,0)\) and one in \((0,1)\), since its signs at \(-1,0,1\) are
positive, negative, positive. For a positive odd derivative the additional
cosine root lies strictly in \((-1,0)\) and does not coincide with a sine
zero. Thus the complete all-order real-rootedness assertion follows from
the formulas, rather than the finite 576-case scan.

On \(\pi-iy\), direct differentiation gives
\(F'=ig\) and \(F''=-h\). Hence
\(E_{0,\lambda}=f+\lambda g\) and
\(E_{1,\lambda}=i(g+\lambda h)\), with the signs exactly as printed.
The function \(g+\lambda h\) is strictly positive for every \(y\ge0\),
and \(f+\lambda g\) increases from a negative value at zero to a positive
value at \(\delta\). This proves the unique lower-ray zero and the signed
quotient obstruction for every fixed \(\lambda>0\).

The residue \((1-\epsilon)/(4\epsilon-1)\), the quartic obtained by
multiplication by \(2q^2\), and the fixture \(-259/621\) all check.
For the quantitative zero bracket, \(h\) increases on \([0,\delta]\):
\(h'=\sinh y(16\epsilon\cosh y-1)>0\) away from zero. Integrating the
upper and lower curvature bounds produces the stated square-root bounds
with their directions correct. The thin-strip expansion
\(\rho=\delta^2/2+O(\delta^4)\) is also correct.

## 2. Companion parity and the 25/79 constant

From the Fourier integral,

\[
F^{(r)}=i^r\int u^r\Phi(u)
       \left(e^{izu}+(-1)^r e^{-izu}\right)du.
\]

Subtracting \(i\lambda F^{(r+1)}\), with the same frozen \(\lambda\),
gives exactly \(i^r(P+(-1)^rN)\). Differentiating changes the reflected
sign and gives \(i^{r+1}(P_1-(-1)^rN_1)\). No reflection term is lost.

The centered cosine inequality gives \(|P|\ge A(1-T^2v/2)\).
The two Cauchy--Schwarz reflection bounds and
\(mA\ge2M_r\mu\) give precisely the printed \(\alpha,\beta\).
The quotient identity \((1+n)/(1+d)\) then proves the disk enclosure.
Under the sufficient bounds, the first beta term is at most \(8/96\),
and the second is at most \(\sqrt{65}/96<9/96\); alpha is at most
\(8/96\). Thus the strict error bound \(25/79\) is valid.

The moments and the parity identities have the correct normalization even
though the discrete checker drops a common factor in the half-line masses.
That factor cancels from every mean, variance and quotient.

Minor interface clarification recommended: the positive tilted variance
uses the tilted \(u^{r+3}\) moment because the density includes
\(1+u/\mu\). The existing phrase "exponential integrability of the moments
needed below" covers it, so this is not a proof gap. Listing this moment
explicitly would make the generic source interface easier to implement.

The drift law and accumulated logarithmic lower bound are exact moment
identities. They do not prove failure of a method that accounts for drift,
and the source text retains that boundary.

## 3. Rouché margin and compact-source transfer

The bump transform is entire and even. Its normalized support bound gives
\(|B-1|<1/2\) throughout the chosen disk. The cosine Taylor remainder is
at most \(a^2\cosh(\delta+a)/2\le sa/8\), giving the first factor's
\(7sa/8\) margin. The second factor has margin at least \(3c/4\).
Together the actual product estimate is stronger than the quoted bound:

\[
|BC|>\frac{21}{32}\epsilon csa
        >\frac12\epsilon csa.
\]

The theta perturbation is at most \(\epsilon csa/4\) on the same
boundary. The disk contains exactly the one simple upper zero of the
trigonometric source and excludes its conjugate and all real zeros.
Rouché therefore proves a nonreal zero of the complete smooth transform.
The factor two in the Fourier transform is correct: the half-line bump
coefficient \(1/2\) produces \(B(z)\cos z\).

The smooth source has an even extension at zero: the two translated bumps
vanish in a neighborhood of zero, and the theta component has the matching
jets established by inherited R16. It is strictly positive, including at
zero, because \(\tau>0\) and the theta density is positive.

The transfer of inherited S06 is legitimate for each fixed perturbation.
On \([0,U]\), positivity and smoothness bound \((\log\Phi_*)''\) above;
\(-r/u^2\) dominates that bound uniformly for sufficiently large \(r\).
Beyond \(U\), the theta tail is exact and its second log derivative is
eventually negative. Thus the tilted density is globally strictly log
concave at high order. Its high-order modes leave the compact support, so
the unit saddle neighborhoods have exactly the theta log-derivative
estimates. The exterior exponential argument and the two cases
\(y\le r/w\), \(y\ge r/w\) give S06's uniform variance estimate with
constants and starting order depending on the fixed perturbation.
The stated regime \(T^2\log r/r\to0\) follows. There is no asserted
uniformity over arbitrary compact perturbations or near-linear regime.

The compact/theta ratio and the total-variation bound are correct.
For every prescribed fixed exponential rate, choose \(V>U\) once to
make \((U/V)^r\) decay at that rate; the prefactor may depend strongly
on \(V\). The text correctly separates weighted moments from total
variation of probability measures.

## 4. Scope relative to inherited mathematics

The inherited S06 proof already supplies the frozen-companion high-order
entry mechanism and the moment/variance tools. The new sector statement is
an explicit finite sufficient criterion extracted from those tools, with
an unoptimized numerical constant. The moment drift reformulates the
already audited varying-parameter defect.

The discrete and smooth sources make the existing low-order boundary
concrete. Their elementary countermodels do not challenge a source-faithful
exact-theta descent estimate. The unchanged-tail construction uses generic
Rouché and saddle stability; no mathematical priority claim is justified
by this repository comparison. It supplies a precise source-class
obstruction, not a new RH-positive estimate.

The finite checker authenticates its exact finite controls only. It does
not certify the analytic Rouché or uniform saddle arguments, which were
reviewed on paper here, and it does not evaluate actual xi.
