# Word-count
A web application that count words in the text input

# Rules & Assumptions

## 1. Word Definition Criteria

### Excluded as words:
- **Numeric sequences:**  
  Examples: `"123"`, `"45.6"`
- **Independent punctuation marks:**  
  Examples: `"!"`, `"?"`
- **Emoji characters:**  
  Examples: `"👍"`, `"😀"`

### Valid word requirements:
- Must contain at least one alphabetic character

**Examples:**  
`"great!"`, `"hel1o"`, `"test123"`

---

## 2. Input Constraints

### Minimum requirement:
- At least 1 non-whitespace character

### Maximum capacity:
- 10,000 character limit (including whitespace)
- Submissions exceeding the limit are rejected

---

## 3. Word Separation Logic

### Primary delimiters:
```python
[" ", "-", "|"]  # Space, Hyphen, Vertical Pipe
```
## Usage on docker
Build the docker image
```
docker build -f Dockerfile -t wordcount .
```

Run the docker image:
```
 docker compose up -d
```

Visit http://localhost:8000 in your browser

## Tests

To run the tests, run pytest in the word-count directory
```
 pytest -W ignore::DeprecationWarning
```

Our tests cover the following cases:
The count functionality, multiline texts, texts bigger than max size, text with number, text with emojis, text with special characters, text with "-" delimiter and empty words


## Output sample
![alt text](image.png)

## Next steps
#### Need to develop support for non latin languages such as Japanese and Korean;
#### The algorithm can be optimized for better performance in the space and time dimensions;
#### The supported delimiters can be expanded 
#### Add support on the frontend for word count frequency
#### Add logging to the application
#### Expand tests to cover more edge cases
#### Resolve deprecationg warning
#### Add a login to the form