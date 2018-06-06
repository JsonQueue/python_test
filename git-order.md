[toc]

## 1. 基本命令
### 配置用户名

	git config --global user.name "xxx"                      

### 配置邮件

	git config --global user.email "xxx@xxx.com"            
### 初始化git仓库
以下命令会使你的当前目录变成Git可以管理的仓库

	git init
### 添加文件
向Git仓库添加文件,分为两步
	
	git add <file>
	git commit -m<message>

添加全部文件（git add --all的缩写）

	 git add -A  

提交被修改和被删除的文件，不包括新文件
（git add --update的缩写）

	git add -u  

提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件
	
	git add .  

### 查看工作区状态

	git status

### 查看修改内容
如果查看状态后发现有文件被修改过，查看修改内容的命令如下：

	git diff


### 切换版本
HEAD指向的版本就是当前版本，Git允许我们在版本的历史之间穿梭，使用以下命令：
	
	git reset --hard commit_id。

### 查看提交历史
以下命令可以查看提交历史，以便确定要回退到哪个版本。

	git log

### 查看命令历史
以下命令可以查看命令历史，以便确定要回到未来的哪个版本。

	git reflog
### 查看文件修改信息
得到整个文件的每一行的详细修改信息：包括SHA串，日期和作者。
	
	git blame file_name

### 丢弃工作区的修改
当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，使用以下命令：

	git checkout -- file

### 丢弃暂存区的修改
当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分为两步：

	git reset HEAD <file>
	git checkout -- file

### 删除文件：

	git rm

### 关联远程库
要关联一个远程库，使用命令：

	git remote add origin git@server-name:path/repo-name.git；

关联远程库后，使用以下命令（可推送最新修改，第一次会推送master分支的所有内容）

	git push -u origin master

### 克隆远程库
要克隆一个仓库，首先必须知道仓库的地址，然后使用以下命令克隆：

	git clone
## 2.分支管理
&ensp;&ensp;相比同类软件，Git有很多优点。其中很显著的一点，就是版本的分支（branch）和合并（merge）十分方便。有些传统的版本管理软件，分支操作实际上会生成一份现有代码的物理拷贝，而Git只生成一个指向当前版本（又称"快照"）的指针，因此非常快捷易用。
### 查看分支：
	
	git branch

### 创建分支：

	git branch <name>

### 切换分支：

	git checkout <name>

### 创建、切换分支：

	git checkout -b <name>

### 合并某分支到当前分支：

	git merge <name>

&ensp;&ensp;合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。

### 删除分支：

	git branch -d <name>

### 查看分支合并图：

	git log --graph

### 暂存你的工作
&ensp;&ensp;暂存也称为储藏，可以获取你工作目录的中间状态——也就是你修改过的被追踪的文件和暂存的变更——并将它保存到一个未完结变更的堆栈中，随时可以重新应用。
	
	git stash

要查看现有的暂存

	git stash list

恢复暂存,但是恢复后，stash内容并不删除

	git stash apply

删除暂存

	git stash drop

恢复并删除暂存，恢复的同时把stash内容也删了

	git stash pop


### bug分支
修复bug时，我们会通过创建新的bug分支进行修复，然后合并，最后删除；

先把当前工作现场“储藏”起来，即上面的暂存
	
	git stash
	
然后去修复bug，修复后，再执行以下命令回到工作现场

	git stash pop

### feature分支

开发一个新feature，最好新建一个分支；

如果要丢弃一个没有被合并过的分支，可以通过以下强行删除。

	git branch -D <name>


### 查看远程库信息
本地新建的分支如果不推送到远程，对其他人就是不可见的；

	
	git remote -v；

### 从本地推送分支
如果推送失败，先用git pull抓取远程的新提交；

	git push origin branch-name，
    
### 在本地创建和远程分支对应的分支
本地和远程分支的名称最好一致

	git checkout -b branch-name origin/branch-name，；

### 建立本地分支和远程分支的关联

	git branch --set-upstream branch-name origin/branch-name；

### 从远程抓取分支
如果有冲突，要先处理冲突。
	
	git pull

###多人协作
多人协作的工作模式通常是这样：

1. 首先，可以试图用git push origin < branch-name >推送自己的修改；

2. 如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；

3. 如果合并有冲突，则解决冲突，并在本地提交；

4. 没有冲突或者解决掉冲突后，再用git push origin < branch-name >推送就能成功！

如果git pull提示no tracking information，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream-to < branch-name > origin/< branch-name >。

### 整理提交历史
rebase操作可以把本地未push的分叉提交历史整理成直线；

rebase的目的是使得我们在查看历史提交的变化时更容易，因为分叉的提交需要三方对比。

	git rebase

## 3. 标签管理
&ensp;&ensp;发布一个版本时，我们通常先在版本库中打一个标签（tag），这样，就唯一确定了打标签时刻的版本。将来无论什么时候，取某个标签的版本，就是把那个打标签的时刻的历史版本取出来。所以，标签也是版本库的一个快照。
### 查看所有标签

	git tag
### 新建标签
以下命令用于新建一个标签，默认为HEAD，也可以指定一个commit id

	git tag <tagname>
### 指定标签信息

	git tag -a <tagname> -m "标签信息"
### 推送一个本地标签

	git push origin <tagname>	

### 推送全部未推送过的本地标签

	git push origin --tags

### 删除一个本地标签

	git tag -d <tagname>

### 删除一个远程标签

	git push origin :refs/tags/<tagname>






