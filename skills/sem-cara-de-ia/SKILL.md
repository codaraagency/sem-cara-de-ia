---
name: sem-cara-de-ia
description: Revisa textos fornecidos em português brasileiro para reduzir escrita genérica ou artificial, preservando fatos e voz. Use para pedidos de deixar um texto menos robótico, tirar a cara de IA, manter a voz do autor ou analisar o que soa artificial. Também atende perguntas sobre aparente autoria por IA, com análise de estilo e sem veredito de autoria. Não se aplica a perguntas gerais sem tarefa de revisão textual.
---

# Sem Cara de IA

Edite o mínimo necessário para que o texto cumpra seu propósito com a voz de quem escreveu. Os padrões são heurísticas editoriais, sem ranking validado de frequência ou poder de detecção.

## Escolher o modo

- **Edição:** quando o usuário pedir para revisar, melhorar ou deixar mais natural. É o padrão para uma invocação com texto sem outra orientação.
- **Análise:** quando pedir para apontar problemas, avaliar se soa artificial ou perguntar se foi escrito por IA. “Detecção” é um nome antigo para este modo. Cite trechos e explique o efeito; não ofereça reescritas sem solicitação.
- **Análise e edição:** quando ambas forem pedidas, entregue ambas, na ordem solicitada.

Se o texto já estiver na conversa, use-o. Se faltar o texto, peça somente esse material. Infira gênero e público quando forem claros; pergunte apenas se a resposta mudar uma decisão editorial importante.

## Preservar o conteúdo

- Mantenha números, datas, nomes, responsáveis, causas, condições, negações, fontes, compromissos e incertezas. Não transforme “pode” em “vai”, correlação em causa ou opinião em fato.
- Use detalhes concretos apenas quando estiverem no texto ou no contexto fornecido. Não invente resultados, referências, vivências, motivos de atraso ou promessas para melhorar a escrita.
- Uma afirmação presente no original não se torna falsa apenas porque falta sua fonte na conversa. Se houver alegação relevante sem sustentação acessível, preserve seu sentido e sinalize a lacuna fora do texto; não a certifique, fortaleça ou elimine silenciosamente. Só faça correção substantiva quando houver base e o pedido a comportar.
- Preserve citações literais, nomes de interface, comandos e URLs. Edite o texto ao redor; não altere a fala citada para fazê-la soar natural.
- Se uma lacuna impedir uma boa reescrita, melhore o restante e indique o dado que falta. Não insira marcadores como “[inserir dado]” no texto final sem pedido.

## Decidir o que mudar

Leia o texto inteiro e identifique propósito, registro, ritmo, humor e escolhas pessoais. Na ausência de amostras do autor, use o próprio texto como referência e não alegue reproduzir uma voz que não conhece.

Priorize alterações de sentido e falta de informação necessária; depois examine redundância, abstração sem explicação, contrastes artificiais, estrutura repetitiva e inadequação do tom. Para cada intervenção, identifique o problema concreto e considere se a construção tem uma função legítima.

- Palavras como “crucial”, “robusto”, “jornada” e “além disso” não são proibidas.
- Preserve passivas naturais, cautela acadêmica, contrastes reais, listas úteis e recursos literários.
- Em prosa corrente em pt-BR, não introduza travessões para dar ênfase, explicar uma frase simples ou criar pausas que uma vírgula, dois-pontos ou ponto resolveriam naturalmente. Se o original acumular intercalações com travessão, simplifique a pontuação sem perder relações e sentido. Preserve travessões funcionais, como os de diálogo, apartes claros e ritmo literário intencional; não use uma contagem fixa como critério.
- Respeite o pt-BR do autor, incluindo oralidade e variações regionais. Não adicione gírias ou erros para simular humanidade; não formalize uma mensagem casual sem pedido.
- Retire resíduos do processo, como ofertas de adaptação coladas em um comunicado final, quando não fizerem parte do documento solicitado.
- Se o texto já funcionar, mantenha-o. Não há cota de alterações.

Para uma revisão simples, estas instruções bastam. Consulte apenas o apoio necessário:

| Situação | Referência |
| --- | --- |
| Revisão ampla ou necessidade de nomear um padrão com precisão | [Padrões e exceções](references/padroes.md), na família relevante |
| Dúvida sobre gênero, voz, lacuna factual ou decisão de manter | [Exemplos de decisão](references/exemplos.md) |
| Manutenção ou avaliação desta skill | [Casos e critérios de avaliação](eval.md) |

## Entregar

**Edição:** devolva o texto completo revisado. Acrescente uma explicação breve das mudanças relevantes quando útil; respeite “só o texto”, extensão e formato pedidos. Se nada exigir mudança, devolva o original e, se couber, informe que o manteve.

**Análise:** para cada problema, apresente citação exata, nome do padrão e efeito no contexto. Use o código P quando ajudar na rastreabilidade; se usar um código, confira-o na referência. Agrupe ocorrências repetidas. Não invente alertas para completar a resposta. Se não encontrar problema relevante, diga isso.

**Pergunta sobre autoria:** explique brevemente que o estilo isolado não permite confirmar autoria. Apresente apenas observações sustentadas pelo texto, sem porcentagem de IA, veredito ou promessa de passar por detectores. Não repita essa ressalva em revisões comuns que não perguntam sobre autoria.

Antes de entregar, compare original e revisão: alguma informação, condição, ressalva ou escolha de voz mudou sem autorização? Corrija a divergência e retire comentários de bastidor do texto final.
