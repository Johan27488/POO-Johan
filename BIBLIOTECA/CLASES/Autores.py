from datetime import datetime
import re
from rut_chile import rut_chile

class Paises:
    def __init__(self, codigo_pais):
        self.codigo_pais = codigo_pais

class Autor(Paises):
    def __init__(self, id_autor, nombre_autor, codigo_pais, fecha_nac, fecha_def, biografia_autor, foto_autor):
        super().__init__(codigo_pais)
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.fecha_nac = fecha_nac
        self.fecha_def = fecha_def
        self.biografia_autor = biografia_autor
        self.foto_autor = foto_autor
    
    def manejo_fechas(self, fecha):
        """Convierte una fecha en formato 'dd/mm/yyyy' a 'yyyy-mm-dd'."""
        fecha_dt = datetime.strptime(fecha, '%d/%m/%Y')
        return fecha_dt.strftime('%Y-%m-%d')
