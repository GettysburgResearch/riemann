// Restartable segmented reconnaissance for Nicolas's primorial criterion.
// STATUS: ordinary long-double computation; NOT a rigorous sign certificate.
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>
#include <vector>

struct State {
    uint64_t processed_limit = 1;
    uint64_t last_prime = 0;
    uint64_t k = 0;
    long double theta = 0;
    long double log_product = 0;
    long double previous_defect = std::numeric_limits<long double>::quiet_NaN();
    long double minimum_defect = std::numeric_limits<long double>::infinity();
    uint64_t minimum_k = 0;
    uint64_t upward_steps = 0;
    uint64_t violations = 0;
};

static std::vector<uint32_t> simple_primes(uint64_t limit) {
    std::vector<uint8_t> sieve(limit + 1, 1);
    sieve[0] = 0;
    if (limit >= 1) sieve[1] = 0;
    for (uint64_t p = 2; p * p <= limit; ++p) {
        if (sieve[p]) for (uint64_t x = p * p; x <= limit; x += p) sieve[x] = 0;
    }
    std::vector<uint32_t> out;
    for (uint64_t p = 2; p <= limit; ++p) if (sieve[p]) out.push_back(static_cast<uint32_t>(p));
    return out;
}

static State read_state(const std::string& path) {
    State s;
    std::ifstream in(path);
    if (!in) return s;
    std::unordered_map<std::string, std::string> v;
    std::string line;
    while (std::getline(in, line)) {
        auto pos = line.find('=');
        if (pos != std::string::npos) v[line.substr(0, pos)] = line.substr(pos + 1);
    }
    auto u = [&](const char* key, uint64_t& x) { if (v.count(key)) x = std::stoull(v[key]); };
    auto f = [&](const char* key, long double& x) { if (v.count(key)) x = strtold(v[key].c_str(), nullptr); };
    u("processed_limit", s.processed_limit); u("last_prime", s.last_prime); u("k", s.k);
    f("theta", s.theta); f("log_product", s.log_product); f("previous_defect", s.previous_defect);
    f("minimum_defect", s.minimum_defect); u("minimum_k", s.minimum_k);
    u("upward_steps", s.upward_steps); u("violations", s.violations);
    return s;
}

static void write_state(const std::string& path, const State& s) {
    std::ofstream out(path);
    out << std::setprecision(36);
    out << "processed_limit=" << s.processed_limit << '\n';
    out << "last_prime=" << s.last_prime << '\n';
    out << "k=" << s.k << '\n';
    out << "theta=" << s.theta << '\n';
    out << "log_product=" << s.log_product << '\n';
    out << "previous_defect=" << s.previous_defect << '\n';
    out << "minimum_defect=" << s.minimum_defect << '\n';
    out << "minimum_k=" << s.minimum_k << '\n';
    out << "upward_steps=" << s.upward_steps << '\n';
    out << "violations=" << s.violations << '\n';
}

int main(int argc, char** argv) {
    if (argc < 4) {
        std::cerr << "usage: scan end_limit state.txt result.json [segment_odds]\n";
        return 2;
    }
    const uint64_t end = std::stoull(argv[1]);
    const std::string state_path = argv[2], result_path = argv[3];
    const uint64_t segment_odds = argc > 4 ? std::stoull(argv[4]) : (1ULL << 21);
    State s = read_state(state_path);
    if (end < s.processed_limit) {
        std::cerr << "end limit precedes state\n";
        return 2;
    }
    const uint64_t start_limit = s.processed_limit;
    const uint64_t start_k = s.k;
    const long double gamma = 0.577215664901532860606512090082402431L;

    auto process_prime = [&](uint64_t p) {
        ++s.k;
        s.last_prime = p;
        s.theta += logl(static_cast<long double>(p));
        s.log_product += -log1pl(-1.0L / static_cast<long double>(p));
        if (s.k >= 2) {
            const long double defect = s.log_product - gamma - logl(logl(s.theta));
            if (std::isfinite(s.previous_defect) && defect > s.previous_defect) ++s.upward_steps;
            if (defect < s.minimum_defect) { s.minimum_defect = defect; s.minimum_k = s.k; }
            if (defect <= 0) ++s.violations;
            s.previous_defect = defect;
        }
    };

    uint64_t low_bound = s.processed_limit + 1;
    if (low_bound <= 2 && end >= 2) process_prime(2);
    uint64_t low = std::max<uint64_t>(3, low_bound);
    if ((low & 1) == 0) ++low;
    if (low <= end) {
        uint64_t root = static_cast<uint64_t>(sqrtl(static_cast<long double>(end)));
        while ((root + 1) <= end / (root + 1)) ++root;
        while (root > end / root) --root;
        const auto base = simple_primes(root);
        for (uint64_t seg_low = low; seg_low <= end;) {
            const uint64_t max_count = (end - seg_low) / 2 + 1;
            const uint64_t count = std::min<uint64_t>(segment_odds, max_count);
            const uint64_t seg_high = seg_low + 2 * (count - 1);
            std::vector<uint8_t> composite(count, 0);
            for (uint32_t pp : base) {
                if (pp == 2) continue;
                const uint64_t p = pp, p2 = p * p;
                if (p2 > seg_high) break;
                uint64_t x = p2;
                if (x < seg_low) x = ((seg_low + p - 1) / p) * p;
                if ((x & 1) == 0) x += p;
                for (; x <= seg_high; x += 2 * p) composite[(x - seg_low) / 2] = 1;
            }
            for (uint64_t i = 0; i < count; ++i) if (!composite[i]) process_prime(seg_low + 2 * i);
            if (seg_high >= end - 1) break;
            seg_low = seg_high + 2;
        }
    }
    s.processed_limit = end;
    write_state(state_path, s);

    const long double defect = s.previous_defect;
    std::ofstream out(result_path);
    out << std::setprecision(25);
    out << "{\n"
        << "  \"experiment_id\": \"X-1501\",\n"
        << "  \"classification\": \"EMPIRICAL_NOT_CERTIFIED\",\n"
        << "  \"start_limit\": " << start_limit << ",\n"
        << "  \"end_limit\": " << end << ",\n"
        << "  \"start_k\": " << start_k << ",\n"
        << "  \"k\": " << s.k << ",\n"
        << "  \"last_prime\": " << s.last_prime << ",\n"
        << "  \"theta\": " << s.theta << ",\n"
        << "  \"log_product\": " << s.log_product << ",\n"
        << "  \"log_defect\": " << defect << ",\n"
        << "  \"normalized_ratio\": " << expl(defect) << ",\n"
        << "  \"minimum_log_defect\": " << s.minimum_defect << ",\n"
        << "  \"minimum_k\": " << s.minimum_k << ",\n"
        << "  \"upward_steps_after_k2\": " << s.upward_steps << ",\n"
        << "  \"floating_violations\": " << s.violations << ",\n"
        << "  \"backend\": \"segmented exact integer sieve; long-double libm recurrence (non-rigorous)\",\n"
        << "  \"proof_boundary\": \"a nonpositive value would only be a candidate until every prime and transcendental comparison is independently certified\"\n"
        << "}\n";
    std::cerr << "processed (" << start_limit << ',' << end << "] primes=" << (s.k - start_k)
              << " total_k=" << s.k << " defect=" << std::setprecision(18) << defect << '\n';
    return 0;
}
