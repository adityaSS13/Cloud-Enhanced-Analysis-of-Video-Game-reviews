# Cloud Enhanced Analysis of Game Reviews

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/project-repo.git
    ```

2. **Install Python:**

   Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/)

3. **Create a virtual environment:**

    ```bash
    python -m venv <name>
    ```

4. **Activate the virtual environment:**

    - On Windows:

      ```bash
      <name>\Scripts\activate
      ```

    - On Unix or macOS:

      ```bash
      source <name>/bin/activate
      ```

5. **Install dependencies:**

    ```bash
    pip install flask transformers requests torch
    ```

6. **Run the app in debug mode:**

    ```bash
    flask --app game_rec run --debug
    ```

Now, you can access the application at [http://localhost:5000](http://localhost:5000) in your web browser.
