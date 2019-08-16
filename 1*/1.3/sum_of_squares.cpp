#include <iostream>


int square(int x) {
  return x * x;
}

int sum_of_squares_of_two_top(int a, int b, int c) {
  if (a < b && a < c) {
    return square(b) + square(c);
  }
  else if (b < c && b < a) {
    return square(a) + square(c);
  }
  else {
    return square(a) + square(b);
  }
}
