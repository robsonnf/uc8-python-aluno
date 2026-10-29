# UC8: Desenvolver e organizar interface gráfica para aplicações desktop — Aluno

Material de estudo e prática da **UC8 do Curso Técnico em Desenvolvimento de Sistemas**, voltado à construção de interfaces gráficas para aplicações desktop com **Python · Tkinter e ttk**.

O percurso reúne **20 aulas e 60 horas de carga horária total**. Você começa com entradas, funções e validações no terminal, passa para formulários e eventos e avança até aplicações com módulos, cadastros, carrinho, pagamentos fictícios, arquivos, banco SQLite, testes e documentação.

**[Acessar as aulas online](https://robsonnf.github.io/uc8-python-aluno/)** · **[Abrir o índice local](index.html)** · **[Consultar o percurso do curso](CURRICULUM.md)**

## Comece por aqui

1. Abra o site das aulas ou extraia a cópia baixada e abra `index.html`.
2. Selecione a aula indicada pelo professor e confira os objetivos e os pré-requisitos.
3. Estude a explicação e execute o exemplo pequeno no seu computador, comparando com o resultado esperado.
4. Leia o briefing antes do desafio: ele retoma os conceitos, propõe uma previsão e aponta os arquivos da prática.
5. Faça sua tentativa, execute os testes pedidos e registre o que observou.
6. **Baixe seus arquivos e exporte os registros antes de trocar de aula, atualizar ou fechar a página.**

Você pode ler o material pelo celular. Para desenvolver e executar os programas com janelas, use um computador com Python e ambiente gráfico.

## O que você vai aprender

- Ler dados, converter tipos, usar funções e condições e orientar a correção de entradas inválidas.
- Construir formulários com Tkinter/ttk, organizar campos e responder a cliques por callbacks.
- Separar edição, confirmação e consulta para preservar os dados quando uma tentativa falha.
- Organizar classes, módulos e responsabilidades, reutilizando o trabalho das aulas anteriores.
- Trabalhar com produtos, clientes, pedidos, quantidades, pagamentos fictícios e identificação por ID.
- Ler e gravar JSON, exportar CSV e persistir dados com SQLite.
- Integrar cadastro, pedido e venda, conferir transações, testar falhas e preparar uma entrega reproduzível.

O projeto integrador é uma sorveteria. Cadastro, conversor de moedas, sistema escolar e pizzaria ajudam a construir e transferir essas habilidades; a amostra de academia apoia a análise de responsabilidades e vínculos. Use os dados fictícios propostos nas atividades.

## Como cada aula está organizada

| Parte | Como usar |
|---|---|
| Objetivos e pré-requisitos | Identifique o que deverá conseguir fazer e quais arquivos ou conhecimentos retomar. |
| Antes da aula — Teoria, quando disponível | Retome o conceito, execute o ensaio curto e confira o que consegue explicar antes dos exercícios. |
| Diagnóstico ou retomada | Registre sua hipótese sem consulta; depois compare seu raciocínio com a discussão da aula. |
| Problema concreto e explicação | Entenda a necessidade da regra antes de escrever o código. |
| Exemplo comentado e resultado esperado | Faça um ensaio pequeno separado do projeto e confira a saída real. |
| Alteração guiada | Mude um ponto por vez, preveja o efeito e execute novamente. |
| Briefing e desafio individual | Retome os conceitos necessários e localize os arquivos que você vai trabalhar. |
| Critérios e pistas | Confira o que caracteriza a conclusão; abra as pistas progressivamente quando precisar. |
| Investigação e registros | Compare previsão e observação, explique uma correção e anote seu próximo teste. |

As aulas oferecem três pistas por atividade. Elas ajudam a investigar sem completar o trabalho por você. As respostas selecionadas na página são registros da sua tentativa; a discussão e a correção são acompanhadas pelo professor. Este material não inclui gabaritos ou soluções docentes.

## Acessar online ou baixar

### Pelo navegador

Acesse [o site das aulas](https://robsonnf.github.io/uc8-python-aluno/) e escolha uma aula. Você não precisa clonar o repositório, instalar Git ou usar Node.js para estudar online.

### Baixar uma cópia completa

1. Na página deste repositório no GitHub, clique em **Code → Download ZIP**.
2. Extraia o ZIP inteiro. Não abra o material diretamente de dentro do arquivo compactado.
3. Na pasta extraída, abra `index.html` no navegador.
4. Preserve a estrutura de pastas: páginas, estilos, scripts e anexos trabalham juntos.

Se preferir e já tiver Git, também pode obter uma cópia com:

```powershell
git clone https://github.com/robsonnf/uc8-python-aluno.git
cd uc8-python-aluno
```

A leitura, os exemplos e os anexos locais funcionam offline depois de baixar o pacote completo. Links para documentação externa e envio de atividades precisam de internet. Para usar os editores e a exportação, mantenha JavaScript habilitado. Sem ele, use a versão de leitura e registre a tentativa no seu editor ou caderno.

### Servidor local opcional

Abrir `index.html` é suficiente para consultar o material. Se quiser servir a pasta por um endereço local e já tiver **Node.js 18 ou superior**, abra o terminal na pasta que contém `package.json` e execute:

```powershell
npm start
```

No PowerShell, se `npm.ps1` estiver bloqueado, use:

```powershell
npm.cmd start
```

Não é necessário executar `npm install` nem alterar a política do PowerShell. Abra o endereço mostrado no terminal, normalmente `http://localhost:4321/`. Se a porta estiver ocupada, o servidor tenta outra e informa o endereço usado. Ele atende somente neste computador por padrão. Use **Ctrl + C** no terminal para encerrá-lo.

Esse servidor entrega as páginas do curso; a execução dos exercícios Python acontece separadamente no seu computador.

## Preparar e executar os exercícios Python

Para praticar, você precisa de um interpretador Python 3 compatível com a orientação da aula, um editor de texto/código e, nas atividades de interface, Tkinter/ttk funcionando. VS Code pode ser usado; escolha o interpretador preparado no laboratório ou indicado pelo professor.

No terminal, confira:

```powershell
python --version
python -m tkinter
```

O primeiro comando mostra a versão disponível. O segundo deve abrir uma pequena janela de demonstração do Tkinter; feche-a depois da conferência. No Windows, se sua instalação usa o lançador `py`, os equivalentes são `py --version` e `py -m tkinter`.

Tkinter acompanha muitas distribuições de Python, mas pode estar ausente em algumas instalações. Se o teste falhar, confira o interpretador e peça orientação para o ambiente do laboratório. Não use `pip install tkinter` como correção. PySimpleGUI e CustomTkinter aparecem apenas em comparações opcionais; siga as condições da aula antes de preparar essas bibliotecas.

### Organize o trabalho por aula

Crie uma pasta de trabalho separada do material baixado. Exemplo:

```text
meus-exercicios-uc8/
├── A01/
│   ├── terminal.py
│   ├── cadastro.py
│   └── registro-a01.md
├── A04/
│   ├── medias.py
│   ├── sistema_escolar.py
│   └── registro-a04.md
└── A06/
    ├── aluno.py
    ├── verificar_modelo.py
    └── main.py
```

Baixe os iniciais pelos links da atividade ou por **Fontes e anexos**. Eles contêm partes a completar: abrir ou executar um inicial não significa que o desafio foi resolvido. Nas aulas que reutilizam módulos, preserve a versão anterior que funciona e siga as instruções para adaptá-la. Mantenha os arquivos que importam uns aos outros na mesma pasta indicada pela aula.

Abra o terminal nessa pasta, salve suas alterações e execute o arquivo solicitado. Por exemplo, na A04, depois de trabalhar nos respectivos arquivos:

```powershell
python medias.py
python sistema_escolar.py
```

O primeiro exercita a lógica no terminal; o segundo usa uma janela. Nas aulas com vários módulos, siga o comando de entrada indicado — frequentemente `python main.py` — e execute o verificador quando solicitado. Não tente executar `.md`, `.json` ou `.csv` como programas Python.

Use o resultado esperado do exemplo e os critérios do desafio para conferir a execução. Registre um caso válido, um caso de erro e a nova tentativa após a correção, conforme a matriz de cada aula.

## Navegação e controles

| Controle | Uso |
|---|---|
| Grade das aulas | Mostra os encontros e os atalhos para as partes da aula atual. **P**, fora de um campo de edição, alterna a grade; **Escape** a fecha. |
| Aula anterior / Próxima aula | Avança entre as aulas presentes no pacote. Salve seu trabalho antes de navegar. |
| Lua / Sol | Lua ativa o tema escuro; sol ativa o claro. A preferência acompanha os links e pode ser guardada no navegador. |
| Etapa anterior / Próxima / Ver todas | Percorre as alterações guiadas do exemplo. São controles diferentes da navegação entre aulas. |
| Ampliar para apresentação | Alterna a visualização ampliada do conteúdo. |
| Pistas e detalhes | Abre orientações de investigação e regras para consulta. |
| Versão para leitura ou impressão / ↗ | Abre a leitura da aula ou da seção; use o comando de impressão do navegador para imprimir ou salvar em PDF. |

Os botões podem ser acionados com Enter ou Espaço quando estão em foco. Dentro do editor de rascunho, Tab insere indentação. A impressão usa fundo claro; a versão de leitura apresenta pistas e detalhes abertos para consulta.

## Usar o editor de rascunhos

O editor da página permite preparar sua tentativa e registrar uma observação manual. **Ele não executa Python, não abre a interface do seu programa e não verifica automaticamente o resultado.** Execute e teste os arquivos no seu computador.

| Ação | Resultado |
|---|---|
| Editar | Altera o rascunho somente na sessão atual da página. |
| Copiar meu rascunho | Copia o texto para usar no editor do computador. Se o navegador bloquear a cópia, selecione o texto e use Ctrl + C ou baixe o arquivo. |
| Baixar meu arquivo | Salva somente aquele arquivo com o conteúdo atual do seu rascunho. |
| Reiniciar | Descarta as alterações daquele painel e restaura o modelo inicial. |
| Expandir painel | Amplia o espaço do editor. |
| Resultado observado | Registra o que você viu ao executar fora do site; esse texto é informado por você. |

Depois de baixar um arquivo e editá-lo no computador, o site não acompanha essas mudanças. Conserve e entregue a versão que você realmente executou.

## Guardar o trabalho e exportar os registros

**Rascunhos, respostas e anotações não têm salvamento automático.** Recarregar, sair da aula ou fechar a aba pode perder a tentativa. A preferência de tema não é um backup do seu trabalho.

Antes de sair:

1. Use **Baixar meu arquivo** nos arquivos que deseja conservar separadamente.
2. Preencha os registros da prática e a reflexão. Use a identificação combinada com o professor.
3. Clique em **Exportar registros da aula** e confira o arquivo `.md` baixado.
4. Guarde também os arquivos que você editou e executou no computador, junto dos recursos solicitados pela atividade.

O registro exportado reúne identificação preenchida, escolhas nas questões, itens marcados para discussão, anotações, reflexão e rascunhos modificados na página, com suas observações. Nas aulas que oferecem o bloco de teoria, inclui também as marcações do checklist de autoexplicação. Ele não recolhe arquivos do computador nem substitui a entrega dos `.py` e demais arquivos solicitados. Arquivos `.md` podem ser abertos em um editor de texto ou no VS Code.

**Limpar sessão** apaga escolhas, anotações e rascunhos da página depois da confirmação. Exporte e confira o que precisa conservar antes de usar esse botão.

## Entregar as atividades

Baixar e exportar são ações locais. O envio ao professor é feito por você, no canal combinado. Confira quais arquivos a aula pede, use dados fictícios nos testes e mantenha uma cópia do que entregou.

## Salve sua entrega no OneDrive

Baixe ou exporte seus registros e os arquivos da atividade. Abra a pasta no OneDrive, entre com a conta autorizada e envie os arquivos baixados. Confira se eles aparecem na pasta antes de encerrar.

[Abrir pasta de entrega no OneDrive](https://senacrsedu-my.sharepoint.com/:f:/g/personal/01606371045_senacrs_edu_br/IgAw6ZzfVcGZS56vSyOV1YSaATvbA9sC2I-Iv76Rs_34IdU?e=gKMkOG).

Se o destino pedir autenticação ou informar falta de acesso, entre com a conta autorizada e consulte o professor. A página do curso não entra na sua conta, não envia arquivos automaticamente e não confirma o recebimento da atividade.

## Aulas e arquivos disponíveis

Este pacote contém A01, A02, A03, A04, A05, A06, A07, A08, A09, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20.

Os links abaixo apontam somente para aulas presentes nesta cópia. Um pacote isolado pode apresentar outros encontros na grade como **Em outro pacote**; para acessá-los, use o site ou a cópia completa.

| Aula | Tema | Acesso neste pacote |
|---|---|---|
| A01 | Diagnóstico, revisão Python e cadastro simples | [Abrir aula](lessons/0001-diagnostico-cadastro.html) |
| A02 | Evolução do cadastro | [Abrir aula](lessons/0002-evolucao-cadastro.html) |
| A03 | Conversor de moedas | [Abrir aula](lessons/0003-conversor.html) |
| A04 | Sistema escolar básico | [Abrir aula](lessons/0004-escolar-basico.html) |
| A05 | Sistema escolar ampliado | [Abrir aula](lessons/0005-escolar-ampliado.html) |
| A06 | Sistema escolar modular — classes | [Abrir aula](lessons/0006-escolar-modular.html) |
| A07 | Sorveteria inicial | [Abrir aula](lessons/0007-sorveteria-inicial.html) |
| A08 | Sorveteria e pagamentos | [Abrir aula](lessons/0008-sorveteria-pagamentos.html) |
| A09 | Catálogo e carrinho | [Abrir aula](lessons/0009-catalogo-carrinho.html) |
| A10 | Pizzaria inicial — transferência | [Abrir aula](lessons/0010-pizzaria-inicial.html) |
| A11 | Pizzaria — estados e pagamento | [Abrir aula](lessons/0011-pizzaria-evolucao.html) |
| A12 | Mercado — navegação e JSON | [Abrir aula](lessons/0012-mercado-json.html) |
| A13 | Pizzaria — CSV e demonstração de login | [Abrir aula](lessons/0013-pizzaria-relatorios.html) |
| A14 | SQLite — primeira persistência | [Abrir aula](lessons/0014-sqlite.html) |
| A15 | CRUD — produtos e clientes | [Abrir aula](lessons/0015-crud.html) |
| A16 | Controllers, componentes e contratos | [Abrir aula](lessons/0016-controllers.html) |
| A17 | Integração e CustomTkinter | [Abrir aula](lessons/0017-integracao.html) |
| A18 | Revisão, testes e README | [Abrir aula](lessons/0018-revisao-testes.html) |
| A19 | Academia e demonstrações individuais | [Abrir aula](lessons/0019-academia-demonstracoes.html) |
| A20 | Relacionamentos, recuperação e encerramento | [Abrir aula](lessons/0020-relacionamentos-recuperacao.html) |

## Estrutura deste projeto

```text
index.html          índice das aulas
CURRICULUM.md       percurso e objetivos gerais
lessons/            aulas interativas e versões leitura-*.html
anexos/             iniciais e materiais públicos das atividades
assets/             estilos, temas e interações das páginas
scripts/servir.mjs  servidor local opcional
package.json        comando npm start
README.md           este guia
LEIA-ME.txt         cópia do guia para leitura em texto
```

Preserve essas pastas ao copiar o material. Você não precisa alterar os arquivos de `assets/` ou do servidor para realizar os exercícios: trabalhe nos arquivos indicados nas atividades, na sua pasta de trabalho.

## Problemas frequentes

| Situação | O que conferir |
|---|---|
| A página abriu sem estilos ou com links quebrados | Extraia o ZIP inteiro e preserve `assets/`, `lessons/` e `anexos/`. Abra `index.html` na pasta extraída. |
| Python não foi encontrado | Confira a instalação e o interpretador do terminal/editor. No Windows, teste `py --version` se esse lançador estiver disponível. |
| Tkinter não abriu | Confira a saída de `python -m tkinter`, o interpretador selecionado e a disponibilidade de ambiente gráfico; peça orientação ao professor. |
| Um import não encontra seu módulo | Confira nome, extensão e pasta dos arquivos. Evite nomes como `tkinter.py` ou `math.py`, que podem esconder bibliotecas. |
| Copiar não funcionou | Use o download ou selecione o texto e copie manualmente. |
| O botão de exportar ou o editor não apareceu | Confira se JavaScript está habilitado e se todos os arquivos foram extraídos; a leitura também está disponível sem esses controles. |
| A aula online parece antiga | Atualize com Ctrl + F5. Para uma cópia offline, baixe a versão atual preservando sua pasta de exercícios e seus registros. |
| O arquivo baixado ganhou `(1)` no nome | Organize as versões e confira qual arquivo você executou e qual irá entregar. |
| O navegador recebeu a edição, mas o programa executa o código antigo | Baixe/salve a versão nova e confirme o caminho do arquivo executado pelo terminal ou pelo editor. |

Para pedir ajuda, informe a aula, o arquivo ou botão, a ação realizada, a mensagem de erro e o resultado esperado. Envie um caso pequeno com dados fictícios. Se estiver estudando com um tutor, peça uma pista ou uma pergunta que ajude a investigar sua tentativa.

## Conferência antes de concluir uma aula

- [ ] Consigo explicar o problema e os conceitos usados no desafio.
- [ ] Executei o arquivo correto e comparei a previsão com o resultado.
- [ ] Testei os casos solicitados, incluindo erro e nova tentativa.
- [ ] Registrei uma correção e o que ainda precisa de teste.
- [ ] Baixei os arquivos, exportei os registros e conferi os downloads.
- [ ] Fiz o envio manual pelo canal combinado e preservei uma cópia local.
