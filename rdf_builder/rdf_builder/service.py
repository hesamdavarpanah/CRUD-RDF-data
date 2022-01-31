from nameko.rpc import rpc
from nameko_structlog import StructlogDependency

from CRUD.data_property.data_parser import DataReader
from CRUD.simple_crud.crud import RDFBuilderCRUD


# nameko microservice
class RDFBuilder:
    name = "rdf_crud"

    log = StructlogDependency()

    @rpc
    def new_instance(self, data):
        data_reader = DataReader(data)
        crud = RDFBuilderCRUD(id=data_reader.get_id)
        crud.create(lang=data_reader.get_language, data=data_reader.get_data, dir_name="resources")
        return self.log.info(message="the service is running")
