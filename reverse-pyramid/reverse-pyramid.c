#include <stdio.h>
int main(){
   int input;
   scanf("%d",&input);
   for(int i=input/2+1; i>=0; i--){
      for (int k=(input/2+1)-i; k>0; k--){
         printf(" ");
      }
      for(int j=i*2-1; j>0; j--){
         printf("*");
      }
      printf("\n");
   }
   return 0;
}