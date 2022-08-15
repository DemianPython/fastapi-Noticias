from fastapi import FastAPI
import services as _services

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenido a esta api de noticias"}


@app.get("/noticias/ciudad")
async def ciudad_noticias():
    return _services.get_ciudad_noticias()

@app.get("/noticias/deportes")
async def ciudad_noticias():
    return _services.get_deportes_noticias()
    
@app.get("/noticias/ultimas-noticias")
async def ciudad_noticias():
    return _services.get_ultimas_noticias()

@app.get("/noticias/region")
async def ciudad_noticias():
    return _services.get_region_noticias()

@app.get("/noticias/ocio")
async def ciudad_noticias():
    return _services.get_ocio_noticias()

@app.get("/noticias/policiales")
async def ciudad_noticias():
    return _services.get_policia_noticias()

