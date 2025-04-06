

class BaseConfig:
    _instance = None

    def __new__(cls, config_path="default.json"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config(config_path)

        return cls._instance

    def _load_config(self, config_path):
        import json
        with open(config_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

class AetherGazerConfig(BaseConfig):
    pass