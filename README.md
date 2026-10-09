# 🖼️ 图像处理实验室

> 一个面向初学者的交互式图像处理教学实验平台  
> Python + OpenCV + Streamlit

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-图像处理-green)](https://opencv.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-交互界面-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📌 项目简介

本项目将经典图像处理算法做成一个简单直观的网页实验平台。

用户可以上传图片，在左侧调整参数，并实时观察处理前后的效果。

项目特别适合：

- 图像处理课程实验
- Python / OpenCV 入门
- 计算机视觉基础教学
- 算法原理演示
- 学生课程设计与二次开发

## ✨ 主要功能

### 1. 平滑处理

使用高斯滤波降低图像噪声和细小纹理。

可以调整：

- 模糊程度
- 高斯卷积核大小

### 2. 边缘提取

使用 Canny 算法检测图像边缘。

可以调整：

- 低阈值
- 高阈值

### 3. 油画效果

使用多次双边滤波模拟油画视觉效果。

可以调整：

- 画笔大小
- 涂抹强度

### 4. 抽象主义效果

使用 K-Means 进行颜色量化，减少图像颜色数量，再叠加轮廓线形成色块化效果。

可以调整：

- 颜色数量 K
- 轮廓强度

### 5. 多算法组合 ⭐

项目不是只能选择一个功能。

可以同时开启：

```text
平滑 → 风格化 → 边缘提取
```

例如：

```text
原图
 ↓
高斯平滑
 ↓
K-Means 色彩量化
 ↓
Canny 边缘检测
 ↓
轮廓叠加
 ↓
最终结果
```

这也是本项目用于教学时重点展示的内容。

## 📁 项目结构

```text
image-processing-lab/
├── app.py
├── image_processing.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── assets/
│   └── README.md
└── docs/
    └── 教学指南.md
```

其中：

- `app.py`：网页界面、参数控制和处理流程
- `image_processing.py`：具体图像处理算法
- `requirements.txt`：项目依赖
- `README.md`：项目说明
- `docs/教学指南.md`：教学使用建议
- `assets/`：项目截图和示例图片

## 🚀 本地运行

### 第一步：安装 Python

建议使用 Python 3.10 或更高版本。

### 第二步：下载项目

```bash
git clone https://github.com/你的用户名/image-processing-lab.git
cd image-processing-lab
```

如果没有使用 Git，也可以直接在 GitHub 页面下载 ZIP。

### 第三步：安装依赖

```bash
python -m pip install -r requirements.txt
```

### 第四步：启动

```bash
python -m streamlit run app.py
```

浏览器打开：

```text
http://localhost:8501
```

## 🧠 算法原理

### 高斯滤波

高斯滤波通过高斯函数产生的卷积核，对邻域像素进行加权平均。

简单理解：

> 一个像素的新值，不再只由自己决定，而是参考周围像素。

核越大，通常平滑程度越强。

### Canny 边缘检测

Canny 是经典边缘检测算法，基本流程可以理解为：

```text
灰度化
 ↓
高斯平滑
 ↓
计算梯度
 ↓
非极大值抑制
 ↓
双阈值检测
 ↓
边缘连接
```

低阈值和高阈值会影响最终检测到的边缘数量。

### K-Means 颜色量化

K-Means 将大量不同颜色的像素划分成 K 个颜色簇。

```text
大量颜色
 ↓
寻找 K 个颜色中心
 ↓
每个像素归类
 ↓
用颜色中心替换原颜色
 ↓
少量颜色组成的色块
```

K 越小，颜色越少，抽象化通常越明显。

### 双边滤波

双边滤波在平滑图像的同时尽量保留边缘。

本项目通过多次双边滤波模拟油画效果，不依赖额外的 OpenCV xphoto 模块，因此更容易在不同环境运行。

## 🎓 教学建议

推荐按照下面顺序进行实验：

1. 先上传一张普通照片。
2. 只开启“平滑处理”，观察核大小变化。
3. 关闭平滑，开启“边缘提取”，观察两个阈值变化。
4. 选择“油画”，观察双边滤波效果。
5. 选择“抽象主义”，观察 K 值变化。
6. 最后同时开启多个功能，观察算法组合产生的结果。

建议学生每次只改变一个参数，这样更容易理解参数与结果之间的关系。

## 🔧 二次开发

如果你想添加新的算法，可以：

1. 在 `image_processing.py` 中新增函数。
2. 在 `app.py` 中添加对应的参数控件。
3. 将算法加入处理流水线。
4. 在“算法原理”区域补充说明。

例如可以继续加入：

- 灰度化
- 二值化
- 直方图均衡化
- 锐化
- 腐蚀
- 膨胀
- 开运算
- 闭运算
- 透视变换
- 旋转
- 缩放
- 轮廓检测

## 🤝 贡献

欢迎通过 Issue 或 Pull Request 提出建议、修复问题或添加新的教学算法。

## 📄 开源协议

本项目采用 MIT License。

详见 [LICENSE](LICENSE)。

## ⚠️ 免责声明

本项目主要用于学习、教学和实验演示。

图像处理结果受输入图片、参数和算法实现影响，不保证适用于所有实际生产场景。

---

## English

An English version of this README is available at **[README.en.md](README.en.md)**.

The app supports both Chinese and English. On first launch it tries to detect the browser's preferred language; use the language switch button in the sidebar to change it. The selected language is stored in the URL (`?lang=zh` or `?lang=en`), so it survives refreshes and can be bookmarked.
