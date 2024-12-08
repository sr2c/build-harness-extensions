.PHONY: cliff/init cliff/release-tag

cliff/init:
	git cliff --init

cliff/release-tag:
	@test -d .git || (echo "Error: .git directory not found. Please ensure you are in the root directory of the Git repository." && exit 1)
	git cliff --bump -o
	git add CHANGELOG.md
	NEW_VERSION=$$(git cliff --bumped-version) && \
	git commit -m "chore: release $$NEW_VERSION" && \
	git tag $$NEW_VERSION && \
	echo "New tag: $$NEW_VERSION"
