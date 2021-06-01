FROM gospatial/tegola:v0.13.0
WORKDIR /
# --- Create minimal deployment image, just alpine & the binary
#LABEL io.gospatial.version="0.6.0_beta"
RUN apk add gettext \
	&& apk add python3 \
	&& apk add bash 
COPY --from=gospatial/tegola /opt /opt
ENTRYPOINT []

COPY main.py main.py
RUN chmod +x main.py
RUN mkdir -p tegola_config/
COPY configTemplate.toml tegola_config/configTemplate.toml

# RUN envsubst < "/tegola_config/configTemplate.toml" > "/tegola_config/config.toml"
# CMD ["/opt/tegola", "--config", "tegola_config/config.toml", "serve"]
CMD python3 main.py  