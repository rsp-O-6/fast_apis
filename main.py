from collections import defaultdict
from fastapi import FastAPI 
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.utilities.exception_handling import CustomException
import sys
from src.router import router
# from src.router import router

app = FastAPI()

# ✅ CORS allow for Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Production me yaha pe apna Angular domain specify karna better hoga
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include router from src
app.include_router(router)

# ✅ Custom validation error handler
@app.exception_handler(RequestValidationError)
async def custom_form_validation_error(request, exc: RequestValidationError):
    reformatted_message = defaultdict(list)
    for pydantic_error in exc.errors():
        loc, msg = pydantic_error["loc"], pydantic_error["msg"]
        filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc
        field_string = ".".join(str(item) for item in filtered_loc)
        reformatted_message[field_string].append(msg)

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {"detail": "Invalid request", "errors": reformatted_message}
        ),
    )

# ✅ Simple test route
@app.get("/test")
def test():
    return {"message": "API is working properly"}

# ✅ Exception handling test
@app.get("/exception-test")
def test_exception_handling():
    try:
        a = 2 / 0
    except Exception as e:
        raise CustomException(e, sys)