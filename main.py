from fastapi import FastAPI
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError

from exception_handlers import request_validation_exception_handler, http_exception_handler, unhandled_exception_handler
from middleware import log_request_middleware
app = FastAPI(
    responses={404: {"description": "Not found bal bla"}},
)

app.middleware("http")(log_request_middleware)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

# If b is zero -> implicit HTTPException with status code 500 and detail "Internal Server Error"
@app.get("/divide")
def do_divide(a: int, b: int):
    return a/b

@app.get("/divide_with_explicit_exception")
def do_divide2(a: int, b: int):
    try:
        return a/b
    except ZeroDivisionError:
        raise HTTPException(status_code=500, detail="Division by zero is not allowed")