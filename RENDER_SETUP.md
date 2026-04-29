# 🚀 Guia de Deploy no Render

## ⚙️ Configurações Necessárias no Render

### 1️⃣ Crie uma instância de PostgreSQL no Render
1. Dashboard Render → New → PostgreSQL
2. Nome: `axia-db`
3. Region: mesmo da sua app
4. Copie a `DATABASE_URL` fornecida

### 2️⃣ Configure a Web Service
1. Dashboard Render → New → Web Service
2. Conecte seu repositório GitHub
3. **Settings:**

#### Build Command:
```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
```

#### Start Command:
```bash
gunicorn axia.wsgi:application
```

### 3️⃣ Adicione Variáveis de Ambiente
No Dashboard Render, vá para `Environment`:

| Chave | Valor |
|-------|-------|
| `DEBUG` | `False` |
| `DATABASE_URL` | (copie do PostgreSQL criado acima) |
| `SECRET_KEY` | (mantenha o valor atual do settings.py) |
| `ALLOWED_HOSTS` | `seu-app-name.onrender.com` |

### 4️⃣ Deploy
- Commit e push para GitHub
- Render faz o deploy automaticamente

---

## ✅ Checklist Final

- [ ] PostgreSQL criado no Render
- [ ] Web Service conectado ao repositório
- [ ] Variáveis de ambiente configuradas
- [ ] Build command correto
- [ ] Start command com gunicorn
- [ ] Acessar `seu-app-name.onrender.com`

---

## 🐛 Se der erro:
1. Acesse Logs no Render e procure por erros
2. Verifique se `DATABASE_URL` está correto
3. Certifique-se de que as migrações rodaram
