FROM public.ecr.aws/lambda/python:3.8


RUN /var/lang/bin/python3.8 -m pip install --upgrade pip
RUN pip install -U pip

# Copy function code
 COPY ./ ${LAMBDA_TASK_ROOT}/

RUN  python3 -m pip install --no-cache-dir -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

RUN mkdir /.cache

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]
