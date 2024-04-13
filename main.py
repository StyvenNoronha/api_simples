from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date
#uvicorn main:app --reload

app = FastAPI()

class Todo(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[date]

lista = []

@app.post('/inserir')
def inserir(todo: Todo):
    try:
        lista.append(todo)
        return{'status':'sucesso'}
    except:
        return{'status':'erro'}
    
@app.post('/listar')
def listar(opcao: int = 0):
    if opcao == 0:
        print('teste 01')
        return lista
    elif opcao == 1:
        print('teste 01')
        return list(filter(lambda x: not x.realizada, lista))
    elif opcao == 2:
        print('teste 01')
        return list(filter(lambda x: x.realizada, lista))


@app.get('/lista/{id}')
def lista(id: int):
    try:
        return lista[id]    
    except:
        return{'status':'erro Id nao encontrado'}
    

@app.post('/altera')
def altera(id: int):
    try:
        lista[id].realizada = not lista[id].realizada
        return{'status':'operação realidaza com sucesso'}
    except:
        return{'status':'erro 404'}     

@app.post('/excluir')
def excluir(id: int):
    try:
        del lista[id]
        return{'status':'operação realidaza com sucesso'}
    except:
        return{'status':'erro 404'}    
 



