# Two-cluster replay record

Status: AUTHOR VALIDATED; independent proof/source review and freeze pending.

The producer first authenticates frozen mixed packet
a7334a169cfa8ca5b1f0721692d9c888e79ba5cb, including its proof, preregistration,
producer, artifact and test binding. That predecessor in turn authenticates
the frozen E4 and actual theta-source chain.

Author run:

    python two_cluster_replay.py --write
    python two_cluster_replay.py --check
    python -O two_cluster_replay.py --check
    python -m unittest tests/test_architecture_e_pass_two_cluster.py
    python -O -m unittest tests/test_architecture_e_pass_two_cluster.py

Ruff check and format passed before the final write. All three producer modes
passed. All 17 tests passed in ordinary Python (1.462 s) and optimized Python
(1.462 s). Final proof SHA-256:
bb1b82864ec8657ef1670f9af0986c0a8ef93e427551ab7bfacfa2ba41c60e7e.

The replay reconstructs the complete rational Sylvester solution, both block
similarity products, a separate cubic functional-calculus control, literal
exponential source functions, and the confluent Newton residual. It also
checks every rational bound used in the continuum proof. It samples no Xi
values and does not infer continuum positivity from the three panels.

