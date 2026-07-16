"""Application entrypoint. The ONLY file that knows about both layers."""
from capture.hotkey_listener import start_listener
from services.reading_service import make_audio_from_text


def main() -> None:
    """Start the app."""
    # "hey listener, whenever you grab text, run make_audio_from_text on it."
    # the listener never imports the service; we hand the function in from here.
    start_listener(make_audio_from_text)


if __name__ == "__main__":
    main()
