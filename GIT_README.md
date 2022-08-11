## Git 명령어 정리

### branch 생성/push
```
git clone repository_url
git branch branch_name     -- local에 branch생성
git checkout branch_name   -- branch 접속

git branch -b branch_name  -- branch생성하고 바로 체크아웃
```

```
git add .   -- 수정한 파일 모두 추가
git commit -m "message" -- commit
git push origin branch_name  -- branch로 push한다.
```

git에서 여러 브랜치를 관리할 때, 꼭 해당 브랜치로 checkout하고 commit/push해야 한다.    

### tag생성/push

```
git tag <tag name> -m "message"
git push origin <tag name>
```

### stash
: branch작업 내용을 backup한다.

```
git stash       -- 작업 backup
git stash list  -- stash list확인
git stash apply stash@{0} -- stash@{0} 번 적용
git stash drop stash@{0}  -- stash@{0} 번 삭제
git stash apply -- 목록에 있는 stash 모두 적용
git stash drop -- 목록에 있는 stash 모두 삭제
```


### git 연결해제

```
git remote -v     -- remote 확인
git remote remove origin  -- 연결해제
find ./ -name ".git" | xargs rm -Rf   -- .git 파일 삭제
```

### branch 삭제
```
git branch -d branch이름    -- branch 삭제 (로컬)

git branch -d branch이름    -- branch 강제삭제 (로컬 - head에 소스 올라가져있으면 -d로 삭제안됨)

git push origin --delete branch이름    -- 저장소에서 branch 삭제
```
