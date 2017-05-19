FROM andrewosh/binder-base
MAINTAINER Jason Gravel <jason.gravel93@gmail.com>
USER root




# Install Julia kernel
RUN sudo pip install pandas
RUN sudo pip install bs4
RUN sudo pip install ipywidgets
RUN sudo pip install IPython
RUN sudo pip install urllib2

USER main
