close all
clear all
clc

%% q (a,b,c,d)
syms x(t)
dist_list = [];
ratio = [];
Kt = 53.3 * 0.001;
Kv = 179;
Ke = 1/Kv/0.105;
Vs = 30;
R = 1.74;
m = 100;
r = 0.5;
rotor_I = 181;
J = rotor_I * 1e-7 + m * r^2;
%N = 1;


for N=1:100
    Dx = diff(x);
    ode = diff(x,t,2) == -(Kt * Ke / ((J/N^2)*R)) * diff(x,t) + (Kt * Vs)/((J/N^2) * R);
    cond1 = x(0) == 0;
    cond2 = Dx(0) == 0;
    conds = [cond1 cond2];
    xSol(t) = dsolve(ode,conds);
    xSol = simplify(xSol);
    dist = double(subs(xSol, t, 5));
    dist_list(N) = dist * r * 1/N;
    ratio(N) = N;
end

[dist_max, index] = max(dist_list);
N_opt = ratio(index)
dist_max

figure
plot(ratio, dist_list)    

%% q (e)
syms x(t)
dist_list = [];
Kt = 131 * 0.001;
Kv = 72.7;
Ke = 1/Kv/0.105;
Vs = 30;
R = 6.89;
m = 100;
r = 0.5;
rotor_I = 181;
J = rotor_I * 1e-7 + m * r^2;
N_list = [3.5 4.3 6 12 15 19 21 26 36 43 53 66 74 81 91]; 

for i = 1:length(N_list)
    Dx = diff(x);
    ode = diff(x,t,2) == -(Kt * Ke / ((J/N_list(i)^2)*R)) * diff(x,t) + (Kt * Vs)/((J/N_list(i)^2) * R);
    cond1 = x(0) == 0;
    cond2 = Dx(0) == 0;
    conds = [cond1 cond2];
    xSol(t) = dsolve(ode,conds);
    xSol = simplify(xSol);
    dist = double(subs(xSol, t, 5));
    dist_list(i) = dist * r * 1/N_list(i);
end

[dist_max, index] = max(dist_list);
N_opt = N_list(index)
dist_max

figure
plot(N_list, dist_list)    
    