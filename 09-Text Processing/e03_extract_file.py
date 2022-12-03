path_tokens = input().split('\\')

name_extension = path_tokens[-1].split('.')

file_name = name_extension[0]
extension_name = name_extension[1]

print(f'File name: {file_name}')
print(f'File extension: {extension_name}')
