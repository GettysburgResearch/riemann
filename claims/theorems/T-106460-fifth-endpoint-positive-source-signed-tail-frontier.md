# T-106460 — Fifth-endpoint positive-source signed-tail frontier for ninety percent

Claim ID: `T-106460`  
Status: **UNCONDITIONAL EXACT REDUCTION; ONE SIGNED SHALLOW-COMPANION ESTIMATE OPEN**  
Created: 2026-08-25  
Depends on: `L-106432--L-106439`; pinned fifth-derivative input used by `T-105290`  
RH status: **unproved**

The direct `K=5` endpoint telescope combines the strongest pinned fixed-order
real-zero input on this branch with one actual-Xi positive source.  It avoids
five separate reverse--Rolle rungs and their coherent physical assembly.

## 1. Direct fifth endpoint

Put

\[
\boxed{
U_{5,T}
 ={(\Xi-i\lambda_T\Xi')
    (\Xi^{(5)}+i\lambda_T\Xi^{(6)})
   \over
   (\Xi+i\lambda_T\Xi')
    (\Xi^{(5)}-i\lambda_T\Xi^{(6)})}.
}
\tag{T-106460.1}
\]

At finite regular scope,

\[
\operatorname{wind}U_{5,T}=R_0(T,2T)-R_5(T,2T).
\]

The surviving numerator is

\[
2i\lambda_T
\bigl(\Xi\Xi^{(6)}-\Xi'\Xi^{(5)}\bigr).
\]

By `L-106439`, up to a fixed harmless sign its Fourier transform is

\[
\boxed{
\Lambda_5(\xi)
 ={1\over2}\int
 (v-u)(v^5-u^5)
 \Phi(u)\Phi(v)du
 \ge0.
}
\tag{T-106460.2}
\]

Thus the literal actual-Xi endpoint numerator is already a positive Hankel
source; no frozen-to-actual numerator transfer remains.

## 2. Correct hard-band split

For a predeclared positive-frequency bandwidth `H_T`, define

\[
V_{5,T}
 =\int_0^\infty
 \min(H_T,\xi)|\widehat U_{5,T}(-\xi)|^2d\xi,
\]

and

\[
\Delta_{5,T}
 =\int_{H_T}^\infty(\xi-H_T)
 \bigl(
  |\widehat U_{5,T}(-\xi)|^2
  -|\widehat U_{5,T}(\xi)|^2
 \bigr)d\xi.
\]

Then exactly

\[
\boxed{
R_0(T,2T)
\ge R_5(T,2T)
 -V_{5,T}-(\Delta_{5,T})_+-o(N).
}
\tag{T-106460.3}

Both terms are literal quotient quantities and have the residue/model-space
normal forms of `L-106433--L-106436`.

## 3. Visible term from divisor height mass

For a finite canonical-product truncation `p_T` of degree `n_T`, the fifth
endpoint denominator is

\[
D_{5,T}
 =(p_T+i\lambda_Tp_T')
  (p_T^{(5)}-i\lambda_Tp_T^{(6)}).
\]

The proof of `L-106437--L-106438` applies without change and gives

\[
\boxed{
V_{5,T}
 \le8H_T\mathfrak h(p_T)
     +8\lambda_TH_T n_T.
}
\tag{T-106460.4}

Define `HEIGHTBAND106460` to mean a source-pinned cofinal truncation and
predeclared parameters satisfying

\[
{H_T\mathfrak h(p_T)\over N(T,2T)}\to0,
\qquad
{n_T\over N(T,2T)}=1+o(1),
\qquad
\lambda_TH_T\to0,
\]

with all window, outer-factor and confluent tails `o(N)`.  Under this input,

\[
V_{5,T}=o(N).
\]

The finite inequality is proved.  The Xi cofinal statement requires a pinned
quantitative zero-density/truncation passage and is not silently assumed.

## 4. Ninety-percent constant

The retained unconditional fixed-order input is

\[
\liminf {R_5(T,2T)\over N(T,2T)}>{997\over1000}.
\]

Its margin above ninety percent is

\[
{997\over1000}-{9\over10}={97\over1000}.
\]

Define

```text
FIFTHSIGNED106460:

limsup_(T->infinity)
 (Delta_(5,T))_+ / N(T,2T)
 < 97/1000.
```

Then

\[
\boxed{
\mathrm{HEIGHTBAND}_{106460}
+\mathrm{FIFTHSIGNED}_{106460}
\Longrightarrow
\liminf_{T\to\infty}{N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-106460.5}

More generally, if a fixed order `K` has a pinned real-zero proportion
`alpha_K`, the direct endpoint block needs total visible plus signed-tail cost
strictly below `alpha_K-0.9`.

## 5. Improvement over the five-rung assembly

The theorem removes the following former interfaces:

```text
five separate companion windings;
intermediate derivative companions;
phase-family diagonal excess at each rung;
cross-rung coherent Hankel assembly;
frozen-to-actual numerator identification.
```

The surviving conclusion-bearing object is one signed tail for the actual
fifth endpoint quotient.  It is an explicit difference of shallow pole/zero
residue Grams.  A bound below `9.7%` is sufficient; a subpower estimate is not
needed for ninety percent.

## 6. Boundary

```text
all-order endpoint telescope                    PROVED EXACT
K=5 exterior-square positive Xi source          PROVED UNCONDITIONALLY
finite visible height-mass estimate              PROVED EXACT
HEIGHTBAND106460 Xi cofinal passage              OPEN / SOURCE-PIN REQUIRED
FIFTHSIGNED106460                               OPEN / RECORD-BEARING
conditional ninety-percent implication          PROVED EXACT
ninety percent / density one / RH               UNPROVED
```
