"""图像处理算法模块。

本文件只负责算法，不负责 Streamlit 界面。
适合教学时单独阅读和修改。
"""

import cv2
import numpy as np


def gaussian_blur(image: np.ndarray, kernel_size: int) -> np.ndarray:
    """高斯平滑。kernel_size 必须为正奇数。"""
    if kernel_size < 3 or kernel_size % 2 == 0:
        raise ValueError("kernel_size 必须是大于等于 3 的奇数。")
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)


def canny_edges(image: np.ndarray, min_val: int, max_val: int) -> np.ndarray:
    """Canny 边缘检测，返回单通道边缘图。"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, min_val, max_val)


def oil_painting_effect(
    image: np.ndarray,
    size: int,
    strength: int,
) -> np.ndarray:
    """使用多次双边滤波模拟油画效果。

    不依赖 cv2.xphoto，因此在常见的 opencv-python-headless
    环境中也可以运行。
    """
    result = image.copy()

    for _ in range(max(1, strength)):
        result = cv2.bilateralFilter(
            result,
            d=size,
            sigmaColor=75,
            sigmaSpace=75,
        )

    return cv2.bilateralFilter(
        result,
        d=size,
        sigmaColor=100,
        sigmaSpace=100,
    )


def color_quantization(image: np.ndarray, k: int) -> np.ndarray:
    """K-Means 颜色量化。"""
    if k < 2:
        raise ValueError("k 必须大于等于 2。")

    data = image.reshape((-1, 3)).astype(np.float32)

    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        20,
        1.0,
    )

    _, labels, centers = cv2.kmeans(
        data,
        k,
        None,
        criteria,
        8,
        cv2.KMEANS_PP_CENTERS,
    )

    centers = np.uint8(centers)
    result = centers[labels.flatten()]
    return result.reshape(image.shape)


def overlay_edges(
    image: np.ndarray,
    edges: np.ndarray,
    strength: int = 100,
) -> np.ndarray:
    """把 Canny 轮廓以黑色叠加到原图上。"""
    result = image.copy()

    kernel_size = 2 if strength < 160 else 3
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    thick_edges = cv2.dilate(edges, kernel, iterations=1)

    result[thick_edges > 0] = (0, 0, 0)
    return result
