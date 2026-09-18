# Notas de submissão do plugin

## Visão geral

Sem Cara de IA revisa textos em português brasileiro para reduzir escrita genérica e preservar voz, fatos e incertezas. A análise editorial cita trechos e explica problemas de escrita, sem determinar autoria.

## Modos

- **Edição:** texto revisado com intervenção mínima; respeita pedidos de devolver só o texto.
- **Análise:** observações com citações exatas, sem reescrita não solicitada. “Detecção” continua reconhecido como nome anterior desse modo.
- Ambos podem ser pedidos juntos.

## Avaliação

Os [18 casos de regressão](skills/sem-cara-de-ia/eval.md) cobrem fidelidade factual, negação, condicionais, citações, voz, exemplos que devem permanecer e cumprimento do formato. São especificações de avaliação, não resultados experimentais.

A skill deve evitar inventar dados ou fontes, reescrever quando o pedido é só análise, impor informalidade e atribuir certeza ou porcentagem de autoria por IA. Deve aceitar que um texto já claro não precisa de alteração.

## Distribuição

Versão 1.1.0. O pacote inclui a skill, duas referências, critérios de avaliação e metadados de interface. Não depende de servidor próprio nem de conta adicional à do ambiente que executa a skill.

As 40 heurísticas são editoriais. A pesquisa e seus limites estão no [discovery](documents/README.md). Nenhuma taxa de detecção ou frequência geral é reivindicada.
