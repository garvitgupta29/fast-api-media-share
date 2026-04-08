import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="app.app:app", host="0.0.0.0", port=8000, reload=True)
    # app.app:app means from app folder -> app file -> app variable
    # Now either we just have to do uv run main.py
    # After that either we can directly go to 127.0.0.1:8000 or localhost:8000 
    # with /hello-world and we can directly go to our endpoint.
    # localhost:8000/hello-world
    # Or we can use localhost:8000/docs to directly check and test our endpoints
    # We can also use localhost:8000/redoc to get similar information as docs
    

