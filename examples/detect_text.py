from betterocr import detect_text

text = detect_text(
    "./demo.jpg",
    ["ch_sim", "en"],  # use zh for both ch_sim(easy_ocr), chi_sim(tesseract)
    context="",  # product name
    tesseract={},
    ai_option={
        "base_url": "http://localhost:11434/v1",
        "api_key": "sk-9f1f8600616043b4a403f0f6aa64807f",
    },
    ai_client={"model": "qwen2"},
)
print("\n")
print(text)
