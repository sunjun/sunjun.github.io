---
layout: post
title: "Use vimdiff as git mergetool"
categories:
- 技术
tags:
- git


---

###任何版本控制在合并的时候都有可能发生冲突现象，git也不例外，即使git的自动合并功能很智能，如何使用vimdiff作为git的一种merge tool呢？  
####首先，是配置git：  


{% highlight bash%}

git config --global merge.tool vimdiff
git config mergetool.prompt false

{% endhighlight bash%}


####然后，遇到冲突时，运行：


{% highlight bash%}

git mergetool

{% endhighlight bash%}


####最后，跳到vimdiff的merge窗口里面你要选择的部分，进行一下操作：


{% highlight vim%}

:diffg RE  " get from REMOTE
:diffg BA  " get from BASE
:diffg LO  " get from LOCAL

{% endhighlight vim%}

* REMOTE: 当前分支状态
* BASE: 远程分支和当前分支状态之前的状态
* LOCAL: 远程分支的状态
