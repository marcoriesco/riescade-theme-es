import xml.etree.ElementTree as ET

# Abrir o arquivo XML
tree = ET.parse('es_systems.xml')
root = tree.getroot()

# Dicionário para armazenar os nomes de sistema por hardware
sistemas_por_hardware = {}

# Iterar sobre todos os sistemas no arquivo XML
for system in root.findall('system'):
    # Tentar encontrar a tag hardware e obter seu conteúdo
    hardware_tag = system.find('hardware')
    if hardware_tag is not None:
        hardware_text = hardware_tag.text
        # Se o hardware já estiver no dicionário, adicionar o nome do sistema a ele
        if hardware_text in sistemas_por_hardware:
            sistemas_por_hardware[hardware_text].append(system.find('name').text)
        else:
            sistemas_por_hardware[hardware_text] = [system.find('name').text]

# Escrever os nomes de sistema em arquivos correspondentes
for hardware, sistemas in sistemas_por_hardware.items():
    with open(f'{hardware}.txt', 'w') as file:
        for sistema in sistemas:
            file.write(f'{sistema}\n')
