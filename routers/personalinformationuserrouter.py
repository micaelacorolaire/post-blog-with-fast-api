from fastapi import APIRouter
from models.personalinformationuser import personaldatauser

personaldatauser={'name':'micaela','lastname':'corolaire','age':29,'nacionality':'argentina','email':'corolairem@gmail.com','password':'sarasa'}

router=APIRouter()
@router.get('/personaldatauser')
def get_personaldatauser():
    return personaldatauser

@router.get('/personaldatauser/{name}')
def get_name(name:str):
    return list(filter(lambda item:item[name]==name,personaldatauser))

@router.get('/personaldatauser/{lastname}')
def get_lastname(lastname:str):
    return list(filter(lambda item:item['lastname']==lastname,personaldatauser))

@router.get('/personaldatauser/{age}')
def get_age(age:int):
    return list(filter(lambda item:item['age']==age,personaldatauser))

@router.get('/personaldatauser/{nacionality}')
def get_nacionality(nacionality:str):
    return list(filter(lambda item:item['nacionality']==nacionality,personaldatauser))

@router.get('/personaldatauser/{email}')
def get_email(email:str):
    return list(filter(lambda item:item['email']==email,personaldatauser))

@router.get('/personaldatauser/{password}')
def get_password(password:str):
    return list(filter(lambda item:item['password']==password,personaldatauser))

