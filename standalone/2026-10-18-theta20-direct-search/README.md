# Direct degree-20 theta search — unsuccessful exploratory pass

**Status: NO_DEGREE_20_CERTIFICATE. No new RH theorem, zero-free boundary,
critical native estimate, or improved certified theta realization is claimed.**
This is a preserved numerical investigation and a reusable full-state search
implementation, not a proof packet. Nothing here changes #988 or #992.

## What was attempted

The exact degree-18 constructions in #981/#988 and the local positive-loop
operation in #992 suggested a concrete target: match the next even moment,
through degree 20, without leaving the ferromagnetic parameter class. This
pass tried simultaneous representative-edge directions, grouped dense graphs,
full small visible-spin graphs, hidden-spin extensions, and independent
Gaussian convolutions. The Gaussian models are a different probability-law
ansatz, not finite Ising realizations with the same spin count.

**None of the searches reached a validated root.** In particular, no new
configuration is certified to match even the lower nine equations exactly.
A small residual below is not comparable to the certified raw twentieth-moment
excess of an upstream model whose lower moments match exactly.

## Recorded outcomes

The objective is the Euclidean norm of ten approximate orthogonal-polynomial
expectations E[p_2(Y)], ..., E[p_20(Y)]. The polynomials are derived from the
numerical theta moments in `target.json`. It is NOT the raw moment-20 error.

| Search family | Recorded objective norm | Result |
|---|---:|---|
| Four dense groups, 32 visible spins | 3.25482328695e-4 | No root |
| Six dense groups, 44 visible spins | 2.11009208822e-5 | No root |
| Five groups, 12 visible spins, Gaussian convolution | 9.25075145478e-6 | No root |
| 12 visible + 3 hidden spins, Gaussian convolution | 1.26866684567e-5 | No root |
| Complete 12-visible-spin graph, Gaussian convolution | 1.02947062492e-5 | No root |
| Complete 12-visible + 3 hidden graph, Gaussian convolution | 9.55162815391e-6 | No root |
| Same complete visible graph, negative couplings permitted | 5.39727070530e-7 | REJECTED for Lee–Yang use |

The rejected last run has minimum coupling approximately -0.136967270586.
It is also not an exact numerical root. Its smaller objective supplies neither
a ferromagnetic solution nor an impossibility proof for the positive class.
The boundary reached by an optimizer is not a mathematical obstruction.

Separately, `loop_tangent.py` considers 54 new edges between the eleven
representative component roots of #992, excluding its existing (7,9) edge.
This is NOT every missing edge of the 282-spin graph. A numerical linear
program under its stated 20%-margin tangent box predicts a -0.00762814352
raw next-moment change. No nonlinear path or endpoint was validated; the LP
is not a degree-20 existence or nonexistence certificate.

## Reproduction

Python, NumPy, SciPy and mpmath are required. Exact versions actually used are
in `EXECUTION.json`. No network is required for replay.

```sh
python test_models.py
python -O test_models.py
python replay_candidates.py
python -O replay_candidates.py
```

The nine tests include exact rational compressed-versus-full Gibbs sums,
exact covariance differentiation, hidden-spin enumeration, Gaussian moment
checks, numerical analytic-Jacobian checks, and rejection of invalid signs.
Their scope is finite assembly, not the theta source or an infinite theorem.

`CANDIDATE_REPLAY.json` records successful re-evaluation of unsuccessful
candidates. The program deliberately never promotes a small objective to a
certificate. To continue a bounded admissible search into a NEW file:

```sh
python search.py --steps 100 --output new_candidate.json
```

Historical development scripts and candidate records are preserved separately.
The main reusable interface is `models.py`; the historical scripts are not
presented as an independently reviewed software library. `loop_tangent.py`
writes a separate recomputation file and does not change its old receipt.

## Source and numerical limitations

`theta_source.py` freshly recomputed moments through degree 40 using 60-digit
mpmath quadrature, eight explicit theta indices and integration on [0,3].
The stored search moments agree at relative error below 3.8e-55. Formula-based
bounds for the omitted index/time tails are included. **Neither quadrature
nor arithmetic errors were enclosed by directed intervals.** Agreement of
precision runs is not a source certificate. The degree-40 moments are used
only to condition a search for matching through degree 20.

No upstream directed source/root certificate was rerun, no interval Newton
or Krawczyk acceptance test passed, and no independently reviewed new theorem
was produced. Every search result is exploratory. Failed/timed-out development
attempts are not counted as certificates. An early grouped random initial guess
exceeded its upper bound; that run failed and the initialization was corrected.

## Exact upstream scope

- #992: `b586b518a8de634444c1e987a0bba03c593198f0`, source density,
  positive-loop parameters, exact conditional graph law, and local covariance
  operation. Its certification is prior work, not new verification here.
- #988: `86c156baa3f10296a26e066f5f4d276776b79c27`, consulted at PR-description
  scope; its distinct lower discrepancy is not surpassed by any certificate here.
- #991: `b4d97d837214cf14fc09c093f66a50e798288afa`, the preceding extraction
  improvement leaves its fixed-denominator mean bound open. No such bound was
  derived from this spin investigation.

The finite-state formulas, moment conditioning and Gibbs covariance derivative
are classical. No worldwide novelty or best-known-result claim is made.

## Publication

**NOT PUSHED.** The current connected GitHub actions expose reads/searches but
no create/update/push action. The available container has no gh executable or
GitHub-token environment variable; GitHub DNS lookup failed. See
`PUBLICATION_ACCESS.json`. No new remote branch, PR, or commit was created.
The add-only patch is prepared for the #992 snapshot above and changes no
inherited proof, certificate, or integrated status.
