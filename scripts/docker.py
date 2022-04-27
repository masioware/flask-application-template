from os import system

docker_tag = "flaskapplicationtemplate"


def docker_build():
    file = "Dockerfile"
    version = "latest"

    system("poetry update")
    system("poetry export > requirements.txt")

    build_params = f'--pull --rm -f "{file}" -t {docker_tag}:{version}'
    system(f'docker build {build_params} "."')


def docker_run():
    system(f"docker run -d -p 80:5000 --name {docker_tag} {docker_tag}:latest")


def docker_stop():
    system(f"docker stop {docker_tag}")


def docker_delete():
    system(f"docker rm -f {docker_tag}")
