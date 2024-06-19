class Usuario:
  def __init__(self, nombre, password):
    self.nombre = nombre
    self.password = password

usuario1 = Usuario('Marta', 'marta1234')


print(usuario1.nombre)
print(usuario1.password)