# json2cmap
Paraview provides colormap JSON file is converted to cmap for matplotlib

Parviewで`Mapping Data` -> `Choose Preset` -> 何かPresetsを選ぶ -> `Export`
とすると以下のような`JSON`ファイルが出力されて、`Matplotlib`から直接は利用できない。

```JSON
[
	{
		"ColorSpace" : "RGB",
		"DefaultMap" : true,
		"Name" : "Cold and Hot",
		"NanColor" : 
		[
			1,
			1,
			0
		],
		"RGBPoints" : 
		[
			0,
			0,
			1,
			1,
			0.45000000000000001,
			0,
			0,
			1,
			0.5,
			0,
			0,
			0.50196078431400004,
			0.55000000000000004,
			1,
			0,
			0,
			1,
			1,
			1,
			0
		]
	}
]
```

ここでは、この`JSON`ファイルをpythonから利用できる`pkl`ファイルへ変換するルーチンを提供する。

```python
# paraviewから出力されたJSONファイルをtest.jsonとする
from json2cmap import json2cmap
json_file = 'test.json'
json2cmap(json_file)
```
とすると`cmap`情報が含まれた`test.pkl`が生成される。利用するときは
```python
import pickle
import matplotlib.pyplot as plt
import numpy as np

with open('test.pkl','rb') as f:
    cmap = pickle.load(f)
     
x = np.linspace(0,1,30)
y = np.linspace(0,1,30)
X, Y = np.meshgrid(x,y,indexing='ij')
Z = np.sin(X)*np.cos(3*Y)
plt.pcolormesh(X,Y,Z,cmap=cmap)
plt.show()
```

などとする。