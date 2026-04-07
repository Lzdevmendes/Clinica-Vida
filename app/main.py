from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth_routes, paciente_routes, consulta_routes, doctor_routes
# Import all models to ensure relationships are registered
from app.models import user, patient, doctor, consulta

app = FastAPI(
    title="Clínica Vida+ API",
    version="1.0.0",
    description="API para gerenciamento de clínica médica: pacientes, médicos e consultas.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix='/auth', tags=['Authentication'])
app.include_router(paciente_routes.router, prefix='/api', tags=['Patients'])
app.include_router(consulta_routes.router, prefix='/api', tags=['Consultations'])
app.include_router(doctor_routes.router, prefix='/api', tags=['Doctors'])


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "Clínica Vida+ API"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
