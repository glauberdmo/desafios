# Desafio 1: Strings

## Descrição da solução
Foi pedido que desenvolvesse um meio de quebrar uma string em um tamanho parametrizado, para isso foi desenvolvida uma classe TextBreaker.
	
## Setup
Para rodar esse projeto clone o repositório e siga os exemplos de uso:

```
    # O construtor da classe recebe o texto e tamanho por linha
    OutputText = TextBreaker(text_to_break,40)    

    #Escolha o alinhamento
    OutputText.alignment_justify() 
    OutputText.alignment_right()
    OutputText.alignment_left() #default

    #Use esse método para imprimir todo o texto quebrado no terminal
    OutputText.print_rows()

    #Retorno por item
    primeira_linha = OutputText[0]
```