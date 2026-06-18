# Day 24 学習記録

## 今日やったこと

- GitHubへの追加の仕方を確認した
- `git remote add origin ...` で、PCのGitとGitHubリポジトリを接続した
- `git push -u origin master` で、ローカルのcommit履歴をGitHubへ送った
- `git status`、`git remote -v`、`git branch -vv` で状態を確認した

## 詰まったところ

- GitHub公開ではコマンドが多く、流れを覚えるのが少し大変だった

## 学んだこと

- `remote` は、PCのGitリポジトリとGitHub上のリポジトリをつなぐ接続先
- `push` は、PCにあるcommit履歴をGitHubへ反映する操作
- `git status` で `working tree clean` と表示されると、未commitの変更がない
- `origin/master` と同期していれば、GitHub側にも同じ履歴が送られている
