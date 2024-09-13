# Requirements

1. Python 3
2. (optional) Allure reports (local installation on MacOS: ```brew install allure```)

# Execution

## Set up python virtual env

```python3 -m venv venv ```

## Activate virtual env

```source venv/bin/activate```

## Install required dependencies 

```pip install -r requirements.txt```

## Run pytest

```pytest```

## Optional: Run tests using Allure Reports

```
mkdir reports
pytest --alluredir=reports
allure serve reports
```
