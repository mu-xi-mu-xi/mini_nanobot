mini_nanobot/ 
│ ├── core/ 
│ ├── agent.py 
│ ├── response.py 
│ └── message.py 
│ ├── channels/ 
│ ├── base.py 
│ ├── cli.py 
│ └── feishu.py 
│ ├── providers/ 
│ ├── base.py 
│ └── zhipu.py 
│ ├── tools/ 
│ ├── base.py 
│ ├── registry.py 
│ └── builtin/ 
│ ├── skills/ 
│ ├── loader.py 
│ └── weather/ 
│ ├── skill.yaml 
│ └── run.py 
│ ├── mcp/ 
│ ├── client.py 
│ └── manager.py 
│ ├── memory/ 
│ └── store.py 
│ └── main.py

## 遇到的问题
前后的属性名称，函数名称不一致，不要太相信ai的自动补全
在正式开发项目前要明确项目结构，可以花UML类图和时序图来帮助理解，编码

简直是可歌可泣，终于成功实现了一个tool和provider的全流程打通
```
(nanobot) PS D:\project\mini_nanobot> python main.py
G:\miniconda\envs\nanobot\Lib\site-packages\requests\__init__.py:113: RequestsDependencyWarning: urllib3 (2.6.3) or chardet (7.0.0)/charset_normalizer (3.4.4) doesn't match a supported version!
  warnings.warn(
The weather in Beijing is currently showing a temperature of 4 degrees (likely Celsius). This appears to be quite cold! For more detailed weather information like conditions, humidity, wind speed, and forecasts, you might want to check a more comprehensive weather service.
```