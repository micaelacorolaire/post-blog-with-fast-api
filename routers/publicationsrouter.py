from fastapi import APIRouter
from models.publications import publications 
publications={'title':'the secret window','content':'was about a mistery man and his house','pub_date':'2013','author':'stephen king'}
router=APIRouter()
@router.get('/publications')
def get_publications():
    return publications

@router.get('/publications/{title}')
def get_title(title:str):
    return list(filter(lambda item:item['title']==title,publications))

@router.get('/publications/{content}')
def get_publications(content:str):
    return list(filter(lambda item:item['content']==content,publications))

@router.get('/publications/{pub_date}')
def get_pub_date(pub_date:int):
    return list(filter(lambda item:item['pub_date']==pub_date,publications))

@router.get('/publications/{author}')
def get_author(author:str):
    return list(filter(lambda item:item['author']==author,publications))