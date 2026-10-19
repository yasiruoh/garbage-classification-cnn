import io
import json
import streamlit as st
from src.validation import check_bytes

st.set_page_config(page_title='Garbage Classification CNN', page_icon="🔬", layout="wide")
st.title('Garbage Classification CNN')
st.caption('ResNet50 convolutional classification across twelve waste categories.')
threshold = st.sidebar.slider("Review threshold", 0.0, 1.0, 0.5, 0.05)
st.sidebar.caption("Local inference • JSON export • No fabricated predictions")


from PIL import Image, ImageOps
from src.engine import predict
uploaded = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])
camera = st.camera_input("Or capture an image")
selected = uploaded or camera
if selected:
    try:
        data = check_bytes(selected.getvalue())
        image = ImageOps.exif_transpose(Image.open(io.BytesIO(data))).convert("RGB")
        if image.width * image.height > 20_000_000:
            raise ValueError("Image exceeds 20 megapixels.")
        st.image(image, caption="Input image", use_container_width=True)
        if st.button("Analyze image", type="primary"):
            with st.spinner("Running inference"):
                result, annotated = predict(image, threshold)
            if annotated is not None:
                st.image(annotated, caption="Detections", use_container_width=True)
                buffer = io.BytesIO()
                Image.fromarray(annotated).save(buffer, format="PNG")
                st.download_button("Download annotated image", buffer.getvalue(), "annotated.png", "image/png")
            if "total" in result:
                st.metric("Detections in this image", result["total"])
            if "label" in result:
                st.subheader(result["label"])
                st.caption("Model scores are not guarantees of correctness.")
            st.json(result)
            st.download_button("Download JSON", json.dumps(result,indent=2), "result.json", "application/json")
    except Exception as exc:
        st.error(f"Analysis unavailable: {exc}")
        st.info("Check dependency installation, available memory, and access to the documented upstream model host. No fallback prediction is substituted.")
