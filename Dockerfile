FROM python:3.6

WORKDIR /app

RUN pip install --no-cache-dir numpy==1.18.5 pandas matplotlib\
    scipy==1.5.4 \
    torch==1.0.0 -f https://download.pytorch.org/whl/cpu/torch_stable.html \
    tensorflow==2.1.3 \
    tensorflow-probability==0.9.0 \
    scikit-learn==0.23.2 \
    statsmodels\
    scipy

