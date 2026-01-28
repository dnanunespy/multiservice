import os
import django

# Configura o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multiservice.settings")
django.setup()

from django.contrib.auth.models import User

def criar():
    # Defina aqui seu usuário e senha provisórios
    USER = "danilo"
    PASS = "Dna@nunes10"
    EMAIL = "dnanunes@outlook.com"

    if not User.objects.filter(username=USER).exists():
        print(f"Criando superusuário {USER}...")
        User.objects.create_superuser(USER, EMAIL, PASS)
        print("✅ Superusuário criado com sucesso!")
    else:
        print("⚠️ Usuário já existe.")

if __name__ == "__main__":
    criar()