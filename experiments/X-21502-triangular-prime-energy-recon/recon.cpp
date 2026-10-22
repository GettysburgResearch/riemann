#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

struct Event {
    long double x;
    long double delta_slope;
    bool operator<(const Event& other) const { return x < other.x; }
};

static long double phi(long double t) {
    if (t < 0.0L || t > 2.0L) return 0.0L;
    return t <= 1.0L ? t : 2.0L - t;
}

static long double window(long double t) {
    const long double a = 1.0L;
    const long double h = logl(4.0L);
    return phi(t - a) - 2.0L * phi(t - a - h);
}

static long double integrate_window_square(long double lower, long double upper) {
    const long double a = 1.0L;
    const long double h = logl(4.0L);
    std::vector<long double> knots = {
        lower, upper, a, a + 1, a + 2, a + h, a + h + 1, a + h + 2};
    std::sort(knots.begin(), knots.end());
    long double total = 0.0L;
    for (size_t i = 0; i + 1 < knots.size(); ++i) {
        long double left = std::max(lower, knots[i]);
        long double right = std::min(upper, knots[i + 1]);
        if (right <= left) continue;
        long double gl = window(left);
        long double gr = window(right);
        total += (right - left) * (gl * gl + gl * gr + gr * gr) / 3.0L;
    }
    return total;
}

int main() {
    constexpr int LIMIT = 10000000;
    constexpr int FIRST_BLOCK = 2;
    constexpr int LAST_BLOCK = 16;

    std::vector<bool> is_prime(LIMIT + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; 1LL * p * p <= LIMIT; ++p) {
        if (!is_prime[p]) continue;
        for (long long n = 1LL * p * p; n <= LIMIT; n += p) is_prime[n] = false;
    }

    const long double a = 1.0L;
    const long double h = logl(4.0L);
    std::vector<Event> events;
    events.reserve(4000000);
    std::vector<long double> diagonal(LAST_BLOCK + 1, 0.0L);
    long long prime_power_count = 0;

    for (int p = 2; p <= LIMIT; ++p) {
        if (!is_prime[p]) continue;
        const long double logp = logl((long double)p);
        long long n = p;
        while (n <= LIMIT) {
            const long double logn = logl((long double)n);
            const long double weight = logp / sqrtl((long double)n);
            const long double base = logn + a;
            const long double locations[6] = {
                base, base + 1, base + 2,
                base + h, base + h + 1, base + h + 2};
            const long double changes[6] = {1, -2, 1, -2, 4, -2};
            for (int k = 0; k < 6; ++k) {
                events.push_back({locations[k], weight * changes[k]});
            }
            for (int j = FIRST_BLOCK; j <= LAST_BLOCK; ++j) {
                diagonal[j] += weight * weight * integrate_window_square(
                    (long double)j - logn,
                    (long double)(j + 1) - logn);
            }
            ++prime_power_count;
            if (n > LIMIT / p) break;
            n *= p;
        }
    }

    std::sort(events.begin(), events.end());
    std::vector<long double> energy(LAST_BLOCK + 1, 0.0L);
    long double value = 0.0L;
    long double slope = 0.0L;
    long double previous = events.front().x;

    auto integrate_signal = [&](long double left, long double right) {
        long double cursor = left;
        while (cursor < right) {
            int block = (int)floorl(cursor);
            long double endpoint = std::min(right, (long double)(block + 1));
            long double dt = endpoint - cursor;
            long double piece = value * value * dt
                + value * slope * dt * dt
                + slope * slope * dt * dt * dt / 3.0L;
            if (block >= FIRST_BLOCK && block <= LAST_BLOCK) energy[block] += piece;
            value += slope * dt;
            cursor = endpoint;
        }
    };

    size_t index = 0;
    while (index < events.size()) {
        const long double location = events[index].x;
        if (location > LAST_BLOCK + 1.0L) break;
        integrate_signal(previous, location);
        long double change = 0.0L;
        while (index < events.size() && fabsl(events[index].x - location) < 1e-18L) {
            change += events[index].delta_slope;
            ++index;
        }
        slope += change;
        previous = location;
    }
    integrate_signal(previous, (long double)(LAST_BLOCK + 1));

    std::cout << std::setprecision(18);
    std::cout << "{\n";
    std::cout << "  \"classification\": \"LONG_DOUBLE_RECONNAISSANCE\",\n";
    std::cout << "  \"prime_limit\": " << LIMIT << ",\n";
    std::cout << "  \"prime_power_count\": " << prime_power_count << ",\n";
    std::cout << "  \"complete_blocks\": [\n";
    for (int j = FIRST_BLOCK; j <= LAST_BLOCK; ++j) {
        long double off = energy[j] - diagonal[j];
        std::cout << "    {\"j\": " << j
                  << ", \"total\": " << (double)energy[j]
                  << ", \"diagonal\": " << (double)diagonal[j]
                  << ", \"off_diagonal\": " << (double)off
                  << ", \"total_over_diagonal\": "
                  << (double)(energy[j] / diagonal[j]) << "}";
        std::cout << (j == LAST_BLOCK ? "\n" : ",\n");
    }
    std::cout << "  ]\n}\n";
}
