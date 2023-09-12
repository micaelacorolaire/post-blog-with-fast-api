from fastapi import FastAPI,Query,Path
from models.login import login
from models.personalinformationuser import personaldatauser
from models.publications import publications
from routers import loginrouter,personalinformationuserrouter,publicationsrouter
from database import conn


app=FastAPI()
app.include_router(loginrouter.router)
app.include_router(personalinformationuserrouter.router)
app.include_router(publicationsrouter.router)

@app.get('/')
def message():
    return 'welcome to my page made it with Fast Api , enjoy the experience'

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,port=8000)
    