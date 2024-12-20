from fastapi import FastAPI, status
from routes import user_routes, book_routes, borrow_routes



app = FastAPI(title="E-Library API System", 
             )


@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"message":  "Welcome to E-Library API System"}


app.include_router(user_routes.user_router, tags= ["Users"])
app.include_router(book_routes.book_router, tags=["Books"])
app.include_router(borrow_routes.borrow_router, tags=["Borrow Books"])


