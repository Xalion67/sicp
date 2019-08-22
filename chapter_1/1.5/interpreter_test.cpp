int p() {
  return p();
}

int test(int x, int y) {
  if (x == 0) {
    return 0;
  }
  return y;
}

int main() {
  test(0, p());

  return 0;
}
