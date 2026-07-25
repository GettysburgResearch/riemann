# Workflow trigger

This child branch exists only to trigger the `d0801-circulant-completion` workflow defined on its base branch.

The workflow now:

1. byte-replays the completed X-2805 one-direction Schur target gate;
2. replays the exact L-8505 static operator budget;
3. runs all adversarial exact checker and hybrid-merger tests;
4. compiles the vector-independent binary80/binary128 coefficient producer under the audited floating contract;
5. evaluates target segment 2000 as a real coefficient-shard control;
6. reconstructs the complete discovery Toeplitz matrix;
7. solves optimized Hermitian circulant-completion LPs at sizes 2048, 2560, 3072, and 4096.

No numerical sign from this trigger is a proof. A successful completion or fast shard must still be frozen, replayed, and independently audited under its declared proof contract.

Retriggered after adding L-8503--L-8505 and the hybrid coefficient-source implementation.
