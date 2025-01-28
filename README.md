# Side Scripts

This repository contains two main scripts: a Selenium bot for automating web interactions and a FastAPI backend for fake authentication.

## Table of Contents

- [Selenium Bot](#selenium-bot)
- [Fake Authentication Backend](#fake-authentication-backend)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Selenium Bot

The Selenium bot script is located in the `bot_selenium` directory. It automates the process of logging into a web application and adding a new patient.

### Features

- Logs into a web application using provided credentials.
- Fills out a form to add a new patient with various details.
- Submits the form and closes the browser.

### File

- [bot_selenium/bot.py](bot_selenium/bot.py)

## Fake Authentication Backend

The fake authentication backend is a FastAPI application located in the `fake_auth_backend` directory. It provides endpoints for user login and protected routes.

### Features

- Provides a `/login` endpoint for user authentication.
- Generates JWT tokens for authenticated users.
- Provides a `/protected` endpoint to verify JWT tokens.

### File

- [fake_auth_backend/app.py](fake_auth_backend/app.py)

## Setup

### Prerequisites

- Python 3.7+
- Selenium WebDriver (ChromeDriver)
- FastAPI
- Uvicorn
- JWT

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/side-scripts.git
    cd side-scripts
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Download and install ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/).

## Usage

### Running the Selenium Bot

1. Navigate to the [bot_selenium](http://_vscodecontentref_/1) directory:
    ```sh
    cd bot_selenium
    ```

2. Run the bot script:
    ```sh
    python bot.py
    ```

### Running the Fake Authentication Backend

1. Navigate to the [fake_auth_backend](http://_vscodecontentref_/2) directory:
    ```sh
    cd fake_auth_backend
    ```

2. Start the FastAPI server:
    ```sh
    uvicorn app:app --reload
    ```

3. The backend will be available at `http://localhost:8000`.

## License

This project is licensed under the MIT License.