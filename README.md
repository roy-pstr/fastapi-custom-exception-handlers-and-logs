# FastAPI Custom Exception Handlers And Logs
This repository demonstrate a way to override FastAPI default exception handlers and logs with your own

## Features
- Add milliseconds time measurements to the requests' logs. 
- Custom HTTPException handler.
- Custom Request Validation handler - with extra details on the client input data.
- Custom Unhandled exception handler - with extra details on the error reason.

## Setup
```
poetry install
```

## Start
```
poetry run uvicorn main:app --reload
```

