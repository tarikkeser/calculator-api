from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings (BaseSettings):
    app_name: str = "Calculator API"
    app_version: str = "2.0.0"
    
    #class Config:
        #env_file = ".env"
        
    # Pydantic 2.x uses SettingsConfigDict instead of Config    
    model_config = SettingsConfigDict(env_file=".env")
        
# instance of Settings to load environment variables        
settings = Settings()
