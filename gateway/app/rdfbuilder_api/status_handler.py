from fastapi import status


def map_error_code_to_status_code(error_status):
    status_mapping = {
        "RDF data created": status.HTTP_201_CREATED,
        "The rdf_crud service is running": status.HTTP_200_OK,
        "Not connected to logs": status.HTTP_206_PARTIAL_CONTENT,
        Exception: status.HTTP_500_INTERNAL_SERVER_ERROR,
        FileNotFoundError: status.HTTP_406_NOT_ACCEPTABLE,
        FileExistsError: status.HTTP_409_CONFLICT
    }
    return status_mapping.get(error_status)
