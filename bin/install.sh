#!/bin/bash
export BUILD_HARNESS_EXT_ORG=${1:-sr2c}
export BUILD_HARNESS_EXT_PROJECT=${2:-build-harness-extensions}
export BUILD_HARNESS_EXT_BRANCH=${3:-main}
export BUILD_HARNESS_EXT_GIT="https://gitlab.com/${BUILD_HARNESS_EXT_ORG}/${BUILD_HARNESS_EXT_PROJECT}.git"

if [ "$BUILD_HARNESS_EXT_PROJECT" ] && [ -d "$BUILD_HARNESS_EXT_PROJECT" ]; then
	  echo "Removing existing $BUILD_HARNESS_EXT_PROJECT"
	    rm -rf "$BUILD_HARNESS_EXT_PROJECT"
fi

echo "Cloning ${BUILD_HARNESS_EXT_GIT}#${BUILD_HARNESS_EXT_BRANCH}..."
git clone -c advice.detachedHead=false --depth=1 -b $BUILD_HARNESS_EXT_BRANCH $BUILD_HARNESS_EXT_GIT
