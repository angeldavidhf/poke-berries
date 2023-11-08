# Poke-berries

Poke-berries is a Python web application built with [FastAPI](https://fastapi.tiangolo.com/) that provides berry statistics and generates histogram charts for berry growth times. It interacts with an external API to obtain berry data and stores it in Redis for caching and quick retrieval.

## Features

- Retrieve and display statistics of various berries.
- Generate histogram charts of berry growth times.
- Store berry statistics in Redis for improved performance.

## Table of Contents

- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Technologies](#technologies)

## Architecture

Your project follows a RESTful architecture, which means that it focuses on resources (in this case, berry statistics) and uses standard HTTP methods (GET) to interact with those resources. The routes and controllers in endpoints.py define how these resources are accessed and manipulated.

- Simplified MVC (Model-View-Controller): Although not a pure MVC approach, your project has elements that resemble this pattern.
    - Model: The logic related to obtaining, calculating and storing berry statistics is contained in redis_client.py. This file manages the data in Redis and performs statistical calculations.
    - View: In your project, views are not typical of an MVC model, as FastAPI handles serialization of responses in JSON or HTML. However, in endpoints.py, you define the routes and controllers that handle API requests and responses.
    - Controller: In your project, the controller is represented by the functions in endpoints.py. These functions define how HTTP requests are handled and how models (berry data in Redis) are interacted with and responses are generated.
- Data Access Layer (Redis): You use Redis as a storage layer for berry statistics. Interaction with Redis is handled in redis_client.py, which includes methods for checking if data is in Redis, calculating statistics, and storing data in Redis.

```bash
  +-------------------------------------+
  |   External API (Berry Data)         |
  +-------------------------------------+
                     |
                     v
  +-------------------------------------+
  |     FastAPI Application             |
  |     +---------------------+         |
  |     | /api/allBerryStats  |         |
  |     |   (Retrieve and     |         |
  |     |    Store Stats)     |         |
  |     +---------------------+         |
  |     | /api/berryHistogram |         |
  |     |   (Generate and     |         |
  |     |   Display Charts)   |         |
  +-------------------------------------+
                     |
                     v
  +-------------------------------------+
  |     Redis (Caching)                 |
  +-------------------------------------+
                     |
                     v
  +-------------------------------------+
  |     Matplotlib (Charts)             |
  +-------------------------------------+
```

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher.
- Docker.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pokeberries.git
   cd pokeberries
   ```

2. Define your `.env` file, this is the configuration used locally

   ```bash
    # Configuration PokeAPI
    POKEAPI_BASE_URL=https://pokeapi.co/api/v2
    POKEAPI_BERRIES_ENDPOINT=/berry
    
    # Configuration Redis
    REDIS_HOST=localhost
    REDIS_PORT=6379
    
    # Configuration FastAPI
    APP_PORT=8000
    APP_HOST=localhost
   ```

3. Create a virtual environment and activate it (optional but recommended):

   ```bash
    python -m venv venv
    source venv/bin/activate
   ```

4. Install project dependencies
   
   ```bash
    pip install -r requirements.txt
   ```

5. Starting docker image services

    ```docker
    docker-compose up
   ```

:partying_face: :clap: This will start application on http://localhost:8000 

## API Endpoints

- **/api/allBerryStats**: Get berry statistics. If data is available in Redis, it is retrieved; otherwise, data is fetched from an external API, stored in Redis, and returned.

- **/api/berryHistogram**: Get a histogram chart of berry growth times. If data is available in Redis, a chart is generated; otherwise, data is fetched, stored, and a chart is created.

For more details on API endpoints and their usage, refer to the code in  `app/api/endpoints.py `.

## Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

