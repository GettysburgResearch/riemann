"""Record hashes and counters of observed durable checkpoint files."""
import argparse
import datetime
import fcntl
from hashlib import sha256
import json
from pathlib import Path

from replay_839_later_windows import WINDOWS, save


def add_observation(history, report, data, label):
    fields = data.splitlines()[0].decode().split()
    magic, identity, points, *numbers = fields
    if (magic, identity, int(points)) != (
        "observatory-839-checkpoint-v1", report["checkpoint_identity"], WINDOWS[label][0]
    ):
        raise ValueError(f"Observed checkpoint identity mismatch for {label}")
    counts = dict(zip(("nodes", "leaves", "basic", "affine", "max_stack", "waiting"), map(int, numbers), strict=True))
    if counts["nodes"] + 1 != 2 * counts["leaves"] + counts["waiting"]:
        raise ValueError(f"Observed checkpoint counters inconsistent for {label}")
    digest = sha256(data).hexdigest()
    previous = history[-1] if history else None
    if previous and previous["checkpoint_sha256"] == digest:
        return
    if previous and counts["nodes"] < previous["counts"]["nodes"]:
        raise ValueError(f"Durable checkpoint rolled back for {label}")
    record = {
        "observed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "attempt_utc": report["attempt_utc"], "worker_pid": report["pid"],
        "checkpoint_identity": identity, "checkpoint_sha256": digest, "counts": counts,
        "previous_observation_sha256": previous["observation_sha256"] if previous else None,
    }
    record["observation_sha256"] = sha256(json.dumps(record, sort_keys=True).encode()).hexdigest()
    history.append(record)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--result-dir", type=Path, required=True)
    args = parser.parse_args()
    history_path = args.result_dir / "839_checkpoint_observation_history.json"
    with (args.work_dir / "observatory-history.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        full = json.loads(history_path.read_text()) if history_path.exists() else {
            "scope": "Periodic observations of trusted local durable state, not a proof of earlier traversal prefix.",
            "windows": {label: [] for label in WINDOWS},
        }
        for label in WINDOWS:
            state = args.work_dir / label / "search.checkpoint"
            report = args.result_dir / f"839_reference_{label}_checkpoint_replay.json"
            if state.exists() and report.exists():
                add_observation(full["windows"][label], json.loads(report.read_text()), state.read_bytes(), label)
        save(history_path, full)
    for label, records in full["windows"].items():
        if records:
            print(label, records[-1]["counts"], records[-1]["checkpoint_sha256"])


if __name__ == "__main__":
    main()
