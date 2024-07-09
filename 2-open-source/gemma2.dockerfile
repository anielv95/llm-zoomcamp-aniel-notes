FROM ollama/ollama

COPY . . 

RUN mv ollama/ /root/.ollama

ENTRYPOINT ["/bin/ollama"]
CMD ["serve"]