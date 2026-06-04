//write a programm to print area of triangle 
#include <stdio.h>
int main()
{
    int width=10;
    int height=6;
    float area;
	printf("width of triangle:%d\n",width);
	printf("height of triangle:%d\n",height);
    area = (width*height) / 2.0;

    printf("Area of triangle=%f",area);
    return 0;
}
