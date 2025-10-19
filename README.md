# news_summarizerAI

A web-based **News Summarizer** built with **FastAPI** and **Streamlit**, leveraging the `microsoft/phi-3-mini-4k-instruct` model from **Hugging Face Transformers** for generating concise summaries of news articles.

---

## Features

- Summarizes news articles quickly and accurately.
- Built with **FastAPI** for API endpoints.
- **Streamlit** frontend for easy user interaction.
- Uses **Hugging Face Transformers** model `microsoft/phi-3-mini-4k-instruct`.
- Easy deployment and scalable architecture.

---

## Architecture

```

[Streamlit Frontend] <--> [FastAPI Backend] <--> [Transformers Model]

````

1. **Frontend**: Streamlit app for user input and displaying summaries.
2. **Backend**: FastAPI handles requests and interacts with the model.
3. **Model**: `microsoft/phi-3-mini-4k-instruct` generates text summaries.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/news-summarizer.git
cd news-summarizer
````

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

**`requirements.txt`** should include:

```
fastapi
uvicorn
streamlit
transformers
torch  # or accelerate + bitsandbytes if using GPU optimization
```

---

## Usage

### Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

By default, FastAPI runs at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

Open the link displayed in the terminal to access the web app.

---

## API Endpoints

* `POST /summarize`
  Request body:

```json
{
  "text": "Your news article text here"
}
```

Response:

```json
{
  "summary": "Generated summary of the news article"
}
```

---

## Example

**Input Article:**

> "NASA announced a new mission to study the Moon’s water ice deposits. The mission aims to send a rover to collect samples and analyze the surface composition."

**Generated Summary:**

> "NASA plans a lunar mission to study water ice deposits using a rover to collect and analyze samples."

---

## Model Details

* **Model:** `microsoft/phi-3-mini-4k-instruct`
* **Type:** Instruction-tuned language model
* **Framework:** Hugging Face Transformers
* **Max Context:** 4k tokens

---

## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature-name`
5. Create a pull request.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

* [FastAPI](https://fastapi.tiangolo.com/)
* [Streamlit](https://streamlit.io/)
* [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
* [Microsoft Phi-3 Mini](https://huggingface.co/microsoft/phi-3-mini-4k-instruct)
