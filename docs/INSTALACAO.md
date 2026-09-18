# Instalação

Sem Cara de IA é uma skill com arquivos de apoio. Instale a pasta `skills/sem-cara-de-ia/` inteira; copiar só o `SKILL.md` quebra os links para padrões e exemplos.

## Claude Code

```bash
mkdir -p ~/.claude/skills/sem-cara-de-ia
cp -R skills/sem-cara-de-ia/. ~/.claude/skills/sem-cara-de-ia/
```

Reinicie a sessão se o ambiente não detectar a skill imediatamente. Depois, use pedidos como:

```text
Use $sem-cara-de-ia para revisar este texto, preservando minha voz: ...
```

## Codex

Para usar a skill diretamente a partir deste repositório publicado, peça ao `$skill-installer` do Codex que instale `codaraagency/sem-cara-de-ia`. O instalador pode baixar skills de outros repositórios; abra uma nova sessão depois da instalação.

O pacote também pode entrar em um marketplace de plugins. No Codex CLI, abra `/plugins`, instale-o no marketplace configurado e inicie uma nova sessão. A disponibilidade em marketplaces depende da configuração ou submissão feita pelo mantenedor.

O arquivo ZIP de uma release é um artefato de distribuição verificável. Ele não deve ser apresentado como um instalador universal: use o fluxo de marketplace ou de skill do ambiente que estiver em uso. Consulte a [documentação oficial de plugins](https://learn.chatgpt.com/docs/build-plugins) para o fluxo atualizado.

## Release do GitHub

1. Abra a página de [releases](https://github.com/codaraagency/sem-cara-de-ia/releases).
2. Baixe `sem-cara-de-ia-plugin-<versão>.zip` quando precisar do artefato distribuível.
3. Instale pelo marketplace ou fluxo de skills que seu ambiente oferecer.
4. Confira se os arquivos `references/padroes.md` e `references/exemplos.md` estão ao lado de `SKILL.md` quando a instalação usar a pasta da skill.

## Atualização

Substitua a pasta inteira pela versão mais recente. Não misture referências de uma versão com o `SKILL.md` de outra.
