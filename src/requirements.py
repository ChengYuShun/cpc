with open('requirements.txt', 'r') as f:
    data = f.read().split('\n')
    while '' in data:
        data.remove('')

requirements = (
    "chardet",
    "ply"
)

def config():
    import importlib
    import pip
    for i in range(len(requirements)):
        require = requirements[i]
        try:
            importlib.import_module(require)
        except:
            print(f'\033[1mMissing Important Dependence `{require}`\nTrying to Install for You...\033[0m')
            pip.main(['install', data[i]])