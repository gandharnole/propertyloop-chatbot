# 🧠🔍 Smart Property Assistant – Built by Gandhar Sidhaye

> A two-agent AI chatbot designed to assist tenants and landlords by:
> - Detecting visible property issues from images
> - Answering tenancy-related legal questions
> - Suggesting local service providers based on user location

---

## ✨ Features

### 🯞 Agent 1 – Image-Based Property Issue Detection
- Accepts uploaded property images
- Uses **BLIP** (Bootstrapped Language-Image Pretraining) model for caption generation
- Detects visible issues like mold, water leakage, cracks, damp walls
- Returns helpful suggestions based on AI-generated description

### 🧰 Local Services Recommender (Bonus Feature)
- Based on the detected issue & UK town input
- Returns a list of mock local service providers (dummy database)
- Helps users find relevant professionals like plumbers, contractors, or mold specialists

### 📘 Agent 2 – Tenancy FAQ Assistant
- Answers tenancy-related legal questions
- Powered by **Gemini 1.5 Pro (Google GenAI)**
- Provides helpful, region-aware answers (default: UK)
- Covers rent rules, eviction, deposits, lease terms, and more

---

## 💠 Tech Stack

| Component           | Tool / Model Used                            |
|---------------------|----------------------------------------------|
| UI                  | Streamlit                                    |
| Image Captioning    | BLIP (Salesforce/blip-image-captioning-base) |
| Language Model (FAQ)| Gemini 1.5 Pro (Google Generative AI)        |
| Logic Layer         | Python                                       |
| Data Handling       | In-memory dummy service database (dictionary)|

---

## 🧪 How to Run Locally

1. **Clone or download** the project folder
2. Create virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your **Gemini API key** in code:
   ```python
   genai.configure(api_key="your-gemini-key-here")
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🎥 Demo Video

👉 https://drive.google.com/file/d/17Y9f1lJWVJtYhfzCIXGLLUT8ayJCPCwe/view?usp=sharing

---

## 📍 Example Use Case

> - A user uploads an image of a moldy ceiling in Manchester  
> - Agent 1 detects the issue as mold  
> - System returns mold-related suggestions + contacts in Manchester  
> - User then asks: “Can my landlord increase rent anytime?”  
> - Agent 2 replies with a legally accurate response tailored for the UK

---

## 🤛️ About Me

**Gandhar Sidhaye**  
Final Year B.E. Student – Vidyalankar Institute of Technology  
📍 Mumbai, India  
🛠️ Passionate about AI, user-first solutions, and clean architecture

