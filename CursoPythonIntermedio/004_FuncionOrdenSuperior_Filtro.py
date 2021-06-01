DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    python_list = list(map(lambda worker: worker["name"], all_python_devs))
    
    all_Platzi_worker = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    platzi_list = list(map(lambda worker: worker["name"], all_Platzi_worker))
    
    adults =  [worker["name"] for worker in DATA if worker["age"] > 18]
    old_people = [worker | {"old":worker["age"]>70} for worker in DATA]

    print('')
    '''
    Se imprimen los nombres de las personas que estan especializadas
    en python con filter y map
    '''
    for worker in python_list:
        print(worker)
    
    print('')
    '''
    Se imprimen los nombres de las personas que trabajan en Platzi
    con filter y map
    '''
    for worker in platzi_list:
        print(worker)
    
    print('')
    '''
    Se imprimen los nombres de las personas que tson mayores de 
    8 años con list/dictionary
    '''
    for worker in adults:
        print(worker)
    
    print('')
    '''
    Se imprime el nuevo diccionario agregando la bandera old
    con list/dictionary
    '''
    for worker in old_people:
        print(worker)

if __name__ == '__main__':
    run()