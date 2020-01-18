class RemoveFirefighterRequestSerializers:

    @staticmethod
    def to_model(json_string) -> str:
        return json_string.get("id", "")
