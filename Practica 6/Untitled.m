I0=imread('nodules1.tif');
imshow(I0);
figure, imhist(I0);
I=im2double(I0);
I=1-im2bw(I, graythresh(I));
se = strel('disk',8);
E = imerode(I,se);
D = imdilate(E,se);
F=I-D;
figure, imshow(F)
