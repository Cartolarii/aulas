#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
	
main(){
  char genero = ' ';
  int idade = 0;
  float salario = 0;

  printf("Digite o genero: ");
  scanf("%c",&genero);
  printf("Digite a idade: ");
  scanf("%d",&idade);
  printf("Digite o salario: ");
  scanf("%f",&salario);

  printf("Gênero: %c \n",genero);
  printf("Idade: %d \n",idade);
  printf("Idade: %3d \n",idade);
  printf("Salario: %f \n",salario);
  printf("Salario: %8.2f \n",salario);
}
