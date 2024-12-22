scicv_Init();

img = imread("image.jpg");

matplot(img);

delete_Mat(img);

img_gray = imread(("image.jpg"), CV_LOAD_IMAGE_GRAYSCALE);

matplot(img_gray);

delete_Mat(img_gray);
