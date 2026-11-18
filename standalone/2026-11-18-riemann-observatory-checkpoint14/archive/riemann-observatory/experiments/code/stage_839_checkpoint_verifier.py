"""Stage the pinned verifier with narrow checkpoint hooks, leaving the vendor file unchanged."""
import argparse
from hashlib import sha256
from pathlib import Path


CODE = Path(__file__).resolve().parent
SOURCE = CODE / "vendor/839_reference/verify.cpp"
EXPECTED_SHA256 = "c30310214c121d0acf4b4ae562f396c1e13be13992b1f01e02df584dbd602142"


def stage():
    raw = SOURCE.read_bytes()
    if sha256(raw).hexdigest() != EXPECTED_SHA256:
        raise ValueError("Pinned verifier source digest mismatch")
    source = raw.decode()
    edits = [
        ("#include <expected>\n", "#include <expected>\n#include <filesystem>\n#include <fcntl.h>\n#include <unistd.h>\n"),
        ("    StackExhausted\n", "    StackExhausted,\n    CheckpointError,\n    CheckpointPause\n"),
        ("// The cells that the distance of a pair can lie in", (CODE / "839_reference_checkpoint.inc").read_text()
         + "\n// The cells that the distance of a pair can lie in"),
        ("    [[nodiscard]] std::expected<void, Error> run() {",
         "    [[nodiscard]] std::expected<void, Error> run(const SearchCheckpoint& checkpoint) {"),
        ("        while (stackSize > 0U) {\n            --stackSize;",
         """        if (!checkpoint.load(statistics_, stack_, stackSize, parameters)) {
            return std::unexpected(Error::CheckpointError);
        }
        while (stackSize > 0U) {
            if (!checkpoint.path.empty() && statistics_.nodes > 0U &&
                ((statistics_.nodes % checkpoint.interval) == 0U || statistics_.nodes == checkpoint.pauseAt)) {
                if (!checkpoint.save(statistics_, stack_, stackSize)) {
                    return std::unexpected(Error::CheckpointError);
                }
                if (statistics_.nodes == checkpoint.pauseAt) {
                    return std::unexpected(Error::CheckpointPause);
                }
            }
            --stackSize;"""),
        ("            statistics_.maximumStack = std::max(statistics_.maximumStack, stackSize);\n        }\n        return {};",
         """            statistics_.maximumStack = std::max(statistics_.maximumStack, stackSize);
        }
        if (!checkpoint.save(statistics_, stack_, stackSize)) {
            return std::unexpected(Error::CheckpointError);
        }
        return {};"""),
        ('        return "the stack of boxes is full";',
         '''        return "the stack of boxes is full";
    case Error::CheckpointError:
        return "checkpoint data or I/O error";
    case Error::CheckpointPause:
        return "intentional pause after durable checkpoint";'''),
        ('''    if (arguments.size() != 3U) {
        std::cerr << "usage: verify params.txt kernel_lower.bin\\n";
        return ExitCode::UsageError;
    }''',
         '''    if ((arguments.size() != 3U) && (arguments.size() != 5U) && (arguments.size() != 6U)) {
        std::cerr << "usage: verify params.txt kernel_lower.bin [checkpoint identity [test-pause-at-node-count]]\\n";
        return ExitCode::UsageError;
    }
    SearchCheckpoint checkpoint{};
    if (arguments.size() >= 5U) {
        checkpoint.path = arguments[3U];
        checkpoint.identity = arguments[4U];
        if (checkpoint.path.empty() || checkpoint.identity.size() != 64U ||
            checkpoint.identity.find_first_not_of("0123456789abcdef") != std::string::npos) {
            return ExitCode::UsageError;
        }
    }
    if (arguments.size() == 6U) {
        const auto& value = arguments[5U];
        if (value.empty() || value.find_first_not_of("0123456789") != std::string::npos) {
            return ExitCode::UsageError;
        }
        std::istringstream parser{value};
        if (!(parser >> checkpoint.pauseAt) || checkpoint.pauseAt == 0U) {
            return ExitCode::UsageError;
        }
    }'''),
        ("    const std::expected<void, Error> outcome{search.run()};",
         "    const std::expected<void, Error> outcome{search.run(checkpoint)};"),
        ('        if (outcome.error() != Error::Unresolved) {',
         '''        if (outcome.error() == Error::CheckpointPause) {
            return static_cast<ExitCode>(75U);
        }
        if (outcome.error() != Error::Unresolved) {'''),
        ("#include <span>\n", "#include <span>\n#include <sstream>\n"),
    ]
    for old, new in edits:
        if source.count(old) != 1:
            raise ValueError(f"Nonunique checkpoint insertion anchor: {old!r}")
        source = source.replace(old, new)
    return source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    args.destination.write_text(stage())
