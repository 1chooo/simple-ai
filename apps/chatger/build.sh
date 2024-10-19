#!/bin/bash

source venv/bin/activate

uvicorn run:main --host 127.0.0.1 --port 5002
