FROM andrewosh/binder-base

USER root
RUN pip install pandas
RUN pip install bs4
RUN pip install ipywidgets
RUN pip install IPython
RUN pip install urllib2
