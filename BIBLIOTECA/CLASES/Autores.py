from datetime import datetime

# Clase base que representa un país
class Paises:
    def __init__(self, codigo_pais):
        self.codigo_pais = codigo_pais  # Atributo protegido (encapsulación)

# Clase Autor que hereda de Paises
class Autor(Paises):  # Herencia: Autor hereda de la clase Paises
    def __init__(self, id_autor, nombre_autor, codigo_pais, fecha_nac, fecha_def, biografia_autor, foto_autor):
        super().__init__(codigo_pais)  # Llamada al constructor de la clase base (herencia)
        # Encapsulación: Atributos de la clase Autor están protegidos por el método __init__
        self.id_autor = id_autor  # Atributo encapsulado
        self.nombre_autor = nombre_autor  # Atributo encapsulado
        self.fecha_nac = fecha_nac  # Atributo encapsulado
        self.fecha_def = fecha_def  # Atributo encapsulado
        self.biografia_autor = biografia_autor  # Atributo encapsulado
        self.foto_autor = foto_autor  # Atributo encapsulado
    
    def manejo_fechas(self, fecha):
        """Convierte una fecha en formato 'dd/mm/yyyy' a 'yyyy-mm-dd'."""
        fecha_dt = datetime.strptime(fecha, '%d/%m/%Y')  # Convierte la fecha de string a objeto datetime
        return fecha_dt.strftime('%Y-%m-%d')  # Devuelve la fecha en el nuevo formato

# Nota sobre conceptos de programación:
# - Encapsulación: Atributos de la clase Paises y Autor están protegidos y se accede a ellos a través de métodos.
# - Herencia: La clase Autor hereda de la clase Paises, lo que permite reutilizar su funcionalidad.
# - Polimorfismo: Se podría aplicar si la clase Paises tiene métodos que la clase Autor sobrescriba, permitiendo un comportamiento específico.
