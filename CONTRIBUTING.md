# Como contribuir

Obrigado por ajudar a melhorar Sem Cara de IA. O projeto aceita correções de documentação, exemplos, casos de avaliação, melhorias de empacotamento e propostas para a skill.

## Antes de abrir uma issue

Verifique se o caso já aparece em [issues](https://github.com/codaraagency/sem-cara-de-ia/issues) ou nos [40 padrões](skills/sem-cara-de-ia/references/padroes.md). Para um problema de escrita, inclua contexto suficiente: gênero, público, pedido feito à skill, texto de entrada, resposta observada e por que ela falha.

Remova dados pessoais, material confidencial e textos sobre os quais você não tem direito de compartilhar.

## Propostas para a skill

Um novo padrão precisa descrever:

1. O trecho e o problema editorial observável.
2. O contexto em que ele aparece.
3. Uma exceção legítima ou caso em que não deve ser alterado.
4. O risco de uma edição inadequada.
5. Um caso de avaliação que permita verificar o comportamento.

Não trate uma expressão isolada como prova de autoria. Evite regras baseadas em “sempre”, contagens arbitrárias ou alegações de frequência sem corpus comparável. Preservar fatos, condições, citações e voz tem prioridade sobre encurtar o texto.

## Desenvolvimento local

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build_plugin.py --check
```

Os testes verificam o pacote. Os casos E01–E18 em [eval.md](skills/sem-cara-de-ia/eval.md) são uma suíte comportamental manual: registre modelo, versão, pedido integral e resposta antes de alegar melhoria.

## Pull requests

- Mantenha cada PR pequeno e com um propósito claro.
- Atualize exemplos e testes quando mudar o comportamento da skill.
- Não inclua `dist/`, dependências locais ou arquivos temporários.
- Explique alterações de comportamento e limites conhecidos na descrição.
- Use português brasileiro nos textos voltados ao usuário.

## Licença

Ao contribuir, você concorda que suas contribuições sejam distribuídas sob a [MIT](LICENSE).
