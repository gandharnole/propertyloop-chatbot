import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import google.generativeai as genai
import os

st.set_page_config(page_title="PropertyLoop Chatbot", page_icon="🏡")

genai.configure(api_key="AIzaSyAUg_MmrhQcPbjQXUmPsPyeTRU2LmmVQWY")

# Dummy database for service regarding the problem
SERVICE_DATABASE = {
    "London": {
        "mold": ["MoldAway London - 0207 123 4567"],
        "crack": ["WallFix Contractors - 0208 555 4321"],
        "plumber": ["PipePro Plumbing - 0203 888 2222"]
    },
    "Manchester": {
        "mold": ["FreshAir Manchester - 0161 234 5678"],
        "crack": ["BuildSafe UK - 0161 876 4321"],
        "plumber": ["FlowFix Services - 0161 900 1234"]
    },
    "Birmingham": {
        "mold": ["DampGuard Midlands - 0121 555 7890"],
        "crack": ["StructoCheck - 0121 678 9999"],
        "plumber": ["RapidPlumb - 0121 456 0000"]
    },
    "default": {
        "plumber": ["UK National Plumbing - 0800 000 1111"],
        "mold": ["Nationwide Mold Solutions - 0800 222 3333"],
        "crack": ["SafeWalls UK - 0800 999 8888"]
    }
}

# To load BLIP
@st.cache_resource
def load_blip():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_blip()

# Agent 1: Image Issue Detection & Troubleshooting

def analyze_image(image):
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def troubleshoot_issue(caption):
    return f"Detected issue: {caption}. Please consult a property expert for further evaluation."

def get_services(location, caption):
    caption = caption.lower()
    issue_keywords = {
        "mold": ["mold", "mould", "fungus", "black spots"],
        "crack": ["crack", "fracture", "split", "gap"],
        "leak": ["leak", "leaking", "drip", "burst", "overflow", "spray"],
        "plumber": ["pipe", "plumbing", "water line", "spray", "flow", "burst"],
        "damp": ["damp", "moisture", "wet wall", "humidity"]
    }
    for issue_type, keywords in issue_keywords.items():
        if any(kw in caption for kw in keywords):
            matched = SERVICE_DATABASE.get(location.lower().capitalize(), SERVICE_DATABASE["default"]).get(issue_type, [])
            return matched
    return []

# Streamlit App UI
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🧠🔍 Smart Property Assistant - Built by Gandhar</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Your intelligent assistant for property issue detection and tenancy support.</p>", unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.markdown("#### Powered by:\n- BLIP\n- Gemini 1.5 Pro\n- Streamlit")

query_type = st.radio("Choose query type:", ["Image Issue Detection", "Tenancy FAQ"])

if query_type == "Image Issue Detection":
    st.markdown("### 🧾 Agent 1: Image-Based Problem Detection")
    uploaded_file = st.file_uploader("Upload a property image:", type=["jpg", "jpeg", "png"])
    user_location = st.text_input("Enter your UK town for local service suggestions:", value="London")
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)
        with st.spinner("🔍 Analyzing your image for property issues..."):
            caption = analyze_image(image)
            st.markdown(f"**BLIP Caption:** `{caption}`")
            suggestion = troubleshoot_issue(caption)
            st.markdown(f"**Suggestion:** {suggestion}")

            local_services = get_services(user_location, caption)
            if local_services:
                st.markdown("#### 🧰 Local Experts Who Can Help You")
                for s in local_services:
                    st.markdown(f"- {s}")
            else:
                st.markdown("*No specific services found for this issue in your area.*")

#Agent 2: Tenancy FAQ using genAI
elif query_type == "Tenancy FAQ":
    st.markdown("### 📄 Agent 2: Tenancy FAQ Assistant")
    question = st.text_input("Ask a tenancy-related question:")
    location = st.text_input("Enter your location (default: UK):", value="UK")
    if question:
        with st.spinner("💬 Fetching the most relevant legal guidance..."):
            model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
            prompt = f"A user from {location} asked a tenancy-related question:\n{question}\n\nPlease provide a clear, legally accurate, and helpful answer based on general UK tenancy laws."
            response = model.generate_content(prompt)
            st.markdown(f"**Answer:** {response.text}")