import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class CameraPoseVisualizer:
    def __init__(self, xlim, ylim, zlim):
        self.fig = plt.figure(figsize=(18, 7))
        self.ax = self.fig.add_subplot(projection='3d')
        self.ax.set_aspect("auto")
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        self.ax.set_zlim(zlim)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_zlabel('z')
        print('initialize camera pose visualizer')

    def extrinsic2pyramid(self, extrinsic, color='r', focal_len_scaled=5, aspect_ratio=0.3):
        vertex_std = np.array([[0, 0, 0, 1],
                               [focal_len_scaled * aspect_ratio, -focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                               [focal_len_scaled * aspect_ratio, focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                               [-focal_len_scaled * aspect_ratio, focal_len_scaled * aspect_ratio, focal_len_scaled, 1],
                               [-focal_len_scaled * aspect_ratio, -focal_len_scaled * aspect_ratio, focal_len_scaled, 1]])
        vertex_transformed = vertex_std @ extrinsic.T
        meshes = [[vertex_transformed[0, :-1], vertex_transformed[1][:-1], vertex_transformed[2, :-1]],
                            [vertex_transformed[0, :-1], vertex_transformed[2, :-1], vertex_transformed[3, :-1]],
                            [vertex_transformed[0, :-1], vertex_transformed[3, :-1], vertex_transformed[4, :-1]],
                            [vertex_transformed[0, :-1], vertex_transformed[4, :-1], vertex_transformed[1, :-1]],
                            [vertex_transformed[1, :-1], vertex_transformed[2, :-1], vertex_transformed[3, :-1], vertex_transformed[4, :-1]]]
        self.ax.add_collection3d(
            Poly3DCollection(meshes, facecolors=color, linewidths=0.3, edgecolors=color, alpha=0.35))

    def customize_legend(self, list_label):
        list_handle = []
        for idx, label in enumerate(list_label):
            color = plt.cm.rainbow(idx / len(list_label))
            patch = Patch(color=color, label=label)
            list_handle.append(patch)
        plt.legend(loc='right', bbox_to_anchor=(1.8, 0.5), handles=list_handle)

    def colorbar(self, max_frame_length):
        cmap = mpl.cm.rainbow
        norm = mpl.colors.Normalize(vmin=0, vmax=max_frame_length)
        self.fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), orientation='vertical', label='Frame Number')

    def show(self):
        plt.title('Extrinsic Parameters')
        plt.show()


class CameraPoseVisualizer_cus:
    def __init__(self, xlim, ylim, zlim):
        self.fig = plt.figure(figsize=(18, 7))
        self.ax = self.fig.add_subplot(projection='3d')
        self.ax.set_aspect("auto")
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        self.ax.set_zlim(zlim)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_zlabel('z')
        print('initialize camera pose visualizer')

    def extrinsic2pyramid(self, extrinsic, focal, near=1.0, far=2.0, color='r', focal_len_scaled=1, x_y_ratio=1.5):
        focal_x = focal[0]
        focal_y = focal[1]

        aspect_ratio_x = 1 / focal_x
        aspect_ratio_y = 1 / focal_y
    
        vertex_std = np.array([[0, 0, 0, 1],
                               [focal_len_scaled * aspect_ratio_x * x_y_ratio * near, -focal_len_scaled * aspect_ratio_y * near, focal_len_scaled * near, 1],
                               [focal_len_scaled * aspect_ratio_x * x_y_ratio * near, focal_len_scaled * aspect_ratio_y * near, focal_len_scaled * near, 1],
                               [-focal_len_scaled * aspect_ratio_x * x_y_ratio * near, focal_len_scaled * aspect_ratio_y * near, focal_len_scaled * near, 1],
                               [-focal_len_scaled * aspect_ratio_x * x_y_ratio* near, -focal_len_scaled * aspect_ratio_y * near, focal_len_scaled * near, 1],
                               [focal_len_scaled * aspect_ratio_x * x_y_ratio * far, -focal_len_scaled * aspect_ratio_y * far, focal_len_scaled * far, 1],
                               [focal_len_scaled * aspect_ratio_x * x_y_ratio * far, focal_len_scaled * aspect_ratio_y * far, focal_len_scaled * far, 1],
                               [-focal_len_scaled * aspect_ratio_x * x_y_ratio * far, focal_len_scaled * aspect_ratio_y * far, focal_len_scaled * far, 1],
                               [-focal_len_scaled * aspect_ratio_x * x_y_ratio * far, -focal_len_scaled * aspect_ratio_y * far, focal_len_scaled * far, 1]])

        vertex_transformed = vertex_std @ extrinsic.T
        meshes = [[vertex_transformed[0, :-1], vertex_transformed[1][:-1], vertex_transformed[2, :-1]],
                            [vertex_transformed[0, :-1], vertex_transformed[2, :-1], vertex_transformed[3, :-1]],
                            [vertex_transformed[0, :-1], vertex_transformed[3, :-1], vertex_transformed[4, :-1]],
                            [vertex_transformed[0, :-1], vertex_transformed[4, :-1], vertex_transformed[1, :-1]],
                            [vertex_transformed[1, :-1], vertex_transformed[2, :-1], vertex_transformed[3, :-1], vertex_transformed[4, :-1]],
                            [vertex_transformed[1, :-1], vertex_transformed[2, :-1], vertex_transformed[6, :-1], vertex_transformed[5, :-1]],
                            [vertex_transformed[2, :-1], vertex_transformed[3, :-1], vertex_transformed[7, :-1], vertex_transformed[6, :-1]],
                            [vertex_transformed[3, :-1], vertex_transformed[4, :-1], vertex_transformed[8, :-1], vertex_transformed[7, :-1]],
                            [vertex_transformed[4, :-1], vertex_transformed[1, :-1], vertex_transformed[5, :-1], vertex_transformed[8, :-1]],
                            [vertex_transformed[5, :-1], vertex_transformed[6, :-1], vertex_transformed[7, :-1], vertex_transformed[8, :-1]]
                            ]
        self.ax.add_collection3d(
            Poly3DCollection(meshes, facecolors=color, linewidths=0.3, edgecolors=color, alpha=0.35))

    def customize_legend(self, list_label):
        list_handle = []
        for idx, label in enumerate(list_label):
            color = plt.cm.rainbow(idx / len(list_label))
            patch = Patch(color=color, label=label)
            list_handle.append(patch)
        plt.legend(loc='right', bbox_to_anchor=(1.8, 0.5), handles=list_handle)

    def colorbar(self, max_frame_length):
        cmap = mpl.cm.rainbow
        norm = mpl.colors.Normalize(vmin=0, vmax=max_frame_length)
        self.fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), orientation='vertical', label='Frame Number')

    def show(self):
        plt.title('Extrinsic Parameters')
        plt.show()