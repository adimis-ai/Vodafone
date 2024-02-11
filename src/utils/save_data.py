def save_file(filename: str, content: str):
    with open(f"{filename}.txt", 'w', encoding='utf-8') as file:
        file.write(content)