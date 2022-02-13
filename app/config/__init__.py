from pydantic import BaseSettings


class MongoConfig(BaseSettings):
    host: str
    username: str
    password: str
    class Config:
        env_prefix = 'MONGO_'
