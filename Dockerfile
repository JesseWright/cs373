FROM python:3.5.2

RUN pip install --upgrade pip && \
    pip --version             && \
    pip install coverage      && \
    pip install numpy         && \
    pip install pylint

CMD bash
