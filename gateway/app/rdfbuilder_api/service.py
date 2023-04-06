from fastapi import FastAPI, Depends, Response
from nameko.standalone.rpc import ClusterRpcProxy
from .models import Data
from ..core import config
from .status_handler import map_error_code_to_status_code

app = FastAPI()


# Fastapi service
@app.get("/health")
async def health_check(settings: config.Settings = Depends(config.get_settings)):
    with ClusterRpcProxy(settings.cluster_rpc_proxy_config) as rpc:
        health = rpc.rdf_crud.health_check()
        status = map_error_code_to_status_code(health)
    return Response(content=health, status_code=status)


@app.post("/instances")
async def send_data(data: Data, settings: config.Settings = Depends(config.get_settings)):
    item_dict = data.dict()
    with ClusterRpcProxy(settings.cluster_rpc_proxy_config) as rpc:
        result = rpc.rdf_crud.create(item_dict)
    return Response(content=result, status_code=map_error_code_to_status_code(result))
