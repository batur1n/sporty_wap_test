## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.7 or higher (and added to PATH)
- Pip (Python package installer)


## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/batur1n/sporty_wap_test.git
cd sporty_wap_test
```

### 2. Create virtual environment (venv)
For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
For Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the tests
```bash
pytest test_twitch_streamer_page.py
```

### Project structure
```bash
.
├── conftest.py               # WebDriver setup using Pytest fixtures
├── requirements.txt          # List of dependencies
├── test_twitch_logo.py       # Test which opens Twitch streamer page and takes a screenshot
└── README.md                 # Project documentation
```
