# leetcode-desktop
这份文档将帮助你在终端搭建连接 leetcode.com 的服务

## 1 安装 npm 和 nodejs
```Bash
sudo apt install npm  
npm -v # 查看版本
```
```Bash
sudo npm install -g n # 安装用于安装 nodejs 的模块 n  
sudo n stable
```
如果报错：  
```Bash
sudo npm install -g n  
/usr/local/lib/node_modules/npm/bin/npm-cli.js:79  
      let notifier = require('update-notifier')({pkg})  
      ^^^  

SyntaxError: Block-scoped declarations (let, const, function, class)  
not yet supported outside strict mode  
    at exports.runInThisContext (vm.js:53:16)  
    at Module._compile (module.js:374:25)  
    at Object.Module._extensions..js (module.js:417:10)  
    at Module.load (module.js:344:32)  
    at Function.Module._load (module.js:301:12)  
    at Function.Module.runMain (module.js:442:10)  
    at startup (node.js:136:18)  
    at node.js:966:3  
```
则如下操作：  
```Bash
cd /usr/local/lib/node_modules  
mv npm/ /tmp/usr_local_lib_node_modules_npm  
```
然后重新执行  
```Bash
sudo npm install -g n # 安装用于安装 nodejs 的模块 n  
sudo n stable
```
