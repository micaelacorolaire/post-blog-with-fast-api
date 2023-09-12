from fastapi import APIRouter,Path,Query
from models.login import login

login={'email':'corolairem@gmail.com','password':'origami','nickname':'micky'}

router=APIRouter()
@router.get('/login')
def add_login():
    return login

@router.get('/login/{email}')
def get_email(email:str):
    return list(filter (lambda item:item['email']==email,login))

@router.get('/login/{password}')
def get_password(password:str):
    return list(filter(lambda item:item['password']==password,login))

@router.get('/login/{nickname}')
def get_nickname(nickname:str):
    return list(filter(lambda item:item['nickname']==nickname,login))


