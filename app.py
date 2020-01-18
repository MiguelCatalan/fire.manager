from typing import List

from chalice import Chalice

from fire_manager.application.firefighter.add_firefighter.firefighter_request_error_serializers import \
    NewFirefighterErrorSerializers
from fire_manager.application.firefighter.add_firefighter.firefighter_request_serializers import \
    NewFirefighterRequestSerializers
from fire_manager.application.firefighter.list_firefighters.firefighter_serializers import FirefightersSerializers, \
    FirefighterSerializers
from fire_manager.data.firefighter.FirefighterLocalRepository import FirefighterLocalRepository
from fire_manager.domain.firefighter.add_firefighter.add_firefighter_usecase import \
    AddFirefighterUseCase
from fire_manager.domain.firefighter.add_firefighter.new_firefighter_request import \
    NewFirefighterRequest
from fire_manager.domain.firefighter.firefighter import Firefighter
from fire_manager.domain.firefighter.list_firefighters.list_all_firefighters_usecase import \
    ListAllFirefightersUseCase

app = Chalice(app_name='firefighter_manager')


@app.route('/list_firefighters')
def list_firefighters():
    local_repository = FirefighterLocalRepository()
    use_case = ListAllFirefightersUseCase(local_repository)

    firefighters: List[Firefighter] = use_case.execute()
    return FirefightersSerializers.to_json(firefighters)


@app.route('/new_firefighter', methods=['POST'])
def new_firefighter():
    local_repository = FirefighterLocalRepository()
    use_case = AddFirefighterUseCase(local_repository)

    current_request = app.current_request.json_body
    new_firefighter_request: NewFirefighterRequest = NewFirefighterRequestSerializers.to_model(
        current_request)

    try:
        firefighter: Firefighter = use_case.execute(new_firefighter_request)
    except Exception as error:
        return NewFirefighterErrorSerializers.to_http_error(error)
    else:
        return FirefighterSerializers.to_json(firefighter)
