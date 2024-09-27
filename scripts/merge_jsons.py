import json
import os

# Diretório onde estão os arquivos JSON
json_directory = '/home/alanapaula/Documentos/Mestrado/rejuvenescimento/rodrigo/JSON/dfs'

# Lista de arquivos JSON
json_files = [
    'data_cpp.json',
    'data_java.json',
    'data_javascript.json',
    'data_python.json'
]

# Função para carregar JSON de um arquivo
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Função para combinar várias listas de posts
def merge_jsons(*json_lists):
    combined = []
    for json_list in json_lists:
        combined.extend(json_list)  # Junta todas as listas em uma
    return combined

# Carregar e combinar todos os JSONs
combined_json = []
for json_file in json_files:
    file_path = os.path.join(json_directory, json_file)
    json_data = load_json(file_path)
    combined_json = merge_jsons(combined_json, json_data)

# Salvar o resultado combinado em um novo arquivo JSON
output_path = os.path.join(json_directory, 'json_combinado.json')
with open(output_path, 'w', encoding='utf-8') as output_file:
    json.dump(combined_json, output_file, ensure_ascii=False, indent=4)

print(f"JSONs combinados com sucesso! Arquivo salvo em: {output_path}")

