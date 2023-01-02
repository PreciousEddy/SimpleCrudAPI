# Building an API with Python with FastAPI

- [x] Install Fastapi using:
     ` pip install Fastapi `

- [x] Install ASGI server, for production such as Uvicorn or Hypercorn using this below code:
   ` pip install "uvicorn[standard]" `

- [x] Create a MOVIES API
    - Create a file `main.py` with :

      ```
      From fastapi import FastAPI
       
      app = FastAPI()
      ``` 

- [x] ## Run the server with:
    ` uvivorn main:app -- reload `