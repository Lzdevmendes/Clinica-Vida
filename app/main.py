from fastapi import FastAPI
from app.routes import auth_routes, paciente_routes, consulta_routes

app = FastAPI(title="Clínica Vida+ API", version="0.1")
app.include_router(auth_routes.router, prefix='/auth')
# incluir outras rotas

if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host='0.0.0.0', port=8000)