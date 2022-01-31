from fastapi import FastAPI, Depends
from nameko.standalone.rpc import ClusterRpcProxy

from .models import Data
from ..core import config

app = FastAPI()


# Fastapi service
@app.put("/new_instance")
async def send_data(data: Data, settings: config.Settings = Depends(config.get_settings)):
    item_dict = data.dict()
    with ClusterRpcProxy(settings.cluster_rpc_proxy_config) as rpc:
        result = rpc.rdf_crud.new_instance(item_dict)
    return result
