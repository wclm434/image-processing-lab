import streamlit as st
import cv2
import numpy as np

from image_processing import (
    gaussian_blur,
    canny_edges,
    oil_painting_effect,
    color_quantization,
    overlay_edges,
)

# ============================================================
# Page setup and bilingual text
# ============================================================
st.set_page_config(
    page_title="图像处理实验室 | Image Processing Lab",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded",
)

TEXT = {
    "zh": {
        "app_name": "图像处理实验室",
        "switch": "🌐 Switch to English",
        "subtitle": "面向初学者的交互式图像处理教学工具",
        "features": "处理功能",
        "smooth": "① 平滑处理",
        "edge": "② 边缘提取",
        "style": "③ 风格化",
        "smooth_params": "平滑参数",
        "blur": "模糊程度",
        "blur_help": "数值越大，图像越平滑。",
        "edge_params": "边缘参数",
        "low": "低阈值",
        "high": "高阈值",
        "style_params": "风格参数",
        "style_label": "风格",
        "oil": "油画",
        "abstract": "抽象主义",
        "brush": "画笔大小",
        "painting_strength": "涂抹强度",
        "colors": "颜色数量",
        "contour": "轮廓强度",
        "how_to": "使用方法",
        "step1": "① 上传图片",
        "step2": "② 勾选一个或多个处理功能",
        "step3": "③ 调整对应参数",
        "step4": "④ 查看原图与最终结果",
        "pipeline": "多个功能会按照“平滑 → 风格化 → 边缘”的顺序依次处理。",
        "hero_title": "交互式图像处理系统",
        "hero_text": "基于 Python、OpenCV 与 Streamlit，帮助初学者通过可视化参数理解经典图像处理算法。",
        "upload": "上传图片",
        "upload_label": "选择 JPG、JPEG 或 PNG 图片",
        "upload_hint_title": "请先上传一张图片",
        "upload_hint": "上传后可以同时选择多个图像处理功能。",
        "read_error": "图片读取失败，请重新上传。",
        "choose_feature": "请在左侧至少选择一个处理功能。",
        "smooth_tag": "平滑",
        "edge_tag": "边缘提取",
        "not_selected": "未选择处理功能",
        "result": "处理结果",
        "original": "原图",
        "processed": "处理后的图片",
        "algorithm": "📚 查看当前算法原理",
        "gaussian_desc": "**高斯平滑**：使用高斯分布产生的卷积核对邻域像素进行加权平均，可以降低噪声和细小纹理。核大小越大，平滑效果通常越明显。",
        "canny_desc": "**Canny 边缘检测**：根据图像灰度变化寻找边缘。低阈值和高阈值共同决定哪些梯度变化会被保留。",
        "oil_desc": "**油画效果**：使用双边滤波反复平滑颜色，同时尽量保留边缘，模拟颜色块状、颜料涂抹的视觉效果。",
        "abstract_desc": "**K-Means 色彩量化**：把大量像素颜色聚类成较少的颜色中心，从而形成明显的色块；再结合轮廓线得到更强的抽象视觉效果。",
        "dimensions": "图片尺寸",
        "format": "图片格式",
        "file_size": "文件大小",
        "functions_used": "使用功能",
        "count_unit": "个",
        "save": "保存处理结果",
        "save_hint": "当前图片可以保存为 PNG 格式。",
        "download": "下载处理后的图片",
        "download_name": "处理后的图片.png",
    },
    "en": {
        "app_name": "Image Processing Lab",
        "switch": "🌐 切换为中文",
        "subtitle": "An interactive image-processing learning tool for beginners",
        "features": "Processing tools",
        "smooth": "① Smoothing",
        "edge": "② Edge detection",
        "style": "③ Stylization",
        "smooth_params": "Smoothing settings",
        "blur": "Blur strength",
        "blur_help": "Larger values generally produce a smoother image.",
        "edge_params": "Edge settings",
        "low": "Low threshold",
        "high": "High threshold",
        "style_params": "Style settings",
        "style_label": "Style",
        "oil": "Oil painting",
        "abstract": "Abstract",
        "brush": "Brush size",
        "painting_strength": "Paint effect strength",
        "colors": "Number of colors",
        "contour": "Contour strength",
        "how_to": "How to use",
        "step1": "① Upload an image",
        "step2": "② Enable one or more processing tools",
        "step3": "③ Adjust the parameters",
        "step4": "④ Compare the original and result",
        "pipeline": "Enabled tools run in this order: Smoothing → Stylization → Edges.",
        "hero_title": "Interactive Image Processing",
        "hero_text": "Built with Python, OpenCV, and Streamlit. Explore classic image-processing algorithms through visual controls.",
        "upload": "Upload image",
        "upload_label": "Choose a JPG, JPEG, or PNG image",
        "upload_hint_title": "Upload an image to get started",
        "upload_hint": "After uploading, you can combine multiple image-processing tools.",
        "read_error": "Could not read this image. Please upload it again.",
        "choose_feature": "Enable at least one processing tool in the sidebar.",
        "smooth_tag": "Smoothing",
        "edge_tag": "Edge detection",
        "not_selected": "No tools selected",
        "result": "Result",
        "original": "Original image",
        "processed": "Processed image",
        "algorithm": "📚 Learn how the algorithms work",
        "gaussian_desc": "**Gaussian smoothing**: A Gaussian kernel computes a weighted average of neighboring pixels, helping reduce noise and fine texture. Larger kernels usually create a stronger smoothing effect.",
        "canny_desc": "**Canny edge detection**: Finds edges based on grayscale changes. The low and high thresholds determine which gradient changes are retained.",
        "oil_desc": "**Oil-painting effect**: Repeated bilateral filtering smooths colors while trying to preserve edges, creating a painterly, block-like appearance.",
        "abstract_desc": "**K-Means color quantization**: Groups pixel colors into a smaller set of color centers to create bold color regions. Contour lines add a more abstract look.",
        "dimensions": "Image dimensions",
        "format": "Image format",
        "file_size": "File size",
        "functions_used": "Tools used",
        "count_unit": "",
        "save": "Save result",
        "save_hint": "The processed image can be saved as a PNG file.",
        "download": "Download processed image",
        "download_name": "processed_image.png",
    },
}

