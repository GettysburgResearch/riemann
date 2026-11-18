// Observatory checkpoint adapter for the staged C++ reference verifier.
// This adapter has no mathematical acceptance predicates.
bool syncCheckpointPath(const std::filesystem::path& path, const int flags) {
    const int descriptor = ::open(path.c_str(), flags);
    if (descriptor < 0) {
        return false;
    }
    const bool synced = ::fsync(descriptor) == 0;
    const bool closed = ::close(descriptor) == 0;
    return synced && closed;
}

class SearchCheckpoint {
  public:
    std::filesystem::path path;
    std::string identity;
    std::uint64_t interval{1000000U};
    std::uint64_t pauseAt{};

    bool load(Statistics& stats, std::array<Box, kStackCapacity>& stack, std::size_t& size,
              const Parameters& parameters) const {
        if (path.empty()) {
            return true;
        }
        std::error_code error{};
        const bool exists = std::filesystem::exists(path, error);
        if (!exists) {
            return !error;
        }
        std::ifstream input{path};
        std::string magic;
        std::string storedIdentity;
        std::size_t points{};
        if (!(input >> magic >> storedIdentity >> points >> stats.nodes >> stats.leaves >> stats.basic >> stats.affine
                    >> stats.maximumStack >> size) ||
            magic != "observatory-839-checkpoint-v1" || storedIdentity != identity || points != kPointCount ||
            size >= kStackCapacity || size > stats.maximumStack ||
            stats.maximumStack == 0 || stats.maximumStack >= kStackCapacity ||
            stats.nodes > std::numeric_limits<std::uint64_t>::max() / 2U ||
            stats.leaves > stats.nodes || stats.basic > stats.leaves ||
            stats.affine != stats.leaves - stats.basic ||
            stats.nodes + 1U != 2U * stats.leaves + size) {
            return false;
        }
        for (std::size_t index = 0U; index < size; ++index) {
            for (std::size_t gap = 0U; gap < kGapCount; ++gap) {
                Grid& lower = stack[index].lower[gap];
                Grid& upper = stack[index].upper[gap];
                if (!(input >> lower >> upper) || lower < parameters.minimumGap ||
                    lower > upper || upper > parameters.gridLength) {
                    return false;
                }
            }
        }
        std::string ending;
        std::string extra;
        if (!(input >> ending) || ending != "end" || (input >> extra) || !input.eof()) {
            return false;
        }
        std::clog << "verify: restored " << stats.nodes << " completed boxes, " << size << " waiting\n";
        return true;
    }

    bool save(const Statistics& stats, const std::array<Box, kStackCapacity>& stack,
              const std::size_t size) const {
        if (path.empty()) {
            return true;
        }
        const std::filesystem::path temporary{path.string() + ".tmp"};
        std::ofstream out{temporary, std::ios::trunc};
        out << "observatory-839-checkpoint-v1 " << identity << ' ' << kPointCount << ' '
            << stats.nodes << ' ' << stats.leaves << ' ' << stats.basic << ' '
            << stats.affine << ' ' << stats.maximumStack << ' ' << size << '\n';
        for (std::size_t index = 0U; index < size; ++index) {
            for (std::size_t gap = 0U; gap < kGapCount; ++gap) {
                out << stack[index].lower[gap] << ' ' << stack[index].upper[gap] << ' ';
            }
            out << '\n';
        }
        out << "end\n";
        out.close();
        if (!out.good() || !syncCheckpointPath(temporary, O_RDONLY)) {
            return false;
        }
        std::error_code error{};
        std::filesystem::rename(temporary, path, error);
        const auto directory = path.has_parent_path() ? path.parent_path() : std::filesystem::path{"."};
        return !error && syncCheckpointPath(directory, O_RDONLY | O_DIRECTORY);
    }
};
