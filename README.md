# github项目
- 原github作者[ tianshipapa ](https://github.com/tianshipapa)和
[ymyuuu ]（https://github.com/ymyuuu/BestDomain）
- 老王只是合并两个项目
- github项目地址
## 优选域名 ， IP 取决于抓取的 网站
- bestcf.cfcs.us.kg 
- api.cfcs.us.kg

![image.png](https://img.lwxpz.me/file/1736315762020_image.png)

https://github.com/jc-lw/youxuanyuming

![image.png](https://img.kjzl.me/images/18b0be4bca205491b1aaf70983319fe504bef426.png)




# cfipcaiji 原理和需要修改的地方

- 每3小时自动抓取  https://ip.164746.xyz 的优选ip，形成ip.txt 
- 还有js自动生成的https://cf.090227.xyz 
![image.png](https://img.kjzl.me/images/51e6dd9bbb99f98d3241509b804d98a4fc1fa5db.png)

- `caijiip.yml `文件夹里面改成你自己的，否则报错
![image.png](https://img.kjzl.me/images/0ddaaecae1242f12aadaa847662d56a23398cda5.png)
- `collect_ips.py`文件 这里是抓取优选IP的网站，如需要可自行修改
![image.png](https://img.kjzl.me/images/38a3d57288da468b17964664e54da54a4175ba0e.png)

# BestDomain 需要Cloudflare API令牌

- 这里修改你的二级域名开头
![image.png](https://img.kjzl.me/images/85362a2f5680355d4d73a2293ce82099c42e3308.png)
![image.png](https://img.kjzl.me/images/5def5f757d7a63978358e5a950714bed3dc6c213.png)
- 把上面的链接 修改成 你自己的链接，因为你抓取优选ip可能跟我不一样。
![image.png](https://img.kjzl.me/images/52f07d0b88279fb13694e1071d3184082408cf3d.png)



1. 创建 Cloudflare API 令牌
访问 [Cloudflare API Tokens](https://dash.cloudflare.com/profile/api-tokens)

2. 选择需要解析的域名，创建编辑 DNS 权限的` CF_API_TOKEN`
![image.png](https://img.kjzl.me/images/35feefcde1ed0cc08e430e419de73b892157d35c.png)


3. 在你的 GitHub 仓库中，设置 `CF_API_TOKEN `为你的 Cloudflare API 令牌
![image.png](https://img.kjzl.me/images/004eb6d2c8441cfa266129b3906e43e60bf99090.png)


4. 配置 GitHub Actions 定时任务
- 编辑 [.github/workflows/main.yml](.github/workflows/main.yml) 文件，设置 `cron` 表达式以定义任务运行时间
"# youxuanyuming" 

# 设置完成 
![image.png](https://img.kjzl.me/images/defa31617244ae82e89f05480be397eb3938f15e.png)
这里就是 运行完成，去ping出来的优选IP
![image.png](https://img.kjzl.me/images/8816d5204054629815ecf6add95e9e244849e85b.png)


# 开源协议
欢迎使用、修改和传播这个脚本！如果你觉得它对你有帮助，记得来点个 Star ⭐ 哦～

- 💡 免责声明： 本脚本由作者热爱 Linux 的灵魂驱动编写，虽尽力确保安全，但任何使用问题请自负风险！

赞助声明
本项目由 VTEXS 的「开源项目免费 VPS 计划」提供算力支持。
感谢 VTEXS 对开源社区的支持！

其实修改完项目要求改的部分也基本上够用了

不想继续折腾就修改完要求的部分就行了

记得就是得自己删除caijiip.yml 重新创建caijiip.yml后运行一下 好像这样ip.txt才会更新内容

要不然你运行完ip.txt的内容不会更新

看情况来就行 如果更新了 就不用删除来了 看情况

不折腾版本到这里可以了

下面是自己根据gpt修改或者添加的内容

fork完修改完时间以及需要修改的部分后 进行下面的操作

注意修改时间的参数 别太频繁了 4小时就很不错

工作流都是有自己对应的文件的

一个py需要一个yml yml就是工作流文件

caijiip.yml Update IP List 这两个是一组对应的东西 除了运行时间别瞎改了 bug多

记得fork后先改时间 运行成功后再删除caijiip.yml 重新创建caijiip.yml后运行一下 好像这样ip.txt才会更新内容

创建了remove_invalid_ips.py和remove_invalid_ips.yml 去不可用去重复的ip

有这两个后(remove_invalid_ips.py和remove_invalid_ips.yml)其实不需要动bestdomain了 因为已经有需要的效果了

第一个在首页创建 第二个在工作流的页面创建

最新更改 在工作流里添加了 auto_all.yml 运行对应的workflow

好像就是三合一了

Tips:ip.txt变了 raw会变得慢 不是不变 Ctrl + F5 多刷新刷新就行 或者等5分钟




