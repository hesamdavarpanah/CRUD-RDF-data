from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    rabbit_schema: str = "amqp"
    rabbit_user: str = "guest"
    rabbit_password: str = "guest"
    rabbit_host: str = "172.16.238.11"
    rabbit_port: int = 5672

    @property
    def amqp_uri(self):
        return f"{self.rabbit_schema}://{self.rabbit_user}:{self.rabbit_password}@{self.rabbit_host}:{self.rabbit_port}/"

    @property
    def cluster_rpc_proxy_config(self):
        return {"AMQP_URI": self.amqp_uri}


@lru_cache()
def get_settings():
    return Settings()
