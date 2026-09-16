#include "../methods/finding_roots.h"
#include <cmath>

double f(double x) {
  // Real function
  return -25 + 82 * x - 90 * pow(x, 2) + 44 * pow(x, 3) - 8 * pow(x, 4) +
         0.7 * pow(x, 5);
}

int main() {
  FindingRoots fr;
  fr.bisectionMethod(f, 0.5, 1);
  return 0;
}
