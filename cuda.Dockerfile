FROM pytorch/pytorch:1.0-cuda10.0-cudnn7-runtime as base

RUN conda install -c conda-forge tensorflow==2.1.3 tensorflow-probability==0.9.0 numpy==1.18.5 scipy==1.5.4 matplotlib statsmodels