def detect_browser_language():
    """Choose a sensible first language from the browser's language header."""
    try:
        accept_language = st.context.headers.get("Accept-Language", "").lower()
        # Prefer English only when the browser lists English before Chinese.
        first_language = accept_language.split(",", 1)[0].split(";", 1)[0].strip()
        return "en" if first_language.startswith("en") else "zh"
    except Exception:
        return "zh"


if "language" not in st.session_state:
    # The URL parameter keeps the user's manual choice across refreshes and can be bookmarked.
    saved_language = st.query_params.get("lang")
    st.session_state.language = saved_language if saved_language in ("zh", "en") else detect_browser_language()
    st.query_params["lang"] = st.session_state.language


def tr(key):
    return TEXT[st.session_state.language][key]


def switch_language():
    old_language = st.session_state.language
    new_language = "en" if old_language == "zh" else "zh"
    # Keep the selected style valid when the translated option labels change.
    current_style = st.session_state.get("style_choice")
    if current_style == TEXT[old_language]["oil"]:
        st.session_state["style_choice"] = TEXT[new_language]["oil"]
    elif current_style == TEXT[old_language]["abstract"]:
        st.session_state["style_choice"] = TEXT[new_language]["abstract"]
    st.session_state.language = new_language
    # Store the choice in the URL so it survives page refreshes and can be bookmarked.
    st.query_params["lang"] = new_language

