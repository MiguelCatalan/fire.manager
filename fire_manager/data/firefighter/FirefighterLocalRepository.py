from random import randint
from typing import List

from interface import implements

from fire_manager.domain.firefighter.add_firefighter.new_firefighter_request import \
    NewFirefighterRequest
from fire_manager.domain.firefighter.firefighter import Firefighter
from fire_manager.domain.firefighter.firefighter_repository import FirefighterRepository


class FirefighterLocalRepository(implements(FirefighterRepository)):
    __in_memory_firefighter_list: List[Firefighter]

    def __init__(self):
        self.__in_memory_firefighter_list = list()
        self.__populate_list()

    def get_all_firefighters(self) -> List[Firefighter]:
        return self.__in_memory_firefighter_list

    def search_firefighter_by_email(self, email: str) -> Firefighter:
        return next((firefighter for firefighter in self.__in_memory_firefighter_list if
                     firefighter.email == email), None)

    def save_firefighter(self, request: NewFirefighterRequest) -> Firefighter:
        random_id = randint(100, 999)  # TODO: improve this assignation
        firefighter: Firefighter = Firefighter(
            firefighter_id=str(random_id),
            email=request.email,
            name=request.name,
            phone=request.phone
        )
        self.__in_memory_firefighter_list.append(firefighter)
        return firefighter

    def get_firefighter(self, firefighter_id: str) -> Firefighter:
        return next((firefighter for firefighter in self.__in_memory_firefighter_list if
                     firefighter.firefighter_id == firefighter_id), None)

    def remove_firefighter(self, firefighter_id: str) -> bool:
        firefighter: Firefighter = self.get_firefighter(firefighter_id)
        self.__in_memory_firefighter_list.remove(firefighter)
        return True

    def __populate_list(self):
        self.__in_memory_firefighter_list.append(
            Firefighter(
                firefighter_id="123",
                email="tom@test.com",
                name="Tom",
                phone="+34666666666"
            ))
        self.__in_memory_firefighter_list.append(
            Firefighter(
                firefighter_id="321",
                email="mot@test.com",
                name="Mot",
                phone="+34555555555"
            ))
