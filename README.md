# Sem Cara de IA

[![Licença MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-0057D8.svg)](LICENSE)
[![Validação](https://github.com/codaraagency/sem-cara-de-ia/actions/workflows/plugin.yml/badge.svg)](https://github.com/codaraagency/sem-cara-de-ia/actions/workflows/plugin.yml)
[![Release](https://img.shields.io/github/v/release/codaraagency/sem-cara-de-ia?display_name=tag&color=0057D8)](https://github.com/codaraagency/sem-cara-de-ia/releases)

Skill de revisão para português brasileiro. Ela reduz formulações genéricas e repetitivas sem apagar fatos, incertezas, citações ou a voz de quem escreveu.

> “Isso foi escrito por IA?” não tem resposta confiável só pelo estilo. Sem Cara de IA revisa padrões editoriais observáveis; não atribui autoria nem promete resultado em detectores.

## O que faz

- **Edita:** melhora clareza, precisão e naturalidade com a menor intervenção possível.
- **Analisa:** cita trechos que soam mecânicos ou genéricos e explica o efeito, sem reescrever quando esse for o pedido.
- **Preserva:** números, datas, condições, negações, promessas, fontes, nomes de interface, URLs e citações literais.

Ela também mantém estruturas que cumprem uma função: cautela acadêmica, termos técnicos, contrastes reais, listas instrucionais, oralidade brasileira e recursos literários.

## Instalação

Há instruções completas para [Claude Code](docs/INSTALACAO.md#claude-code), [Codex](docs/INSTALACAO.md#codex) e instalação a partir de um [release do GitHub](docs/INSTALACAO.md#release-do-github).

Para Claude Code, copie a pasta inteira da skill:

```bash
mkdir -p ~/.claude/skills/sem-cara-de-ia
cp -R skills/sem-cara-de-ia/. ~/.claude/skills/sem-cara-de-ia/
```

## Uso

```text
Use $sem-cara-de-ia para revisar este e-mail, preservando os fatos e a minha voz: ...

Só aponte o que soa artificial, sem reescrever: ...

Revise e devolva só o texto: ...
```

| Pedido | Entrega |
| --- | --- |
| “Deixe mais natural” | Texto revisado, com explicação breve se ela ajudar. |
| “Só analise” | Trechos citados, padrão e efeito no contexto. |
| “Analise e reescreva” | Análise seguida da revisão. |
| “Só o texto” | Apenas o texto final. |

## Como decide o que mudar

A skill usa 40 heurísticas editoriais organizadas por função, com exceções explícitas. Ela não proíbe palavras isoladas como “crucial” ou “robusto”; avalia se o trecho acrescenta sentido no contexto.

- [Padrões e exceções](skills/sem-cara-de-ia/references/padroes.md)
- [Exemplos de decisão](skills/sem-cara-de-ia/references/exemplos.md)
- [Casos de avaliação](skills/sem-cara-de-ia/eval.md)

## Desenvolvimento

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build_plugin.py --check
python3 scripts/build_plugin.py
```

O último comando cria `dist/sem-cara-de-ia-plugin-<versão>.zip`. O pacote inclui a skill completa, referências, critérios de avaliação e metadados. A validação não mede a qualidade da resposta de um modelo; os casos comportamentais estão descritos em [`eval.md`](skills/sem-cara-de-ia/eval.md).

Para publicar uma nova versão, siga o [guia de release](docs/PUBLICAR_NO_GITHUB.md). O workflow valida o pacote em pull requests e cria uma release com o ZIP ao receber uma tag `v*`.

## Limites

As 40 heurísticas são critérios editoriais, não um classificador de autoria. Nenhuma taxa de detecção ou frequência geral é reivindicada. As referências da skill trazem padrões, exceções e casos de avaliação necessários ao uso.

## Contribuir

Leia [CONTRIBUTING.md](CONTRIBUTING.md) antes de abrir uma issue ou pull request. Bugs de segurança devem seguir [SECURITY.md](SECURITY.md).

## Licença

Distribuído sob a [licença MIT](LICENSE).