# ============================================================
# Page styling
# ============================================================
st.markdown(
    """
<style>
[data-testid="stAppViewContainer"] { background: #f5f7fb; }
[data-testid="stHeader"] { background: rgba(245,247,251,.9); }
.block-container { max-width: 1450px; padding-top: 1.6rem; padding-bottom: 3rem; }
[data-testid="stSidebar"] { background: #18212f; }
[data-testid="stSidebar"] * { color: #eef2f7; }
.sidebar-title { font-size: 24px; font-weight: 800; color: white; }
.sidebar-subtitle { font-size: 12px; color: #aab5c4; margin: 4px 0 18px; }
.sidebar-label { color: #9eabba; font-size: 12px; font-weight: 700; margin: 18px 0 8px; }
.help-box { background: #222e3e; border: 1px solid #334155; border-radius: 12px; padding: 12px; font-size: 12px; color: #b9c4d2; line-height: 1.7; margin-top: 15px; }
.hero { background: white; border: 1px solid #e5e9f0; border-radius: 20px; padding: 27px 30px; margin-bottom: 18px; box-shadow: 0 8px 26px rgba(15,23,42,.05); }
.hero-title { color: #172033; font-size: 30px; font-weight: 800; }
.hero-text { color: #697586; margin-top: 7px; font-size: 14px; }
.card { background: white; border: 1px solid #e5e9f0; border-radius: 18px; padding: 18px 20px; box-shadow: 0 6px 20px rgba(15,23,42,.04); }
.section-title { color: #172033; font-size: 20px; font-weight: 800; margin-bottom: 12px; }
.small-title { color: #475467; font-size: 13px; font-weight: 700; }
.mode-tag { display: inline-block; padding: 5px 10px; border-radius: 999px; background: #eef2ff; color: #4f46e5; font-size: 12px; font-weight: 700; margin: 2px 4px 2px 0; }
.info { background: white; border: 1px solid #e5e9f0; border-radius: 15px; padding: 14px 16px; }
.info-name { color: #98a2b3; font-size: 11px; font-weight: 700; }
.info-value { color: #172033; font-size: 17px; font-weight: 800; margin-top: 4px; }
.empty { background: white; border: 1px dashed #cbd5e1; border-radius: 18px; padding: 60px 20px; text-align: center; }
.empty-icon { font-size: 40px; }
.empty-title { color: #344054; font-size: 18px; font-weight: 800; margin-top: 8px; }
.empty-text { color: #98a2b3; font-size: 13px; margin-top: 5px; }
.download { background: #18212f; border-radius: 17px; padding: 18px 20px 20px; margin-top: 18px; }
.download-title { color: white; font-size: 16px; font-weight: 800; }
.download-text { color: #aab5c4; font-size: 12px; margin-top: 4px; }
.stDownloadButton > button { width: 100%; margin-top: 12px; border-radius: 10px !important; font-weight: 700 !important; }
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# Sidebar controls
# ============================================================
with st.sidebar:
    st.button(tr("switch"), on_click=switch_language, use_container_width=True)
    st.markdown(f'<div class="sidebar-title">🖼️ {tr("app_name")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sidebar-subtitle">{tr("subtitle")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sidebar-label">{tr("features")}</div>', unsafe_allow_html=True)

    use_smooth = st.checkbox(tr("smooth"), key="use_smooth")
    use_edge = st.checkbox(tr("edge"), key="use_edge")
    use_style = st.checkbox(tr("style"), key="use_style")

    kernel_size = 7
    min_val, max_val = 50, 150
    style_options = [tr("oil"), tr("abstract")]
    style = style_options[0]
    brush_size, painting_strength = 7, 2
    k, edge_strength = 6, 100

    if use_smooth:
        st.markdown(f'<div class="sidebar-label">{tr("smooth_params")}</div>', unsafe_allow_html=True)
        kernel_size = st.slider(tr("blur"), 3, 31, 7, 2, help=tr("blur_help"), key="kernel_size")

    if use_edge:
        st.markdown(f'<div class="sidebar-label">{tr("edge_params")}</div>', unsafe_allow_html=True)
        min_val = st.slider(tr("low"), 0, 255, 50, key="min_val")
        max_val = st.slider(tr("high"), 0, 255, 150, key="max_val")
        if min_val > max_val:
            min_val, max_val = max_val, min_val

    if use_style:
        st.markdown(f'<div class="sidebar-label">{tr("style_params")}</div>', unsafe_allow_html=True)
        style = st.selectbox(tr("style_label"), style_options, key="style_choice")
        if style == tr("oil"):
            brush_size = st.slider(tr("brush"), 3, 15, 7, 2, key="brush_size")
            painting_strength = st.slider(tr("painting_strength"), 1, 5, 2, key="painting_strength")
        else:
            k = st.slider(tr("colors"), 2, 15, 6, key="color_count")
            edge_strength = st.slider(tr("contour"), 50, 250, 100, key="edge_strength")

    st.markdown(
        f"""
        <div class="help-box">
        <b>{tr('how_to')}</b><br>
        {tr('step1')}<br>{tr('step2')}<br>{tr('step3')}<br>{tr('step4')}<br><br>
        {tr('pipeline')}
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# Main header and upload
# ============================================================
st.markdown(
    f"""
    <div class="hero">
        <div class="hero-title">{tr('hero_title')}</div>
        <div class="hero-text">{tr('hero_text')}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(f'<div class="card"><div class="section-title">{tr("upload")}</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(tr("upload_label"), type=["jpg", "jpeg", "png"], key="image_upload")
st.markdown("</div>", unsafe_allow_html=True)

if uploaded_file is None:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="empty">
            <div class="empty-icon">＋</div>
            <div class="empty-title">{tr('upload_hint_title')}</div>
            <div class="empty-text">{tr('upload_hint')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()

file_bytes = np.frombuffer(uploaded_file.getvalue(), dtype=np.uint8)
image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
if image is None:
    st.error(tr("read_error"))
    st.stop()

# ============================================================
# Multi-step processing pipeline
# ============================================================
result = image.copy()
active_names = []

if use_smooth:
    result = gaussian_blur(result, kernel_size)
    active_names.append(tr("smooth_tag"))

if use_style:
    if style == tr("oil"):
        result = oil_painting_effect(result, brush_size, painting_strength)
        active_names.append(tr("oil"))
    else:
        result = color_quantization(result, k)
        active_names.append(tr("abstract"))

if use_edge:
    edges = canny_edges(result, min_val, max_val)
    if use_style:
        result = overlay_edges(result, edges, strength=edge_strength)
    else:
        result = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    active_names.append(tr("edge_tag"))

if not active_names:
    result = image.copy()
    active_names = [tr("not_selected")]
    st.info(tr("choose_feature"))

original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
tags = "".join(f'<span class="mode-tag">{name}</span>' for name in active_names)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f'<div class="card"><div class="section-title">{tr("result")}</div><div>{tags}</div></div>',
    unsafe_allow_html=True,
)
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown(f'<div class="card"><div class="small-title">{tr("original")}</div>', unsafe_allow_html=True)
    st.image(original_rgb, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="card"><div class="small-title">{tr("processed")}</div>', unsafe_allow_html=True)
    st.image(result_rgb, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# Algorithm explanations
# ============================================================
with st.expander(tr("algorithm")):
    if use_smooth:
        st.markdown(tr("gaussian_desc"))
    if use_edge:
        st.markdown(tr("canny_desc"))
    if use_style and style == tr("oil"):
        st.markdown(tr("oil_desc"))
    if use_style and style == tr("abstract"):
        st.markdown(tr("abstract_desc"))

# ============================================================
# Image information
# ============================================================
height, width = image.shape[:2]
file_size_kb = uploaded_file.size / 1024
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

def add_info(name, value):
    st.markdown(
        f'<div class="info"><div class="info-name">{name}</div><div class="info-value">{value}</div></div>',
        unsafe_allow_html=True,
    )

with c1:
    add_info(tr("dimensions"), f"{width} × {height}")
with c2:
    add_info(tr("format"), uploaded_file.type.split("/")[-1].upper())
with c3:
    add_info(tr("file_size"), f"{file_size_kb:.1f} KB")
with c4:
    add_info(tr("functions_used"), f"{0 if active_names == [tr('not_selected')] else len(active_names)} {tr('count_unit')}")

# ============================================================
# Download
# ============================================================
success, encoded_image = cv2.imencode(".png", result)
if success:
    st.markdown(
        f'<div class="download"><div class="download-title">{tr("save")}</div><div class="download-text">{tr("save_hint")}</div>',
        unsafe_allow_html=True,
    )
    st.download_button(
        tr("download"),
        data=encoded_image.tobytes(),
        file_name=tr("download_name"),
        mime="image/png",
    )
    st.markdown("</div>", unsafe_allow_html=True)
