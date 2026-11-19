from fastapi import APIRouter,Depends,HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db_avsf
# from auth.jwt import validar_token
# from models.usuario import Usuario
from models.catalogos import Dependencias, Areas, Puesto, Region, Estados_Mexico,Tipo_Aduana,Tipo_Alerta,Aduanas,Eventos,Aduana_Tipo_Alerta,Estado_Aviso,Estado_Aprobacion,Usuarios
# from schemas.usuario import (UsuarioCreate,UsuarioDelete,UsuarioEstatusUpdate)
import math 

router = APIRouter(
    prefix="/catalogos",
    tags=["Catalogos"]
)


@router.get("/dependencias")
def get_dependencias(
    db:Session = Depends(get_db_avsf),
    # usuario  = Depends(validar_token)
):

    dependencias = (
        db.query(Dependencias)
        # .order_by(Usuario.id_usuario.asc())
        .all())

    return dependencias
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@router.get("/areas")
def get_areas(
    db:Session = Depends(get_db_avsf),
):

    areas = (
        db.query(Areas)
        .all())

    return areas
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@router.get("/puesto")
def get_puesto(
    db:Session = Depends(get_db_avsf),
):

    puesto = (
        db.query(Puesto)
        .all())

    return puesto
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@router.get("/region")
def get_region(
    db:Session = Depends(get_db_avsf),
):

    region = (
        db.query(Region)
        .all())

    return region
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@router.get("/edo_mexico")
def get_edo_mexico(
    db:Session = Depends(get_db_avsf),
):

    edo_mexico = (
        db.query(Estados_Mexico)
        .all())

    return edo_mexico
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@router.get("/tipo_aduana")
def get_tipo_aduana(
    db:Session = Depends(get_db_avsf),
):

    tipo_aduana = (
        db.query(Tipo_Aduana)
        .all())

    return tipo_aduana

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@router.get("/tipo_alerta")
def get_tipo_alerta(
    db:Session = Depends(get_db_avsf),
):

    tipo_alerta = (
        db.query(Tipo_Alerta)
        .all())

    return tipo_alerta

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@router.get("/aduanas")
def get_aduanas(
    db:Session = Depends(get_db_avsf),
):

    aduanas = (
        db.query(Aduanas)
        .all())

    return aduanas
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@router.get("/eventos")
def get_eventos(
    db:Session = Depends(get_db_avsf),
):

    eventos = (
        db.query(Eventos)
        .all())

    return eventos
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@router.get("/ad_tipo_alerta")
def get_ad_tipo_alerta(
    db:Session = Depends(get_db_avsf),
):

    ad_tipo_alerta = (
        db.query(Aduana_Tipo_Alerta)
        .all())

    return ad_tipo_alerta

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@router.get("/edo_aprobacion")
def get_edo_aprobacion(
    db:Session = Depends(get_db_avsf),
):

    edo_aprobacion = (
        db.query(Estado_Aprobacion)
        .all())

    return edo_aprobacion
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@router.get("/Nvo_aviso")
def get_catalogos_iniciales(
    db:Session = Depends(get_db_avsf),
):
    dependencias = (db.query(Dependencias).all())
    areas = (db.query(Areas).all())
    tipo_aduana = (db.query(Tipo_Aduana).all())
    eventos = (db.query(Eventos).all())

    return {
        "dependencias": dependencias,
        "areas": areas,
        "tipo_aduana": tipo_aduana,
        "eventos": eventos
    }


@router.get("/usuarios_area/{id_area}")
def get_usuarios_x_area(
    id_area: int,
    db: Session = Depends(get_db_avsf)
):
    usuarios = (
        db.query(Usuarios)
        .filter(Usuarios.id_area == id_area)
        .order_by(Usuarios.nombres.asc())
        .all()
    )

    return [
        {
            "id_usuario": u.id_usuario,

            "nombre_completo": " ".join(
                parte.strip()
                for parte in [u.nombres, u.paterno, u.materno]
                if parte and parte.strip()
            ),
            "id_area": u.id_area,
        }
        for u in usuarios
    ]

