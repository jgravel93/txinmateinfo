FROM andrewosh/binder-base
MAINTAINER Jason Gravel <jgravel@uci.edu>
USER root




# Install Julia kernel
RUN pip install pandas
RUN pip install bs4
RUN pip install ipywidgets
RUN pip install IPython
RUN pip install urllib

USER main
