from urllib.parse import quote_plus

SECRET_KEY = "pY9IK5IKQN7eYaS3R48GDqsA1gz0rE1sAepoi2G4pHL"
ALGORITHM = "HS256"

# 1. Ajusta los datos de conexión para PostgreSQL
DB_USER = "postgres"                  # Tu usuario de Postgres (ej. postgres)
DB_PASSWORD = "12345"           # Tu contraseña
DB_HOST = "localhost"                # IP o servidor
DB_PORT = "5432"                      # Puerto por defecto de Postgres
DB_NAME = "avisos_folio"                       # Nombre de tu base de datos

# 2. Construye la URL estándar de SQLAlchemy para PostgreSQL
DATABASE_URL_AVSF = (
    f"postgresql+psycopg2://{DB_USER}:{quote_plus(DB_PASSWORD)}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)