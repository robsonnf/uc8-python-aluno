# Meu registro A06 — objetos e módulos

Nome/código individual:
Turma e data:

## Hipóteses sem consulta
O que fica confirmado após erro na quinta nota?
Qual a diferença entre editar, confirmar e limpar?
O que aconteceria se dois nomes apontassem para o mesmo objeto?

## Arquitetura antes do código
Pasta com aluno.py, verificar_modelo.py e main.py:
Qual arquivo contém regras? Qual cria widgets? Quem importa quem?
O que __init__ cria em cada nova instância?
Por que duas chamadas Aluno() diferem de rui = lia?
O que self identifica em uma chamada de método?

## Testes executados
Preencha para cada caso: previsão | resultado observado | correção e nova tentativa.
Não marque como executado um teste ainda pendente.
- T01: Importar aluno sem Tk, sem janela e sem leitura de teclado.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T02: Criar dois objetos; listas distintas; ambos sem média antes de confirmar.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T03: Lia/T1/[6,7,8,9,10] e Rui/T2/[5,5,5,5,5]; médias 8.0 e 5.0.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T04: Atualizar só Lia; Rui mantém identificação, notas e média.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T05: Após válido, tentar nome/turma vazios; preservar todo o registro.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T06: Após válido, erro na quinta nota; preservar os três atributos e resumo.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T07: Testar 0 e 10, vírgula/ponto, negativos, >10, nan, inf, vazio e texto.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T08: Recusar quantidade diferente de cinco notas, sem alterar o válido.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T09: Alterar a lista de textos original após atualizar; notas confirmadas não mudam.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T10: Executar verificar_modelo.py sem abrir GUI; cada assert corresponde a um caso.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T11: Consultar antes do primeiro válido: orientação e nenhuma janela vazia.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T12: Confirmar Lia e abrir C1; editar Rui e errar a última nota: C1 e confirmado permanecem.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T13: Corrigir e confirmar Rui; C2 mostra Rui e C1 conserva Lia.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T14: Limpar os sete campos; último registro e consultas continuam disponíveis.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T15: Fechar consultas por botão, X e Escape; principal e outra consulta continuam funcionando.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T16: Conferir grupos, rótulos, expansão e percurso Tab; funcionar sem PNG.
  Previsão: 
  Observado: 
  Correção/reteste: 
- T17: Encerrar a principal e reabrir: começar sem registro; nenhum arquivo de dados gravado.
  Previsão: 
  Observado: 
  Correção/reteste: 

## Explicação individual
Mostre dois objetos independentes e uma tentativa inválida após um válido.
Indique a linha que confirma o conjunto e por que a interface não repete a regra.
O que um assert verifica? Qual caso ainda falta?
Minha dificuldade e próximo teste:

Entrega: aluno.py, verificar_modelo.py, main.py e este registro.
Somente dados fictícios. A página não executa Python nem envia arquivos automaticamente.
