# 35) Crie uma classe Usuario com dois atributos "privados": _email e _senha.
# A classe deve ter um setter para o _email que valida se o valor fornecido contém o caractere '@'.
# A classe deve ter um setter para a _senha que valida se o valor tem no mínimo 8 caracteres.
# A classe deve ter um getter para o _email que retorna o email em letras minúsculas (se o email estiver em letras maiúsculas, o getter deve converter).
# A classe deve ter um getter para a _senha que retorna a senha criptografada 
# (por exemplo, substituindo todos os caracteres por asteriscos *, mas a senha original deve ser mantida).

class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        

    @property
    def email(self):
         return self._email.lower() 
    @email.setter
    def email(self, novo_email):
        if '@' not in novo_email:
            raise ValueError("Email Inválido. Deve contem o caractere '@'.")
        self._email = novo_email

    @property
    def senha(self):
        return '*' * len(self._senha)
    
    @senha.setter
    def senha(self, nova_senha):
        if not isinstance(nova_senha, str) or len(nova_senha) < 8:
            raise ValueError("A senha deve ter no mínimo 8 caracteres.")
        self._senha = nova_senha
try:
 usuario = Usuario("jose@email.com", "Carro138")
 print("Email:", usuario.email)
 print("Senha:", usuario.senha)
except ValueError as e:
    print("Erro:", e)

    
    