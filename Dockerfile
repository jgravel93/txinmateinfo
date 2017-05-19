MAINTAINER Jason Gravel <jason.gravel93@gmail.com>

RUN /bin/bash -c "source activate python3"

RUN pip install pandas
RUN pip install bs4
RUN pip install urllib
RUN pip install ipywidgets
