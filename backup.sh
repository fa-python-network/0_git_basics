#! /bin/bash
echo "Hello, World"
#greet user
user = nastya
echo "Hello, $nastya"
n =6
echo 'define f(x) {if (x>1){return x*f(x-1)};return 1}
           f(6)' | bc
