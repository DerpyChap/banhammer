workflow "DerpyChap" {
  on = "push"
  resolves = ["Publish Python Package"]
}

action "Publish Python Package" {
  needs = "Master"
  uses = "mariamrf/py-package-publish-action@v0.0.2"
  secrets = ["TWINE_USERNAME", "TWINE_PASSWORD"]
  env = {
    BRANCH = "master"
    PYTHON_VERSION = "3.6.0"
  }
}

action "Master" {
  uses = "actions/bin/filter@master"
  args = "branch master"
}
