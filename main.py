"""Application entrypoint."""
from capture.hotkey_listener import start_listener


def main() -> None:
    """Start the app."""
    start_listener()


if __name__ == "__main__":
    main()
