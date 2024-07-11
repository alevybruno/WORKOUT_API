from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field("Nome do centro de treinamento", example="CT King", max_length=20)]
    endereco: Annotated[str, Field("Endereço do centro de treinamento", example="Rua x, Quadra 2", max_length=60)]
    proprietario: Annotated[str, Field("Proprietário do centro de treinamento", example="Marcos", max_length=30)]
    