# Git



## Git 설치

## Git 기본명령어

- git 로컬 저장소 생성하기

  -> VSCode 터미널에서 해당폴더로 접근 후 생성 가능

  - git init 명령어를 실행하면 새로운 저장소 생성

  ```
  $ git init
  ```

  - .git 폴더가 생성되며 프로젝트 관리 파일이 들어 있음

- git 상태 확인

  - 현재 저장소 내 파일들을 확인해 볼 수 있다.(모니터링)

  ```
  $ git status
  ```

- Index에 파일 추가 (git add)

  ```
  $ git add [파일명] 또는 git add . (해당 폴더 한번에 올리기)
  ```

  - 이력관리 대상에 포함되지 않으면 Untracked file이라고 표시

  - 인덱스에 포함된 파일은 Changes to be commited 라고 표시

  - 인덱스에 추가된 파일을 제외하려면

    ```
    $ git rm --cached [파일명]
    ```

- git 변경사항 확정

  ```
  $ git commit -m "메시지"
  ```

- git commit 작성자(설정)

  ```
  $ git config --global user.email [github 이메일]
  $ git config --global user.name [github 닉네임]
  
  # git 설정 확인
  $ git config --global -l
  ```

- git log

  - 저장소 내부의 Commit을 확인하는 것

- 원격 저장소 등록

  ```
  $ git remote and origin https://github.com/[본인 github 닉네임]/TIL.git
  ```

- 원격 저장소 삭제

```
$ git remote rm origin https://github.com/[본인 github 닉네임]/TIL.git
```







- 원격 저장소 업로드

  ```
  $ git push 또는 git push origin [브랜치명]
  ```









# 명령어

1. **/ Root Directory**
2. **~ Home Directory**
   - 사용자에게 할당된 폴더
3. . / ..
   - 현재 위치한 폴더, 현재 위치한 폴더 기준으로 상위 폴더
4. Pwd
   - 현재 폴더의 경로
5. **Ctrl + C **
   - 실행중인 프로세스 취소
6. **Ctrl + L **
   - 터미널 정리하기
7. ls
   - 현재 폴더 표시
   - ls - al : 세부표시
8. cd 폴더명
   - 해당 폴더로 이동
9. **cd .. **
   - 상위 폴더로 이동
10. **mkdir [폴더명]**



- 폴더 생성

1. rmdir [폴더명], rm [파일명]
   - 폴더 삭제 또는 파일 삭제
   - rm -r 지정한 폴더 및 파일 삭제, f추가시 강제삭제
2. **mv [파일 및 폴더명] **
   - 파일 이동
3. **touch [파일명] **
   - 파일을 생성 (확장자 명까지)
4. start, open <파일명>
   - 파일 실행
5. echo
   - 파일 출력



