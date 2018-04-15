FROM kbase/kbase:sdkbase2.latest
MAINTAINER KBase Developer
# -----------------------------------------
# In this section, you can install any system dependencies required
# to run your App.  For instance, you could place an apt-get update or
# install line here, a git checkout to download code, or run any other
# installation scripts.

# Update certs
#RUN apt-get update
#RUN apt-get install ca-certificates

## Fix Python SSL warnings for python < 2.7.9 (system python on Trusty is 2.7.6)
## https://github.com/pypa/pip/issues/4098
#RUN pip install pip==8.1.2
#RUN pip install --disable-pip-version-check requests requests_toolbelt pyopenssl --upgrade

# Here we install a python coverage tool and an
# https library that is out of date in the base image.
RUN pip install coverage


# Install SparCC
#
RUN mkdir -p /kb/module/lib
RUN mkdir -p /kb/module/bin
WORKDIR /kb/module/lib
RUN curl https://bitbucket.org/yonatanf/sparcc/get/default.tar.gz > sparcc.tar.gz && \
     tar xfz sparcc.tar.gz && \
     ln -s yonatanf-sparcc-05f4d3f31d77 sparcc && \
     cp sparcc/*py /kb/module/bin

# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
