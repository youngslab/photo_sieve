
# PHOTO SIEVE
선택된 압축 형식 사진 파일(ex. jpg)에 대한 원본(ex. NEF) 파일을 찾아 복사해 주는 유틸리티. 

# Preequsites
사전에 아래 프로그램이 설치 되어야한다. 
- [python3](https://www.python.org/downloads/)


# How to use

#### 1. 원본사진들의 폴더를 확인한다. 
*주의 - 폴더아래 raw 파일만 존재해야한다. 다른 폴더에 이름이 같은 파일이 존재하면 원치 않는 결과물이 나올 수 있으니 주의해야 한다.*)

#### 2. 선택된 사진들의 폴더를 확인한다.  


#### 3. 실행
python script file `sieve.py`를 실행 시키기 편한 곳에 위치 시킨후 터미널을 열어 프롬프트에서 바로 실행 시킨다. 

`.\sieve.py [원본사진 폴더] [선택사진 폴더]`

#### 4. 확인
결과물은 `[선택사진 폴더]\raw` 아래로 복사된며 결과 창에 선택된 사진의 개수와 복사된 사진의 개수를 확인하여 빠진 결과물이 없는지 확인한다. 또 빠진 항목이 있으면 어떤 파일이 빠졌는지 로그가 남음으로 원본 사진을 확인한다. 
