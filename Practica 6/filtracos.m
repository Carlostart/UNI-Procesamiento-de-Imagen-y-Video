I0=imread('Fig5.25(a).jpg');
I=im2double(I0);imshow(I);[M,N]=size(I);
for i=[3 6 10]
 F=fft2(I);
 H=lpfilter('gaussian',M,N,5*i);
 G=H.*F;
 I1=real(ifft2(G));
 figure,imshow(I1)
end