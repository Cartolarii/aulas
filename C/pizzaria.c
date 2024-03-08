#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	float conta = 0, desconto = 0, valor_pos = 0;
	int qtd_p = 0;
	char escolha;
	
	printf("digite a quantidade de pesoas: ");
	scanf("%d", &qtd_p);
	printf("digite o valor total: ");
	scanf("%f", &conta);
	printf("digite o valor dado de desconto: ");
	scanf("%f", &desconto);
	
	valor_pos = conta - (conta * desconto	/100);
	
	
	while(true) {
		printf("Quer receber o valor individual? (s/n):\n");
		scanf("%c", &escolha);
		escolha = tolower(escolha);
		if(escolha == 's'){
			printf("\n\no valor por pessoa com desconto e: %.2f", valor_pos/qtd_p );
		break;
		}
		
		else if (escolha == 'n'){
			printf("\no valor total com desconto e: %.2f", valor_pos);
		break;
		}
		else{
		}
			
		}
		
	
	}


		
