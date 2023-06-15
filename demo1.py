import numpy as np
from util.camera_pose_visualizer import CameraPoseVisualizer_cus

if __name__ == '__main__':
    # argument : the minimum/maximum value of x, y, z
    visualizer = CameraPoseVisualizer_cus([-50, 50], [-50, 50], [0, 50])

    # argument : extrinsic matrix, color, scaled focal length(z-axis length of frame body of camera
    visualizer.extrinsic2pyramid(np.eye(4), [1, 1], near=1.0, far=10.0)

    visualizer.show()
