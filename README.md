
<!-- markdownlint-disable -->
# build-harness-extensions
[![pipeline status](https://gitlab.com/sr2c/build-harness-extensions/badges/main/pipeline.svg?ignore_skipped=true)](https://gitlab.com/sr2c/build-harness-extensions/-/pipelines)
[![latest release](https://gitlab.com/sr2c/build-harness-extensions/-/badges/release.svg)](https://gitlab.com/sr2c/build-harness-extensions/-/tags)
[![gitlab stars](https://img.shields.io/gitlab/stars/sr2c/build-harness-extensions)](https://gitlab.com/sr2c/build-harness-extensions/-/starrers)
<!-- markdownlint-restore -->

[![README Header][readme_header_img]][readme_header_link]

[![SR2 Communications Limited][logo]](https://www.sr2.uk/)

<!--




  ** DO NOT EDIT THIS FILE
  **
  ** This file was automatically generated by the `build-harness`.
  ** 1) Make all changes to `README.yaml`
  ** 2) Run `make init` (you only need to do this once)
  ** 3) Run`make readme` to rebuild this file.
  **
  ** (We maintain HUNDREDS of open source projects. This is how we maintain our sanity.)
  **





-->

Our extensions to Cloud Posse's [build-harness](https://github.com/cloudposse/build-harness). Cloud Posse have made
a great collection of Makefiles to facilitate building Golang projects, Dockerfiles, Helm charts, and more. At SR2
Communications, our technologies sometimes differ from Cloud Posse's choice and sometimes they're the same. That's
why we're grateful that they've built us a way to add extensions to their framework to benefit from the existing
collection while also being able to work with the technologies that we work with every day.

Our primary technologies are:

* Ansible
* Docker Compose (existing Cloud Posse module)
* GitLab
* Python
* Terraform (existing Cloud Posse module)

---







It's 100% Open Source and licensed under the [BSD 2-clause License](LICENSE).









## Usage




### Simple usage

Add a Makefile to the project like:

```make
SHELL := /bin/bash

export README_TEMPLATE_FILE ?= build-harness-extensions/templates/README.md.gotmpl

-include $(shell curl -sSL -o .build-harness-ext "https://gitlab.com/sr2c/build-harness-extensions/-/raw/main/Makefile.bootstrap"; echo .build-harness-ext)
```

### Ansible collection

You can add additional variables to adjust the behaviour of the targets, for an Ansible module for example:

```make
SHELL := /bin/bash

export README_TEMPLATE_FILE ?= $(BUILD_HARNESS_EXTENSIONS_PATH)/templates/README.md.gotmpl

export README_DEPS ?= docs/ansible.md docs/targets.md

-include $(shell curl -sSL -o .build-harness-ext "https://gitlab.com/sr2c/build-harness-extensions/-/raw/main/Makefile.bootstrap"; echo .build-harness-ext)
```

### Ansible role

You do not need to add a complete new Makefile for an Ansible role that is part of a collection, simply add a
Makefile to include the Makefile of the collection:

```make
include ../../Makefile
```

build-harness will automatically discover the path for the build-harness and build-harness-extensions directories.

### Terraform module

Project specific targets may be added to the Makefile. Document the additional targets using two # signs to have
the target automatically documented in the README. Use the HELP_FILTER variable to limit the help target to showing
only the relevant targets for the project:

```make
SHELL := /bin/bash

export HELP_FILTER ?= help|terraform|lint
export README_TEMPLATE_FILE ?= build-harness-extensions/templates/README.md.gotmpl

# List of targets the `readme` target should call before generating the readme
export README_DEPS ?= docs/targets.md docs/terraform.md

-include $(shell curl -sSL -o .build-harness-ext "https://gitlab.com/sr2c/build-harness-extensions/-/raw/main/Makefile.bootstrap"; echo .build-harness-ext)

## Lint terraform code
lint:
	$(SELF) terraform/install terraform/get-modules terraform/lint terraform/validate tflint
```






<!-- markdownlint-disable -->
## Makefile Targets
```text
Available targets:

  aws/install                         Install aws cli bundle
  aws/shell                           Start a aws-vault shell with access to aws api
  bash/lint                           Lint all bash scripts
  chamber/install                     Install chamber
  chamber/shell                       Start a chamber shell with secrets exported to the environment
  clean                               Clean build-harness
  codefresh/export                    DEPRECATED!!! Export codefresh additional envvars
  codefresh/notify/slack/build        Send notification from codefresh to slack using "build" template
  codefresh/notify/slack/deploy       Send notification from codefresh to slack using "deploy" template
  codefresh/notify/slack/deploy/webapp Send notification from codefresh to slack using "deploy" template with exposed endpoint
  codefresh/notify/slack/sync         Send notification from codefresh to slack using "codefresh-sync" template
  codefresh/pipeline/export           Export pipeline vars
  codefresh/sync/apply                Codefresh pipelines sync - Apply the changes
  codefresh/sync/auth/%               Authentificate on codefresh account
  codefresh/sync/deps                 Install dependencies for codefresh sync
  codefresh/sync/diff                 Codefresh pipelines sync - Show changes
  codefresh/sync/pipeline/export      Export sync pipeline vars
  codefresh/trigger/webhook           Trigger a CodeFresh WebHook
  completion/install/bash             Install completion script for bash
  compose/build                       Build local dev environment
  compose/down                        Stop local dev environment
  compose/monitor                     Show containers resource usage
  compose/monitor/follow              Monitor in time containers resource usage
  compose/purge                       Purge local dev environment
  compose/rebuild                     Rebuild custom containers for local dev environment
  compose/restart                     Restart local dev environment
  compose/top                         Show top for containers
  compose/up                          Start local dev environment (daemonized)
  docker/build                        Build docker image
  docker/clean                        Cleanup docker.                     WARNING!!! IT WILL DELETE ALL UNUSED RESOURCES
  docker/clean/containers             Cleanup docker containers.          WARNING!!! IT WILL DELETE ALL UNUSED CONTAINERS
  docker/clean/images                 Cleanup docker images.              WARNING!!! IT WILL DELETE ALL UNUSED IMAGES
  docker/clean/images/all             Cleanup docker images all.          WARNING!!! IT WILL DELETE ALL IMAGES
  docker/clean/networks               Cleanup docker networks.            WARNING!!! IT WILL DELETE ALL UNUSED NETWORKS
  docker/clean/volumes                Cleanup docker volumes.             WARNING!!! IT WILL DELETE ALL UNUSED VOLUMES
  docker/image/promote/local          Promote $SOURCE_DOCKER_REGISTRY/$IMAGE_NAME:$SOURCE_VERSION to $TARGET_DOCKER_REGISTRY/$IMAGE_NAME:$TARGET_VERSION
  docker/image/promote/remote         Pull $SOURCE_DOCKER_REGISTRY/$IMAGE_NAME:$SOURCE_VERSION and promote to $TARGET_DOCKER_REGISTRY/$IMAGE_NAME:$TARGET_VERSION
  docker/image/push                   Push $TARGET_DOCKER_REGISTRY/$IMAGE_NAME:$TARGET_VERSION
  docker/login                        Login into docker hub
  docs/ansible.md                     Generate documentation for an Ansible collection or role
  docs/copyright-add                  Add copyright headers to source code
  docs/github-action.md               Update `docs/github-action.md` from `action.yaml`
  docs/github-actions-reusable-workflows.md Update `docs/github-actions-reusable-workflows.md` from `.github/workflows/*.yaml`
  docs/targets.md                     Update `docs/targets.md` from `make help`
  docs/terraform-split.md             Generate documentation for a Terraform module, splitting out inputs relating to cloudposse/label/null
  docs/terraform.md                   Update `docs/terraform.md` from `terraform-docs`
  geodesic/deploy                     Run a Jenkins Job to Deploy $(APP) with $(CANONICAL_TAG)
  git/aliases-update                  Update git aliases
  git/export                          Export git vars
  git/submodules-update               Update submodules
  github/download-private-release     Download release from github
  github/download-public-release      Download release from github
  github/latest-release               Fetch the latest release tag from the GitHub API
  github/push-artifacts               Push all release artifacts to GitHub (Required: `GITHUB_TOKEN`)
  gitleaks/install                    Install gitleaks
  gitleaks/scan                       Scan current repository
  go/build                            Build binary
  go/build-all                        Build binary for all platforms
  go/clean                            Clean compiled binary
  go/clean-all                        Clean compiled binary and dependencies
  go/deps                             Install dependencies
  go/deps-dev                         Install development dependencies
  go/fmt                              Format code according to Golang convention
  go/install                          Install cli
  go/lint                             Lint code
  go/test                             Run tests
  go/vet                              Vet code
  helm/chart/build                    Build chart $CHART_NAME from $SOURCE_CHART_TPL
  helm/chart/build-all                Alias for helm/chart/build/all. Depricated.
  helm/chart/build/all                Build chart $CHART_NAME from $SOURCE_CHART_TPL for all available $SEMVERSIONS
  helm/chart/clean                    Clean chart packages
  helm/chart/create                   Create chart $CHART from starter scaffold
  helm/chart/promote/local            Promote $SOURCE_CHART_FILE to $TARGET_VERSION
  helm/chart/promote/remote           Promote $CHART_NAME from $SOURCE_VERSION to $TARGET_VERSION. ($SOURCE_CHART_REPO_ENDPOINT required)
  helm/chart/publish                  Alias for helm/chart/publish/all. WARNING: Eventually will became functional equal to helm/chart/publish/one
  helm/chart/publish/all              Publish chart $CHART_NAME to $TARGET_CHART_REPO_ENDPOINT
  helm/chart/publish/package          Publish chart $SOURCE_CHART_FILE to $REPO_GATEWAY_ENDPOINT
  helm/chart/starter/fetch            Fetch starter
  helm/chart/starter/remove           Remove starter
  helm/chart/starter/update           Update starter
  helm/delete/failed                  Delete all failed releases in a `NAMESPACE` subject to `FILTER`
  helm/delete/namespace               Delete all releases in a `NAMEPSACE` as well as the namespace
  helm/delete/namespace/empty         Delete `NAMESPACE` if there are no releases in it
  helm/install                        Install helm
  helm/repo/add                       Add $REPO_NAME from $REPO_ENDPOINT
  helm/repo/add-current               Add helm remote dev repos
  helm/repo/add-remote                Add helm remote repos
  helm/repo/build                     Build repo
  helm/repo/clean                     Clean helm repo
  helm/repo/fix-perms                 Fix repo filesystem permissions
  helm/repo/info                      Show repo info
  helm/repo/lint                      Lint charts
  helm/repo/update                    Update repo info
  helm/serve/index                    Build index for serve helm charts
  helm/toolbox/upsert                 Install or upgrade helm tiller 
  helmfile/install                    Install helmfile
  help                                Help screen
  help/all                            Display help for all targets
  help/short                          This help short screen
  init                                Init build-harness
  jenkins/run-job-with-tag            Run a Jenkins Job with $(TAG)
  make/lint                           Lint all makefiles
  packages/delete                     Delete local copy of packages repository
  packages/install                    Download packages repository
  packages/install/%                  Install package (e.g. helm, helmfile, kubectl)
  packages/reinstall                  Reinstall local copy of packages repository
  packages/reinstall/%                Reinstall package (e.g. helm, helmfile, kubectl)
  packages/uninstall/%                Uninstall package (e.g. helm, helmfile, kubectl)
  python/bandit                       Run bandit to detect security issues
  python/deps                         Install base dependencies with pip (from requirements.txt)
  python/deps/%                       Install extra dependencies with pip (from requirements-%.txt)
  python/deps/all                     Install all dependencies with pip (from base and requirements-*.txt)
  python/deps/list                    List available extra dependency sets
  python/init                         Initialise a Python project with templates
  python/mypy                         Run mypy to detect type issues
  readme                              Alias for readme/build
  readme/build                        Create README.md by building it from README.yaml
  readme/init                         Create basic minimalistic .README.md template file
  readme/lint                         Verify the `README.md` is up to date
  semver/export                       Export semver vars
  slack/notify                        Send webhook notification to slack
  slack/notify/build                  Send notification to slack using "build" template
  slack/notify/deploy                 Send notification to slack using "deploy" template
  sr2/ok                              Print OK
  template/build                      Create $OUT file by building it from $IN template file
  template/deps                       Install dependencies
  terraform/bump-tf-12-min-version    Rewrite versions.tf to bump modules with minimum core version of '0.12.x' to '>= 0.12.26'
  terraform/fmt                       Format terraform
  terraform/get-modules               (Obsolete) Ensure all modules can be fetched
  terraform/get-plugins               (Obsolete) Ensure all plugins can be fetched
  terraform/install                   Install terraform
  terraform/lint                      Format check terraform
  terraform/loosen-constraints        and convert "~>" constraints to ">=".
  terraform/precommit                 Terraform pull-request routine check/update
  terraform/rewrite-required-providers Rewrite versions.tf to update existing configuration to add an explicit source attribute for each provider
  terraform/tflint                    Lint terraform (with tflint)
  terraform/upgrade-modules           This target has not been upgraded to handle registry format
  terraform/validate                  Basic terraform sanity check
  tflint                              Alias for tflint/{install,init,run}
  tflint/init                         Initialise tflint
  tflint/install                      Install terraform
  tflint/run                          Run tflint
  tfmodule/init                       Initialise a Terraform module with templates
  travis/docker-login                 Login into docker hub
  travis/docker-tag-and-push          Tag & Push according Travis environment variables

```
<!-- markdownlint-restore -->




## Help

**Got a question?** We got answers.

File a GitLab [issue](https://gitlab.com/sr2c/build-harness-extensions/-/issues), send us an [email][email] or join our [Matrix Community][matrix].

[![README Commercial Support][readme_commercial_support_img]][readme_commercial_support_link]

## Matrix Community

[![Matrix badge](https://img.shields.io/badge/Matrix-%23dev%3Asr2.uk-blueviolet)][matrix]

Join our [Open Source Community][matrix] on Matrix. It's **FREE** for everyone! This is the best place to talk shop, ask questions, solicit feedback, and work together as a community to build on our open source code.

## Contributing

### Bug Reports & Feature Requests

Please use the [issue tracker](https://gitlab.com/sr2c/build-harness-extensions/-/issues) to report any bugs or file feature requests.

### Developing

If you are interested in being a contributor and want to get involved in developing this project or help out with our other projects, we would love to hear from you! Shoot us an [email][email].

In general, PRs are welcome. We follow the typical "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitLab
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull Request** so that we can review your changes

**NOTE:** Be sure to merge the latest changes from "upstream" before making a pull request!


## Copyright

Copyright © 2021-2024 SR2 Communications Limited












## License

![License: BSD 2-clause](https://img.shields.io/badge/License-BSD%202--clause-blue)

```text
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
   disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
   disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```


## Trademarks

All other trademarks referenced herein are the property of their respective owners.

## About

This project is maintained by [SR2 Communications Limited][website].

[![SR2 Communications Limited][logo]][website]

We're a [DevOps services][website] company based in Aberdeen, Scotland. We ❤️ open source software and
specialise in digital human rights and humanitarian projects.

We offer [paid support][website] on all of our projects.

Check out [our other projects][gitlab], or [hire us][website] to get support with using our projects.

## Trans Rights

![Trans Rights Are Human Rights][trans_rights]

Trans is an umbrella term to describe people whose gender is not the same as, or does not sit comfortably with, the
sex they were assigned at birth. *Like all people*, they have the right to be treated with dignity and respect and to
have their human rights protected.

Trans people face significant discrimination and prejudice in many areas of their lives, including employment,
education, housing, and healthcare. They are also at increased risk of violence and hate crimes. These issues
can have a serious impact on the physical and mental well-being of trans people and can prevent them from fully
participating in society.

Trans rights are therefore an important part of the broader struggle for human rights. Everyone, regardless of
their gender identity, should be able to live their lives free from discrimination and to enjoy the same rights and
opportunities as everyone else. This includes the right to express their gender identity and to be treated with respect
and dignity.

It is important for society to recognize and respect the rights of trans people, and to take steps to address the
discrimination and prejudice that they face. This can include supporting policies and laws that protect trans
people from discrimination and promoting acceptance and understanding of trans people within the broader
community.

* [Four Pillars'](https://www.fourpillarsuk.org/) mission is to support the LGBT+ community in manners of Mental,
  Emotional, Physical & Sexual Health and offer information & support on a person-to-person basis to build a community
  that supports itself through peer education; thereby allowing individuals to make informed choices to improve their
  overall health & wellbeing.

* [Gendered Intelligence](https://genderedintelligence.co.uk/) is a trans-led and trans-involving grassroots organisation
  with a wealth of lived experience, community connections of many kinds, and a depth and breadth of trans community
  knowledge. They offer staff training, consultancy, youth work, mentoring and undertake public engagement activities.

If you have the means and you have benefited from this open source project, please consider making a donation to either
(or both) of the above groups.


## Contributors

<!-- markdownlint-disable -->
|  [![irl][irlxyz_avatar]][irlxyz_homepage]<br/>[irl][irlxyz_homepage] | [![Abel Luck][abelxluck_avatar]][abelxluck_homepage]<br/>[Abel Luck][abelxluck_homepage] |
|---|---|
<!-- markdownlint-restore -->

  [irlxyz_homepage]: https://gitlab.com/irlxyz
  [irlxyz_avatar]: https://gitlab.com/uploads/-/system/user/avatar/5895869/avatar.png?width=130
  [abelxluck_homepage]: https://gitlab.com/abelxluck

  [abelxluck_avatar]: https://secure.gravatar.com/avatar/0f605397e0ead93a68e1be26dc26481a?s=200&amp;d=identicon


<!-- markdownlint-disable -->
  [logo]: https://www.sr2.uk/readme/logo.png
  [website]: https://www.sr2.uk/?utm_source=gitlab&utm_medium=readme&utm_campaign=sr2c/build-harness-extensions&utm_content=website
  [gitlab]: https://go.sr2.uk/gitlab?utm_source=gitlab&utm_medium=readme&utm_campaign=sr2c/build-harness-extensions&utm_content=gitlab
  [contact]: https://go.sr2.uk/contact?utm_source=gitlab&utm_medium=readme&utm_campaign=sr2c/build-harness-extensions&utm_content=contact
  [matrix]: https://go.sr2.uk/matrix?utm_source=gitlab&utm_medium=readme&utm_campaign=sr2c/build-harness-extensions&utm_content=matrix
  [linkedin]: https://www.linkedin.com/company/sr2uk/
  [email]: mailto:contact@sr2.uk
  [readme_header_img]: https://www.sr2.uk/readme/paid-support.png
  [readme_header_link]: https://www.sr2.uk/?utm_source=gitlab&utm_medium=readme&utm_campaign=sr2c/build-harness-extensions&utm_content=readme_header_link
  [readme_commercial_support_img]: https://www.sr2.uk/readme/paid-support.png
  [readme_commercial_support_link]: https://go.sr2.uk/commerical-support?utm_source=gitlab&utm_medium=readme&utm_campaign=sr2c/build-harness-extensions&utm_content=readme_commercial_support_link
  [trans_rights]: https://img.shields.io/badge/Trans%20Rights-Human%20Rights-lightblue?logo=data:img/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAADVJREFUeNpijD73i4EUwMRAIiBZA+PXlTsGm5P+//8/yJzE8m3VzkHmJNL9kKbqNMicBBBgAM3lCr5JiK9jAAAAAElFTkSuQmCC
<!-- markdownlint-restore -->
