# Aula 01 - Introdução ao Git e GitHub

## Comandos aprendidos

### Navegação no terminal
- `pwd` → mostra o diretório atual
- `ls` → lista arquivos e pastas
- `cd` → navega entre pastas
- `ls -a` → mostra arquivos e pastas ocultas
- `clear` → limpa o terminal

### Git básico
- `git init .` → inicia versionamento no diretório
- `git status` → mostra status do repositório
- `git add <arquivo>` → adiciona arquivo para staging
- `git add .` → adiciona todos os arquivos
- `git commit -m "mensagem"` → cria commit
- `git log` → histórico de commits
- `git reset` → tira do staging
- `git reset <idCommit>` → volta para commit específico

### Branches
- `git branch` → lista branches
- `git checkout -b <nome>` → cria e troca para branch
- `git merge <branch>` → mescla branch
- `git branch -D <branch>` → deleta branch

---
📌 **Observações:**
- Pastas iniciadas com `.` são ocultas.
- `./` → diretório atual
- `../` → diretório superior
