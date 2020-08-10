
# PHOTO SIEVE
선택된 압축 형식 사진 파일(ex. jpg)에 대한 원본(ex. NEF) 파일을 찾아 복사해 주는 유틸리티. 아래 가이드는 Mac, Window10 기준으로 작성되었다. 

# Preequsites

#### 1. python 
사전에 아래 프로그램이 설치 되어야한다. 만약 설치가 안되었다면 아래 site를 방문하여 설치하도록 한다.
- [python3](https://www.python.org/downloads/) 

#### 2. sevice.py
python으로 만들어진 app으로 sieve.py 파일을 download 받아 자신의 home directory에 위치시킨다. 자세한 내용은 아래 `How to download the sieve.py`에서 설명한다. 
- Windows : `c:\User\XXX`
- Mac : `Usrs\XXX`

##### How to download the sieve.py

우선 Terminal을 실행 시켜 아래와 같이 file을 download 받는다. Terminal 실행시키는 방법은 아래 `1. Terminal을 실행한다.` 에서 자세한 내용을 확인할 수 있다. 

```
## MAC
> cd ~ 
> wget https://raw.githubusercontent.com/youngslab/photo_sieve/master/sieve.py

## Windows
> curl https://raw.githubusercontent.com/youngslab/photo_sieve/master/sieve.py --output sieve.py
```



# How to use

### 1. Terminal을 실행한다. 
photo sieve는 termianl 기반으로 동작하는 app으로 각 OS에 맞는 terminal을 실행 시켜야 한다. Terminal이 실행 된 위치는 보통 기본으로 Home directory이다. 만약 sieve.py가 다른 위치에 있다면 해당 폴더로 이동한다. 

- Windows: `window key + R` -> "cmd" 입력
- Mac : `app list` > `기타` -> `termianl` 앱 실행 


#### 1. 원본사진들의 폴더를 확인한다. 
*주의 - 폴더아래 파일들의 이름은 유일해야한다. 그렇지 않다면 원치않는 결과가 나올 수 있음에 유의한다.*)

#### 2. 선택된 사진들의 폴더를 확인한다.  


#### 3. 실행
Terminal에서 python script file을 아래와 같은 명령어로 실행 시킨다.  사진 폴더 입력할 때, Finder/File expleorer 에서 폴더를 terminal로 drag&drop으로 하면 편하다. 


##### MAC & Window
```
./sieve.py [원본사진 폴더] [선택사진 폴더]
```

#### 4. 확인
결과물은 `[선택사진 폴더]\raw` 아래로 복사된며 결과 창에 선택된 사진의 개수와 복사된 사진의 개수를 확인하여 빠진 결과물이 없는지 확인한다. 또 빠진 항목이 있으면 어떤 파일이 빠졌는지 로그가 남음으로 원본 사진을 확인한다. 

