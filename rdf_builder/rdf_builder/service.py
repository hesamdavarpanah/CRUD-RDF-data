from nameko.rpc import rpc
from nameko_structlog import StructlogDependency
from .CRUD.data_property.data_parser import DataReader
from .CRUD.simple_crud.crud import RDFBuilderCRUD
from .CRUD.simple_crud.utility import Logger


# nameko microservice
class RDFBuilder:
    name = "rdf_crud"

    log = StructlogDependency()

    @rpc
    def health_check(self):
        logger = Logger()
        try:
            # Service status response
            self.log.info(f"{self.name}.{self.health_check.__name__}: started")
            self.log.info(f"{self.name}.{self.health_check.__name__} service is running...")
            self.log.info(f"{self.name}.{self.health_check.__name__}: ended.")
            response = f"The {self.name} service is running"

            # Send log to mongodb
            logger.insert_data(service_name=f"{self.name}.{self.health_check.__name__}", service_status=response,
                               message=response, data_loaded="test")
            return response
        except Exception as error:
            self.log.info(f"The {self.name}.{self.health_check.__name__} service is not running")
            # Send log to mongodb
            logger.insert_data(service_name=self.name, service_status=error.__class__(), message=error.__str__(),
                               data_loaded=error.__str__())
            return error

    @rpc
    def create(self, data):
        logger = Logger("logs", "log_collection")

        # Read and parse data
        data_reader = DataReader(data)
        try:
            self.log.info(f"{self.name}.{self.create.__name__}: started")
            self.log.info(message=f"{data} loaded")
            crud = RDFBuilderCRUD(id=data_reader.get_id)

            # Send data to CRUD
            message = crud.create(lang=data_reader.get_language, data=data_reader.get_data, dir_name="resources")
            self.log.info(message=message)
            response = f"The {self.name}.{self.create.__name__} service is running"
            logger.insert_data(service_name=f"{self.name}.{self.create.__name__}", message=message,
                               service_status=response,
                               data_loaded=[data])
            self.log.info(message=f"{self.name}.{self.create.__name__}: ended.")
            return message
        except Exception as error:
            logger.insert_data(service_name=f"{self.name}.{self.create.__name__}", service_status=error.__str__(),
                               message=error.__str__(),
                               data_loaded=error.__str__())
            return error
