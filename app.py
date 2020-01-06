from typing import List

from chalice import Chalice

from fire_manager.application.firefighter_serializers import FirefightersSerializers
from fire_manager.data.firefighter.FirefighterLocalRepository import FirefighterLocalRepository
from fire_manager.domain.firefighter.firefighter import Firefighter
from fire_manager.domain.firefighter.list_all_firefighters_usecase import ListAllFirefightersUseCase

app = Chalice(app_name='firefighter_manager')

@app.route('/list_firefighters')
def list_firefighters():
    local_repository = FirefighterLocalRepository()
    use_case = ListAllFirefightersUseCase(local_repository)
    firefighters: List[Firefighter] = use_case.execute()
    return FirefightersSerializers.to_json(firefighters)
