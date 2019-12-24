#include<stdio.h>
#include<conio.h>
void main()
{
    int r,i,j,c;
    scanf("%d %d",&r,&c);
    for(i=1;i<=r;i++)
    {
        for(j=1;j<=c;j++)
        {
            if((i==1 && j==1) || (i==1 && j==c) || (i==r && j==1) || (i==r && j==c))
            {
                printf("0 ");
            }
            else{printf("1 ");}
        }
        printf("\n");
    }
}
