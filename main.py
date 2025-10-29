from flask import Flask
from src.core.env_loader import initialize_environment
from src.ingest.api.endpoint import ingest_api

# Inicializar o Flask
app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(ingest_api)

if __name__ == "__main__":
    # Carregar variáveis de ambiente
    initialize_environment()
    # Rodar o servidor Flask
    app.run()