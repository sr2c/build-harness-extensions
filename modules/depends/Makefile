
## Ensure that a command is installed and available in the PATH
depends/%:
	@if ! command -v $* >/dev/null 2>&1; then \
	  echo "Error: $* is not installed." >&2; \
	  exit 1; \
	fi
