import api.v1.endpoints
from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response, Request
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
from models.usuario_model import UsuarioModel
from models.tarefa_model import TarefaModel
from core.deps import get_session
from core.security import gerar_hash_senha, comparar_senha
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from schemas.usuario_schema import * 
from schemas.tarefa_schema import * 
from core.auth import criar_acess_token, get_current_user

router = APIRouter()

@router.post('/', response_model=TarefaSchema)
async def post_tarefa(tarefa: TarefaSchema, db: AsyncSession = Depends(get_session), usuarioLogado: UsuarioSchemaBase = Depends(get_current_user)):
    nova_tarefa: TarefaModel = TarefaModel(
        usuario_id=usuarioLogado.id, 
        nome=tarefa.nome, 
        descricao=tarefa.descricao, 
        concluido=tarefa.concluido, 
        criado_em = str(datetime.now()), 
        atualizado_em = str(datetime.now()))
    async with db as session:
        try:
            session.add(nova_tarefa)
            await session.commit()
            return nova_tarefa
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Não foi possivel criar novo usuário')



@router.get('/', response_model=List[TarefaSchema])
async def get_tarefas(request: Request, db: AsyncSession = Depends(get_session), usuarioLogado = Depends(get_current_user)):
    page: int = int(request.query_params.get('page'))
    page_size: int = int(request.query_params.get('page_size'))
    offset: int = ((page - 1) * page_size)  

    async with db as session:
        query = select(TarefaModel).filter(TarefaModel.usuario_id == usuarioLogado.id) if request.query_params.get('nome') == None else select(TarefaModel).filter(TarefaModel.usuario_id == usuarioLogado.id).filter(TarefaModel.nome == request.query_params.get('nome')) 
        query = query.limit(page_size).offset(offset)
        result = await session.execute(query)
        tarefas: List[TarefaSchema] = result.scalars().unique().all()
    
        return tarefas



@router.get('/{id}', response_model=TarefaSchema)
async def get_tarefa(id: int, db: AsyncSession = Depends(get_session), usuarioLogado = Depends(get_current_user)):
    async with db as session:
        query = select(TarefaModel).filter(TarefaModel.id == id).filter(TarefaModel.usuario_id == usuarioLogado.id)
        result = await session.execute(query)
        tarefa: TarefaSchema = result.scalars().unique().one_or_none()
        if tarefa:
            return tarefa
        else:
            raise HTTPException(detail='Tarefa não encontrada',
                                status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
async def delete_tarefa(id: int, db: AsyncSession = Depends(get_session), usuarioLogado = Depends(get_current_user)):
    async with db as session:
        query = select(TarefaModel).filter(TarefaModel.id == id).filter(TarefaModel.usuario_id == usuarioLogado.id)
        result = await session.execute(query)
        tarefa: UsuarioModel = result.scalars().unique().one_or_none()
        if tarefa:
            await session.delete(tarefa)
            await session.commit()
            Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Tarefa não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)
        

@router.put('/{id}', response_model=TarefaSchema ,status_code= status.HTTP_202_ACCEPTED)
async def put_tarefa(id: int, tarefa: TarefaSchema,db: AsyncSession = Depends(get_session), usuarioLogado = Depends(get_current_user)):
    async with db as session:
        query = select(TarefaModel).filter(TarefaModel.id == id).filter(TarefaModel.usuario_id == usuarioLogado.id)
        result = await session.execute(query)
        tarefa_update: TarefaSchema = result.scalars().unique().one_or_none()
        if tarefa_update:
            tarefa_update.nome = tarefa.nome
            tarefa_update.descricao = tarefa.descricao 
            tarefa_update.concluido = tarefa.concluido
            tarefa_update.atualizado_em = str(datetime.now())
            await session.commit()
            return tarefa_update
        else:
            raise HTTPException(detail='Tarefa não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)
        


