from pydantic_settings import BaseSettings

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
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
