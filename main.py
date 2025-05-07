# from collections import defaultdict
# from fastapi import FastAPI 
# from fastapi.exceptions import RequestValidationError
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse
# from fastapi import status
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
from src.utilities.exception_handling import CustomException



# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



# @app.exception_handler(RequestValidationError)
# async def custom_form_validation_error(request, exc):
#     reformatted_message = defaultdict(list)
#     for pydantic_error in exc.errors():
#         loc, msg = pydantic_error["loc"], pydantic_error["msg"]
#         filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc
#         field_string = ".".join(filtered_loc)
#         reformatted_message[field_string].append(msg)

#     return JSONResponse(
#         status_code=status.HTTP_400_BAD_REQUEST,
#         content=jsonable_encoder(
#             {"detail": "Invalid request", "errors": reformatted_message}
#         ),
#     )


# @app.get('/test')
# def test():
#     return 'Api is working properly'



def test_exception_handling():
    try:
        a = 2/0
    except Exception as e:
        raise CustomException(e, sys) 