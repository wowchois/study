### Git 

#### branch 생성/push
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

#### tag생성/push
