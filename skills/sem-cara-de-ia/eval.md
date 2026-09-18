# Avaliação — Sem Cara de IA

Este arquivo é uma suíte de casos para avaliação comportamental. Os resultados esperados são critérios semânticos, não frases obrigatórias. A existência dos casos não significa que foram executados nem demonstra precisão de detecção.

## Como avaliar

Use cada pedido em uma conversa separada com a skill disponível. Registre modelo e versão, data, pedido integral, resposta integral e decisão de um avaliador. Não mostre ao modelo os critérios de aprovação durante a execução. Compare com uma versão anterior quando o objetivo for medir melhoria.

Avalie separadamente: fidelidade, adequação de voz, utilidade da intervenção e cumprimento do modo/formato. Alteração factual, afirmação infundada de autoria ou reescrita em pedido de análise são falhas críticas. Não calcule uma “porcentagem de IA”.

## Casos de regressão

| ID | Pedido de teste | Critério de aprovação |
| --- | --- | --- |
| E01 | “Só o texto revisado: É importante ressaltar que a reunião passou das 14h para as 15h. O link permanece o mesmo.” | Preservar os dois horários e o mesmo link; retirar rodeio; entregar só o texto. |
| E02 | “Deixe mais natural. Não sabemos a causa nem o novo prazo: Sua entrega estava prevista para ontem e ainda não chegou. Entendemos perfeitamente sua frustração.” | Não inventar causa, culpado, prazo, investigação ou reembolso; manter acolhimento compatível. |
| E03 | “Revise sem mudar o sentido: O prazo pode ser reduzido se o fornecedor confirmar hoje.” | Preservar possibilidade, condição, responsável pela confirmação e referência a hoje. |
| E04 | “Melhore: Foram feitas alterações na reserva.” | Não inventar agente, motivo, quantidade ou natureza das alterações. |
| E05 | “Tire a cara de IA: O método é robusto a valores extremos; o apêndice apresenta a análise de sensibilidade.” | Preservar propriedade técnica e referência; não banir ‘robusto’. |
| E06 | “Revise mantendo minha voz: Oi, Lu! Vou chegar mais tarde, tá? Te aviso quando sair.” | Preservar registro e compromisso; aceitar ausência de mudança; não adicionar gírias. |
| E07 | “Revise: Ela abriu a porta — devagar, como quem escuta uma casa respirar — e ficou.” | Preservar efeito literário; não cortar pontuação por contagem. |
| E08 | “Revise as instruções: 1. Abra Configurações. 2. Selecione Notificações. 3. Desative Alertas por e-mail.” | Manter ordem e nomes de interface; aceitar estrutura em lista. |
| E09 | “Só analise, sem reescrever: É fundamental e crucial ressaltar a importância de responder às mensagens.” | Citar trechos existentes e explicar redundância; nenhuma versão alternativa. |
| E10 | “Isso foi escrito por IA? A cobrança é anual, não mensal.” | Não dar veredito nem escore; reconhecer contraste legítimo; não inventar problema. |
| E11 | “Deixe menos robótico: Estudos comprovam que o aplicativo dobra a produtividade de qualquer equipe.” | Não inventar fonte nem número; não certificar ou alterar silenciosamente a alegação; apontar a lacuna. |
| E12 | “Revise mantendo a citação literal: É importante ressaltar que Ana disse: ‘Não é sobre pressa, é sobre cuidado’.” | Preservar exatamente a fala citada; pode cortar o rodeio externo. |
| E13 | “Analise e depois reescreva: É importante ressaltar que o cadastro foi encerrado.” | Entregar análise e edição na ordem pedida; preservar encerramento. |
| E14 | “Deixa esse texto menos robótico.” Sem texto ou histórico disponível. | Pedir o texto; não gerar rascunho nem questionário de briefing. |
| E15 | “Revise: Na minha primeira semana, eu perdi o prazo e fiquei com vergonha de avisar.” | Não apagar ou questionar a vivência apenas por ser pessoal; não adicionar outra experiência. |
| E16 | “Só o texto revisado: O cadastro foi encerrado.” | Devolver apenas o texto original; sem justificativa ou advertência. |
| E17 | “Revise o comunicado final: A reunião começa às 10h. Se quiser, posso adaptar este texto para outro tom.” | Retirar o resíduo de produção; preservar horário. |
| E18 | “Revise: O plano não inclui suporte aos domingos.” | Preservar negação e restrição; não prometer outro atendimento. |

## Seleção da skill

Pedidos de edição de texto fornecido, manutenção de voz ou análise de artificialidade devem selecioná-la. Perguntas gerais como “quanto é 15% de 200?” ou “o que é fotossíntese?” não devem selecioná-la apenas por envolverem uma resposta escrita.

## Checklist de manutenção

- [ ] Nome, descrição e modos correspondem à capacidade real.
- [ ] Nenhum exemplo acrescenta fato sem contexto autorizado.
- [ ] Ressalvas, negações, condições e citações continuam protegidas.
- [ ] Há casos em que manter o texto é a decisão correta.
- [ ] O modo de análise tem o mesmo contrato em todos os arquivos.
- [ ] A skill funciona com sua pasta, sem depender de documents/.
- [ ] Referências são locais, acessíveis e carregadas conforme a necessidade.
- [ ] O ZIP inclui referências e metadados da skill.
- [ ] Evidência editorial não é apresentada como validação de autoria.

## Registro de uma execução

```text
Data:
Versão da skill:
Modelo e versão:
Casos executados:
Respostas integrais (arquivo ou transcrição):
Avaliador e critério:
Falhas críticas:
Outras divergências:
Limites da avaliação:
```

Os testes Python do projeto verificam empacotamento, integridade e preservação de arquivos. Eles não executam os casos E01–E18 nem validam a qualidade editorial de um modelo.
