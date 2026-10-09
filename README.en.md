# 🖼️ Image Processing Lab

> An interactive image-processing learning platform for beginners.  
> Built with Python, OpenCV, and Streamlit.

[简体中文](README.md) | **English**

## Overview

Image Processing Lab turns classic image-processing algorithms into an approachable web app. Upload an image, adjust parameters in the sidebar, and compare the original and processed results.

## Features

- **Gaussian smoothing** — reduce noise and fine details with an adjustable kernel size.
- **Canny edge detection** — tune the low and high thresholds.
- **Oil-painting effect** — simulate painterly color regions with repeated bilateral filtering.
- **Abstract style** — use K-Means color quantization and contour overlays.
- **Composable pipeline** — enable several tools at once; they run in the order Smoothing → Stylization → Edge Detection.
- **Chinese/English interface** — detects the browser's preferred language on first launch; use the language button to switch. The choice is saved in the URL, so it survives refreshes and can be bookmarked.
- **PNG export** — download the processed image.

## Project structure

```text
image-processing-lab/
├── app.py
├── image_processing.py
├── requirements.txt
├── README.md
├── README.en.md
├── LICENSE
├── .gitignore
├── assets/
└── docs/
    └── 教学指南.md
```

## Run locally

Recommended: Python 3.10 or newer.

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Then open <http://localhost:8501> in your browser.

## Algorithm notes

- **Gaussian blur:** computes a weighted average of neighboring pixels using a Gaussian kernel.
- **Canny:** detects edges using image gradients and two thresholds.
- **Oil-painting simulation:** repeated bilateral filtering smooths colors while attempting to preserve edges.
- **K-Means quantization:** groups pixel colors into a smaller number of color centers; contours are then overlaid for a stronger graphic style.

## Contributing

Bug reports, documentation improvements, and new image-processing experiments are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the MIT License. See [LICENSE](LICENSE).
