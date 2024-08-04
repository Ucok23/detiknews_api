# Detik News Search Unofficial API
This script can search and return list of news result

## Features

- Search for news articles by query
- Retrieve detailed article content
- Limit the number of search results

## Prerequisites

- Python 3.x
- Pip (Python package installer)
- Virtual environment (optional but recommended)

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment** (optional):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

    Make sure you have a `requirements.txt` file with necessary dependencies. For this project, it might include:

    ```
    Flask
    requests
    beautifulsoup4
    ```

## Configuration

Ensure that your `script` file contains the `DetikNewsApi` class and is correctly implemented. The Flask app in `main.py` uses this class for making API requests.

## Usage

1. **Run the Flask application**:

    ```bash
    python main.py
    ```

2. **Access the API endpoints**:

    - **Search for news articles**:
        - For details and limit:
            ```http
            GET /search?q=<query>&detail=<true|false>&limit=<number>
            ```
        - Without details and limit:
            ```http
            GET /search?q=<query>
            ```

    - **Parameters**:
        - `q`: The search query (required).
        - `detail`: Whether to include the full article body in the response (`true` or `false`). Defaults to `false`.
        - `limit`: The maximum number of results to return. Defaults to `None`.

    - **Example Request**:

        ```
        GET /search?q=makan%20siang%20gratis&detail=true&limit=5
        ```

    - **Example Response**:

        ```json
        {
            "status": 200,
            "data": [
                {
                    "judul": "Example Title",
                    "link": "https://news.detik.com/example",
                    "gambar": "https://example.com/image.jpg",
                    "body": "Full article body...",
                    "waktu": "2024-08-04T12:34:56"
                }
                // Additional articles...
            ],
            "length": 5
        }
        ```