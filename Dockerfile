FROM andrewosh/binder-base
MAINTAINER Jason Gravel <jgravel@uci.edu>
USER root




# Install Julia kernel
RUN sudo -h pip install pandas
RUN sudo -h pip install bs4
RUN sudo -h pip install ipywidgets
RUN sudo -h pip install IPython
RUN sudo -h pip install urllib2

USER main
