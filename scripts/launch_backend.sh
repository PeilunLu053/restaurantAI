#!/bin/bash
cd "$(dirname "$0")/.."
uvicorn backend.main:app --reload
