"""One explicit policy for original-analysis distributions, including PDF scope."""
from pathlib import PurePosixPath

PRIVATE_PARTS = frozenset({'sources', 'raw_discovery', '__pycache__', '.git', '.lake',
                           'uniform78_rmt_sources'})
ORIGINAL_PDFS = frozenset({
    'final_synthesis/synthesis.pdf',
    'experiments/results/witness62_prefix_transition.pdf',
    'experiments/results/witness62_weighted_criterion_phase.pdf',
    'experiments/results/augmented_moment63_escape.pdf',
    'experiments/results/probability_chains64.pdf',
    'experiments/results/prime_band_round11.pdf',
})


def is_distributable(relative):
    path = PurePosixPath(str(relative))
    return (not (set(path.parts) & PRIVATE_PARTS)
            and path.suffix.lower() not in {'.pyc', '.zip'}
            and (path.suffix.lower() != '.pdf' or str(path) in ORIGINAL_PDFS))
