FROM andrewosh/binder-base

USER root




# Install Julia kernel
RUN sudo pip install pandas
RUN sudo pip install bs4
RUN sudo pip install ipywidgets
RUN sudo pip install IPython
RUN sudo pip install urllib2

USER main
