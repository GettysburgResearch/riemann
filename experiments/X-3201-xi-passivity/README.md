# X-3201 — Reconnaissance for xi-log-derivative passivity violations

Experiment ID: X-3201  
Status: EMPIRICAL  
Agent: `gpt56-06`  
Issue: #32  
Date: 2026-07-23  
Related claims: D-3201, L-3201, L-3202, M-3201  
Candidate IDs: none

## Research question

Can the RH condition

\[
\operatorname{Re}\frac{\xi'(s)}{\xi(s)}>0,
\qquad \operatorname{Re}s>1/2,
\]

be turned into a compact point or Pick-matrix counterexample search with clear
synthetic controls?

## What this experiment does

`prototype.py` implements, with ordinary `mpmath` arithmetic,

\[
\frac{\xi'(s)}{\xi(s)}=
\frac1s+\frac1{s-1}-\frac12\log\pi
+\frac12\psi(s/2)+\frac{\zeta'(s)}{\zeta(s)}
\]

and the finite kernel

\[
K_{jk}=
\frac{F(s_j)+\overline{F(s_k)}}{s_j+\overline{s_k}-1}.
\]

It has three roles:

1. an RH-compatible synthetic zero set on `Re(rho)=1/2`, which must produce
   positive scalar values and a positive Pick matrix;
2. a functional-equation-symmetric off-line synthetic orbit
   `{0.6±20i,0.4±20i}`, which must produce a negative witness;
3. low-height `xi` calibration at modest points where the real part is known
   empirically to be positive.

This is not a ball-arithmetic verifier.

## Run

```bash
python prototype.py --dps 80 --output results/calibration.json
python -m unittest discover -s tests -v
python -m py_compile prototype.py tests/test_prototype.py
```

Dependency:

```bash
python -m pip install -r requirements.txt
```

## Recorded result

At 80 decimal digits:

- seven unit tests passed;
- the on-line synthetic `3x3` Pick matrix had smallest eigenvalue
  approximately `0.0582185316491`;
- the off-line synthetic point `0.55+20i` had
  `Re F approximately -13.3332708346`;
- the off-line synthetic `2x2` Pick matrix had smallest eigenvalue
  approximately `-315.300391406`;
- the six low-height `xi` calibration real parts were positive;
- the low-height `4x4` Pick matrix had smallest eigenvalue approximately
  `0.0925292686838`.

The committed JSON digest is printed in the session report.

## Tests

The tests cover:

- scalar positivity for a finite on-line zero set;
- positive-semidefinite Pick behavior for that set;
- scalar and matrix negativity for an off-line symmetric orbit;
- Hermitian kernel assembly;
- the completed functional equation `F(1-s)=-F(s)`;
- low-height sign calibration;
- rejection of points on or left of the critical line.

## Limitations

1. `mpmath` gives no rigorous error bounds.
2. The actual calibration points are far below the current certified zero
   height and cannot be new candidates.
3. No search above `3*10^12` was run.
4. Eigenvalues are reconnaissance diagnostics only; L-3202 promotes a fixed
   exact-vector Rayleigh form instead.
5. The synthetic controls validate conventions, not the analytic theorem.

## Next experiment

Implement the same formulas with FLINT/Arb balls and exact dyadic inputs. The
first proof-grade milestone is a calibration certificate, not a counterexample
claim.
