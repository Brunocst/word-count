from fastapi import FastAPI, Request, Form 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.count import WordCount

WORD_MAX_LEN = 10000
app = FastAPI(
    version ="0.1.0",
    title="Word Count API",
    description="The API for the word count form"
)

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class= HTMLResponse)
async def file(request: Request):
    """Render the form"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class= HTMLResponse)
async def process_response(request: Request, text: str=Form("")):
    """Process the text and return the number of requests"""
    error = None
    count = None

    try:
        if not text:
            error = "A text input is required"
        elif len(text) > WORD_MAX_LEN:
            error = f"The input is too long (max {WORD_MAX_LEN} characters)"
        else:
            sentence = WordCount(text)
            count = sentence.text_processing_pipeline()
    except Exception as e:
        print(f"Error {e} while processing the text")
        error = "Unexpected error while handling the text"

    context = {
        "request": request,
        "text": text,
        "word_count": count,
        "error": error
    }

    return templates.TemplateResponse("index.html", context)
