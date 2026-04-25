# Our Stack Cheat Sheet

## Frontend (11ty)

- `{{ variable }}` = output data
- `{% if x %}` = conditional
- Frontmatter = `--- title: My Page ---`

## HTMX

- `hx-get="/url"` = get data from the api
- `hx-post="/url"` = send POST
- `hx-target="#id"` = where to put response
- `hx-swap="innerHTML"` = how to insert

## Backend (FastAPI)

```python
@app.post("/action")
def action(data: str = Form(...)):
    db.collection.insert_one({...})
    return "<div>HTML response</div>"
```

**Always return HTML code not JSON!**

## MongoDB with Motor

```python
# Import
from motor.motor_asyncio import AsyncIOMotorClient

# Connect (one time)
client = AsyncIOMotorClient(MONGODB_URL)
db = client.carebridge

# CREATE
await db.todos.insert_one({"title": "Buy milk"})

# READ
todo = await db.todos.find_one({"_id": id})
todos = await db.todos.find().to_list(100)

# UPDATE
await db.todos.update_one({"_id": id}, {"$set": {"done": True}})

# DELETE
await db.todos.delete_one({"_id": id})
```

**Remember** to use `.to_list()` when using `.find()`:

```python
# ❌ Wrong - returns cursor, not data
results = await db.todos.find()

# ✅ Correct - gets actual data
results = await db.todos.find().to_list(100)
```

**You're ready. Go build something great.** 🚀
