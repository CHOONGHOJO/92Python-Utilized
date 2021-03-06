# 파일 기본
import os
print(os.getcwd()) # current working directory
os.chdir("/home/cjoe731/PythonDataWorkspace")
print(os.getcwd()) # current working directory
os.chdir("/home/cjoe731/Desktop/python(NadoCoding)/92Python 활용편/94 업무자동화(RPA) basic/92desktop/")
print(os.getcwd())

os.chdir("..") # 부모 폴더로 이동
os.chdir("../..") # 조부모 폴더로 이동
os.chdir("c:/") # 절대 경로로 이동


# 파일 경로 만들기
file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
print(file_path)


# 파일 경로에서 폴더 정보 가져오기
print(os.path.dirname(r"/home/cjoe731/Desktop/python(NadoCoding)/92Python 활용편/94 업무자동화(RPA) basic/92desktop/my_file.txt"))


# 파일 정보 가져오기
import time
import datetime


# 파일의 생성 날자
ctime = os.path.getctime("1_env.py")
print(ctime)
print(datetime.datetime.fromtimestamp(ctime))
# 날자 정보를 strftime 을 통해서 yyyymmdd hh:mm:dd 형태로 출력
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))


# 파일의 수정 날자
mtime = os.path.getmtime("1_env.py")
print(mtime)
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))


# 파일의 마지막 접근 날자
atime = os.path.getatime("1_env.py")
print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))


# 파일 크기
size = os.path.getsize("1_env.py")
print(size) # byte 단위


# 파일 목록
print(os.listdir()) # 모든 폴더, 파일 목록
file_path = os.path.dirname(
    "/home/cjoe731/Desktop/python(NadoCoding)/92Python 활용편/94 업무자동화(RPA) basic/92desktop/")
file_name = os.listdir(file_path)
print(file_name)


# 하위 폴더 모두 포함, 파일 목록 가져오기
file_path = (".") # 현재 폴더
file_path = ("강의source") # 현재 폴더
file_path = ("2_desktop") # 현재 폴더
result = os.walk(file_path)
for root, dirs, files in result:
    print(root, dirs, files)


# 폴더 내에서 특정 파일을 찾으려면 ?
name = "11_file_system.py"
result = []
# for root, dirs, files in os.walk("."): # 현재 경로
for root, dirs, files in os.walk(os.getcwd()): # 전체 경로
    if name in files:
        result.append(os.path.join(root, name))
print(result)


# 특정 type, pattern  가진 파일 찾기
# *.xlsx, *.txt, 지동화*.png
import fnmatch
pattern = "*.html" # .png로 끝나는 모든 파일
pattern = "file*.png" # .png로 끝나는 모든 파일
result = []
for root, dirs, files in os.walk("."): # 현재 경로
    for name in files:
        # [a.png, b.txt, c.html, 11_file_system.py, ...]
        if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 메치
            result.append(os.path.join(root, name))
print(result)


# 현재 위치 기준으로, 주어진 경로가 파일?, 폴더?
print(os.path.isdir("강의source")) # folder?
print(os.path.isfile("강의source")) # file?

print(os.path.isdir("10_log.py")) # folder?
print(os.path.isfile("10_log.py")) # file?


# 주어진 경로가 존재하는가?
# if os.path.exists("10_log.py"):
if os.path.exists("강의source"):
    print("파일 또는 폴더가 존재합니다.")
else:
    print("존재하지 않습니다.")


# 파일 만들기
open("new_file.txt", "a").close() # 빈 파일 생성


# 파일명 변경
os.rename("new_file.txt", "new_file_rename.txt") # new_file.txt =>new_file_rename.txt 로 이름변경


# 파일 삭제
os.remove("new_file_rename.txt")


# 폴더 만들기
os.mkdir("new_folder") # 현재 경로에서 만듬
os.mkdir("new_folder/test") # 절대 경로에서 만듬

os.mkdir("new_folders/a/b/c") # 실패
os.makedirs("new_folders/a/b/c") # 성공


# 폴더명 바꾸기
os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# 폴더안이 비었을 때만 가능
os.rmdir("new_folder_rename") # 폴더안이 비었을 때만 가능

# 폴더가 비어있지 않아도 삭제
import shutil # shell utilities
shutil.rmtree("new_folders") # 폴더가 비어있지 않아도 삭제


# 파일 복사하기

# 폴더 안으로 복사
# copy, copyfile : 메타정보 복사 x
# copy2 : 메타정보 복사 o

shutil.copy("file_menu.png", "test_folder") #원본경로, 대상경로
shutil.copy("file_menu.png", "test_folder/file_menu_copied.png") #원본경로, 대상경로 ( 새로운 이름)
shutil.copyfile("file_menu.png", "test_folder/file_menu_copied2.png") #원본경로, 대상파일경로 ( 새로운 이름)

shutil.copy2("file_menu.png", "test_folder/copy2.png") #원본경로, 대상경로 ( 새로운 이름)


# 폴더 복사
shutil.copytree("test_folder", "copytree_folder2") # 원본 폴더 경로, 대상 폴더 경로


# 폴더 이동
shutil.move("test_folder", "copytree_folder3") # 원본 폴더 경로, 대상 폴더 믿으로 이동 )
