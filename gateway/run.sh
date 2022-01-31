#!/bin/bash

uvicorn gateway.app.api.service:app --reload --host 0.0.0.0 --port 8000