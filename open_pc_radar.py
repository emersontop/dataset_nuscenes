import open3d as o3d

# Caminhos

PATH_DATASET_NUSCENES_MINI = '/home/live/Data/nuScenes'
PATH_DADOS_RADAR_FRONT = '/home/live/Data/nuScenes/samples/RADAR_FRONT'

# Carrega o arquivo .pcd
arquivo_pcd = '/n008-2018-08-27-11-48-51-0400__RADAR_FRONT__1535385099396173.pcd'
pcd = o3d.io.read_point_cloud(PATH_DADOS_RADAR_FRONT+arquivo_pcd)

# Exibe informações sobre o arquivo
print(pcd)

# Visualiza a nuvem de pontos
o3d.visualization.draw_geometries([pcd])
