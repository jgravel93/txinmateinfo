MAINTAINER Jason Gravel <jason.gravel93@gmail.com>

RUN /bin/bash -c "source activate python3"

RUN pip3 install pandas
RUN pip3 install bs4
RUN pip3 install urllib
RUN pip3 install ipywidgets
