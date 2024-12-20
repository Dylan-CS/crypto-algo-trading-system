from pydantic_settings import BaseSettings
from typing import Dict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Crypto Trading API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Nacos配置
    NACOS_SERVER: str = "192.168.86.216:8848"
    NACOS_NAMESPACE: str = "d554e4e8-3a66-4661-ab17-75d6c7510eb3"
    SERVICE_NAME: str = "fastapi-service"
    SERVICE_IP: str = "192.168.86.216"
    SERVICE_PORT: int = 8000
    
    # 新增配置
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/crypto_trading"
    EXCHANGE_API_KEY: str = "your_exchange_api_key_here"
    RISK_LIMITS: Dict = {
        "max_position": 1000,
        "max_loss": 100,
        "max_drawdown": 0.2
    }
    MODEL_PARAMS: Dict = {
        "layers": 4,
        "units": 50,
        "dropout": 0.2,
        "sequence_length": 60
    }
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
