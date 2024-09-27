import json

# Caminho para o arquivo de posts
file_path = '/home/alanapaula/Documentos/Mestrado/rejuvenescimento/rodrigo/outrasLinguagens/data_python.json'

# Carregar o arquivo JSON
with open(file_path, 'r') as file:
    posts_data = json.load(file)

# Criar um dicionário para armazenar posts únicos, usando o postId como chave
unique_posts = {}
duplicate_ids = []

for post in posts_data:
    post_id = post['postId']
    # Se o postId já estiver no dicionário, adicionar o postId à lista de duplicados
    if post_id in unique_posts:
        duplicate_ids.append(post_id)
    else:
        unique_posts[post_id] = post

# Converter os valores do dicionário em uma lista de posts únicos
unique_posts_list = list(unique_posts.values())

# Caminho para salvar a lista de posts únicos
output_file_path = '/home/alanapaula/Documentos/Mestrado/rejuvenescimento/rodrigo/JSON/data_python.json'

# Salvar a lista de posts únicos de volta em um arquivo JSON
with open(output_file_path, 'w') as file:
    json.dump(unique_posts_list, file, indent=4)

# Verificar e listar os IDs duplicados, se houver
if duplicate_ids:
    print(f"\nNúmero de IDs duplicados encontrados: {len(duplicate_ids)}")
    print("Lista de IDs duplicados (mostrando 10 primeiros):")
    
    # Exibir IDs duplicados de forma mais legível, 10 por linha
    for i in range(0, len(duplicate_ids), 10):
        print(", ".join(map(str, duplicate_ids[i:i+10])))  # Mostra 10 IDs por linha
else:
    print("Nenhum ID duplicado foi encontrado.")

# Exibir uma amostra dos posts, contagem de posts originais e únicos
print("*" * 50)
print("Amostra de 5 posts únicos:", unique_posts_list[:5])
print("*" * 50)
print(f"Número total de posts originais: {len(posts_data)}")
print(f"Número de posts únicos: {len(unique_posts_list)}")

