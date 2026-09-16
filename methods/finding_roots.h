#pragma once
#include <cmath>
#include <cstdlib>
#include <format>
#include <functional>
#include <iostream>

struct Result {
  bool success;
  double root;
  int iterations;
};

class FindingRoots {
public:
  int MAX_ITERATIONS;
  double PRECISION;
  bool PRINT_ITERATIONS;

  FindingRoots()
      : MAX_ITERATIONS(10), PRECISION(0.001), PRINT_ITERATIONS(true) {}

  bool oppositeSigns(double a, double b) {
    return (a > 0 && b < 0) || (a < 0 && b > 0);
  }

  Result bisectionMethod(std::function<double(double)> f, double a, double b) {
    double f_a = f(a), f_b = f(b);
    if (f_a == 0)
      return Result(true, a, 0);
    if (f_b == 0)
      return Result(true, b, 0);
    if (!oppositeSigns(f_a, f_b)) {
      std::cout << "Error: f(a) and f(b) must have opposite signs" << std::endl;
      return Result(false, 0, 0);
    }
    double c, f_c;
    int iter = 1;
    while (iter <= MAX_ITERATIONS) {
      c = (a + b) / 2;
      f_c = f(c);
      if (PRINT_ITERATIONS) {
        std::cout << "Iteration " << iter << ":\t";
        std::cout << "a =  " << std::format("{:.6f}", a) << ":\t";
        std::cout << "b =  " << std::format("{:.6f}", b) << ":\t";
        std::cout << "c =  " << std::format("{:.6f}", c) << ":\t";
        std::cout << "f(c) =  " << std::format("{:.6f}", f_c) << std::endl;
      }
      if (std::abs(f_c) < PRECISION)
        return Result({true, c, iter});
      if (oppositeSigns(f_a, f_c)) {
        b = c;
        f_b = f_c;
      } else {
        a = c;
        f_a = f_c;
      }
      iter++;
    }
    return Result({true, c, MAX_ITERATIONS});
  }
};
