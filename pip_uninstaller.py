import subprocess

# Obtener la lista de paquetes instalados
result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
packages = result.stdout.decode('utf-8').split('\n')

# Eliminar cada paquete instalado
for package in packages:
    if package.strip():
        subprocess.run(['pip', 'uninstall', '-y', package.split('=')[0]])
