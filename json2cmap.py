
def json2cmap(json_file):
    import numpy as np
    import pickle
    from matplotlib.colors import LinearSegmentedColormap
    import json

    # .jsonより前のファイル名を取得
    split_json = json_file.split('.')
    filename = split_json[0]
    
    
    # JSONデータを読み込む
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    
    rgb_points = json_data[0]["RGBPoints"]
    control_points = rgb_points[::4]
    red_values = rgb_points[1::4]
    green_values = rgb_points[2::4]
    blue_values = rgb_points[3::4]

    # 正規化値とRGB値の配列を作成
    norm_vals = np.linspace(0, 1, 255)
    red_vals = np.interp(norm_vals, control_points, red_values)
    green_vals = np.interp(norm_vals, control_points, green_values)
    blue_vals = np.interp(norm_vals, control_points, blue_values)

    # カラーマップのリストを作成
    cmap_list = []
    for i in range(len(norm_vals)):
        cmap_list.append((norm_vals[i], [red_vals[i], green_vals[i], blue_vals[i]]))

    # カラーマップを作成
    cmap = LinearSegmentedColormap.from_list("ColdHot", cmap_list)

    with open(filename+'.pkl','wb') as f:
        pickle.dump(cmap,f)
   
if __name__ == "__main__":
    json_file = 'paraview_colormaps/cool_and_hot.json'
    json2cmap(json_file)
