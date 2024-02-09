from fastapi import FastAPI
from banco_db.models import CustomUser,Transferir
from banco_db.connect_db import session

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Bem vindo a nossa api"}


@app.post("/create/customuser")
async def custom_user(
    nome_completo: str,
    email: str,
    codigo_do_agente: int,
    saldo: float,
    numero_da_conta: int,
    numero_de_contacto: int,
    tipo_de_conta: str = "Normal",
    ):

    customuser = CustomUser(
        nome_completo=nome_completo,
        email=email,
        codigo_do_agente=codigo_do_agente,
        tipo_de_conta=tipo_de_conta,
        saldo=saldo,
        numero_da_conta=numero_da_conta,
        numero_de_contacto=numero_de_contacto,
    )
    
    session.add(customuser)
    session.commit()
    return {"custom user":{
        'nome completo':customuser.nome_completo,
        'email':customuser.email,
        'codigo_do_agente':customuser.codigo_do_agente,
        'tipo_de_conta':customuser.tipo_de_conta,
        'saldo':saldo,
        'numero_da_conta':numero_da_conta,
        'numero_de_contacto':numero_de_contacto,
    }}


@app.get("/customuser/view")
async def custom_user():
    usuario = session.query(CustomUser)
    return  usuario.all()


@app.post("/customuser/view")
async def transferir(numero_da_conta:int,montante:float):
    print("Numero da conta>> ",numero_da_conta)
    print("Montante>> ",montante)    

    usuario_principal = session.query(CustomUser).filter_by(numero_da_conta='987654321').first()

    usuario = session.query(CustomUser).filter_by(numero_da_conta=numero_da_conta).first()

    if(usuario_principal.saldo<=20 and montante<=20):
        return 'Saldo insuficiente'
    
    elif(usuario_principal.saldo>montante):

        if (usuario.numero_da_conta==numero_da_conta and usuario.saldo):
            usuario_principal.saldo-=montante
            usuario.saldo+=montante
            session.add(usuario,usuario_principal)
            session.commit()
            print("Saldo Enviado!")

            return {
                'id':usuario.id,
                'nome_completo':usuario.nome_completo,
                'email':usuario.email,
                'codigo_do_agente':usuario.codigo_do_agente,
                'tipo_de_conta':usuario.tipo_de_conta,
                'saldo':usuario.saldo,
                'numero_da_conta':usuario.numero_da_conta,
                'numero_de_contacto':usuario.numero_de_contacto
            }








