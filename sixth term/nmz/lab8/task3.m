N = 4;
x = -3:.1*N:3;
y = -3:.1*N:3;

z = (cos(x'*sin(y+0.08)+0.16));
P = [x; y];
T = z;
net = newrb(P,T);
Y = sim(net, P);

mesh(x,y,z);
