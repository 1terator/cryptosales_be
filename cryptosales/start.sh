#!/bin/bash

exec uvicorn cryptosales.api:app --host=0.0.0.0 --port=80
