from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[str, Field("Nome do atleta", example="João", max_length=50)]
    cpf: Annotated[int, Field("CPF do atleta", example="12345678900", max_length=11)]
    idade: Annotated[int, Field("Idade do atleta", example=20)]
    peso: Annotated[PositiveFloat, Field("Peso do atleta", example=70)]
    altura: Annotated[PositiveFloat, Field("Altura do atleta", example=1.75)]
    sexo: Annotated[str, Field("Sexo do atleta", example="M", max_length=1)]
