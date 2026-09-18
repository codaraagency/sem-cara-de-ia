# Publicar no GitHub

Este guia presume que o repositório `codaraagency/sem-cara-de-ia` foi criado no GitHub e que o GitHub CLI (`gh`) está instalado e autenticado. O projeto pode ser público ou privado; para descoberta e instalação por releases, use público.

## Primeira publicação

```bash
git init -b main
git add .
git commit -m "feat: publicar Sem Cara de IA 1.1.0"
git remote add origin https://github.com/codaraagency/sem-cara-de-ia.git
git push -u origin main
```

No GitHub, defina a descrição:

```text
Skill de revisão editorial em pt-BR que preserva fatos, incertezas e voz.
```

Sugestões de tópicos: `portuguese`, `pt-br`, `writing`, `writing-assistant`, `prompt-engineering`, `ai-writing`, `claude-code`, `codex`, `skills`.

## Criar uma release

1. Confira a versão em `.codex-plugin/plugin.json`, `CHANGELOG.md` e `CITATION.cff`.
2. Execute os testes e a validação local.
3. Faça commit das mudanças.
4. Crie e envie a tag correspondente:

```bash
git tag -a v1.1.0 -m "Sem Cara de IA 1.1.0"
git push origin v1.1.0
```

O workflow do GitHub valida o pacote, anexa o ZIP à release e gera notas a partir dos commits. Confirme a release e o download na aba **Releases** antes de divulgá-la.

## Antes de enviar

- [ ] README descreve o comportamento atual.
- [ ] `CHANGELOG.md`, `CITATION.cff` e manifesto têm a mesma versão.
- [ ] `python3 -m unittest discover -s tests -v` passou.
- [ ] `python3 scripts/build_plugin.py --check` passou.
- [ ] Nenhum arquivo de `dist/`, cache ou dado pessoal entrou no commit.
- [ ] A descrição e os tópicos foram configurados no GitHub.

## Atualização após a publicação

Use uma nova versão para alterações distribuídas. Não sobrescreva uma tag existente nem substitua silenciosamente um ZIP já publicado.
