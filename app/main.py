from fastapi import FastAPI
from app.routes import auth_routes, paciente_routes, consulta_routes
# Import all models to ensure relationships are registered
from app.models import user, patient, doctor, consulta

app = FastAPI(title="Clínica Vida+ API", version="0.1")

app.include_router(auth_routes.router, prefix='/auth', tags=['Authentication'])
app.include_router(paciente_routes.router, prefix='/api', tags=['Patients'])
app.include_router(consulta_routes.router, prefix='/api', tags=['Consultations'])

if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host='0.0.0.0', port=8000)