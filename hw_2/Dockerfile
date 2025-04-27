FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y \
    texlive-latex-base

RUN pip install --no-cache-dir latex-generator-itmo-aniciya

WORKDIR /app

COPY task_1.py .
COPY samples/mycats.jpg samples/.

CMD python3 task_1.py & \
    pdflatex -output-directory=artifacts -aux-directory=artifacts artifacts/table.tex & \
    pdflatex -output-directory=artifacts -aux-directory=artifacts artifacts/image.tex
