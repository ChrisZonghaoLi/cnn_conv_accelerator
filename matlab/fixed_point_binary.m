% This program is used to convert input/weight/bias to fixed point binary
% numbers

close all
clear all

kernel_1_vec = importdata('kernel_1_vec.txt'); % fixed-point weight 
kernel_2_vec = importdata('kernel_2_vec.txt'); % fixed-point biases
kernel_3_vec = importdata('kernel_3_vec.txt'); % fixed-point weight  
bias_1_vec = importdata('bias_1_vec.txt'); % fixed-point biases
bias_2_vec = importdata('bias_2_vec.txt'); % fixed-point biases
bias_3_vec = importdata('bias_3_vec.txt'); % fixed-point biases
I_vec = importdata('I_vec.txt'); % fixed-point biases

% the word-length is 16 bits and 8 bits are for the fraction
length = 16;
frac = 8;

% dimension of each data set
a = size(kernel_1_vec, 1);
b = size(kernel_2_vec, 1);
c = size(kernel_3_vec, 1);
d = size(bias_1_vec, 1);
e = size(bias_2_vec, 1);
f = size(bias_3_vec, 1);
g = size(I_vec, 1);

% convert the first weight vector to binary fixed point
for k = 1:a
    if kernel_1_vec(k, 1) >= 0
        kernel_1_b(k, 1) = string(dec2bin(floor(2^frac * kernel_1_vec(k, 1)), length));
    else 
        kernel_1_b(k, 1) = string(dec2bin(floor(2^length + 2^frac * kernel_1_vec(k, 1)), length)); 
    end
end

% convert the second weight vector to binary fixed point
for l = 1:b
    if kernel_2_vec(l, 1) >= 0
        kernel_2_b(l, 1) = string(dec2bin(floor(2^frac * kernel_2_vec(l, 1)), length));
    else 
        kernel_2_b(l, 1) = string(dec2bin(floor(2^length + 2^frac * kernel_2_vec(l, 1)), length)); 
    end
end
    
% convert the third weight vector to binary fixed point
for m = 1:c
    if kernel_3_vec(m, 1) >= 0
        kernel_3_b(m, 1) = string(dec2bin(floor(2^frac * kernel_3_vec(m, 1)), length));
    else 
        kernel_3_b(m, 1) = string(dec2bin(floor(2^length + 2^frac * kernel_3_vec(m, 1)), length)); 
    end
end
    
% convert the first bias vector to binary fixed point
for n = 1:d
    if bias_1_vec(n, 1) >= 0
        bias_1_b(n, 1) = string(dec2bin(floor(2^frac * bias_1_vec(n, 1)), length));
    else 
        bias_1_b(n, 1) = string(dec2bin(floor(2^length + 2^frac * bias_1_vec(n, 1)), length)); 
    end
end

% convert the second bias vector to binary fixed point
for o = 1:e
    if bias_2_vec(o, 1) >= 0
        bias_2_b(o, 1) = string(dec2bin(floor(2^frac * bias_2_vec(o, 1)), length));
    else 
        bias_2_b(o, 1) = string(dec2bin(floor(2^length + 2^frac * bias_2_vec(o, 1)), length)); 
    end
end

% convert the third bias vector to binary fixed point
for p = 1:f
    if bias_3_vec(p, 1) >= 0
        bias_3_b(p, 1) = string(dec2bin(floor(2^frac * bias_3_vec(p, 1)), length));
    else 
        bias_3_b(p, 1) = string(dec2bin(floor(2^length + 2^frac * bias_3_vec(p, 1)), length)); 
    end
end

% convert the input vector to binary fixed point
for q = 1:10240 %(10 pics)%g
    if I_vec(q, 1) >= 0
        I_b(q, 1) = string(dec2bin(floor(2^frac * I_vec(q, 1)), length));
    else 
        I_b(q, 1) = string(dec2bin(floor(2^length + 2^frac * I_vec(q, 1)), length)); 
    end
end

% Save them to txt file
kernel_1_b_ID = fopen('kernel_1_b.txt','w');
input0 = kernel_1_b;
fprintf(kernel_1_b_ID, '%s\n', input0{:});
fclose(kernel_1_b_ID);

kernel_2_b_ID = fopen('kernel_2_b.txt','w');
input1 = kernel_2_b;
fprintf(kernel_2_b_ID, '%s\n', input1{:});
fclose(kernel_2_b_ID);

kernel_3_b_ID = fopen('kernel_3_b.txt','w');
input2 = kernel_3_b;
fprintf(kernel_3_b_ID, '%s\n', input2{:});
fclose(kernel_3_b_ID);

bias_1_b_ID = fopen('bias_1_b.txt','w');
input3 = bias_1_b;
fprintf(bias_1_b_ID, '%s\n', input3{:});
fclose(bias_1_b_ID);

bias_2_b_ID = fopen('bias_2_b.txt','w');
input4 = bias_2_b;
fprintf(bias_2_b_ID, '%s\n', input4{:});
fclose(bias_2_b_ID);

bias_3_b_ID = fopen('bias_3_b.txt','w');
input5 = bias_3_b;
fprintf(bias_3_b_ID, '%s\n', input5{:});
fclose(bias_3_b_ID);

I_b_ID = fopen('I_b.txt','w');
input6 = I_b;
fprintf(I_b_ID, '%s\n', input6{:});
fclose(I_b_ID);
    