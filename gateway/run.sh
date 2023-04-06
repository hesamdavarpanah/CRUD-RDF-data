#!/bin/bash

uvicorn app.rdfbuilder_api.service:app --reload --host 0.0.0.0 --port 8000