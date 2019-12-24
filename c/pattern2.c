#include<stdio.h>
void main()
{
    int r=5;
    for(int i=1;i<=r;i++)
    {
        for(int j=1;j<=r;j++)
        {
            if(j<=r-i)
            {
                 printf(" ");
            }
            if(j>r-i){
            printf("%d ",i);
            }

        }

        printf("\n");
    }
}
