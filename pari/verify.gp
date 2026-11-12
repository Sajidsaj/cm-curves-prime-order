\\ PARI/GP checks (all of these were run and matched the expected output).

\\ 1. primes p such that y^2 = x^3 + 7 over GF(p) has a prime number of points (OEIS A399358)
\\    expected: 13, 43, 61, 67, 79, 97, 127, 163, 211, 349, 397, 433, 547, ..., 4831
forprime(p=5, 5000, if(p!=7 && isprime(ellcard(ellinit([0,7], p))), print1(p", ")))

\\ 2. least b such that y^2 = x^3 + b over GF(prime(n)) has a prime number of points (0 if none)
\\    expected: [0, 3, 0, 2, 0, 2, 0, 0, 3, 5, 0, 7, 0, 0, 0, 2, 2, 0, 13, 3, 0, 0, 5, 0, 5, 0, 11, 0, 3, 0]
a(n) = my(p=prime(n)); for(b=1, p-1, if(isprime(ellcard(ellinit([0,b], p))), return(b))); 0
vector(30, n, a(n+2))

\\ 3. j = 1728: primes p with a curve y^2 = x^3 + A*x of order 2*prime whose twist also has order 2*prime
\\    expected: 17, 29, 89, 101, 349, 509, 521
forprime(p=5,600, if(p%4==1, ok=0; for(A=1,p-1, N=ellcard(ellinit([A,0],p)); Nt=2*(p+1)-N; if(N%2==0 && isprime(N/2) && Nt%2==0 && isprime(Nt/2), ok=1; break)); if(ok, print1(p", "))))

\\ 4. j = 0: primes p with a prime-order curve whose twist has 3*prime points
\\    expected: 7, 13, 19, 31, 37, 43, 67, 79, 97, 103, 109, 127, 181, 211, 223, 229, 283
forprime(p=5,300, if(p%3==1, ok=0; for(b=1,p-1, N=ellcard(ellinit([0,b],p)); Nt=2*(p+1)-N; if(isprime(N) && Nt%3==0 && isprime(Nt/3), ok=1; break)); if(ok, print1(p", "))))

\\ 5. Special-form primes p = 2^k - c: rows [k, c, b]. PARI computes the order itself (SEA).
\\    expected: 1 1 for the prime tests and 0/1 as shown in the last column
\\    [256,1539,5,1,1,0]  [256,681003,6,1,1,1]  [255,300769,6,1,1,1]  [224,738993,5,1,1,1]  [192,394323,17,1,1,1]
v=[[256,1539,5],[256,681003,6],[255,300769,6],[224,738993,5],[192,394323,17]];
for(i=1,#v, k=v[i][1]; c=v[i][2]; b=v[i][3]; p=2^k-c; n=ellcard(ellinit([0,b],p)); Nt=2*(p+1)-n; print([k,c,b, isprime(p), isprime(n), Nt%3==0 && isprime(Nt/3)]); print("  n = ", n));
