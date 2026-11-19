#SE PONE EXCLUSIVAMENTE LA TABLA
from sqlalchemy import Column, Integer, String
from database import Base

class Dependencias(Base):
    __tablename__ = "avsf_cat_dependencias"

    id_dependencia = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nombre = Column(
        String(100),
        nullable=False
    )
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Areas(Base):
    __tablename__ ="avsf_cat_area"

    id_area = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nombre = Column(
        String(100),
        nullable=False
    )
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Puesto(Base):
    __tablename__ = "avsf_cat_puesto"

    id_puesto = Column(
        Integer,
        primary_key=True,
        index=True
    )

    puesto = Column(
        String(50),
        nullable=False
    )
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Region(Base):
    __tablename__ ="avsf_cat_region"

    id_region = Column(
        Integer,
        primary_key=True,
        index=True
    )

    region = Column(
        String(100),
        nullable=False
    )
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Estados_Mexico(Base):
    __tablename__ = "avsf_cat_estados_mexico"

    id_estado_mexico = Column(
        Integer,
        primary_key=True,
        index=True
    )

    estado = Column(
        String(100),
        nullable=False
    )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Tipo_Aduana(Base):
    __tablename__ = "avsf_tipo_aduana"

    id_tipo_aduana = Column(
        Integer,
        primary_key=True,
        index=True
    )

    tipo_aduana = Column(
        String(100),
        nullable=False
    )
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Tipo_Alerta (Base):
        __tablename__ = "avsf_cat_tipo_alerta"

        id_tipo_alerta = Column(
             Integer,
             primary_key=True,
             index=True
        )

        tipo_alerta = Column(
             String(400),
             nullable=False
        )
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Aduanas(Base):
     __tablename__ = "avsf_cat_aduanas"

     clave_aduana_3 = Column(
          String(3),
          primary_key=True,
          index=True
     )

     nombre_corto = Column(
          String(400),
          nullable=False
     )

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Eventos(Base):
     __tablename__ = "avsf_cat_eventos"

     id_tipo_evento = Column(
          Integer,
          primary_key=True,
          index=True
     )

     tipo_evento = Column(
          String(400),
          nullable=False
     )
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Aduana_Tipo_Alerta(Base):
     __tablename__ = "avsf_aduana_tipo_alerta"

     id_relacion = Column(
          Integer,
          primary_key=True,
          index=True
     )

     id_tipo_alerta = Column(
          Integer,
          nullable=False
     )
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Estado_Aviso(Base):
     __tablename__ = "avsf_cat_est_ado_avisos"

     id_edo_aviso = Column(
          Integer,
          primary_key=True,
          index=True
     )

     edo_aviso = Column(
          String(50),
          nullable=False
     )

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Estado_Aprobacion(Base):
     __tablename__ = "avsf_cat_est_apro_aviso"

     id_edo_apro = Column(
          Integer,
          primary_key=True,
          index=True
     )

     desc_apro = Column(
          String(50),
          nullable=False
     )

class Usuarios(Base):
    __tablename__ = "avsf_det_usuarios"

    id_usuario = Column(
        Integer,
        primary_key=True,
        index=True
    )
    
    nombres = Column(
        String(100)
    )

    paterno = Column(
        String(100)
    )
 
    materno = Column(
        String(100)
    )
    
  
    id_area = Column(
        Integer
    )