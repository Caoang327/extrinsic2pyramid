import numpy as np
import torch
from util.camera_pose_visualizer import CameraPoseVisualizer_cus

if __name__ == '__main__':

    Input_Camera =  torch.tensor([[[-0.6206,  0.7404, -0.2581, -2.8583],
          [-0.7371, -0.6632, -0.1303,  2.6337],
          [-0.2676,  0.1094,  0.9573,  1.4560],
          [0.0,  0.0,  0.0,  1.0]],

         [[-0.9797,  0.1900, -0.0639,  2.6604],
          [-0.1934, -0.9797,  0.0523,  1.6017],
          [-0.0527,  0.0636,  0.9966, -0.9111],
          [0.0,  0.0,  0.0,  1.0]],

         [[-0.9057,  0.4039, -0.1290, -3.1944],
          [-0.4143, -0.9077,  0.0664,  2.3126],
          [-0.0902,  0.1136,  0.9894,  1.0645],
          [0.0,  0.0,  0.0,  1.0]],

         [[ 0.2908, -0.7685,  0.5699,  0.3123],
          [ 0.9481,  0.1514, -0.2796,  3.4408],
          [ 0.1286,  0.6217,  0.7727,  1.0535],
          [0.0,  0.0,  0.0,  1.0]]])
    
    Input_Camera = torch.inverse(Input_Camera).numpy()
    Output_Camera = torch.eye(4)
    temp = torch.tensor([[ 0.9760,  0.2165,  0.0208,  1.0475],
          [-0.1191,  0.6121, -0.7817,  3.2711],
          [-0.1820,  0.7605,  0.6233,  2.5864]])
    Output_Camera[:3] = temp
    Output_Camera = torch.inverse(Output_Camera).numpy()
    # argument : the minimum/maximum value of x, y, z
    visualizer = CameraPoseVisualizer_cus([-4, 4], [-4, 4], [-4, 4])

    # argument : extrinsic matrix, color, scaled focal length(z-axis length of frame body of camera
    visualizer.extrinsic2pyramid(Input_Camera[0], [2.9, 2.9], x_y_ratio=1.0, near=1.0, far=10.0, color='r')
    visualizer.extrinsic2pyramid(Input_Camera[1], [2.9, 2.9], x_y_ratio=1.0,near=1.0, far=10.0, color='g')
    visualizer.extrinsic2pyramid(Input_Camera[2], [2.9, 2.9], x_y_ratio=1.0, near=1.0, far=10.0, color='y')

    visualizer.extrinsic2pyramid(Output_Camera, [2.9, 2.9], x_y_ratio=1.0, near=1.0, far=10.0, color='b')

    visualizer.show()