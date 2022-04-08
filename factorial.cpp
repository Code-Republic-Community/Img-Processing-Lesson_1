#include <iostream>

int factorial(int val)
{
    int64_t result = 1;
    for (int i = 1; i <= val; ++i) {
        result *= i;
    }
    return result;
}

int main()
{
    int val = factorial(10);
    std::cout << val << std::endl;
    return 0;
}
