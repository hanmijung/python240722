import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 대상 폴더 경로
folders = {
    "images": r'C:\Users\student\Downloads\images',
    "data": r'C:\Users\student\Downloads\data',
    "docs": r'C:\Users\student\Downloads\docs',
    "archive": r'C:\Users\student\Downloads\archive'
}

# 폴더가 없으면 생성
for folder in folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# 파일 이동 함수
def move_files(file_types, destination_folder):
    for file_type in file_types:
        for file in os.listdir(download_folder):
            if file.endswith(file_type):
                source = os.path.join(download_folder, file)
                destination = os.path.join(destination_folder, file)
                shutil.move(source, destination)
                print(f'Moved: {file} to {destination_folder}')

# 각 파일 형식별로 파일 이동
move_files(['.jpg', '.jpeg'], folders['images'])
move_files(['.csv', '.xlsx'], folders['data'])
move_files(['.txt', '.doc', '.pdf'], folders['docs'])
move_files(['.zip'], folders['archive'])

print("파일 이동이 완료되었습니다.")
