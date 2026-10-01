# 🎥 AI Video Assistant with RAG

An AI-powered video assistant that transforms long-form videos into structured, searchable knowledge.

The application can process YouTube videos or local audio/video files, transcribe them using OpenAI Whisper, generate summaries and structured information using an LLM, and provide question answering through Retrieval-Augmented Generation (RAG).

## 🚀 Features

- 🎥 Process YouTube videos or local audio/video files
- 🎙️ Speech-to-text transcription using OpenAI Whisper
- 📝 Automatic video/meeting title generation
- 📋 AI-generated summaries
- ✅ Extract action items
- 🔑 Extract key decisions
- ❓ Identify unresolved questions and follow-ups
- 🧠 Create embeddings from transcript content
- 🗄️ Store embeddings in ChromaDB
- 🔍 Semantic search over the transcript
- 💬 Ask questions about the processed video using RAG
- 🤖 Groq-powered LLM responses
- 💻 Runs locally using Python

## 🛠️ Tech Stack

| Technology              | Purpose                           |
| ----------------------- | --------------------------------- |
| Python                  | Core application                  |
| LangChain               | LLM and RAG orchestration         |
| OpenAI Whisper          | Speech-to-text transcription      |
| Groq                    | LLM inference                     |
| GPT-OSS 120B            | Summarization, extraction and Q&A |
| ChromaDB                | Vector database                   |
| Hugging Face Embeddings | Text embeddings                   |
| yt-dlp                  | YouTube audio downloading         |
| FFmpeg                  | Audio conversion                  |
| pydub                   | Audio processing                  |

## 📁 Project Structure

```text
ai-video-assitant.rag/
│
├── core/
│   ├── extractor.py
│   ├── rag_engine.py
│   ├── summaries.py
│   ├── transcriber.py
│   └── vector_store.py
│
├── utils/
│   └── audio_processor.py
│
├── downloads/
├── vector_db/
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/frankuard/video-assistant-with-rag
cd video-assitant-with-rag
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

FFmpeg is required for audio processing.

#### Arch Linux

```bash
sudo pacman -S ffmpeg
```

#### Ubuntu / Debian

```bash
sudo apt install ffmpeg
```

For Windows, install FFmpeg and add it to your system PATH.

Verify the installation:

```bash
ffmpeg -version
```

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
WHISPER_MODEL=small
```

## ▶️ Usage

Run the application with:

```bash
python main.py
```

The application will ask for a YouTube URL or local file path:

```text
Enter YouTube URL or local file path:
```

### YouTube

```text
https://www.youtube.com/watch?v=VIDEO_ID
```

### Local File

```text
downloads/my-video.wav (copy path of it and paste it)
```

After processing, the application generates the title, summary, action items, key decisions, and open questions, then starts the RAG chat.

## 💬 RAG Chat

You can ask questions about the processed video directly from the terminal.

```text
💬 Chat with your meeting (type 'exit' to quit)

You:
```

Example:

```text
You: What were the main topics discussed?
```

```text
You: What action items were assigned?
```

```text
You: What decisions were made?
```

To exit:

```text
exit
```

## 👨‍💻 Author

**Roshan Karki**
