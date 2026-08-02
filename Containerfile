FROM mcr.microsoft.com/devcontainers/python:3.14


ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    build-essential \
    cmake \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

USER vscode
WORKDIR /workspace
