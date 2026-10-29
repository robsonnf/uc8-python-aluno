# A05 — organização e consultas do sistema escolar

Código do estudante:
Arquivos e interpretador executados:

## Retomada sem consulta
Quais dados devem ficar juntos no último registro válido?
Por que uma quinta nota inválida não pode alterar o nome confirmado?
O que o botão recebe em command e quando essa função é executada?
Minhas respostas iniciais:

## Antes de programar
Desenho dos pais: Tk → Frame base → grupos → campos e botões:
Onde cada grid organiza seus filhos?
Diferença entre edição, registro confirmado e retrato da consulta:

## Preveja e depois execute
Dados sempre fictícios. C1/C2 identificam janelas de consulta diferentes.
| Caso | Sequência/verificação | Previsão | Observação | Ajuste |
|---|---|---|---|---|
| T01 | Confirmar que nome/turma, cinco notas e ações possuem os grupos/pais planejados | | | |
| T02 | Lia / T1 / 6,7,8,9,10; calcular e conferir média 8.0 | | | |
| T03 | Antes do primeiro válido, usar Consultar | | | |
| T04 | Confirmar T02 e abrir consulta C1 | | | |
| T05 | Editar Rui / T2 / cinco notas 5, sem calcular; observar C1 | | | |
| T06 | Após T02, tentar outra identificação com quinta nota abc; consultar novamente | | | |
| T07 | Corrigir e confirmar Rui / T2 / cinco notas 5; observar C1 e abrir C2 | | | |
| T08 | Limpar as sete entradas; observar o registro principal e as consultas | | | |
| T09 | Fechar C1 pelo botão; continuar usando a principal e C2 | | | |
| T10 | Abrir outra consulta e fechá-la por Escape | | | |
| T11 | Abrir outra consulta e fechá-la pelo X da própria janela | | | |
| T12 | Repetir 0/10, fora de faixa, vazios, vírgula/ponto e identificação da A04 | | | |
| T13 | Percorrer grupos e botões por Tab/Shift+Tab; ampliar a janela e observar campos | | | |
| T14 | Executar sem marca-a05.png; observar o cabeçalho textual | | | |
| T15 | Se usar PNG próprio, conferir imagem e testar arquivo inválido/ausente com fallback | | | |
| T16 | Executar o script a partir de outra pasta; conferir busca ao lado do script | | | |
| T17 | Fechar a principal com consultas abertas; reabrir e tentar Consultar | | | |

## Imagem local (opcional)
O programa funcionou sem imagem:
Se criei PNG próprio, nome/origem do arquivo e teste realizado:
Qual objeto conserva a referência da imagem:

## Fechamento sem consulta
Por que criar outra Tk/mainloop não é o contrato desta aula?
Por que C1 pode manter o registro antigo depois de um novo válido?
Qual janela cada fechamento destrói?
Minha dificuldade, correção e próxima tentativa:

Entregas: escolar_grupos.py, escolar_janelas.py e este registro.
Não há imagem obrigatória no pacote; use apenas arquivo próprio autorizado se optar por esse teste.

## Teoria e transferência
Consigo identificar o pai e a grade de um campo.
Minha explicação:
Consigo explicar sticky e peso de coluna no redimensionamento.
Minha explicação:
Consigo distinguir edição, confirmado e retrato da consulta.
Minha explicação:
Ligação entre o ensaio e meus arquivos da atividade:
Minha previsão antes da alteração guiada e o resultado observado:

## Continuação em casa
Arquivos/versão executados:
Pasta e comando usados:
Justificativa de 5–8 linhas ou nome do áudio de cerca de 60 segundos:
Decisão do meu código sobre hierarquia de pais, expansão dos grupos, retratos e fechamento das Toplevel:
Minha explicação / anexo:

## Checklist da interface
Controles e rótulos que conferi:
Percurso por Tab/Shift+Tab e acionamento:
Mensagem após erro e possibilidade de corrigir:
Redimensionamento e comportamento que observei:

## Pendências
O que não executei e por quê, incluindo falta de ambiente:
Caso para nova tentativa em sala:
