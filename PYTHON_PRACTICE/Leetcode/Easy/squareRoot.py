def squareRoot( n):
    x = n;
    y = 1;
    e = 0.000001; 
    while (x - y > e):
        x = float((x + y) / 2);
        y = float(n / x);
    return x;
print(squareRoot(8))