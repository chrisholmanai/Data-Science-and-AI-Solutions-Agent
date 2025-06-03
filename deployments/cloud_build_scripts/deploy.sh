#!/bin/bash
echo "Deploying AI agent..."
docker build -t ai-agent .
docker run -p 8000:8000 ai-agent