import json
import os
import subprocess
import sys

import click

from dt import DockerSync


def ensure_success(*args):
    ret = subprocess.run(args)
    if ret.returncode != 0:
        print(f"run cmd: {args} failed")
        sys.exit(1)


def do_sync(c: DockerSync):
    for tag in c.tag:
        src_image = f"{c.src}:{tag}"
        for dst in c.dst:
            dst_image = f"{dst}:{tag}"
            ensure_success("docker", "pull", src_image)
            ensure_success("docker", "tag", src_image, dst_image)
            ensure_success("docker", "push", dst_image)


@click.command("docker-sync")
@click.argument("name")
def main(name: str):
    """
    同步 Docker 镜像
    """
    file = os.path.join(os.path.dirname(__file__), "images", f"{name}.json")

    with open(file) as fp:
        d = json.load(fp)

    v = DockerSync(**d)
    print(f"加载配置... {v=}")
    do_sync(v)


if __name__ == "__main__":
    main()
