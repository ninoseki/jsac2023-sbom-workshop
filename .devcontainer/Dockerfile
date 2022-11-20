# setup vulnerability log4j app
FROM gradle:7.5.1-jdk17 AS builder

WORKDIR /home/gradle/src

COPY --chown=gradle:gradle log4j-vulnerable-app /home/gradle/src

RUN cd /home/gradle/src \
	&& gradle dependencies --write-locks \
	&& gradle bootJar --no-daemon

# setup Python app with Java
FROM python:3.10

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# create the user
RUN groupadd --gid $USER_GID $USERNAME \
	&& useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# setup requirements
RUN apt update \
	&& apt install -y --no-install-recommends \
	sudo \
	default-jdk-headless \
	curl \
	wget \
	git \
	jq \
	vim \
	# install HTTPie
	&& curl -SsL https://packages.httpie.io/deb/KEY.gpg | apt-key add - \
	&& curl -SsL -o /etc/apt/sources.list.d/httpie.list https://packages.httpie.io/deb/httpie.list \
	&& apt update \
	&& apt install -y --no-install-recommends httpie \
	# cleanup
	&& apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
	&& echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
	&& chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME

WORKDIR /app

COPY --from=builder /home/gradle/src/build/libs/*.jar /app/log4j-vulnerable-app/spring-boot-application.jar
COPY --from=builder /home/gradle/src/gradle.lockfile /app/log4j-vulnerable-app/gradle.lockfile

COPY python-vulnerable-app /app/python-vulnerable-app
COPY postCreateCommand.sh .

RUN pip install -U pip \
	&& pip install --no-cache-dir -r /app/python-vulnerable-app/requirements.txt

# install SBOM tools
WORKDIR /tools

RUN curl -Lo sbom-tool https://github.com/microsoft/sbom-tool/releases/latest/download/sbom-tool-linux-x64 \
	&& chmod +x sbom-tool \
	&& sudo mv sbom-tool /usr/local/bin \
	&& curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sudo sh -s -- -b /usr/local/bin
