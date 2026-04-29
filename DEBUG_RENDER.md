# 🐛 Diagnóstico do Erro 500 no Render

## ✅ Passos para Identificar o Erro

### 1. Acesse os Logs do Render
- Dashboard Render → Seu App → Logs
- Procure por linhas com **ERROR** ou **Traceback**
- Copie o erro completo

### 2. Problemas Comuns e Soluções

#### ❌ **Erro: "no such column"**
```
OperationalError: no such column: ...
```
**Solução:** As migrações não foram aplicadas
```bash
python manage.py migrate
```

#### ❌ **Erro: "ModuleNotFoundError"**
```
ModuleNotFoundError: No module named 'xxx'
```
**Solução:** Falta um pacote em `requirements.txt`
- Adicione o pacote
- Commit e push para GitHub
- Render faz rebuild automático

#### ❌ **Erro: "DisallowedHost"**
```
DisallowedHost: Invalid HTTP_HOST header
```
**Solução:** Verifique `ALLOWED_HOSTS` no settings.py
- Deve incluir seu domínio do Render ex: `seu-app.onrender.com`

#### ❌ **Erro: "DEBUG=True" em Produção**
```
Not Allowed Host error ou erro de CSS/JS
```
**Solução:** Definir `DEBUG=False` em Variáveis de Ambiente

#### ❌ **Erro: "no DATABASE_URL"**
```
ImproperlyConfigured: ...
```
**Solução:** 
- Criar PostgreSQL no Render
- Copiar DATABASE_URL
- Adicionar como Variável de Ambiente

### 3. Teste Localmente Antes de Deploy

```bash
# Em desenvolvimento com SQLite
python manage.py runserver

# Simular produção (com PostgreSQL se possível)
DEBUG=False python manage.py runserver
```

### 4. Envie os Logs do Erro

Se ainda não resolver, compartilhe:
- **Erro do log do Render** (copie a parte de ERROR/Traceback)
- **Sua URL do app** (para verificar ALLOWED_HOSTS)
