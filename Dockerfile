FROM andrewosh/binder-base

USER root




# Install Julia kernel
RUN sudo -H pip install pandas
RUN sudo -H pip install bs4
RUN sudo -H pip install ipywidgets
RUN sudo -H pip install IPython
RUN sudo -H pip install urllib2

USER jgravel
